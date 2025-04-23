---
title: تغييرات API العامة في Aspose.Cells 8.8.1
type: docs
weight: 270
url: /ar/net/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.8.0 إلى 8.8.1 التي قد تكون مثيرة للاهتمام لمطوري الوحدات/التطبيقات. يتضمن ليس فقط الطرق العامة الجديدة والمحدثة والفئات المضافة والمحذوفة وما إلى ذلك، ولكن أيضًا وصفًا لأي تغييرات في السلوك في الخلفية في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تصفية البيانات للتحميل**
Aspose.Cells for .NET 8.8.1 قد قدمت تعدداً لتصفية بيانات LoadDataFilterOptions مع خاصية LoadOptions.LoadDataFilterOptions التي يمكن استخدامها لتحديد نوع البيانات التي يجب تحميلها عند بناء دفتر العمل من ملف نموذجي. يمكن أن تحسن عملية تحميل البيانات المصفاة الأداء في الأغراض الخاصة، خاصة عند استخدام واجهات LightCells.

تقدم تعداد LoadDataFilterOptions التالية.

1. الكل لتحميل كل شيء من جدول البيانات.
1. لا شيء للتحميل شيء من جدول البيانات.
1. CellBlank يحمل الخلايا التي تكون قيمها فارغة.
1. CellBool يحمل الخلايا التي تكون قيمها Boolean.
1. CellData يحمل بيانات الخلايا بما في ذلك القيم والصيغ والتنسيق.
1. CellError يحمل الخلايا التي تكون قيمها خطأ.
1. CellNumeric يحمل الخلايا التي تكون قيمها رقمية (بما في ذلك التاريخ والوقت).
1. CellString يحمل الخلايا التي تكون قيمها نص/سلسلة نصية.
1. CellValue يحمل قيم الخلية فقط (جميع الأنواع).
1. تحميل الرسم البياني فقط.
1. تحميل التنسيق الشرطي فقط.
1. تحميل قواعد التحقق من البيانات فقط.
1. تحميل خصائص المستند فقط.
1. تحميل الصيغ بما فيها الأسماء المحددة.
1. تحميل الخلايا المدمجة فقط.
1. تحميل الجداول المحورية فقط.
1. تحميل إعدادات دفتر العمل وورقة العمل فقط.
1. تحميل الأشكال فقط.
1. تحميل تنسيق الخلايا فقط.
1. تحميل جداول Excel/List Objects فقط.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [تصفية البيانات للتحميل](/cells/ar/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **تحويل مباشر للرسم البياني إلى PDF**
لقد قدمت واجهات برمجة التطبيقات Aspose.Cells بالفعل إمكانية عرض الرسوم البيانية إلى PDF أثناء استخدام الطريقة Chart.ToPdf. مع هذا الإصدار، قد فتحت الواجهة برمجة التطبيقات الإصدارة نسخة أخرى من الطريقة المذكورة التي يمكن أن تقبل مثيلًا لمجرى بيانات، مما يتيح للمستخدمين حفظ PDF الرسم البياني في مثيل من MemoryStream.

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

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


### **تمت إضافة خاصية WorkbookSettings.PaperSize**
أضافت الإصدارة Aspose.Cells for .NET 8.8.1 خاصية WorkbookSettings.PaperSize من أجل تعيين حجم الورق الافتراضي للطباعة لجدول البيانات بأكمله. تقبل خاصية WorkbookSettings.PaperSize قيمة من تعداد PaperSizeType الذي يحتوي على الأحجام المحددة مسبقًا لأكثر أنواع الورق للاستخدام في الطباعة.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **تمت إضافة خاصية Shape.TextBody**
أضاف هذا الإصدار من Aspose.Cells for .NET واجهة برمجة التطبيقات خاصية Shape.TextBody من أجل التلاعب بجوانب النص في الأشكال. تستخدم الكود البرمجي التالي الخاصية المذكورة لضبط تأثير الظل للنص في مربع النص.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [ضبط تأثير الظل على النص](/cells/ar/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

var book = new Workbook();

//Access first worksheet of the Workbook

var sheet = book.Worksheets[0];

//Add a TextBox to the ShapeCollection

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Set the text of the TextBox

textBox.Text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

//Set shadow effect for text

for (int i = 0; i < textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **تمت إضافة أسلوب Worksheet.CalculateFormula(string formula, CalculationOptions opts)**
قد عرض الإصدار Aspose.Cells for .NET 8.8.1 حملة تحميل أخرى للطريقة CalculateFormula تقدم القدرة على حساب صيغة معينة مباشرة مع خيارات مخصصة.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [الحساب المباشر للدالة المخصصة](/cells/ar/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **تمت إضافة أسلوب GridCell.CreateValidation**
قدم Aspose.Cells.GridWeb القدرة على إضافة قاعدة التحقق إلى خلية واحدة مباشرةً باستخدام أسلوب GridCell.CreateValidation. يتطلب الأسلوب المذكور معلمتين. الأولى من نوع GridValidationType التي تحدد نوع التحقق، في حين أن المعلمة الثانية (isRequied) هي من نوع بوليان.



**C#**

{{< highlight csharp >}}

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


### **تمت إضافة أسلوب GridCell.RemoveValidation**
قدم Aspose.Cells.GridWeb أيضًا القدرة على إزالة قاعدة التحقق من GridCell باستخدام أسلوب GridCell.RemoveValidation.
## **واجهات برمجة التطبيق القديمة**
### **تمت إهمال خاصية Shape.TextFrame**
يُنصح باستخدام خاصية Shape.TextBody.TextAlignment بدلاً منها.
{{< app/cells/assistant language="csharp" >}}
