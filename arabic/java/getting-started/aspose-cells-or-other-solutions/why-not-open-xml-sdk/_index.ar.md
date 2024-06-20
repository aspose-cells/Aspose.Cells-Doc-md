---
title: لماذا لا نستخدم برنامج تطوير الواجهة البرمجية لـ Open XML؟
type: docs
weight: 20
url: /ar/java/why-not-open-xml-sdk/
---

{{% alert color="primary" %}} 

أحيانًا نسمع هذا السؤال:

**لماذا يجب علينا استخدام منتجات Aspose بدلاً عن مجانية Open XML SDK؟**

هذا السؤال سهل الإجابة: **الميزات والوظائف**.

{{% /alert %}} 
## **ما هو Open XML SDK؟**
وفقًا لمكتبة MSDN، يتم تعريف Open XML SDK على أنه: يبسط Open XML SDK 2.0 مهمة تلاعب حزم Open XML والعناصر الأساسية لمخطط Open XML داخل حزمة. يكتسب Open XML SDK 2.0 العديد من المهام الشائعة التي يقوم بها المطورون على حزم Open XML، بحيث يمكنك القيام بعمليات معقدة مع بضعة أسطر من الكود. تعتبر مستندات OOXML في أساسها ملفات XML مضغوطة ويعد Open XML SDK مجموعة من الفئات التي تسمح لك بالعمل مع محتوى مستندات OOXML بطريقة معتمدة بشكل قوي. وهذا بدلاً من فك ضغط ملف لاستخراج XML، وتحميل ذلك XML في شجرة DOM والعمل مع عناصر وسمات XML مباشرة، يوفر Open XML SDK فئات لفعل ذلك.
## **ما هو Aspose.Cells؟**
Aspose.Cells هي مكتبة فئات تسمح لتطبيقك بأداء المهمات التالية لمعالجة جداول البيانات: تحويل عالي الجودة بين جميع تنسيقات Excel الشهيرة، بما في ذلك التحويل إلى PDF وHTML وTIFF والطباعة. البرمجة مع نموذج كائن الورقة العمل. القدرة على بناء وثائق من شظايا من وثيقة واحدة أو متعددة، مع دمج البيانات تلقائيًا بتنسيقات الأناقة والرسوم البيانية والرسوم. وظائف عالية المستوى، مثل استيراد البيانات من مصادر بيانات مختلفة بما في ذلك Array وArrayList وDataTable / ResultSet. محرك حساب الصيغ القوي الذي يدعم جميع وظائف Microsoft Excel القياسية والمتقدمة تقريبًا.

{{% alert color="primary" %}}
## **قارن بين Open XML SDK وAspose.Cells**
الجدول التالي يقارن ميزات Open XML SDK وAspose.Cells.

|**ميزة أو فئة الميزات**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|صيغ Excel المدعومة أو صيغ أخرى|XLSX|XLS، CSV، SpreadsheetML 2003، XLSX، HTML، محددة بشكل جدولي، ODS، نص عادي (TXT)، PDF، XPS|
|التحويل بين صيغ Excel|لا|نعم|
|<p>برمجة عالية المستوى مع نموذج كائن لورقة العمل:</p><p>- البحث والاستبدال.</p><p>- تجميع جداول البيانات.</p><p>- نسخ الشظايا والأوراق العمل بين دفاتر العمل.</p>|لا|نعم|
|برمجة مفصلة مع نموذج كائن لوثيقة، والوصول إلى العناصر الفردية وخصائص التنسيق لجميع عناصر جدول البيانات.|نعم|نعم|
|وصول مباشر وكامل على مستوى منخفض إلى العناصر والسمات الأساسية للـ XML، مثل معرفات العلاقة، ومعرفات القوائم لمستند OOXML.|نعم|لا|
|<p>إنشاء تقارير، ملء الوثائق بالبيانات:</p><p>- استيراد / تصدير البيانات إلى / من *DataTable /* ResultSet.</p><p>- ميزة العلامات الذكية.</p><p>- إدراج / حذف الصفوف / الأعمدة / النطاقات.</p><p>- مصادر البيانات المخصصة.</p>|لا|نعم|
|<p>عرض وطباعة:* عرض صفحات ورقة العمل إلى صور نقطية (TIFF، TIFF متعددة الصفحات، PNG، JPEG، BMP).* عرض صفحات جدول البيانات إلى صور ناقلة (EMF).* تحويل الرسوم البيانية إلى صور (TIFF، TIFF متعددة الصفحات، PNG، JPEG، BMP، EMF وغيرها).</p><p>- تحديد دقة الصورة والجودة والضغط وخيارات أخرى.</p><p>- طباعة جداول البيانات باستخدام بنية الطباعة .NET. العنصر يحتوي على طريقة طباعة مدمجة لطباعة الأوراق العمل كما هو موضح في معاينة الطباعة في MS Excel.</p>|لا|نعم|
|حساب / إعادة حساب الصيغ بطريقة ديناميكية|لا|نعم|
|المنصات المدعومة|Windows، .NET|Windows، Linux، Java، .NET، Mono|
## **الاستنتاج**
  {{% alert color="primary" %}}Open XML SDK and Aspose.Cells do not compete head to head because they address quite different needs and audiences. Open XML SDK is a class library to provide a strong-typed way to work with OOXML documents. Aspose.Cells is a very useful spreadsheet processing library that provides great support for all Microsoft Excel and other file formats. If all you need to do is a fairly basic programming operation on a XLSX document, then Open XML SDK might be a suitable choice. With Open XML SDK you will be fairly comfortable doing simple tasks like generating a simple XLSX document or removing comments, headers/footers, extracting images or others. Some tasks can be achieved with Open XML SDK, but cannot be achieved with Aspose.Cells. For example, if you need to directly access the XML elements and attributes of an OOXML document, then you should use Open XML SDK.However, if you need to perform complex operations on documents, such as some of the following tasks, then using Aspose.Cells is your best option: Support other file formats in addition to XLSX. Copy fragments and worksheets between workbooks or join workbooks in a way that combines objects, styles and other formatting in an appropriate manner. Replace formatted or unformatted text. High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet. Generate a business document, such as an order with order details from a data source. Convert a document to PDF or XPS so it appears exactly like Microsoft Excel would have converted it. Develop a .NET or Java application. {{% /alert %}}
