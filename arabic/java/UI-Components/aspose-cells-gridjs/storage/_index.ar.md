---
title: العمل مع تخزين GridJs
type: docs
weight: 250
url: /ar/java/aspose-cells-gridjs/storage/
description: يصف هذا المقال معالجة الملف العام لـ GridJs.
keywords: مخزن الملف، التخزين، GridJs، تخزين GridJs، معرف فريد، تنزيل، معرف فريد
aliases:
  - /java/aspose-cells-gridjs/storage-introduction/
  - /java/aspose-cells-gridjs/work-with-storage/
---


# العمل مع تخزين GridJs
##  عملية الملف العامة 
بعد استيراد ملف جدول بيانات ،

سيقوم GridJs بإنشاء ملف تخزين مؤقت بالمعرف المحدد في المجلد **`Config.getFileCacheDirectory()`**،

بتنسيق [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/java/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat")، 

ستقوم GridJs أيضًا بحفظ كل الأشكال/الصور في ملف ضغط zip في مجلد `Config.getPictureCacheDirectory()` لعرض الأشكال/الصور في واجهة المستخدم الخاصة بالعميل في وقت لاحق.

وبعد كل عملية تحديث في واجهة المستخدم،

على سبيل المثال تعيين قيمة الخلية ، تعيين نمط الخلية، وما إلى ذلك،

ستقوم واجهة المستخدم الخاصة بـ GridJs بتشغيل عملية تحديث الخلية.

في هذا العمل يحدث حفظ مرة أخرى إلى الملف المؤقت أثناء طريقة التحديث الخلية.
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
### أين يكون الملف المخبأ بالضبط؟ 

أ. إذا قمنا بتنفيذ GridCacheForStream وضبط GridJsWorkbook.CacheImp.
على سبيل المثال في الكود أدناه يمكننا فقط وضع والحصول على ملف التخزين المؤقت من **"D:\temp"**
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
ب. إذا لم نقم بضبط GridJsWorkbook.CacheImp

ستقوم GridJs بإنشاء وحفظ الملف ضمن مجلد `Config.getFileCacheDirectory()`، وهو دليل الذاكرة المؤقتة الافتراضي الذي يمكننا تعيينه.

### كيفية الحصول على ملف النتيجة المحدث
#### 1. معرّف محدد للملف 
تأكد من وجود توافق تعيين خريطة محددة بين الملف ومعرف اليوسيدي، 

يمكنك دائمًا الحصول على نفس معرف اليوسيدي لاسم ملف محدد، ليس من توليد عشوائي.

على سبيل المثال، ما عليك سوى استخدام اسم الملف.
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

#### 2. مزامنة مع عملية واجهة المستخدم للعميل
في الواقع، بالنسبة لبعض عمليات واجهة المستخدم الخاصة بالعميل،

على سبيل المثال:

تبديل الورقة النشطة إلى أخرى،

تغيير موقع الصورة،

تدوير/تغيير حجم الصورة، إلخ.

لن تتم تفعيل إجراء تحديث الخلية.

بالتالي، إذا كنا نريد الحصول على ملف محدث تمامًا كما يظهر واجهة المستخدم الخاصة بالعميل،

نحتاج إلى القيام بعملية دمج قبل إجراء توصية بحفظ لمزامنة تلك العمليات واجهة المستخدم الخاصة بالعميل.
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
#### 3. الحصول على رابط الملف من الذاكرة المؤقتة
على سبيل المثال: في إجراء التنزيل، يمكنك ببساطة الحصول عليه من دليل الذاكرة المؤقتة عن طريق مُعرِّّف الوحدة.
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

للمزيد من المعلومات التفصيلية، يمكنك التحقق من المثال هنا:
<https://github.com/aspose-cells/Aspose.Cells-for-java/tree/master/Examples_GridJs>
