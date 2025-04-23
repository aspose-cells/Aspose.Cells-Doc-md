---
title: Arbeta med GridJs lagring
type: docs
weight: 250
url: /sv/java/aspose-cells-gridjs/storage/
description: Denna artikel beskriver den allmänna filhanteringen för GridJs.
keywords: filcache,lager,GridJs,GridJs lager,GridJs uid,hämta,unikt id
aliases:
  - /java/aspose-cells-gridjs/storage-introduction/
  - /java/aspose-cells-gridjs/work-with-storage/
---


# Arbeta med GridJs-lagring
## den allmänna filhanteringen 
Efter import av en kalkylbladsfil,

GridJs skapar en cachefil med angiven uid i mappen **`Config.getFileCacheDirectory()`**,

med formatet [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/java/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat"),

GridJs sparar också alla former/bilder till en zip-arkivfil i mappen **`Config.getPictureCacheDirectory()`** för senare visning av former/bilder i klientgränssnittet.

och efter varje uppdatering i klientgränssnittet,

till exempel ställa in cellvärde, ställa in cellstil, osv.,

GridJs klient-sidans js kommer att utlösa kontrolleraction för att utföra en uppdateringscelloperation.

I denna åtgärd kommer en sparning tillbaka till cache-filen att inträffa under UpdateCell-metoden.
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
### Var finns cache-filen faktiskt 

A. Om vi implementerar GridCacheForStream och ställer in GridJsWorkbook.CacheImp.
till exempel i koden nedan kan vi bara sätta och hämta cache-filen från **"D:\temp"**
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
B. Om vi inte ställer in GridJsWorkbook.CacheImp,

GridJs skapar och sparar fil inom mappen **`Config.getFileCacheDirectory()`**, som är standard cachekatalogen som vi kan ställa in.

### hur man får den uppdaterade resultatsfilen
#### 1. ett specifierad uid för filen 
Se till att en specifierad kartläggning korrespondens mellan filen och uid finns, 

Du kan alltid få samma uid för ett angivet filnamn, inte från slumpmässig generering.

Till exempel är det bra att bara använda filnamnet.
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

#### 2. synkronisera med klientens UI-operation
Faktum är att för vissa klienters UI-operation,

till exempel:

växla det aktiva kalkylarket till ett annat,

ändra bildplaceringen,

rotera/ändra bildstorlek, etc.

kommer inte UpdateCell-åtgärden att utlösas.

Så om vi vill få den uppdaterade filen precis som klientens UI visar,

måste vi göra en sammanfogning innan spara-åtgärden för att synkronisera de där klientens UI-operationerna.
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
#### 3. hämta fil-URL från cache
till exempel: i hämtnings-åtgärden kan du bara hämta den från cache-katalogen med uid.
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

För mer detaljerad information kan du kolla exemplet här:
<https://github.com/aspose-cells/Aspose.Cells-for-java/tree/master/Examples_GridJs>
