---
title: تحويل المصنف إلى تنسيقات مختلفة
type: docs
weight: 20
url: /ar/java/converting-workbook-to-different-formats/
---
{{% alert color="primary" %}}

Aspose.Cells يدعم التحويل بين العديد من الصيغ. من الناحية الفنية ، يعني التحويل تحميل مصنف بتنسيق ملف واحد وحفظه في تنسيق آخر.

{{% /alert %}}

## **تحويل ملف Excel إلى XPS**

يتكون تنسيق المستند XPS من علامات XML الهيكلية التي تحدد مخطط المستند والمظهر المرئي لكل صفحة ، إلى جانب قواعد العرض لتوزيع المستندات وأرشفتها وتقديمها ومعالجتها وطباعتها.

لغة الترميز لـ XPS هي مجموعة فرعية من XAML والتي تسمح لها بدمج العناصر الرسومية المتجهة في المستندات ، باستخدام XAML لترميز العناصر الأولية Windows Presentation Foundation (WPF). يتم وصف العناصر المستخدمة من حيث المسارات والأوليات الهندسية الأخرى.

ملف XPS هو في الواقع أرشيف مضغوط Unicoded يستخدم اصطلاحات التغليف المفتوح ، التي تحتوي على الملفات التي تتكون منها الوثيقة. يتضمن ذلك ملف ترميز XML لكل صفحة ، ونص ، وخطوط مضمنة ، وصور نقطية ، ورسومات متجهة ثنائية الأبعاد ، بالإضافة إلى معلومات إدارة الحقوق الرقمية. يمكن فحص محتويات ملف XPS ببساطة عن طريق فتحه في تطبيق يدعم ملفات ZIP.

من Aspose.Cells 6.0.0 ، Microsoft يتم دعم تحويل Excel tp XPS.

### **تحويل ورقة عمل واحدة إلى XPS**

يوضح المثال التالي كيفية تحويل ورقة عمل واحدة في ملف Excel إلى XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **تصدير مصنف كامل إلى XPS**

يوضح المثال التالي كيفية تحويل المصنف بأكمله إلى تنسيق XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **اكسل السريع لتحويل XPS**

يوضح المثال التالي طريقة بسيطة لتحويل ملف Excel مباشرة إلى تنسيق XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **تحويل ملفات Excel إلى MHTML**

