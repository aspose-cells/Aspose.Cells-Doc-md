---
title: GridJs Sunucu Tarafı ile Çalışmak
type: docs
weight: 250
url: /tr/java/aspose-cells-gridjs/how-to-use-api/
description: Bu makale, GridJs deki API leri nasıl kullanacağınızı açıklar.
keywords: GridJs, sunucu, GridCacheForStream
aliases:
  - /java/aspose-cells-gridjs/server/
  - /java/aspose-cells-gridjs/server-api/
  - /java/aspose-cells-gridjs/api-introduction/
  - /java/aspose-cells-gridjs/how-to-use-apis/
  - /java/aspose-cells-gridjs/work-with-serverside-api/
  - /java/aspose-cells-gridjs/work-with-serverside-apis/
---


# GridJs Sunucu Tarafı ile Çalışmak
## 0. Config'de doğru klasör yolunu ayarlayın
 **`Config.setFileCacheDirectory`** çalışma kitabı önbellek dosyası için (gereklidir).
 **`Config.setPictureCacheDirectory`**  çalışma kitabındaki resim dosyaları önbelleği için (isteğe bağlı, varsayılan değer _piccache dosya önbellek dizininde).

depolama detayları için lütfen bu [rehbere](/java/aspose-cells-gridjs/storage/) bakın

## 1. GridCacheForStream’i uygulayın
Yerel dosya depolama için burada bir örnek:

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

## 2. Çalışma sayfası dosyasından json yazarak yanıt akışına yaz.
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
## 3. Çalışma tablosundan resimleri/şekilleri alın
```JAVA
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.

InputStream inputStream = GridJsWorkbook.CacheImp.loadStream(fileid);
```
## 4. Önbellekte çalışma tablosunu güncelle
```JAVA
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.updateCell(p, uid);
```
## 5.  Önbellekte çalışma tablosunu kaydedin
```JAVA
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.mergeExcelFileFromJson(uid, p);
wb.saveToCacheWithFileName(uid, filename,password);
```

Detaylı bilgiler için buradaki örneği kontrol edebilirsiniz:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples_GridJs>
