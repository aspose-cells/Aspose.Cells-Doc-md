---
title: العمل مع تخزين GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/storage/
description: يصف هذا المقال معالجة الملف العام لـ GridJs.
keywords: مخزن الملف، التخزين، GridJs، تخزين GridJs، معرف فريد، تنزيل، معرف فريد
aliases:
  - /net/aspose-cells-gridjs/storage-introduction/
  - /net/aspose-cells-gridjs/work-with-storage/
---


# العمل مع تخزين GridJs
##  عملية الملف العامة 

بعد استيراد ملف جدول بيانات ،

سيقوم GridJs بإنشاء ملف ذاكرة تخزين مؤقت بمعرف فريد محدد وفقًا لتنفيذ GridCacheForStream،

بتنسيق [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat")،

سيحفظ GridJs أيضًا جميع الأشكال/الصور في ملف أرشيف zip في مجلد التخزين المؤقت لعرض الأشكال/الصور لاحقًا في واجهة المستخدم الخاصة بالعميل.

وبعد كل عملية تحديث في واجهة المستخدم،

على سبيل المثال تعيين قيمة الخلية ، تعيين نمط الخلية، وما إلى ذلك،

مستوى العميل لجافا سكريبت من GridJs سيقوم بتشغيل إجراء وحدة التحكم لإجراء عملية تحديث.

في هذا العمل يحدث حفظ مرة أخرى إلى الملف المؤقت أثناء طريقة التحديث الخلية.
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
### أين يكون الملف المخبأ بالضبط؟ 

أ. إذا قمت بتنفيذ GridCacheForStream بنفسك.
على سبيل المثال في الكود أدناه يمكننا فقط وضع والحصول على ملف التخزين المؤقت من **"D:\temp"**
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
ب. إذا لم تقم بضبط GridJsWorkbook.CacheImp، 

لقد نفذت GridJs ذلك بشكل افتراضي بالفعل.

سيقوم GridJs بإنشاء وحفظ ملف ذاكرة التخزين المؤقت ضمن المسار: **`Config.FileCacheDirectory/streamcache`** .

### كيفية الحصول على ملف النتيجة المحدث
#### 1. إنشاء معرف فريد محدد للملف 
تأكد من وجود توافق تعيين خريطة محددة بين الملف ومعرف اليوسيدي، 

على سبيل المثال 

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


#### 2. الحصول على الملف من الذاكرة المؤقتة بواسطة المعرف الفريد
على سبيل المثال: في عملية التحميل، يمكنك فقط الحصول عليه من دليل الذاكرة المؤقتة بواسطة المعرف الفريد واسم الملف.
```C#
	 Stream fileStream = GridJsWorkbook.CacheImp.LoadStream(uid + "/" + filename);
```

للمزيد من المعلومات التفصيلية، يمكنك التحقق من المثال هنا:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
