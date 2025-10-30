---
title: Lavorare con lo storage di GridJs
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/storage/
description: Questo articolo descrive l elaborazione generale dei file per GridJs.
keywords: file cache, archiviazione, GridJs, archiviazione di GridJs, uid di GridJs, scarica, uniqueid
aliases:
  - /net/aspose-cells-gridjs/storage-introduction/
  - /net/aspose-cells-gridjs/work-with-storage/
---


# Lavorare con lo storage di GridJs
##  il processo generale dei file 

Dopo l'importazione di un file di foglio di calcolo ,

GridJs creerà un file di cache con l'UID specificato secondo l'implementazione di GridCacheForStream,

con il formato di [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs salverà anche tutte le forme/immagini in un archivio zip nella cartella cache per la visualizzazione successiva di forme/immagini nell'interfaccia utente client.

e dopo ogni operazione di aggiornamento nell'interfaccia utente del client,

ad esempio impostare il valore della cella, impostare lo stile della cella, ecc. ,

Il js lato client di GridJs innescherà l'azione del controller per eseguire un'operazione di aggiornamento.

In questa azione si verificherà un salvataggio nel file di cache durante il metodo UpdateCell.
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
###  dove si trova effettivamente il file di cache 

A. Se implementi tu stesso GridCacheForStream.
ad esempio nel codice sottostante possiamo semplicemente mettere e ottenere il file di cache da **"D:\temp"**
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
B. Se non imposti GridJsWorkbook.CacheImp, 

GridJs ne ha già implementato uno di default.

GridJs creerà e salverà il file cache all'interno del percorso: **`Config.FileCacheDirectory/streamcache`** .

###  come ottenere il file di risultato aggiornato
#### 1. crea un uid specificato per il file 
Assicurarsi di una corrispondenza mappatura specifica tra il file e l'uid, 

Per esempio 

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


#### 2. ottieni il file dalla cache tramite l'uid
ad esempio: nella azione di download, puoi semplicemente prenderlo dalla directory cache tramite uid e nome file.
```C#
	 Stream fileStream = GridJsWorkbook.CacheImp.LoadStream(uid + "/" + filename);
```

Per maggiori dettagli, puoi controllare l'esempio qui:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
