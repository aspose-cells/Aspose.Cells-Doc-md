---
title: Arbeta med GridJs lagring
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/storage/
description: Denna artikel beskriver den allmänna filhanteringen för GridJs.
keywords: filcache,lager,GridJs,GridJs lager,GridJs uid,hämta,unikt id
aliases:
  - /net/aspose-cells-gridjs/storage-introduction/
  - /net/aspose-cells-gridjs/work-with-storage/
---


# Arbeta med GridJs-lagring
## den allmänna filhanteringen 

Efter import av en kalkylbladsfil,

GridJs kommer att skapa en cache-fil med angivet uid enligt GridCacheForStream-implementeringen,

med formatet [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat"),

GridJs sparar också alla former/bilder till en zip-arkivfil i cachemappen för senare visning av former/bilder i klient-UI.

och efter varje uppdatering i klientgränssnittet,

till exempel ställa in cellvärde, ställa in cellstil, osv.,

GridJs klient-sidans JS kommer att utlösa en kontrollåtgärd för att göra en uppdateringsoperation.

I denna åtgärd kommer en sparning tillbaka till cache-filen att inträffa under UpdateCell-metoden.
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
### Var finns cache-filen faktiskt 

A. Om du implementerar GridCacheForStream själv.
till exempel i koden nedan kan vi bara sätta och hämta cache-filen från **"D:\temp"**
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
B.Om du inte sätter GridJsWorkbook.CacheImp, 

GridJs har redan implementerat en standard.

GridJs kommer att skapa och spara cachefilen inom sökvägen: **`Config.FileCacheDirectory/streamcache`** .

### hur man får den uppdaterade resultatsfilen
#### 1. skapa en specificerad uid för filen 
Se till att en specifierad kartläggning korrespondens mellan filen och uid finns, 

Till exempel 

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


#### 2. hämta filen från cache med hjälp av uid
till exempel: I nedladdningsåtgärden kan du bara hämta den från cachekatalogen med uid och filnamn.
```C#
	 Stream fileStream = GridJsWorkbook.CacheImp.LoadStream(uid + "/" + filename);
```

För mer detaljerad information kan du kolla exemplet här:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
