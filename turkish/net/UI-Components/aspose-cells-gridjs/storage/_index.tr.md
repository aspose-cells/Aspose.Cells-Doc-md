---
title: GridJs depolama ile çalışmak
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/storage/
description: Bu makale, GridJs için genel dosya işleme işlemlerini açıklar.
keywords: dosya önbelleği, depolama, GridJs, GridJs depolama, GridJs uid, indir, benzersiz kimlik
---


# GridJs Depolama ile Çalışmak
## genel dosya işlemi 
Bir elektronik tablo dosyası içe aktarıldıktan sonra,

GridJs, **`Config.FileCacheDirectory`** klasöründe belirtilen uid ile bir önbellek dosyası oluşturacaktır,

[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") formatında,

GridJs ayrıca istemci arayüzünde daha sonra şekilleri/görüntüleri göstermek için bir zip arşiv dosyasına tüm şekilleri/görüntüleri kaydeder, **`Config.PictureCacheDirectory`** klasörüne.

ve istemci arayüzünde her güncelleme işleminden sonra,

örneğin hücre değeri ayarla, hücre stili ayarlama, vb.,

GridJs istemci tarafı js, bir GüncellemeHücresi işlemi yapmak için bir denetleyici eylemi tetikler.

Bu eylem sırasında, Bir GüncellemeHücre yöntemi sırasında önbellek dosyasına bir kayıt gerçekleşecektir.
```C#   
        // post: /GridJs/UpdateCell
        [HttpPost] 
        public ActionResult UpdateCell( )
        {
            string p = HttpContext.Request.Form["p"];
            string uid = HttpContext.Request.Form["uid"];
            GridJsWorkbook gwb = new GridJsWorkbook();
            String ret = gwb.UpdateCell(p, uid);
            return Content(ret, "text/plain", System.Text.Encoding.UTF8);
        }
```
### önbellek dosya aslında nerede 

A. Eğer GridCacheForStream uygularsak ve GridJsWorkbook.CacheImp'i ayarlarsak.
örneğin aşağıdaki kodda **"D:\temp"** dizinine sadece önbellek dosyasını yerleştirebilir ve alabiliriz.
```C#
Config.FileCacheDirectory=@"D:\temp";
GridJsWorkbook.CacheImp=new LocalFileCache();
public class LocalFileCache  : GridCacheForStream
    {

        /// <summary>
        /// Implement this method to savecache,save the stream to the cache object with the key id.
        /// </summary>
        /// <param name="s">the source stream </param>
        /// <param name="uid">the key id.</param>
        public override void SaveStream(Stream s, String uid)
        {//make sure the directory exist
            String filepath = Path.Combine(Config.FileCacheDirectory, uid);
            using (FileStream fs = new FileStream(filepath, FileMode.Create)) 
            {
                s.Position = 0;
                s.CopyTo(fs);
            }

        }

        /// <summary>
        /// Implement this method to loadcache with the key uid,return the stream from the cache object.
        /// </summary>
        /// <param name="uid">the key id</param>
        /// <returns>the stream from  the cache</returns>
        public override Stream LoadStream(String uid)
        {//make sure the directory is exist
            String filepath = Path.Combine(Config.FileCacheDirectory, uid);;
            FileStream fs = new FileStream(filepath, FileMode.Open);
            return fs;
        }
		...
```
B. Eğer GridJsWorkbook.CacheImp'i ayarlamazsak,

GridJs, **`Config.FileCacheDirectory`** içindeki, yani ayarlayabileceğimiz varsayılan önbellek dizininde bir dosya oluşturur ve kaydeder.

### güncellenmiş sonuç dosyasını nasıl alınır
#### 1. dosya için belirtilen bir uid 
Dosya ve uid arasında belirli bir eşleme bağlantısının olması gerektiğinden emin olun, 

bir dosya adı için her zaman aynı uid'yi alabilirsiniz, rastgele oluşturulmaz.

Örneğin, sadece dosya adını kullanmak yeterlidir.
```C#
//in controller  
...
        public ActionResult Uidtml(String filename)
        {

            return Redirect("~/xspread/uidload.html?file=" + filename + "&uid=" +  Path.GetFileNameWithoutExtension(filename));
        }
 ...
        public ActionResult DetailFileJsonWithUid(string filename,string uid)
        {
            String file = Path.Combine(TestConfig.ListDir, filename);
            GridJsWorkbook wbj = new GridJsWorkbook();
            //check if already in cache
           StringBuilder sb= wbj.GetJsonByUid(uid, filename);
            if(sb==null)
            {
                Workbook wb = new Workbook(file);
                wbj.ImportExcelFile(uid, wb);
                sb = wbj.ExportToJsonStringBuilder(filename);
            }

            return Content(sb.ToString(), "text/plain", System.Text.Encoding.UTF8);
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
```C#
//in controller action 
  GridJsWorkbook wb = new GridJsWorkbook();
  wb.MergeExcelFileFromJson(uid, p);
  //after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
  wb.SaveToXlsx(Path.Combine(Config.FileCacheDirectory, uid));
```         
#### 3. önbellekten dosyayı alın
örneğin: indirme işlemi için, uid ile doğrudan önbellek dizininden alabilirsiniz.
```C#
//in controller  

        public async Task<IActionResult> DownloadfromBytes(string uid,string ext)
        {
            byte[] byteArr = await System.IO.File.ReadAllBytesAsync(Path.Combine(Config.FileCacheDirectory, uid) );
            string mimeType = "application/octet-stream";
            return new FileContentResult(byteArr, mimeType)
            {
                FileDownloadName = uid+ ext
            };
        }
```

Daha fazla detaylı bilgi için buradaki örneği kontrol edebilirsiniz:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
