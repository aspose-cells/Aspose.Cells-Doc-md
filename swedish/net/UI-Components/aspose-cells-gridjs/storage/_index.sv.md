---
title: Arbeta med GridJs lagring
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/storage/
description: Den här artikeln beskriver den allmänna behandlingen för Aspose.Cells.GridJs.
keywords: file cache,storage,GridJs,GridJs storage,GridJs uid,download,uniqueid
---
# Arbeta med GridJs Storage
## den allmänna filprocessen
Efter att ha importerat en kalkylarksfil i minnet och visat användargränssnittet,

GridJs kommer att skapa en cachefil med den angivna uid ,

 med formatet av[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

och sedan efter varje uppdateringsåtgärd i användargränssnittet,

till exempel ställ in cellvärde, ställ in cellstil, etc. ,

GridJs klientsida js kommer att utlösa kontrollåtgärder för att utföra en UpdateCell-operation.

I den här åtgärden kommer en spara tillbaka till cachefilen från minnet att ske under UpdateCell-metoden.
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
### var är cachekatalogen
A. Om vi implementerar GridCacheForStream och ställer in GridJsWorkbook.CacheImp.
 till exempel i koden nedan kan vi bara lägga och hämta cachefilen från**"D:\temp"**
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
B.Om vi inte ställer in GridJsWorkbook.CacheImp,

 GridJs kommer att skapa och spara filen i**Config.FileCacheDirectory** , som är standardcachekatalogen som vi kan ställa in.

### hur man får den uppdaterade resultatfilen
#### 1. en specificerad uid för fil
 Se till att en specificerad kartöverensstämmelse mellan filen och uid,

du kan alltid få samma uid för ett specificerat filnamn, inte från slumpmässig generering.

Använd till exempel bara filnamnet är ok.
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

#### 2. synkronisera med användargränssnittet
Egentligen för vissa UI-operationer,

till exempel:

växla det aktiva arket till ett annat,

ändra bildpositionen,

rotera/ändra storlek på bild, etc.

UpdateCell-åtgärden utlöses inte.

Så om vi vill få den uppdaterade filen precis som användargränssnittet visar,

vi måste göra en sammanfogningsoperation innan vi sparar åtgärden för att synkronisera dessa ui-operationer.
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
#### 3. hämta filen från cachen
till exempel: i nedladdningsåtgärden kan du bara hämta den från cachekatalogen med uid.
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
