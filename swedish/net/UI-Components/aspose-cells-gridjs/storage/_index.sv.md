---
title: Arbeta med GridJs lagring
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/storage/
description: Denna artikel beskriver den allmänna filhanteringen för GridJs.
keywords: filcache,lager,GridJs,GridJs lager,GridJs uid,hämta,unikt id
---


# Arbeta med GridJs-lagring
## den allmänna filhanteringen 
Efter import av en kalkylbladsfil,

GridJs kommer att skapa en cache-fil med den angivna uid i mappen **`Config.FileCacheDirectory`**,

med formatet [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat"),

GridJs kommer också att spara alla former/bilder i en ziparkivfil i mappen **`Config.PictureCacheDirectory`** för senare visning av former/bilder i klientgränssnittet.

och efter varje uppdatering i klientgränssnittet,

till exempel ställa in cellvärde, ställa in cellstil, osv.,

GridJs klient-sidans js kommer att utlösa kontrolleraction för att utföra en uppdateringscelloperation.

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

A. Om vi implementerar GridCacheForStream och ställer in GridJsWorkbook.CacheImp.
till exempel i koden nedan kan vi bara sätta och hämta cache-filen från **"D:\temp"**
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
B. Om vi inte ställer in GridJsWorkbook.CacheImp,

kommer GridJs att skapa och spara filen inom **`Config.FileCacheDirectory`**, vilket är standardcachekatalogen som vi kan ställa in.

### hur man får den uppdaterade resultatsfilen
#### 1. ett specifierad uid för filen 
Se till att en specifierad kartläggning korrespondens mellan filen och uid finns, 

Du kan alltid få samma uid för ett angivet filnamn, inte från slumpmässig generering.

Till exempel är det bra att bara använda filnamnet.
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
```C#
//in controller action 
  GridJsWorkbook wb = new GridJsWorkbook();
  wb.MergeExcelFileFromJson(uid, p);
  //after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
  wb.SaveToXlsx(Path.Combine(Config.FileCacheDirectory, uid));
```         
#### 3. hämta filen från cache
till exempel: i hämtnings-åtgärden kan du bara hämta den från cache-katalogen med uid.
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

För mer detaljerad information kan du kolla exemplet här:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
