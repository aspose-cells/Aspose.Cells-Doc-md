---
title: تغييرات API العامة في Aspose.Cells 8.8.1
type: docs
weight: 280
url: /ar/java/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات لـ Aspose.Cells من الإصدار 8.8.0 إلى 8.8.1 التي قد تكون مثيرة للاهتمام لمطوري الوحدات/التطبيقات. يتضمن ليس فقط الطرق العامة الجديدة والمحدثة والفئات المضافة والمحذوفة وما إلى ذلك، ولكن أيضًا وصفًا لأي تغييرات في السلوك في الخلفية في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تصفية البيانات للتحميل**
Aspose.Cells for Java 8.8.1 قد قامت بتعريض تعداد LoadDataFilterOptions جنبًا إلى جنب مع خاصية LoadOptions.LoadDataFilterOptions التي يمكن استخدامها لتحديد نوع البيانات التي يجب تحميلها عند بناء الدفتر من ملف قالب. يمكن أن يحسن تصفية البيانات المحملة الأداء لأغراض خاصة، خاصةً عند استخدام واجهات API LightCells.

تقدم تعداد LoadDataFilterOptions التالية.

1. ALL لتحميل كل شيء من جدول البيانات.
1. NONE لعدم تحميل أي شيء من جدول البيانات.
1. CELL_BLANK يحمل الخلايا التي قيمها فارغة.
1. CELL_BOOL يحمل الخلايا التي تحتوي على قيم منطقية.
1. CELL_DATA يحمل بيانات الخلايا بما في ذلك القيم والصيغ والتنسيق.
1. CELL_ERROR يحمل الخلايا التي قيمها خطأ.
1. CELL_NUMERIC يحمل الخلايا التي قيمها رقمية (بما في ذلك التاريخ والوقت).
1. CELL_STRING يحمل الخلايا التي قيمها نص/نص.
1. CELL_VALUE يحمل قيم الخلية فقط (جميع الأنواع).
1. يحمل CHART الرسوم البيانية فقط.
1. يحمل CONDITIONAL_FORMATTING فقط قواعد التنسيق الشرطي.
1. يحمل DATA_VALIDATION قواعد التحقق من البيانات فقط.
1. يحمل DOCUMENT_PROPERTIES خصائص المستند فقط.
1. يحمل FORMULA الصيغ بما في ذلك الأسماء المحددة.
1. يحمل MERGED_AREA الخلايا المدمجة فقط.
1. يحمل PIVOT_TABLE الجداول الدورية.
1. يحمل SETTINGS إعدادات دفتر العمل والصفحة.
1. يحمل SHAPE الأشكال فقط.
1. يحمل STYLE تنسيقات الخلايا.
1. يحمل TABLE جداول Excel/كائنات القائمة.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقالة المفصلة عن [تصفية البيانات لتحميلها](/cells/ar/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **تحويل مباشر للرسم البياني إلى PDF**
قدمت واجهات برمجة التطبيقات Aspose.Cells بالفعل مرفق تصدير الرسوم البيانية إلى PDF أثناء استخدام طريقة Chart.toPdf. مع هذا الإصدار، قد عرضت واجهة برمجة التطبيقات نسخة جديدة محملة لهذه الطريقة التي يمكن أن تقبل نسخة من OutputStream، مما يسمح للمستخدمين بحفظ PDF الرسم البياني في نسخة من ByteArrayOutputStream.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

Workbook workbook = new Workbook(filePath);

//Access first worksheet containing a chart

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart from the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart to PDF as Stream

ByteArrayOutputStream outStream = new ByteArrayOutputStream();

chart.toPdf(outStream);

{{< /highlight >}}
### **تمت إضافة خاصية WorkbookSettings.PaperSize**
Aspose.Cells for Java 8.8.1 قد عرضت خاصية WorkbookSettings.PaperSize لضبط حجم الورق الافتراضي لجميع ورقات الجدول. تقبل خاصية WorkbookSettings.PaperSize قيمة من تعداد PaperSizeType الذي يحتوي على الأحجام المحددة مسبقاً لأكثر أنواع أوراق الطباعة استخداماً.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **تمت إضافة خاصية Shape.TextBody**
لقد كشفت هذه الإصدارة من API Aspose.Cells for Java عن خاصية Shape.TextBody لتلاعب في جوانب النص في الأشكال. الكود المصغر التالي يستخدم هذه الخاصية لضبط تأثير الظل على النص في مربع النص.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يُرجى مراجعة المقال المفصل حول [ضبط تأثير الظل للنص](/cells/ar/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet of the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Set the text of the TextBox

textBox.setText("This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

//Set shadow effect for text

for (int i = 0; i < textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **تمت إضافة أسلوب Worksheet.calculateFormula(string formula, CalculationOptions opts)**
لقد كشف إصدار Aspose.Cells for Java 8.8.1 عن تحميل آخر لأسلوب Worksheet.calculateFormula الذي يوفر القدرة على حساب صيغة معينة مباشرة مع إعدادات مخصصة.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يُرجى مراجعة المقال المفصل حول [حساب الدالة المخصصة بشكل مباشر](/cells/ar/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **تمت إضافة أسلوب GridCell.createValidation**
قدمت Aspose.Cells.GridWeb القدرة على إضافة القاعدة التحقق مباشرة إلى خلية واحدة باستخدام أسلوب GridCell.createValidation. يتطلب الأسلوب المذكور 2 معلمة. الأولى من نوع GridValidationType التي تحدد نوع التحقق، في حين أن المعلمة الثانية (isRequied) هي من نوع Boolean.

**Java**

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = gridweb.getWorkSheets().get(0);

//Access cell B3

GridCell cell = sheet.getCells().get("B3");

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.createValidation(GridValidationType.WHOLE_NUMBER, true);

val.setFormula1("=20");

val.setFormula2("=40");

val.setOperator(OperatorType.BETWEEN);

val.setShowError(true);

val.setShowInput(true);

{{< /highlight >}}
### **تمت إضافة أسلوب GridCell.removeValidation**
قدمت Aspose.Cells.GridWeb أيضًا القدرة على إزالة قاعدة التحقق من البيانات من GridCell باستخدام الأسلوب GridCell.removeValidation.
## **واجهات برمجة التطبيق القديمة**
### **تمت إهمال خاصية Shape.TextFrame**
يُنصح باستخدام خاصية Shape.TextBody.TextAlignment بدلاً منها.
{{< app/cells/assistant language="java" >}}
