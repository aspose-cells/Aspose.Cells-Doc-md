---
title: العمل مع تخزين GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/storage/
description: يصف هذا المقال معالجة الملف العام لـ GridJs.
keywords: مخزن الملف، التخزين، GridJs، تخزين GridJs، معرف فريد، تنزيل، معرف فريد
---


# العمل مع تخزين GridJs
##  عملية الملف العامة 
بعد استيراد ملف جدول بيانات ،

سيقوم GridJs بإنشاء ملف ذاكرة مؤقتة بالمعرف المحدد في مجلد **`Config.FileCacheDirectory`**،

بتنسيق [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat")،

سوف يقوم GridJs أيضًا بحفظ جميع الأشكال/الصور في ملف أرشيف ضغط في مجلد **`Config.PictureCacheDirectory`** لعرض الأشكال/الصور لاحقًا في واجهة المستخدم الخاصة.

وبعد كل عملية تحديث في واجهة المستخدم،

على سبيل المثال تعيين قيمة الخلية ، تعيين نمط الخلية، وما إلى ذلك،

ستقوم واجهة المستخدم الخاصة بـ GridJs بتشغيل عملية تحديث الخلية.

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

أ. إذا قمنا بتنفيذ GridCacheForStream وضبط GridJsWorkbook.CacheImp.
على سبيل المثال في الكود أدناه يمكننا فقط وضع والحصول على ملف التخزين المؤقت من **"D:\temp"**
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
ب. إذا لم نقم بضبط GridJsWorkbook.CacheImp

سوف تقوم GridJs بإنشاء ملف حفظ داخل **`Config.FileCacheDirectory`**، وهو الدليل الافتراضي للتخزين المؤقت الذي يمكننا ضبطه.

### كيفية الحصول على ملف النتيجة المحدث
#### 1. معرّف محدد للملف 
تأكد من وجود توافق تعيين خريطة محددة بين الملف ومعرف اليوسيدي، 

يمكنك دائمًا الحصول على نفس معرف اليوسيدي لاسم ملف محدد، ليس من توليد عشوائي.

على سبيل المثال، ما عليك سوى استخدام اسم الملف.
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
```C#
//in controller action 
  GridJsWorkbook wb = new GridJsWorkbook();
  wb.MergeExcelFileFromJson(uid, p);
  //after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
  wb.SaveToXlsx(Path.Combine(Config.FileCacheDirectory, uid));
```         
#### 3. الحصول على الملف من الذاكرة المؤقتة
على سبيل المثال: في إجراء التنزيل، يمكنك ببساطة الحصول عليه من دليل الذاكرة المؤقتة عن طريق مُعرِّّف الوحدة.
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

للمزيد من المعلومات التفصيلية، يمكنك التحقق من المثال هنا:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
