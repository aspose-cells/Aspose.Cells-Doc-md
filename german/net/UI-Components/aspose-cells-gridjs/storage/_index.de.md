---
title: Arbeiten mit GridJs-Speicher
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/storage/
description: Dieser Artikel beschreibt die allgemeine Verarbeitung für Aspose.Cells.GridJs.
keywords: file cache,storage,GridJs,GridJs storage,GridJs uid,download,uniqueid
---
# Arbeiten mit GridJs-Speicher
## der allgemeine Dateiprozess
Nachdem Sie eine Tabellenkalkulationsdatei in den Speicher importiert und die Benutzeroberfläche angezeigt haben,

GridJs erstellt eine Cache-Datei mit der angegebenen uid ,

 mit dem Format von[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

und dann nach jedem Update-Vorgang in der Benutzeroberfläche,

zum Beispiel Zellwert festlegen, Zellstil festlegen usw. ,

Clientseitige js von GridJ lösen eine Controller-Aktion aus, um eine UpdateCell-Operation auszuführen.

Bei dieser Aktion wird während der UpdateCell-Methode aus dem Speicher in die Cache-Datei zurückgespeichert.
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
### Wo ist das Cache-Verzeichnis
A. Wenn wir GridCacheForStream implementieren und GridJsWorkbook.CacheImp.
 Zum Beispiel können wir im folgenden Code einfach die Cache-Datei einfügen und abrufen**"D:\temp"**
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
B.Wenn wir GridJsWorkbook.CacheImp nicht festlegen,

 GridJs erstellt und speichert eine Datei innerhalb der**Config.FileCacheDirectory** , das ist das Standard-Cache-Verzeichnis, das wir festlegen können.

### So erhalten Sie die aktualisierte Ergebnisdatei
#### 1. eine angegebene UID für die Datei
 Stellen Sie sicher, dass eine bestimmte Kartenkorrespondenz zwischen der Datei und der UID besteht,

Sie können immer die gleiche UID für einen bestimmten Dateinamen erhalten, nicht durch zufällige Generierung.

Verwenden Sie zum Beispiel einfach den Dateinamen.
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

#### 2. Synchronisierung mit ui-Betrieb
Eigentlich für einige UI-Operationen,

zum Beispiel:

Wechseln Sie das aktive Blatt zu einem anderen,

Ändern Sie die Bildposition,

Bild drehen/skalieren usw.

Die UpdateCell-Aktion wird nicht ausgelöst.

Wenn wir also die aktualisierte Datei genauso erhalten möchten, wie die Benutzeroberfläche zeigt,

Wir müssen vor dem Speichern eine Zusammenführungsoperation durchführen, um diese UI-Operationen zu synchronisieren.
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
#### 3. Holen Sie sich die Datei aus dem Cache
Zum Beispiel: In der Download-Aktion können Sie es einfach aus dem Cache-Verzeichnis per UID abrufen.
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

Für weitere Detailinformationen können Sie das Beispiel hier überprüfen:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