[MHTML](https://en.wikipedia.org/wiki/MHTML) يجمع بين HTML العادي والموارد الخارجية ؛ أي المحتوى الذي يتم ربطه عادةً مثل الصور والرسوم المتحركة والصوت وما إلى ذلك في ملف واحد. يتم استخدامها لرسائل البريد الإلكتروني بامتداد الملف .mht.

{{% alert color="primary" %}}

يدعم Aspose.Cells قراءة وكتابة ملفات MHTML.

{{% /alert %}}

يعد تحويل جدول بيانات إلى MHTML عملية سريعة ، كما هو موضح أدناه.

يوضح مثال الرمز أدناه كيفية حفظ مصنف كملف MHTML.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **تحويل ملفات Excel إلى HTML**

 توفر واجهات برمجة التطبيقات Aspose.Cells الدعم لتصدير جداول البيانات بتنسيق HTML. لهذا الغرض ، يستخدم Aspose.Cells الامتداد**[HtmlSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**فئة تسمح للمطورين بالتحكم في عدة جوانب من الناتج HTML.

يوضح الكود أدناه كيفية استخدام ملف**[HtmlSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**فئة لتصدير ملفات Excel Microsoft إلى تنسيق HTML بدون تحديد معاملات إضافية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

 يمكنك تحقيق نفس النتائج عن طريق تمرير**[SaveFormat.HTML] (https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)** الى**[Workbook.save] (https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save (java.io.OutputStream،٪ 20com.aspose.cells.SaveOptions))** طريقة.

{{% /alert %}}

### **تحديد تفضيلات الصورة لـ HTML**

 بدءًا من 8.0.2 ، تم كشف Aspose.Cells**[ImageOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**ل**[HtmlSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**class ، والتي تتيح للمطورين تحديد تفضيلات الصورة عند حفظ جداول البيانات بتنسيق HTML.

إعدادات الصورة التي يمكن تطبيقها هي:

- **[نوع الصورة] (https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType)**: الحصول على نوع الصورة أو تحديده. يرجى ملاحظة أن جميع الأشكال ، بما في ذلك الرسوم البيانية ، يتم عرضها كصور في الإخراج HTML.
- **[الجودة] (https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality)**: الحصول على جودة الصور أو تعيينها بين 0 إلى 100 ، عند تحديد تنسيق ImageFormat على أنه Jpeg.
- **[VerticalResolution] (https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution)**: الحصول على الدقة الرأسية للصورة أو تعيينها بالنقاط في البوصة.
- **[HorizontalResolution] (https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution)**: الحصول على الدقة الأفقية للصورة أو تعيينها بالنقاط في البوصة.
- **[TiffCompression] (https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression)**الحصول على نوع الضغط للصور أو تحديده عند تحديد تنسيق ImageFormat على أنه Tiff.
- **[شفاف] (https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)**: يشير إلى ما إذا كانت خلفية الصورة يجب أن تكون شفافة عند تحديد ImageFormat كـ Png.

 يوضح الكود أدناه كيفية الاستخدام**[HtmlSaveOptions.ImageOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)** لتحديد التفضيلات المختلفة.

|**عرض جدول البيانات قبل التصدير**|**HTML العرض بعد التصدير**|
|:- |:- |
|![عرض جدول البيانات قبل التصدير](converting-workbook-to-different-formats_1.png)|![HTML العرض بعد التصدير](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **تحويل ملفات Excel إلى PDF**

يتم استخدام وثائق PDF على نطاق واسع كتنسيق قياسي لتبادل الوثائق بين المنظمات والقطاعات الحكومية والأفراد. غالبًا ما يُطلب من مطوري البرامج جهازًا وسيلة لتحويل ملفات Excel Microsoft بسهولة إلى مستندات PDF. Aspose.Cells يدعم هذه الميزات. يوضح هذا المقال كيف.

### **تحويل ملف Excel إلى PDF**

تم تقديم Microsoft Excel إلى PDF التحويل باستخدام Aspose.Cells for Java 2.3.0. من هذا الإصدار ، يمكن Aspose.Cells[تحويل جداول البيانات إلى PDF مباشرة](#direct-conversion) (بما فيها[PDF / أ](#saving-excel-spreadsheets-to-pdfa-complied-files) ) ، بدون منتج آخر. لتحويل جداول البيانات بإصدارات أقدم من Aspose.Cells ،[استخدم Aspose.PDF للتحويل](#conversion-with-asposepdf-asposecells-prior-to-230).

 يقوم Aspose.Cell بتحويل جداول البيانات إلى PDF بدرجة عالية من الدقة والإخلاص. ومع ذلك ، هناك القليل[محددات](/cells/ar/java/converting-workbook-to-different-formats/#conversion-attributes)، المدرجة في نهاية هذه المقالة.

{{% alert color="primary" %}}

 Aspose.Cells for Java يكتب مباشرة المعلومات حول API ورقم الإصدار في وثائق المخرجات. على سبيل المثال ، عند تقديم المستند إلى PDF ، يتم تعبئة Aspose.Cells for Java**تطبيق** حقل بقيمة "Aspose.Cells" و**PDF منتج** حقل بقيمة ، على سبيل المثال "Aspose.Cells for Java v17.9".

يرجى ملاحظة أنه لا يمكنك توجيه Aspose.Cells for Java لتغيير أو إزالة هذه المعلومات من مستندات الإخراج.

{{% /alert %}}

#### **التحويل المباشر**

احفظ ملف Excel مباشرة إلى PDF باستخدام امتداد**[Workbook.save] (https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save (java.io.OutputStream،٪ 20com.aspose.cells.SaveOptions))** الطريقة ، وتقديم**[SaveFormat.PDF] (https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)**عضو الواجهة. التحويل المباشر مثل هذا هو أكثر طرق التحويل كفاءة. لا تفقد البيانات أو التنسيق ولكنها تحافظ على الإخراج PDF وكأنه ملف Excel للإدخال.

 لتحديد اختيارات الأمن عند الحفظ في PDF ، استخدم**[PdfSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **التحويل المتقدم**

يمكنك أيضًا اختيار استخدام ملف**[PdfSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** فئة لتعيين سمات مختلفة للتحويل. تعيين خصائص مختلفة**[PdfSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** ستمنحك class التحكم في إعدادات الطباعة والخط والأمان والضغط لملف PDF الناتج. الخاصية الأكثر شهرة هي**[الامتثال] (https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**التي تمكنك من حفظ ملفات Excel في PDF / A متوافق مع ملفات PDF.

##### **حفظ جداول بيانات Excel في PDF / A الملفات المتوافقة**

يوضح مقتطف الشفرة المقدم أدناه استخدام امتداد**[PdfSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** فئة لحفظ ملفات Excel بتنسيق PDF / A متوافق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **التحويل مع Aspose.Pdf: Aspose.Cells قبل 2.3.0**

 بالنسبة لإصدارات Aspose.Cells السابقة للإصدار 2.3.0 ، تحتاج إلى استخدام مكون مثل[Aspose.PDF for Java](/pdf/java/)لتحويل جداول البيانات إلى ملفات PDF. يعمل كل من Aspose.Cells و Aspose.PDF معًا لتحويل جدول بيانات إلى PDF عبر خطوة وسيطة.

لتحويل جداول البيانات إلى PDF مع Aspose.Cells و Aspose.PDF:

1.  إنشاء كائن من**[مصنف] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**فئة عن طريق استدعاء مُنشئها الفارغ.
1. قم بالعمل المطلوب على جدول البيانات باستخدام Aspose.Cells API.
1. اتصل ب**[Workbook.save] (https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save (java.io.OutputStream،٪ 20com.aspose.cells.SaveOptions))**طريقة حفظ جدول البيانات:
 1. اضبط تنسيق الملف على XML.
 1. حدد Aspose_Pdf (قيمة محددة مسبقًا) من واجهة FileFormatType. يوجه هذا طريقة الحفظ لتكوين جدول بيانات في نموذج XML متوافق مع مخطط Aspose.PDF بحيث يمكن أن يقوم Aspose.PDF for Java بإنشاء مستند PDF.
1. عندما يتم إنشاء ملف XML ، قم بإنشاء كائن من فئة Pdf في حزمة aspose.pdf.
1. استدعاء طريقة bindXML لفئة Pdf ومرر اسم ملف XML الناتج.
1. قم باستدعاء طريقة حفظ فئة Pdf لإنشاء مستند PDF.

يتم تنفيذ الخطوات المذكورة أعلاه أدناه في مثال.

{{% alert color="primary" %}}

إذا كان جدول البيانات الخاص بك يحتوي على صيغ ، فمن الأفضل الاتصال**[Workbook.calculateFormula] (https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula ())** الطريقة قبل تحويل جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة ، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}

#### **سمات التحويل**

نحن نعمل بجد لتحسين التحويل والجوانب الأخرى لـ Aspose.Cells مع كل إصدار. Excel لتحويل PDF له بعض القيود. قد يتم فقد بعض إعدادات التنسيق المحددة في جدول بيانات ، ولا يتم دعم جميع الكائنات الرسومية.

يسرد الجدول أدناه جميع الميزات المدعومة كليًا أو جزئيًا عند التصدير إلى PDF باستخدام Aspose.Cells. هذا الجدول ليس نهائيًا ولا يغطي كافة سمات جدول البيانات. يمكنه أيضًا تحديد تلك الميزات التي قد لا تكون مدعومة أو مدعومة جزئيًا للتحويل.

{{% alert color="primary" %}}

|**عنصر المستند**|**ينسب**|**صافي المدعومة**|**ملاحظات**|
|:- |:- |:- |:- |
|التوافق||نعم||
|دوران||جزئيا|يدعم فقط 90 و -90.|
|إعدادات الخلفية||نعم||
|الحدود|اللون|نعم||
|الحدود|أسلوب الخط|نعم||
|الحدود|عرض الخط|نعم||
|Cell البيانات||نعم||
|تعليقات||لا||
|تنسيق مشروط||نعم||
|خصائص المستند||نعم||
|كائنات الرسم||نعم||
|الخط|بحجم|نعم||
|الخط|اللون|نعم||
|الخط|أسلوب|نعم||
|الخط|تسطير|نعم||
|الخط|تأثيرات|جزئيا|يتم دعم تأثير الشطر فقط|
|الصور||نعم||
|ارتباط تشعبي||نعم||
|الرسوم البيانية||نعم||
|اندمجت Cells||نعم||
|فاصل صفحة||نعم||
|اعداد الصفحة|تذييل الرأس|نعم||
|اعداد الصفحة|الهوامش|نعم||
|اعداد الصفحة|اتجاه الصفحة|نعم||
|اعداد الصفحة|مقاس الصفحه|نعم||
|اعداد الصفحة|منطقة الطباعة|نعم||
|اعداد الصفحة|عناوين الطباعة|نعم||
|اعداد الصفحة|تحجيم|نعم||
|ارتفاع الصف / عرض العمود||نعم||
{{% /alert %}}
