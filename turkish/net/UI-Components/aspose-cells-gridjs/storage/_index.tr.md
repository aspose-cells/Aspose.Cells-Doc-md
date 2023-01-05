---
title: GridJs depolamasıyla çalışma
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/storage/
description: Bu makalede, Aspose.Cells.GridJs için genel işleme açıklanmaktadır.
keywords: file cache,storage,GridJs,GridJs storage,GridJs uid,download,uniqueid
---
# GridJs Depolama ile Çalışma
## genel dosya işlemi
Bir elektronik tablo dosyasını belleğe aktardıktan ve kullanıcı arayüzünü gösterdikten sonra,

GridJs, belirtilen uid ile bir önbellek dosyası oluşturacak,

 formatı ile[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

ve ardından kullanıcı arayüzündeki her güncelleme işleminden sonra,

örneğin hücre değerini ayarla, hücre stilini ayarla, vb. ,

GridJs istemci tarafı j'leri, bir UpdateCell işlemi yapmak için denetleyici eylemini tetikler.

Bu eylemde, UpdateCell yöntemi sırasında bellekten önbellek dosyasına geri kaydetme gerçekleşir.
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
### önbellek dizini nerede
A. GridCacheForStream'i uygular ve GridJsWorkbook.CacheImp'i ayarlarsak.
 örneğin aşağıdaki kodda önbellek dosyasını alıp alabiliriz.**"D:\temp"**
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
B.GridJsWorkbook.CacheImp'i ayarlamazsak,

 GridJ'ler, içinde dosya oluşturacak ve kaydedecektir.**Config.FileCacheDirectory** , ayarlayabileceğimiz varsayılan önbellek dizini.

### güncellenmiş sonuç dosyası nasıl alınır
#### 1. dosya için belirtilen bir uid
 Dosya ve uid arasında belirli bir harita yazışmasının olduğundan emin olun,

rastgele nesilden değil, belirli bir dosya adı için her zaman aynı kullanıcı kimliğini alabilirsiniz.

Örneğin, sadece dosya adını kullanın tamam.
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

#### 2. ui işlemiyle senkronize edin
Aslında bazı ui işlemleri için,

örneğin:

aktif sayfayı başka bir sayfaya geçirin,

görüntü konumunu değiştirmek,

görüntüyü döndürün/yeniden boyutlandırın, vb.

Hücreyi Güncelle eylemi tetiklenmez.

Bu nedenle, güncellenmiş dosyayı kullanıcı arayüzünün gösterdiği gibi almak istiyorsak,

bu ui işlemini senkronize etmek için eylemi kaydetmeden önce bir birleştirme işlemi yapmamız gerekiyor.
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
#### 3. dosyayı önbellekten alın
örneğin: indirme eyleminde, onu uid ile önbellek dizininden alabilirsiniz.
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

Daha ayrıntılı bilgi için, örneği buradan kontrol edebilirsiniz:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
