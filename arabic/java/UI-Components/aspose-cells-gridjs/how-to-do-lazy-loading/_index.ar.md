---
title: كيفية عمل التحميل الكسول في GridJs  
type: docs
weight: 250
url: /ar/java/aspose-cells-gridjs/how-to-do-lazy-loading/
description: تصفيرح هذه المقالة كيفية تنفيذ التحميل الكسول في GridJs.
keywords: GridJs،التحميل الكسول،التحميل عند الطلب،
aliases:
  - /java/aspose-cells-gridjs/lazy-loading/
  - /java/aspose-cells-gridjs/loading-on-demand/

---

## حول التحميل الكسول 
عند التعامل مع ملف جدول بيانات يحتوي على العديد من أوراق العمل، يمكننا تحسين عملية التحميل عن طريق تحميل ورقة العمل النشطة فقط في البداية.

هذه الاستراتيجية تضمن أن استجابة JSON من جانب السيرفر تشمل البيانات ذات الصلة بورقة العمل المختارة فقط في البداية.  

نتيجة لذلك، يقل حركة المرور الأولية بشكل كبير، مما يعزز تجربة المستخدم عن طريق تقليل أوقات التحميل.  

علاوة على ذلك، صُمم GridJs للاستجابة بشكل ديناميكي لتفاعلات المستخدم. تحديدًا، عندما ينقر المستخدم على ورقة عمل مختلفة،

يقوم GridJs بشكل ذكي بإرسال طلب إلى الخادم للحصول على البيانات المتعلقة بتلك الورقة فقط.  

هذه الآلية للتحميل عند الطلب لا تقلل فقط من نقل البيانات غير الضروري، بل تضمن أيضًا أن يكون لدى المستخدم دائمًا أحدث المعلومات الخاصة بورقة العمل التي يعمل عليها حاليًا.  

باتباع هذا النهج، لا نعمل فقط على تحسين وقت التحميل الأولي، بل نحافظ أيضًا على تطبيق سريع وفعال يتكيف جيدًا مع زيادة عدد أوراق العمل في ملف الجدول.

# لتنفيذ التحميل الكسول في GridJs، الخطوات هي
## ضبط خيار التكوين للتحميل الكسول.
على سبيل المثال:
```java 
  Config.setLazyLoading(true);
```
## ضبط عنوان URL للإجراء للتحميل الكسول.
على سبيل المثال:
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
بعد نقر المستخدم على ورقة عمل أخرى غير النشطة، سيتم تفعيل عملية استعلام البيانات تلقائيًا بواسطة تطبيق الجدول الإلكتروني. 

## تنفيذ إجراء التحميل الكسول في وحدة التحكم على جانب الخادم.
على سبيل المثال:
```java
    @PostMapping("/LazyLoading")
    public void lazyLoadingStreamJson(
            @RequestParam(value = "name", required = false) String sheetName,
            @RequestParam(value = "uid", required = false) String uid,
            HttpServletResponse response) throws IOException {

        GridJsWorkbook wbj = new GridJsWorkbook();
        response.setContentType(MediaType.APPLICATION_JSON_VALUE);
        response.setHeader(HttpHeaders.CONTENT_ENCODING, "gzip");

        try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
            try {
				wbj.lazyLoadingStream(gzipOutputStream, uid, sheetName);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        }
    }
```





