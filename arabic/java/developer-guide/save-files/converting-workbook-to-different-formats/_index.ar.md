---
title: تحويل ورقة العمل إلى تنسيقات مختلفة
type: docs
weight: 20
url: /ar/java/converting-workbook-to-different-formats/
---

{{% alert color="primary" %}}

Aspose.Cells تدعم تحويل بين العديد من الصيغ. من الناحية التقنية، التحويل يعني تحميل جدول عمل في تنسيق ملف معين وحفظه في تنسيق آخر.

{{% /alert %}}

## **تحويل Excel إلى XPS**

تنسيق مستند XPS يتألف من وسم XML منظم يحدد تخطيط المستند والمظهر البصري لكل صفحة، جنبًا إلى جنب مع قواعد العرض لتوزيع وأرشفة وعرض ومعالجة وطباعة المستندات.

لغة الوسم لـ XPS هي جزء من XAML الذي يسمح لها بدمج عناصر الرسوميات النقطية في المستندات، باستخدام XAML لتعليم عناصر واجهة برنامج التقديم لـ Windows (WPF) الأساسية. توصف العناصر المستخدمة من حيث المسارات والأشكال الهندسية الأخرى.

الملف XPS في الواقع يعتبر أرشيف ZIP مشفر يستخدم طرائق التعبئة المفتوحة، يضم الملفات التي تشكل المستند. تتضمن هذه الملفات ملف وسم XML لكل صفحة، نص، خطوط مضمنة، صور نقطية، رسوميات ناقلة ثنائية الأبعاد، بالإضافة إلى معلومات إدارة الحقوق الرقمية. يمكن فحص محتويات ملف XPS ببساطة عن طريق فتحه في تطبيق يدعم ملفات ZIP.

من Aspose.Cells 6.0.0، يتم دعم تحويل Microsoft Excel إلى XPS.

### **تحويل ورقة عمل واحدة إلى XPS**

المثال التالي يوضح كيفية تحويل ورقة عمل واحدة في ملف Excel إلى XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **تصدير الدفتر كاملاً إلى XPS**

يوضح المثال التالي كيفية تحويل الدفتر كاملاً إلى تنسيق XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **تحويل سريع من Excel إلى XPS**

المثال التالي يوضح طريقة بسيطة لتحويل مباشرة ملف Excel إلى تنسيق XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **تحويل Excel إلى ملفات MHTML**

[**MHTML**](https://en.wikipedia.org/wiki/MHTML) يجمع بين HTML العادي مع الموارد الخارجية، وهي المحتوى الذي عادة ما يتم ربطه مثل الصور والرسوم المتحركة والصوت وما إلى ذلك في ملف واحد. يتم استخدامها لرسائل البريد الإلكتروني بامتداد الملف .mht.

{{% alert color="primary" %}}

Aspose.Cells تدعم قراءة وكتابة ملفات MHTML.

{{% /alert %}}

تحويل جدول بيانات إلى MHTML عملية سريعة، كما هو موضح أدناه.

يوضح المثال البرمجي أدناه كيفية حفظ دفتر العمل كملف MHTML.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **تحويل ملفات Excel إلى HTML**

توفر واجهات برمجة التطبيقات Aspose.Cells دعماً لتصدير الجداول الحسابية إلى تنسيق HTML. لهذا الغرض، تستخدم Aspose.Cells الفئة [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) التي تسمح للمطورين بالتحكم في العديد من جوانب HTML الإخراج.

الكود أدناه يظهر كيفية استخدام فئة [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) لتصدير ملفات Microsoft Excel إلى تنسيق HTML دون تحديد معلمات إضافية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

يمكنك تحقيق نفس النتائج عن طريق تمرير [**SaveFormat.HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML) إلى الطريقة [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)).

{{% /alert %}}

### **ضبط تفضيلات الصور لصيغة HTML**

ابتداءً من الإصدار 8.0.2، فقد قدمت Aspose.Cells [**ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) للفئة [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)، مما يتيح للمطورين تحديد تفضيلات الصور عند حفظ جداول البيانات في تنسيق HTML.

تفضيلات الصور التي يمكن تطبيقها هي:

