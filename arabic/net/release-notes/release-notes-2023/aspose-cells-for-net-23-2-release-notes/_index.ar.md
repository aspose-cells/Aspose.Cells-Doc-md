---
title: Aspose.Cells for .NET 23.2 ملاحظات الإصدار
type: docs
weight: 11
url: /ar/net/aspose-cells-for-net-23-2-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 23.2](https://www.nuget.org/packages/Aspose.Cells/23.2.0).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
| :- | :- | :- |
|CELLSNET-52620|دعم تحليل / قراءة / حفظ وظائف SCAN و Lambda|
|CELLSNET-52666|يدعم تنسيقات ترقيم الصفحات المتعددة عند تحويل Excel إلى pptx|
|CELLSNET-52627|استخراج نمط الخلية إلى كائن عام (مثل JSON)|
|CELLSNET-52683|Cell. الصيغة ليست هي نفسها المعروضة في MS Excel|
|CELLSNET-52691|تم حساب الصيغ بشكل غير صحيح|
|CELLSNET-52519|مشكلة في قراءة المخططات من ملف Excel (تم إنشاؤه بواسطة Aspose.Cells) حتى Microsoft الرسم البياني API|
|CELLSNET-52544|الرسم البياني إلى PDF يختلف عن الصورة|
|CELLSNET-52635| النص في المخطط في SVG به موضع خاطئ|
|CELLSNET-52585|تعذر تحميل ملف xps الذي تم إنشاؤه بواسطة System.Windows.Xps.Packaging.XpsDocument|
|CELLSNET-52622|لا يمكن توليد SVG بخط مرتفع ومنخفض من ملف Excel|
|CELLSNET-52692|يتم فقد النص في الوثيقة XPS المحولة|
|CELLSNET-52438| فقدان البيانات في حفظ مخطط الجدول المحوري|
|CELLSNET-52555|الاختلاف في موضع الحرف / النص عند تحويل ورقة العمل المحددة إلى HTML|
|CELLSNET-52583|التحويل إلى Docx ينتج عنه صفحة فارغة إضافية|
|CELLSNET-52612|مشكلة في فتح PowerQuery بعد التغيير|
|CELLSNET-52613|تحويل Numbers إلى Pptx ينتج عنه نتيجة مكسورة|
|CELLSNET-52630|HTML لتحويل Excel - لا يتم عرض الجداول بشكل صحيح|
|CELLSNET-52631| يؤدي حفظ ملف XLSX كـ XLSB إلى إتلاف الألوان وإضافة المرشحات|
|CELLSNET-52639|تتم إعادة تعيين تدوير عنوان محور المخطط بعد النسخ باستخدام Aspose.Cells|
|CELLSNET-52662| يفقد استيراد Xml الصيغ في الأعمدة المحسوبة|
|CELLSNET-52671|ملف XmlImport يفسد عند محاولة تحديث الجداول المحورية بالعمود المحسوب|
|CELLSNET-52675|نمط الخلية المفقودة بعد استيراد xml.|
|CELLSNET-52684|تم فقد تنسيق التعليق عند نسخ النطاق|
|CELLSNET-52690|JsonLayoutOptions لا يعمل.|
|CELLSNET-52696|تولد عمليات الجدول ملفات Excel تالفة|
|CELLSNET-52549|حفظ الورقة في HTML باستخدام SmartArt يلقي System.NullReferenceException|

##  **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

###  **يضيف خاصية ChartTextFrame.IsAutomaticRotation**

يشير إلى ما إذا كان سيتم تدوير نص المخطط تلقائيًا.

###  **Obsoletes JsonLayoutOptions.IgnoreObjectTitle و JsonLayoutOptions.IgnoreArrayTitle Properties**

يُرجى استخدام الخاصية JsonLayoutOptions.IgnoreTitle بدلاً من ذلك.

###  **يضيف خاصية JsonLayoutOptions.IgnoreTitle**

عناوين Ingores لسمات Json عند تحويل json إلى Excel.

###  **يضيف طريقة Style.ToJson ()**

يحول نمط ملفات Excel إلى ملف json

###  **يضيف Cell.ToJson () طريقة**

يحول خلية من الخلايا إلى ملف json.

