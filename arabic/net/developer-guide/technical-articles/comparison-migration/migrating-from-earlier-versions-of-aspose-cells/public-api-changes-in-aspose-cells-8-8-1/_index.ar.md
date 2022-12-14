---
title: عام API التغييرات في Aspose.Cells 8.8.1
type: docs
weight: 270
url: /ar/net/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.8.0 إلى 8.8.1 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تصفية البيانات للتحميل**
كشف Aspose.Cells for .NET 8.8.1 تعداد LoadDataFilterOptions مع خاصية LoadOptions.LoadDataFilterOptions التي يمكن استخدامها لتحديد نوع البيانات التي يجب تحميلها عند إنشاء المصنف من ملف قالب. يمكن أن تؤدي تصفية البيانات المحملة إلى تحسين الأداء لأغراض خاصة ، لا سيما عند استخدام واجهات برمجة تطبيقات LightCells.

يوفر تعداد LoadDataFilterOptions التحديدات التالية.

1. كل شيء لتحميل كل شيء من جدول البيانات.
1. لا شيء لتحميل أي شيء من جدول البيانات.
1. يقوم CellBlank بتحميل الخلايا التي تكون قيمها فارغة.
1. يقوم CellBool بتحميل الخلايا التي تكون قيمها منطقية.
1. تقوم CellData بتحميل بيانات الخلايا بما في ذلك القيم والصيغ والتنسيق.
1. يقوم CellError بتحميل الخلايا التي تكون قيمها خطأ.
1. تقوم CellNumeric بتحميل الخلايا التي تكون قيمها رقمية (بما في ذلك التاريخ والوقت).
1. تقوم CellString بتحميل الخلايا التي تكون قيمها نصًا / سلسلة.
1. تقوم CellValue بتحميل قيم الخلايا فقط (كافة الأنواع).
1. الرسم البياني يحمل الرسوم البيانية فقط.
1. يحمّل التنسيق الشرطي قواعد التنسيق الشرطي فقط.
1. يقوم DataValidation بتحميل قواعد التحقق من صحة البيانات فقط.
1. DocumentProperties يقوم بتحميل خصائص المستند فقط.
1. الصيغة تحمل الصيغ بما في ذلك الأسماء المعرفة.
1. يقوم MergedArea بتحميل الخلايا المدمجة فقط.
1. يقوم PivotTable بتحميل الجداول المحورية.
1. تقوم الإعدادات بتحميل إعدادات المصنف وورقة العمل فقط.
1. يقوم الشكل بتحميل الأشكال فقط.
1. يقوم النمط بتحميل تنسيق الخلايا.
1. يقوم الجدول بتحميل جداول Excel / قائمة الكائنات.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[تصفية البيانات للتحميل](/cells/ar/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **مباشرة تحويل الرسم البياني إلى PDF**
لقد وفرت واجهات برمجة التطبيقات Aspose.Cells بالفعل تسهيلات لتقديم المخططات إلى PDF أثناء استخدام طريقة Chart.ToPdf. مع هذا الإصدار ، كشف API عن نسخة أخرى محملة بشكل زائد من الطريقة المذكورة والتي يمكن أن تقبل مثيلاً من البث ، مما يسمح للمستخدمين بحفظ ملف PDF الخاص بالرسم البياني في مثيل MemoryStream.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

var workbook = new Workbook(filePath);

//Access first worksheet containing a chart

var worksheet = workbook.Worksheets[0];

//Access first chart from the worksheet

var chart = worksheet.Charts[0];

//Save the chart to PDF as Stream

using (MemoryStream stream = new MemoryStream())

{

    chart.ToPdf(stream);

}

{{< /highlight >}}


### **تمت إضافة WorkbookSettings.PaperSize Property**
كشف Aspose.Cells for .NET 8.8.1 الخاصية WorkbookSettings.PaperSize لتعيين حجم ورق الطباعة الافتراضي لجدول البيانات بأكمله. تقبل الخاصية WorkbookSettings.PaperSize قيمة من تعداد PaperSizeType الذي يحتوي على الأحجام المحددة مسبقًا لأنواع ورق الطباعة الأكثر استخدامًا.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **تمت إضافة خاصية Shape.TextBody**
كشف هذا الإصدار من Aspose.Cells for .NET API الشكل. TextBody من أجل معالجة جوانب النص في الأشكال. يستخدم المقتطف التالي الخاصية المذكورة لتعيين تأثير الظل للنص في TextBox.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[تعيين تأثير الظل للنص](/cells/ar/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // إنشاء مثيل من المصنف

var book = new Workbook () ؛

// الوصول إلى ورقة العمل الأولى من المصنف

var sheet = book.Worksheets [0] ؛

// أضف TextBox إلى ShapeCollection

var textBox = sheet.Shapes.AddTextBox (2، 0، 2، 0، 100، 400) ؛

// تعيين نص مربع النص

textBox.Text = "يحتوي هذا النص على الإعدادات التالية. \ n \ n تأثيرات النص> الظل> إزاحة القاع"؛

// تعيين تأثير الظل للنص

 لـ (int i = 0 ؛ i< textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **تمت إضافة ورقة العمل .CalculateFormula (صيغة السلسلة ، CalculationOptions) الطريقة**
كشف Aspose.Cells for .NET 8.8.1 عن حمل زائد آخر لطريقة CalculateFormula التي توفر القدرة على حساب صيغة معينة مباشرةً باستخدام الخيارات المخصصة.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[الحساب المباشر للوظيفة المخصصة](/cells/ar/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **تمت إضافة طريقة GridCell.CreateValidation**
قدم Aspose.Cells.GridWeb القدرة على إضافة قاعدة التحقق مباشرة إلى خلية واحدة أثناء استخدام طريقة GridCell.CreateValidation. تتطلب الطريقة المذكورة معلمتين. الأول هو من النوع GridValidationType الذي يحدد نوع التحقق من الصحة ، بينما المعلمة الثانية (isRequied) من النوع Boolean.



**C#**

{{< highlight "csharp" >}}

 //Access first worksheet

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B3

GridCell cell = sheet.Cells["B3"];

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.CreateValidation(GridValidationType.WholeNumber, true);

val.Formula1 = "=20";

val.Formula2 = "=40";

val.Operator = GridOperatorType.Between;

val.ShowError = true;

val.ShowInput = true;

{{< /highlight >}}


### **تمت إضافة طريقة GridCell.RemoveValidation**
يوفر Aspose.Cells.GridWeb أيضًا القدرة على إزالة قاعدة التحقق من صحة البيانات من GridCell أثناء استخدام طريقة GridCell.RemoveValidation.
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **شكل قديم. خاصية TextFrame**
يُنصح باستخدام خاصية Shape.TextBody.TextAlignment بدلاً من ذلك.