- [**ImageType**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType): يحصل على أو يعين نوع الصورة. يرجى ملاحظة أن جميع الأشكال، بما في ذلك الرسوم البيانية، يتم عرضها على هيئة صور في ملف الإخراج HTML.
- [**Quality**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality): يحصل على أو يعين جودة الصور بين 0 إلى 100، عندما يتم تحديد ImageFormat ك Jpeg.
- [**VerticalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution): يحصل على أو يعين الدقة العمودية للصورة بوحدات في البوصة.
- [**HorizontalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution): يحصل على أو يعين الدقة الأفقية للصورة بوحدات في البوصة.
- [**TiffCompression**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression): يحصل على أو يعين نوع الضغط للصور عندما يتم تحديد ImageFormat ك Tiff.
- [**Transparent**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent): يدل على ما إذا كان خلفية الصورة يجب أن تكون شفافة عندما يتم تحديد ImageFormat ك Png.

الكود أدناه يوضح كيفية استخدام [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) لتحديد تفضيلات مختلفة.

|**عرض الجدول الحسابي قبل التصدير**|**عرض HTML بعد التصدير**|
| :- | :- |
|![عرض الجدول الحسابي قبل التصدير](converting-workbook-to-different-formats_1.png)|![عرض HTML بعد التصدير](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **تحويل Excel إلى ملفات PDF**

تُستخدم مستندات PDF على نطاق واسع كصيغة قياسية لتبادل المستندات بين المؤسسات والقطاعات الحكومية والأفراد. غالبًا ما يُطلب من المطورين البرمجيين إيجاد وسيلة لتحويل ملفات Microsoft Excel بسهولة إلى مستندات PDF. تدعم Aspose.Cells هذه الميزات. يوضح هذا المقال كيفية القيام بذلك.

### **تحويل Excel إلى PDF**

تم تقديم تحويل Microsoft Excel إلى PDF مع الإصدار Aspose.Cells for Java 2.3.0. منذ ذلك الإصدار، يمكن لـ Aspose.Cells [تحويل جداول البيانات إلى PDF مباشرة](#direct-conversion) (بما في ذلك [PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files))، بدون منتج آخر. لتحويل جداول البيانات باستخدام الإصدارات الأقدم من Aspose.Cells، [استخدم Aspose.PDF للتحويل](#conversion-with-asposepdf-asposecells-prior-to-230).

يُقوم Aspose.Cell's بتحويل جداول البيانات إلى PDF بدرجة عالية من الدقة والموثوقية. ومع ذلك، هناك بعض ال [قيود](/cells/ar/java/converting-workbook-to-different-formats/#conversion-attributes)، مُدرجة في نهاية هذا المقال.

{{% alert color="primary" %}}

يكتب Aspose.Cells for Java مباشرة المعلومات حول واجهة برمجة التطبيقات ورقم الإصدار في المستندات الناتجة. على سبيل المثال، عند تقديم مستند إلى PDF، يقوم Aspose.Cells for Java بملأ حقل **Application** بالقيمة 'Aspose.Cells' وحقل **PDF Producer** بقيمة مثل 'Aspose.Cells for Java v17.9'.

يرجى ملاحظة أنه لا يمكنك توجيه Aspose.Cells for Java لتغيير أو إزالة هذه المعلومات من المستندات الناتجة.

{{% /alert %}}

#### **التحويل المباشر**

حفظ ملف Excel مباشرة إلى PDF باستخدام الطريقة [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) وتوفير واجهة العضو [**SaveFormat.PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF). مثل هذا التحويل المباشر هو الأكثر كفاءة. فهو لا يفقد البيانات أو التنسيق ولكنه يبقي ملف PDF الناتج يبدو كملف Excel الداخلي.

لاختيار خيارات الأمان عند الحفظ إلى PDF، استخدم [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **التحويل المتقدم**

يمكنك أيضًا استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) لتعيين سمات مختلفة للتحويل. تعيين خصائص مختلفة لفئة [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) سيمنحك السيطرة على إعدادات الطباعة والخط والأمان والضغط لملف PDF الناتج. الخاصية الأبرز هي [**Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance) التي تمكنك من حفظ ملفات Excel إلى ملفات PDF/A متوافقة بتنسيق PDF.

##### **حفظ جداول الإكسل في ملفات PDF/A متوافقة**

الكود أدناه يوضح استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) لحفظ ملفات Excel بتنسيق PDF/A متوافق بتنسيق PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **التحويل باستخدام Aspose.Pdf: Aspose.Cells قبل الإصدار 2.3.0**

بالنسبة لنسخ Aspose.Cells السابقة للإصدار 2.3.0، يجب عليك استخدام مكون مثل [Aspose.PDF for Java](/pdf/java/) لتحويل جداول البيانات إلى ملفات PDF. تعمل Aspose.Cells و Aspose.PDF معًا لتحويل جدول بيانات إلى PDF عبر خطوة وسيطة.

لتحويل جداول البيانات إلى PDF باستخدام Aspose.Cells وAspose.PDF:

1. قم بإنشاء كائن من فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) بالاتصال ببنائه الفارغ.
1. اقم بعملك المطلوب على جدول البيانات باستخدام واجهة برمجة التطبيقات Aspose.Cells.
1. استدعي الطريقة [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) لحفظ جدول البيانات:
   1. تعيين تنسيق الملف إلى XML.
   1. حدد Aspose_Pdf (قيمة محددة مسبقًا) من واجهة FileFormatType. يوجه هذا الإجراء الأسلوب حفظ لتوليد جدول بيانات بتنسيق XML متوافق مع مخطط Aspose.PDF بحيث يمكن لـ Aspose.PDF لـ Java بعد ذلك توليد وثيقة PDF.
