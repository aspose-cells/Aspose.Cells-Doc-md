---
title: Lavorare con lo storage di GridJs
type: docs
weight: 250
url: /it/java/aspose-cells-gridjs/storage/
description: Questo articolo descrive l elaborazione generale dei file per GridJs.
keywords: file cache, archiviazione, GridJs, archiviazione di GridJs, uid di GridJs, scarica, uniqueid
aliases:
  - /java/aspose-cells-gridjs/storage-introduction/
  - /java/aspose-cells-gridjs/work-with-storage/
---


# Lavorare con lo storage di GridJs
##  il processo generale dei file 
Dopo l'importazione di un file di foglio di calcolo ,

GridJs creerà un file cache con l'uid specificato nella cartella **`Config.getFileCacheDirectory()`** ,

con il formato di [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/java/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat"),

GridJs salverà anche tutte le forme / immagini in un archivio zip nella cartella **`Config.getPictureCacheDirectory()`** per la visualizzazione successiva di forme / immagini nell'interfaccia utente client.

e dopo ogni operazione di aggiornamento nell'interfaccia utente del client,

ad esempio impostare il valore della cella, impostare lo stile della cella, ecc. ,

il lato client js di GridJs attiverà l'azione del controller per eseguire un'operazione UpdateCell.

In questa azione si verificherà un salvataggio nel file di cache durante il metodo UpdateCell.
```JAVA  
    @PostMapping("/UpdateCell")
    public ResponseEntity<String> updateCell(HttpServletRequest request) {
        String p = request.getParameter("p");
        String uid = request.getParameter("uid");
        GridJsWorkbook gwb = new GridJsWorkbook();
        String ret;
		try {
			ret = gwb.updateCell(p, uid);
			return new ResponseEntity<>(ret, HttpStatus.OK);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			return new ResponseEntity<>(gwb.errorJson(e.getMessage()), HttpStatus.OK);
		}

    }
```
###  dove si trova effettivamente il file di cache 

A. Se implementiamo GridCacheForStream e impostiamo GridJsWorkbook.CacheImp.
ad esempio nel codice sottostante possiamo semplicemente mettere e ottenere il file di cache da **"D:\temp"**
```JAVA
Config.setFileCacheDirectory("D:\temp");
GridJsWorkbook.CacheImp=new LocalFileCache();
public class LocalFileCache extends GridCacheForStream {

	@Override
	public void saveStream(InputStream s, String uid) {
		// make sure the directory is exist
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		try (FileOutputStream fos = new FileOutputStream(filepath.toString())) {
			s.reset(); // Equivalent to s.Position = 0 in C#
			byte[] buffer = new byte[1024];
			int length;
			while ((length = s.read(buffer)) > 0) {
				fos.write(buffer, 0, length);
			}
			fos.flush();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	@Override
	public InputStream loadStream(String uid) {
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		try {
			return new FileInputStream(filepath);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			return null;
		}
	}

	@Override
	public boolean isExisted(String uid) {
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		return Files.exists(Paths.get(filepath));
	}

	@Override
	public String getFileUrl(String uid) {
		return "/GridJs2/GetFileUseCacheStream?id=" + uid;
	}

}
		...
```
B. Se non impostiamo GridJsWorkbook.CacheImp,

GridJs creerà e salverà il file all'interno della cartella **`Config.getFileCacheDirectory()`**, che è la directory cache predefinita che possiamo impostare.

###  come ottenere il file di risultato aggiornato
#### 1. un uid specifico per il file 
Assicurarsi di una corrispondenza mappatura specifica tra il file e l'uid, 

potete sempre ottenere lo stesso uid per un nome file specificato, non da una generazione casuale.

Ad esempio basta usare il nome del file.
```JAVA
//in controller  

     @GetMapping("/DetailStreamJsonWithUid")
    public void detailStreamJsonWithUid(@RequestParam String filename, @RequestParam String uid,HttpServletResponse response) {


        	Path filePath = Paths.get(listDir, filename);
            GridJsWorkbook wbj = new GridJsWorkbook();

            response.setContentType("application/json");
            response.setHeader("Content-Encoding", "gzip");
            try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
                wbj.importExcelFile(filePath.toString());
                wbj.jsonToStream(gzipOutputStream, filename);
            } catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    }
```

#### 2. sincronizzazione con operazioni UI del client
In realtà per alcune operazioni UI del client,

ad esempio:

passare alla scheda attiva,

cambiare la posizione dell'immagine,

ruotare/ridimensionare l'immagine, ecc.

l'azione di UpdateCell non verrà attivata.

Quindi se vogliamo ottenere il file aggiornato esattamente come lo mostra l'interfaccia utente del client,

dobbiamo eseguire un'operazione di merge prima dell'azione di salvataggio per sincronizzare quelle operazioni UI del client.
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
```JAVA
//in controller action 
  GridJsWorkbook wb = new GridJsWorkbook();
  wb.mergeExcelFileFromJson(uid, p);
  //after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
  wb.saveToCacheWithFileName(uid,filename,password);
```         
#### 3. ottieni l'url del file dalla cache
ad esempio: nell'azione di download, puoi semplicemente prenderlo dalla directory della cache tramite uid.
```JAVA
//in controller  

      String fileUrl = null;
			if (GridJsWorkbook.CacheImp != null) {
				fileUrl = GridJsWorkbook.CacheImp.getFileUrl(uid + "/" + filename);
			} else {
				fileUrl = "/GridJs2/GetFile?id=" + uid + "&filename=" + filename;
			}
			return ResponseEntity.ok("\""+fileUrl+"\"");
```

Per maggiori dettagli, puoi controllare l'esempio qui:
<https://github.com/aspose-cells/Aspose.Cells-for-java/tree/master/Examples_GridJs>
