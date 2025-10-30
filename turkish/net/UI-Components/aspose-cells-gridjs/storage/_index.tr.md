---
title: GridJs depolama ile çalışmak
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/storage/
description: Bu makale, GridJs için genel dosya işleme işlemlerini açıklar.
keywords: dosya önbelleği, depolama, GridJs, GridJs depolama, GridJs uid, indir, benzersiz kimlik
aliases:
  - /net/aspose-cells-gridjs/storage-introduction/
  - /net/aspose-cells-gridjs/work-with-storage/
---


# GridJs Depolama ile Çalışmak
## genel dosya işlemi 

Bir elektronik tablo dosyası içe aktarıldıktan sonra,

GridJs, belirli uid ile GridCacheForStream uygulamasına göre bir önbellek dosyası oluşturacaktır,

[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") formatında,

GridJs ayrıca tüm şekil/resimleri zip arşiv dosyasına kaydeder ve bu dosyayı önbelleğe alır, böylece müşteri arayüzünde şekil/resimler daha sonra görüntülenebilir.

ve istemci arayüzünde her güncelleme işleminden sonra,

örneğin hücre değeri ayarla, hücre stili ayarlama, vb.,

GridJs istemci tarafı js, kontrolcü eylemini tetikler ve güncelleme işlemi yapar.

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

A. Kendiniz GridCacheForStream uygularsanız.
örneğin aşağıdaki kodda **"D:\temp"** dizinine sadece önbellek dosyasını yerleştirebilir ve alabiliriz.
```C#
Config.FileCacheDirectory=@"D:\temp";
GridJsWorkbook.CacheImp=new LocalFileCache();
public class LocalFileCache  : GridCacheForStream
    {

        public LocalFileCache()
        {
            string streampath = Config.FileCacheDirectory;
            if (!Directory.Exists(streampath))
            {

                Directory.CreateDirectory(streampath);

            }
        }
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
B. GridJsWorkbook.CacheImp ayarlamazsanız, 

GridJs zaten varsayılan bir uygulamaya sahiptir.

GridJs, önbellek dosyasını aşağıdaki PATH'te oluşturacak ve kaydedecek: **`Config.FileCacheDirectory/streamcache`** .

### güncellenmiş sonuç dosyasını nasıl alınır
#### 1. Dosya için belirli bir uid oluşturma 
Dosya ve uid arasında belirli bir eşleme bağlantısının olması gerektiğinden emin olun, 

Örneğin 

```C#

...     
        //generte a uid for the file
        String uid = GridJsWorkbook.GetUidForFile(filename)
...
        //get JSON result which will be used in client ui for the file by filename and uid
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


#### 2. Uid ile önbellekten dosya alın
Örneğin: indirme işlemi sırasında, sadece uid ve dosya adıyla önbellek dizininden alınabilir.
```C#
	 Stream fileStream = GridJsWorkbook.CacheImp.LoadStream(uid + "/" + filename);
```

Daha fazla detaylı bilgi için buradaki örneği kontrol edebilirsiniz:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
