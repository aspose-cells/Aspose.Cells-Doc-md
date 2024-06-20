---
title: Arbeiten mit GridJs Speicher
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/storage/
description: Dieser Artikel beschreibt die allgemeine Dateiverarbeitung für GridJs.
keywords: Dateicache, Speicher, GridJs, GridJs Speicher, GridJs UID, herunterladen, eindeutige ID
---


# Arbeiten mit GridJs-Speicher
##  Der allgemeine Dateiprozess 
Nach dem Import einer Tabellendatei erstellt GridJs eine Cache-Datei mit der angegebenen UID im Ordner **`Config.file_cache_directory`** ,

GridJs erstellt eine Cache-Datei mit der angegebenen UID im **`Config.FileCacheDirectory`**-Ordner  ,

im Format von [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs speichert auch alle Formen/Bilder in einer Zip-Archivdatei im **`Config.PictureCacheDirectory`**-Ordner für die spätere Anzeige von Formen/Bildern in der Client-Benutzeroberfläche.

und nach jeder Aktualisierung im Client-UI

zum Beispiel Zellenwert setzen, Zellenstil setzen usw.

GridJs  JavaScript auf Clientseite wird die Controlleraktion zum Durchführen einer UpdateCell-Operation auslösen.

In dieser Aktion wird während der UpdateCell-Methode eine Rückkehr zur Cache-Datei erfolgen.
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
###  wo befindet sich tatsächlich die Cache-Datei 

A. Wenn wir GridCacheForStream implementieren und GridJsWorkbook.CacheImp setzen.
zum Beispiel im folgenden Code können wir die Cache-Datei einfach in **"D:\temp"** ablegen und abrufen
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
B. Wenn wir GridJsWorkbook.CacheImp nicht setzen,

GridJs erstellt und speichert die Datei im **`Config.FileCacheDirectory`** , das als Standard-Cache-Verzeichnis eingestellt werden kann.

### wie man die aktualisierte Ergebnisdatei erhält
#### 1. eine spezifische UID für die Datei 
Stellen Sie sicher, dass es eine spezielle Zuordnung zwischen der Datei und der UID gibt, 

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

#### 2. Synchronisieren mit Client-UI-Betrieb
Tatsächlich für einige Client-UI-Operationen,

zum Beispiel:

Schalten Sie das aktive Blatt zu einem anderen um,

Ändern Sie die Bildposition,

Bild drehen/vergrößern, usw.

Die UpdateCell-Aktion wird nicht ausgelöst.

Deshalb, wenn wir die aktualisierte Datei genauso anzeigen möchten, wie es das Client-UI zeigt,

müssen wir vor der Speicheraktion eine Zusammenführungsoperation durchführen, um diese Client-UI-Operationen zu synchronisieren.
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
#### 3. die Datei aus dem Cache erhalten
zum Beispiel: Bei der Download-Aktion können Sie es einfach aus dem Cache-Verzeichnis nach UID abrufen.
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

Weitere Detailinformationen finden Sie hier:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
