---
title: Arbeiten mit GridJs Speicher
type: docs
weight: 250
url: /de/java/aspose-cells-gridjs/storage/
description: Dieser Artikel beschreibt die allgemeine Dateiverarbeitung für GridJs.
keywords: Dateicache, Speicher, GridJs, GridJs Speicher, GridJs UID, herunterladen, eindeutige ID
aliases:
  - /java/aspose-cells-gridjs/storage-introduction/
  - /java/aspose-cells-gridjs/work-with-storage/
---


# Arbeiten mit GridJs-Speicher
##  Der allgemeine Dateiprozess 
Nach dem Import einer Tabellendatei erstellt GridJs eine Cache-Datei mit der angegebenen UID im Ordner **`Config.file_cache_directory`** ,

GridJs erstellt eine Cache-Datei mit der angegebenen UID im Ordner `Config.getFileCacheDirectory()`,

im Format [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/java/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs speichert außerdem alle Formen/Bilder in eine ZIP-Archivdatei im Ordner `Config.getPictureCacheDirectory()`, um Formen/Bilder später im Client-UI anzuzeigen.

und nach jeder Aktualisierung im Client-UI

zum Beispiel Zellenwert setzen, Zellenstil setzen usw.

GridJs  JavaScript auf Clientseite wird die Controlleraktion zum Durchführen einer UpdateCell-Operation auslösen.

In dieser Aktion wird während der UpdateCell-Methode eine Rückkehr zur Cache-Datei erfolgen.
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
###  wo befindet sich tatsächlich die Cache-Datei 

A. Wenn wir GridCacheForStream implementieren und GridJsWorkbook.CacheImp setzen.
zum Beispiel im folgenden Code können wir die Cache-Datei einfach in **"D:\temp"** ablegen und abrufen
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
B. Wenn wir GridJsWorkbook.CacheImp nicht setzen,

GridJs erstellt und speichert die Datei innerhalb des Ordners `Config.getFileCacheDirectory()`, welcher das Standard-Cache-Verzeichnis ist, das wir festlegen können.

### wie man die aktualisierte Ergebnisdatei erhält
#### 1. eine spezifische UID für die Datei 
Stellen Sie sicher, dass es eine spezielle Zuordnung zwischen der Datei und der UID gibt, 

Sie können immer die gleiche UID für einen bestimmten Dateinamen erhalten, nicht durch zufällige Generierung.

Verwenden Sie zum Beispiel einfach den Dateinamen.
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
```JAVA
//in controller action 
  GridJsWorkbook wb = new GridJsWorkbook();
  wb.mergeExcelFileFromJson(uid, p);
  //after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
  wb.saveToCacheWithFileName(uid,filename,password);
```         
#### 3. Holen Sie sich die Date-URL aus dem Cache
zum Beispiel: Bei der Download-Aktion können Sie es einfach aus dem Cache-Verzeichnis nach UID abrufen.
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

Weitere Detailinformationen finden Sie hier:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples_GridJs>
