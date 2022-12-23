---
title: العمل مع تخزين GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/storage/
description: توضح هذه المقالة المعالجة العامة لـ Aspose.Cells.GridJs.
keywords: file cache,storage,GridJs,GridJs storage,GridJs uid,download,uniqueid
---
# العمل مع تخزين GridJs
## عملية الملف العامة
بعد استيراد ملف ورقة انتشار في الذاكرة وإظهار واجهة المستخدم ،

ستنشئ GridJs ملف ذاكرة تخزين مؤقت باستخدام معرف المستخدم المحدد ،

 بتنسيق[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

وبعد كل عملية تحديث في واجهة المستخدم ،

على سبيل المثال ، قم بتعيين قيمة الخلية ، وتعيين نمط الخلية ، وما إلى ذلك. و

سيطلق تطبيق js من جانب عميل GridJs إجراء وحدة التحكم للقيام بعملية UpdateCell.

في هذا الإجراء ، سيتم حفظ ملف ذاكرة التخزين المؤقت من الذاكرة أثناء طريقة UpdateCell.
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
### أين هو دليل ذاكرة التخزين المؤقت
A. إذا قمنا بتنفيذ GridCacheForStream وقمنا بتعيين GridJsWorkbook.CacheImp.
 على سبيل المثال في الكود أدناه ، يمكننا فقط وضع ملف ذاكرة التخزين المؤقت والحصول عليه من**"D: \ temp"**
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
إذا لم نقم بتعيين GridJsWorkbook.CacheImp ،

 سيقوم GridJs بإنشاء ملف وحفظه داخل ملف**الملف Config.FileCacheDirectory** ، وهو دليل ذاكرة التخزين المؤقت الافتراضي الذي يمكننا تعيينه.

### كيفية الحصول على ملف النتائج المحدث
#### 1. معرف مستخدم محدد للملف
 تأكد من تطابق الخريطة المحدد بين الملف والمعرف الفريد ،

يمكنك دائمًا الحصول على نفس معرف المستخدم لاسم ملف محدد ، وليس من إنشاء عشوائي.

على سبيل المثال فقط استخدم اسم الملف على ما يرام.
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

#### 2. تزامن مع عملية واجهة المستخدم
في الواقع بالنسبة لبعض عمليات واجهة المستخدم ،

على سبيل المثال:

تبديل ورقة النشاط إلى ورقة أخرى ،

تغيير موقع الصورة ،

تدوير / تغيير حجم الصورة ، وما إلى ذلك.

لن يتم تشغيل إجراء UpdateCell.

وبالتالي ، إذا أردنا الحصول على الملف المحدث تمامًا كما تظهر واجهة المستخدم ،

نحتاج إلى إجراء عملية دمج قبل حفظ الإجراء لمزامنة عملية واجهة المستخدم هذه.
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
#### 3. الحصول على الملف من ذاكرة التخزين المؤقت
على سبيل المثال: في إجراء التنزيل ، يمكنك فقط الحصول عليه من دليل ذاكرة التخزين المؤقت بواسطة uid.
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

لمزيد من المعلومات التفصيلية ، يمكنك التحقق من المثال هنا:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