1. عند إنشاء ملف XML، قم بإنشاء كائن من فئة Pdf في حزمة aspose.pdf.
1. استدعاء الطريقة bindXML في فئة Pdf وتمرير اسم ملف الإخراج XML.
1. استدعاء الطريقة save في فئة Pdf لتوليد وثيقة PDF.

يتم تنفيذ الخطوات أعلاه أدناه في مثال.

{{% alert color="primary" %}}

إذا كان جدول البيانات الخاص بك يحتوي على صيغ، فمن الأفضل استدعاء الطريقة [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) قبل عرض الجدول بتنسيق PDF. سيضمن ذلك إعادة حساب القيم التي تعتمد على الصيغة، وعرض القيم الصحيحة في PDF.

{{% /alert %}}

#### **سمات التحويل**

نحن نعمل بجد لتحسين معدل التحويل وجوانب أخرى لـ Aspose.Cells مع كل إصدار. لدينا بعض القيود في تحويل Excel إلى PDF. قد تفقد بعض إعدادات التنسيق المحددة في جدول بيانات، ولن يتم دعم كل الكائنات الرسمية.

الجدول أدناه يوضح جميع الميزات المعتمدة جزئيا أو تمامًا عند تصدير إلى PDF باستخدام Aspose.Cells. هذا الجدول ليس نهائيًا ولا يغطي جميع خصائص جدول البيانات. كما يمكن له تحديد تلك الميزات التي قد لا تكون معتمدة أو مدعومة جزئيًا للتحويل.

{{% alert color="primary" %}}

|**عنصر المستند**|**الخاصية**|**مدعومة بشكل صافي**|**ملاحظات**|
| :- | :- | :- | :- |
|المحاذاة| |نعم| |
|الدوران| |جزئيًا|يدعم فقط 90 و -90.|
|إعدادات الخلفية| |نعم| |
|الحدود|لون|نعم| |
|الحدود|نمط الخط|نعم| |
|الحدود|سمك الخط|نعم| |
|بيانات الخلية| |نعم| |
|التعليقات| |لا| |
|تنسيق شرطي| |نعم| |
|خصائص المستند| |نعم| |
|كائنات الرسم| |نعم| |
|الخط|الحجم|نعم| |
|الخط|اللون|نعم| |
|الخط|النمط|نعم| |
|الخط|التسطير|نعم| |
|الخط|تأثيرات|جزئيًا|يتم دعم تأثير الخط العابر فقط|
|الصور| |نعم| |
|الارتباط| |نعم| |
|رسوم بيانية| |نعم| |
|الخلايا المدمجة| |نعم| |
|فاصل الصفحة| |نعم| |
|إعداد الصفحة|الرأس/التذييل|نعم| |
|إعداد الصفحة|الهوامش|نعم| |
|إعداد الصفحة|اتجاه الصفحة|نعم| |
|إعداد الصفحة|حجم الصفحة|نعم| |
|إعداد الصفحة|منطقة الطباعة|نعم| |
|إعداد الصفحة|عناوين الطباعة|نعم| |
|إعداد الصفحة|تحجيم|نعم| |
|ارتفاع الصف/عرض العمود| |نعم| |
{{% /alert %}}
