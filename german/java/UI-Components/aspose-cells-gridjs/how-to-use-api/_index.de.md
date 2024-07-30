---
title: Arbeiten mit GridJs Server Side
type: docs
weight: 250
url: /de/java/aspose-cells-gridjs/how-to-use-api/
description: In diesem Artikel wird beschrieben, wie man APIs in GridJs verwendet.
keywords: GridJs,server,GridCacheForStream
aliases:
  - /java/aspose-cells-gridjs/server/
  - /java/aspose-cells-gridjs/server-api/
  - /java/aspose-cells-gridjs/api-introduction/
  - /java/aspose-cells-gridjs/how-to-use-apis/
  - /java/aspose-cells-gridjs/work-with-serverside-api/
  - /java/aspose-cells-gridjs/work-with-serverside-apis/
---


# Arbeiten mit GridJs Server Side
## 0. Den richtigen Ordnerpfad in der Konfiguration einstellen
 **`Config.setFileCacheDirectory`** für die Arbeitsmappe-Cache-Datei (erforderlich).
 **`Config.setPictureCacheDirectory`** für die Bild-Dateien-Cache in der Arbeitsmappe (optional, der Standardwert ist _piccache im Datei-Cache-Verzeichnis).

Für Details zur Speicherung schauen Sie sich dieses [Handbuch](/java/aspose-cells-gridjs/storage/) an

## 1. Implementieren von GridCacheForStream
Für die lokale Dateispeicherung, hier ist ein Beispiel:

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

## 2. Schreiben von JSON aus der Tabellendatei in den Antwort-Stream.
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
## 3. Holen Sie sich die Bilder/Formen aus der Tabellenkalkulationsdatei
```JAVA
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.

InputStream inputStream = GridJsWorkbook.CacheImp.loadStream(fileid);
```
## 4. Aktualisieren Sie die Tabellenkalkulationsdatei im Cache
```JAVA
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.updateCell(p, uid);
```
## 5.  Tabellendatei im Cache speichern
```JAVA
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.mergeExcelFileFromJson(uid, p);
wb.saveToCacheWithFileName(uid, filename,password);
```

Für weitere Details können Sie hier das Beispiel überprüfen:
<https://github.com/aspose-cells/Aspose.Cells-for-java/tree/master/Examples_GridJs>
