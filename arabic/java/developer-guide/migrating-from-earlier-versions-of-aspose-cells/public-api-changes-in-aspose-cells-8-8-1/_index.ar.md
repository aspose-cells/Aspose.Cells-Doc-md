---
title: عام API التغييرات في Aspose.Cells 8.8.1
type: docs
weight: 280
url: /ar/java/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.8.0 إلى 8.8.1 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تصفية البيانات للتحميل**
كشف Aspose.Cells for Java 8.8.1 تعداد LoadDataFilterOptions مع خاصية LoadOptions.LoadDataFilterOptions التي يمكن استخدامها لتحديد نوع البيانات التي يجب تحميلها عند إنشاء المصنف من ملف قالب. يمكن أن تؤدي تصفية البيانات المحملة إلى تحسين الأداء لأغراض خاصة ، لا سيما عند استخدام واجهات برمجة تطبيقات LightCells.

يوفر تعداد LoadDataFilterOptions التحديدات التالية.

1. ALL لتحميل كل شيء من جدول البيانات.
1. لا شيء لتحميل أي شيء من جدول البيانات.
1. يقوم CELL_BLANK بتحميل الخلايا التي تكون قيمها فارغة.
1. يقوم CELL_BOOL بتحميل الخلايا التي تكون قيمها منطقية.
1. يقوم CELL_DATA بتحميل بيانات الخلايا بما في ذلك القيم والصيغ والتنسيق.
1. يقوم CELL_ERROR بتحميل الخلايا التي تكون قيمها خطأ.
1. يقوم CELL_NUMERIC بتحميل الخلايا التي تكون قيمها رقمية (بما في ذلك التاريخ والوقت).
1. يقوم CELL_STRING بتحميل الخلايا التي تكون قيمها نصًا / سلسلة.
1. يقوم CELL_VALUE بتحميل قيم الخلايا فقط (كافة الأنواع).
1. يقوم المخطط بتحميل الرسوم البيانية فقط.
1. يقوم CONDITIONAL_FORMATTING بتحميل قواعد التنسيق الشرطي فقط.
1. يقوم DATA_VALIDATION بتحميل قواعد التحقق من صحة البيانات فقط.
1. يقوم DOCUMENT_PROPERTIES بتحميل خصائص المستند فقط.
1. FORMULA تحميل الصيغ بما في ذلك الأسماء المعرفة.
1. يقوم MERGED_AREA بتحميل الخلايا المدمجة فقط.
1. يقوم PIVOT_TABLE بتحميل الجداول المحورية.
1. يقوم SETTINGS بتحميل إعدادات المصنف وورقة العمل فقط.
1. SHAPE يقوم بتحميل الأشكال فقط.
1. STYLE يقوم بتحميل تنسيق الخلايا.
1. يقوم TABLE بتحميل جداول Excel / قائمة الكائنات.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[تصفية البيانات للتحميل](/cells/ar/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **مباشرة تحويل الرسم البياني إلى PDF**
لقد وفرت واجهات برمجة التطبيقات Aspose.Cells بالفعل تسهيلات لتقديم المخططات إلى PDF أثناء استخدام طريقة Chart.toPdf. مع هذا الإصدار ، كشف API عن نسخة أخرى محملة بشكل زائد من الطريقة المذكورة والتي يمكن أن تقبل مثيل OutputStream ، مما يسمح للمستخدمين بحفظ ملف PDF للمخطط في مثيل ByteArrayOutputStream.

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

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
### **تمت إضافة WorkbookSettings.PaperSize Property**
كشف Aspose.Cells for Java 8.8.1 الخاصية WorkbookSettings.PaperSize لتعيين حجم ورق الطباعة الافتراضي لجدول البيانات بأكمله. تقبل الخاصية WorkbookSettings.PaperSize قيمة من تعداد PaperSizeType الذي يحتوي على الأحجام المحددة مسبقًا لأنواع ورق الطباعة الأكثر استخدامًا.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **تمت إضافة خاصية Shape.TextBody**
كشف هذا الإصدار من Aspose.Cells for Java API الشكل. TextBody من أجل معالجة جوانب النص في الأشكال. يستخدم المقتطف التالي الخاصية المذكورة لتعيين تأثير الظل للنص في TextBox.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[تعيين تأثير الظل للنص](/cells/ar/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 // إنشاء مثيل من المصنف

كتاب المصنف = مصنف جديد () ؛

// الوصول إلى ورقة العمل الأولى من المصنف

ورقة عمل = book.getWorksheets (). get (0)؛

// أضف TextBox إلى ShapeCollection

فهرس int = sheet.getTextBoxes (). add (2، 2، 100، 400) ؛

TextBox textBox = sheet.getTextBoxes (). get (index) ؛

// تعيين نص مربع النص

textBox.setText ("يحتوي هذا النص على الإعدادات التالية. \ n \ n تأثيرات النص> الظل> إزاحة القاع")؛

// تعيين تأثير الظل للنص

 لـ (int i = 0 ؛ i< textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **تمت إضافة Worksheet.calculateFormula (صيغة السلسلة ، CalculationOptions) الطريقة**
كشف Aspose.Cells for Java 8.8.1 عن حمل زائد آخر لطريقة Worksheet.calculateFormula التي توفر القدرة على حساب صيغة معينة مباشرةً باستخدام الخيارات المخصصة.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[الحساب المباشر للوظيفة المخصصة](/cells/ar/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **تمت إضافة طريقة GridCell.createValidation**
قدم Aspose.Cells.GridWeb القدرة على إضافة قاعدة التحقق مباشرة إلى خلية واحدة أثناء استخدام طريقة GridCell.createValidation. تتطلب الطريقة المذكورة معلمتين. الأول هو من النوع GridValidationType الذي يحدد نوع التحقق من الصحة ، بينما المعلمة الثانية (isRequied) من النوع Boolean.

**Java**

{{< highlight "csharp" >}}

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
### **تمت إضافة طريقة GridCell.removeValidation**
يوفر Aspose.Cells.GridWeb أيضًا القدرة على إزالة قاعدة التحقق من صحة البيانات من GridCell أثناء استخدام طريقة GridCell.removeValidation.
## **واجهات برمجة التطبيقات التي عفا عليها الزمن**
### **شكل قديم. خاصية TextFrame**
يُنصح باستخدام خاصية Shape.TextBody.TextAlignment بدلاً من ذلك.
