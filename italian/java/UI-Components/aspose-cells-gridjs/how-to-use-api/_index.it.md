---
title: Lavorare con GridJs lato server
type: docs
weight: 250
url: /it/java/aspose-cells-gridjs/how-to-use-api/
description: Questo articolo descrive come utilizzare le API in GridJs.
keywords: GridJs, server, GridCacheForStream
aliases:
  - /java/aspose-cells-gridjs/server/
  - /java/aspose-cells-gridjs/server-api/
  - /java/aspose-cells-gridjs/api-introduction/
  - /java/aspose-cells-gridjs/how-to-use-apis/
  - /java/aspose-cells-gridjs/work-with-serverside-api/
  - /java/aspose-cells-gridjs/work-with-serverside-apis/
---


# Lavorare con GridJs lato server
## 0. imposta il percorso della cartella corretta in Config
 **`Config.setFileCacheDirectory`** per il file di cache del foglio di lavoro (necessario).
 **`Config.setPictureCacheDirectory`** per i file immagine in cache nel workbook (opzionale, il valore predefinito è _piccache nella directory di cache dei file).

per i dettagli di archiviazione, controllare questa [guida](/java/aspose-cells-gridjs/storage/)

## 1. Implementa GridCacheForStream
Per lo storage in file locale, ecco un esempio:

```JAVA

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
```

## 2. Scrivi json dal file del foglio di calcolo allo stream di risposta.
```JAVA
            GridJsWorkbook wbj = new GridJsWorkbook();
            try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
                wbj.importExcelFile(filePath.toString());
                wbj.jsonToStream(gzipOutputStream, filename);
            } catch (IOException e) {
				e.printStackTrace();
            } catch (Exception e) {
				e.printStackTrace();
            }
```
## 3. Ottieni le immagini/forme dal file del foglio di calcolo
```JAVA
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.

InputStream inputStream = GridJsWorkbook.CacheImp.loadStream(fileid);
```
## 4. Aggiorna il file del foglio di calcolo in cache
```JAVA
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.updateCell(p, uid);
```
## 5. Salva il file del foglio di calcolo in cache
```JAVA
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.mergeExcelFileFromJson(uid, p);
wb.saveToCacheWithFileName(uid, filename,password);
```

Per ulteriori informazioni, puoi controllare l'esempio qui:
<https://github.com/aspose-cells/Aspose.Cells-for-java/tree/master/Examples_GridJs>
