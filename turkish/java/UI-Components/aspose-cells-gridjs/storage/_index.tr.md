---
title: GridJs depolama ile çalışmak
type: docs
weight: 250
url: /tr/java/aspose-cells-gridjs/storage/
description: Bu makale, GridJs için genel dosya işleme işlemlerini açıklar.
keywords: dosya önbelleği, depolama, GridJs, GridJs depolama, GridJs uid, indir, benzersiz kimlik
aliases:
  - /java/aspose-cells-gridjs/storage-introduction/
  - /java/aspose-cells-gridjs/work-with-storage/
---


# GridJs Depolama ile Çalışmak
## genel dosya işlemi 
Bir elektronik tablo dosyası içe aktarıldıktan sonra,

GridJs, belirli uid ile önbellek dosyasını **`Config.getFileCacheDirectory()`** klasörüne oluşturacak ,

[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/java/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") formatında ,

GridJs ayrıca tüm şekil/resimleri **`Config.getPictureCacheDirectory()`** klasörüne zip arşiv dosyasına kaydeder, böylece client arayüzünde şekil/resim gösterimi yapılabilir.

ve istemci arayüzünde her güncelleme işleminden sonra,

örneğin hücre değeri ayarla, hücre stili ayarlama, vb.,

GridJs istemci tarafı js, bir GüncellemeHücresi işlemi yapmak için bir denetleyici eylemi tetikler.

Bu eylem sırasında, Bir GüncellemeHücre yöntemi sırasında önbellek dosyasına bir kayıt gerçekleşecektir.
```JAVA  
    @PostMapping("/UpdateCell")
    public ResponseEntity<String> updateCell(HttpServletRequest request) {
        String p = request.getParameter("p");
        String uid = request.getParameter("uid");
        GridJsWorkbook gwb = new GridJsWorkbook();
        String ret;
		try {
			ret = gwb.updateCell(p, uid);
			return new ResponseEntity<>(ret, HttpStatus.OK);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			return new ResponseEntity<>(gwb.errorJson(e.getMessage()), HttpStatus.OK);
		}

    }
```
### önbellek dosya aslında nerede 

A. Eğer GridCacheForStream uygularsak ve GridJsWorkbook.CacheImp'i ayarlarsak.
örneğin aşağıdaki kodda **"D:\temp"** dizinine sadece önbellek dosyasını yerleştirebilir ve alabiliriz.
```JAVA
Config.setFileCacheDirectory("D:\temp");
GridJsWorkbook.CacheImp=new LocalFileCache();
public class LocalFileCache extends GridCacheForStream {

	@Override
	public void saveStream(InputStream s, String uid) {
		// make sure the directory is exist
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		try (FileOutputStream fos = new FileOutputStream(filepath.toString())) {
			s.reset(); // Equivalent to s.Position = 0 in C#
			byte[] buffer = new byte[1024];
			int length;
			while ((length = s.read(buffer)) > 0) {
				fos.write(buffer, 0, length);
			}
			fos.flush();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	@Override
	public InputStream loadStream(String uid) {
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		try {
			return new FileInputStream(filepath);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			return null;
		}
	}

	@Override
	public boolean isExisted(String uid) {
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		return Files.exists(Paths.get(filepath));
	}

	@Override
	public String getFileUrl(String uid) {
		return "/GridJs2/GetFileUseCacheStream?id=" + uid;
	}

}
		...
```
B. Eğer GridJsWorkbook.CacheImp'i ayarlamazsak,

GridJs, varsayılan önbellek dizini olan **`Config.getFileCacheDirectory()`** içerisinde dosya oluşturur ve kaydeder.

### güncellenmiş sonuç dosyasını nasıl alınır
#### 1. dosya için belirtilen bir uid 
Dosya ve uid arasında belirli bir eşleme bağlantısının olması gerektiğinden emin olun, 

bir dosya adı için her zaman aynı uid'yi alabilirsiniz, rastgele oluşturulmaz.

Örneğin, sadece dosya adını kullanmak yeterlidir.
```JAVA
//in controller  

     @GetMapping("/DetailStreamJsonWithUid")
    public void detailStreamJsonWithUid(@RequestParam String filename, @RequestParam String uid,HttpServletResponse response) {


        	Path filePath = Paths.get(listDir, filename);
            GridJsWorkbook wbj = new GridJsWorkbook();

            response.setContentType("application/json");
            response.setHeader("Content-Encoding", "gzip");
            try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
                wbj.importExcelFile(filePath.toString());
                wbj.jsonToStream(gzipOutputStream, filename);
            } catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    }
```

#### 2. istemci arayüzü işlemi ile senkronize olun
Aslında bazı istemci arayüzü işlemleri için,

örneğin:

etkin sayfayı başka bir sayfaya değiştir,

resmin pozisyonunu değiştir,

resmi döndür/boyutlandır, vb.

GüncellemeHücre eylemi tetiklenmeyecektir.

Bu nedenle, güncellenmiş dosyayı istemci arayüzünün gösterdiği gibi almak istiyorsak,

bu istemci arayüzü işlemlerini senkronize etmek için kaydetme işleminden önce bir birleştirme işlemi yapmamız gerekmektedir.
```javascript
//in the js
  function save() {
            if (!xs.buffer.isFinish()) {
              alert('updating is inprogress,please try later');
                return;
            }
            let datas = xs.datas;
            delete datas.history;
            delete datas.search;
            delete datas.images;
            delete datas.shapes;

        var jsondata = {
          sheetname: xs.sheet.data.name,
          actrow: xs.sheet.data.selector.ri,
          actcol: xs.sheet.data.selector.ci,
          datas: xs.getUpdateDatas(),
        };

        const data = {
          p: JSON.stringify(jsondata),
          uid: uniqueid,
        };
		....
		//go on to do ajax post to trigger controller action
```
```JAVA
//in controller action 
  GridJsWorkbook wb = new GridJsWorkbook();
  wb.mergeExcelFileFromJson(uid, p);
  //after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
  wb.saveToCacheWithFileName(uid,filename,password);
```         
#### 3. önbellekten dosya URL'sini alın
örneğin: indirme işlemi için, uid ile doğrudan önbellek dizininden alabilirsiniz.
```JAVA
//in controller  

      String fileUrl = null;
			if (GridJsWorkbook.CacheImp != null) {
				fileUrl = GridJsWorkbook.CacheImp.getFileUrl(uid + "/" + filename);
			} else {
				fileUrl = "/GridJs2/GetFile?id=" + uid + "&filename=" + filename;
			}
			return ResponseEntity.ok("\""+fileUrl+"\"");
```

Daha fazla detaylı bilgi için buradaki örneği kontrol edebilirsiniz:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples_GridJs>
