---
title: العمل مع الخادم الجانبي لـ GridJs
type: docs
weight: 250
url: /ar/java/aspose-cells-gridjs/how-to-use-api/
description: يصف هذا المقال كيفية استخدام واجهات برمجة التطبيقات في جريدجس.
keywords: جريدجس، الخادم، GridCacheForStream
aliases:
  - /java/aspose-cells-gridjs/server/
  - /java/aspose-cells-gridjs/server-api/
  - /java/aspose-cells-gridjs/api-introduction/
  - /java/aspose-cells-gridjs/how-to-use-apis/
  - /java/aspose-cells-gridjs/work-with-serverside-api/
  - /java/aspose-cells-gridjs/work-with-serverside-apis/
---


# العمل مع الخادم الجانبي لـ GridJs
## 0. قم بتعيين مسار المجلد الصحيح في التكوين
 **`Config.setFileCacheDirectory`** لملف التخزين المؤقت للورقة (مطلوب).
 **`Config.setPictureCacheDirectory`** لتخزين ملفات الصور في الورقة (اختياري، القيمة الافتراضية هي _piccache في دليل تخزين الملفات).

لحصول على تفاصيل التخزين، يرجى التحقق من هذا [الدليل](/java/aspose-cells-gridjs/storage/)

## 1. تنفيذ GridCacheForStream
بالنسبة لتخزين الملفات المحلي ، إليك مثال:

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

## 2. كتابة json من ملف ورق العمل إلى تيار الرد.
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
## 3. احصل على الصور/الأشكال من ملف جدول البيانات
```JAVA
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.

InputStream inputStream = GridJsWorkbook.CacheImp.loadStream(fileid);
```
## 4. تحديث ملف جدول البيانات في الذاكرة المؤقتة
```JAVA
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.updateCell(p, uid);
```
## 5.  حفظ ملف جدول البيانات في الذاكرة المؤقتة
```JAVA
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.mergeExcelFileFromJson(uid, p);
wb.saveToCacheWithFileName(uid, filename,password);
```

للحصول على معلومات مفصلة ، يمكنك التحقق من المثال هنا:
<https://github.com/aspose-cells/Aspose.Cells-for-java/tree/master/Examples_GridJs>
