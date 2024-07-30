---
title: Arbeta med GridJs på serversidan
type: docs
weight: 250
url: /sv/java/aspose-cells-gridjs/how-to-use-api/
description: Denna artikel beskriver hur man använder API er i GridJs.
keywords: GridJs, server, GridCacheForStream
aliases:
  - /java/aspose-cells-gridjs/server/
  - /java/aspose-cells-gridjs/server-api/
  - /java/aspose-cells-gridjs/api-introduction/
  - /java/aspose-cells-gridjs/how-to-use-apis/
  - /java/aspose-cells-gridjs/work-with-serverside-api/
  - /java/aspose-cells-gridjs/work-with-serverside-apis/
---


# Arbeta med GridJs på serversidan
## 0. Ange rätt mappväg i Config
 **`Config.setFileCacheDirectory`** för arbetsbokscache-filen (obligatorisk)
 **`Config.setPictureCacheDirectory`** för att spara bildfiler i arbetsboken (valfritt, standardvärdet är _piccache i filcache-mappen).

För lagringsdetaljer, vänligen kolla denna [guide](/java/aspose-cells-gridjs/storage/)

## 1. Implementera GridCacheForStream
För lokal fil lagring, här är ett exempel:

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

## 2. Skriv json från kalkylarksfilen till svarsströmmen
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
## 3. Hämta bilder/former från kalkylbladet
```JAVA
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.

InputStream inputStream = GridJsWorkbook.CacheImp.loadStream(fileid);
```
## 4. Uppdatera kalkylbladet i cache
```JAVA
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.updateCell(p, uid);
```
## 5. Spara kalkylbladet i cache
```JAVA
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.mergeExcelFileFromJson(uid, p);
wb.saveToCacheWithFileName(uid, filename,password);
```

För detaljerad info kan du kolla exemplet här:
<https://github.com/aspose-cells/Aspose.Cells-for-java/tree/master/Examples_GridJs>
