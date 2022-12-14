---
title: Utilizzo dell'archiviazione GridJs
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/storage/
description: Questo articolo descrive l'elaborazione generale per Aspose.Cells.GridJs.
keywords: file cache,storage,GridJs,GridJs storage,GridJs uid,download,uniqueid
---
# Lavorare con lo storage GridJs
## il processo di file generale
Dopo aver importato un foglio di calcolo in memoria e mostrato l'interfaccia utente,

GridJs creerà un file di cache con l'uid specificato,

 con il formato di[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

poi dopo ogni operazione di aggiornamento nell'interfaccia utente,

ad esempio imposta il valore della cella, imposta lo stile della cella, ecc. ,

GridJs lato client js attiverà l'azione del controller per eseguire un'operazione UpdateCell.

In questa azione si verificherà un salvataggio nel file di cache dalla memoria durante il metodo UpdateCell.
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
### dov'è la directory della cache
R. Se implementiamo GridCacheForStream e impostiamo GridJsWorkbook.CacheImp.
 ad esempio nel codice seguente possiamo semplicemente inserire e ottenere il file della cache da**"D:\temp"**
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
B.Se non impostiamo GridJsWorkbook.CacheImp,

 GridJs creerà e salverà il file all'interno del file**Config.FileCacheDirectory** , che è la directory della cache predefinita che possiamo impostare.

### come ottenere il file dei risultati aggiornato
#### 1. un uid specificato per il file
 Assicurati una corrispondenza di mappa specifica tra il file e l'uid,

puoi sempre ottenere lo stesso uid per un nome file specificato, non dalla generazione casuale.

Ad esempio, basta usare il nome del file è ok.
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

#### 2. sincronizzazione con il funzionamento dell'interfaccia utente
In realtà per alcune operazioni dell'interfaccia utente,

per esempio:

cambia il foglio attivo con un altro,

cambiare la posizione dell'immagine,

ruotare/ridimensionare l'immagine, ecc.

l'azione UpdateCell non verrà attivata.

Quindi, se vogliamo ottenere il file aggiornato proprio come mostra l'interfaccia utente,

dobbiamo eseguire un'operazione di unione prima di salvare l'azione per sincronizzare quelle operazioni dell'interfaccia utente.
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
#### 3. ottenere il file dalla cache
ad esempio: nell'azione di download, puoi semplicemente ottenerlo dalla directory della cache tramite uid.
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

Per informazioni più dettagliate, puoi controllare l'esempio qui:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
