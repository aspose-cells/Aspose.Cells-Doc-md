---
title: Arbeiten mit GridJs Speicher
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/storage/
description: Dieser Artikel beschreibt die allgemeine Dateiverarbeitung für GridJs.
keywords: Dateicache, Speicher, GridJs, GridJs Speicher, GridJs UID, herunterladen, eindeutige ID
aliases:
  - /net/aspose-cells-gridjs/storage-introduction/
  - /net/aspose-cells-gridjs/work-with-storage/
---


# Arbeiten mit GridJs-Speicher
##  Der allgemeine Dateiprozess 

Nach dem Import einer Tabellendatei erstellt GridJs eine Cache-Datei mit der angegebenen UID im Ordner **`Config.file_cache_directory`** ,

GridJs erstellt eine Cache-Datei mit der angegebenen UID gemäß der GridCacheForStream-Implementierung.

im Format von [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs speichert auch alle Formen/Bilder in einer Zip-Archivdatei im Cache-Ordner für die spätere Anzeige von Formen/Bildern in der Client-Benutzeroberfläche.

und nach jeder Aktualisierung im Client-UI

zum Beispiel Zellenwert setzen, Zellenstil setzen usw.

Die GridJs-Client-seitige JS löst eine Controller-Aktion zum Aktualisieren aus.

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

A. Wenn Sie GridCacheForStream selbst implementieren.
zum Beispiel im folgenden Code können wir die Cache-Datei einfach in **"D:\temp"** ablegen und abrufen
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
B. Falls Sie GridJsWorkbook.CacheImp nicht setzen, 

GridJs implementiert bereits eine Standardlösung.

GridJs erstellt und speichert die Cache-Datei im Pfad: **`Config.FileCacheDirectory/streamcache`**.

### wie man die aktualisierte Ergebnisdatei erhält
#### 1. Erstellen Sie eine angegebene UID für die Datei 
Stellen Sie sicher, dass es eine spezielle Zuordnung zwischen der Datei und der UID gibt, 

Zum Beispiel 

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


#### 2. Holen Sie die Datei anhand der UID aus dem Cache
Zum Beispiel: Im Download-Action können Sie sie einfach aus dem Cache-Verzeichnis anhand der UID und des Dateinamens abrufen.
```C#
	 Stream fileStream = GridJsWorkbook.CacheImp.LoadStream(uid + "/" + filename);
```

Weitere Detailinformationen finden Sie hier:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
