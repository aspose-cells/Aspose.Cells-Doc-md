---
title: عام API التغييرات في Aspose.Cells 8.4.2
type: docs
weight: 160
url: /ar/java/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

 يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.4.1 إلى 8.4.2 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ،[الفئات المضافة وما إلى ذلك.](/cells/ar/java/public-api-changes-in-aspose-cells-8-4-2/)ولكن أيضًا وصف لأية تغييرات في السلوك خلف الكواليس عام Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **آلية إنشاء المخطط المحسن**
كشفت فئة com.aspose.cells.charts.Chart عن طريقة setChartDataRange لتسهيل مهمة إنشاء المخطط. تقبل طريقة setChartDataRange معلمتين ، حيث تكون المعلمة الأولى من سلسلة النوع التي تحدد منطقة الخلية التي يتم من خلالها رسم سلسلة البيانات. المعلمة الثانية هي من النوع المنطقي الذي يحدد اتجاه الرسم ، أي ؛ ما إذا كنت تريد رسم سلسلة بيانات المخطط من نطاق من قيم الخلايا حسب الصف أو الأعمدة.

يوضح مقتطف التعليمات البرمجية التالي كيفية إنشاء مخطط عمودي مع بضعة أسطر من التعليمات البرمجية بافتراض أن بيانات سلسلة مخطط الرسم البياني موجودة في نفس ورقة العمل من الخلية A1 إلى D4.

**Java**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **الأسلوب VbaModuleCollection.add مضاف**
كشف Aspose.Cells for Java 8.4.2 عن أسلوب VbaModuleCollection.add لإضافة وحدة VBA جديدة إلى مثيل Workbook. يقبل أسلوب VbaModuleCollection.add معلمة من نوع ورقة العمل لإضافة وحدة نمطية خاصة بورقة العمل.

يوضح مقتطف التعليمات البرمجية التالي كيفية استخدام طريقة VbaModuleCollection.add.

**Java**

{{< highlight "csharp" >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add VBA module

int idx = workbook.getVbaProject().getModules().add(worksheet);

//Access the VBA Module, set its name and code

VbaModule module = workbook.getVbaProject().getModules().get(idx);

module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub");

//Save the workbook

workbook.save(output, SaveFormat.XLSM);

{{< /highlight >}}

### **طريقة التحميل الزائد Cells.copyColumns مضافة**
كشف Aspose.Cells for Java 8.4.2 عن نسخة محملة بشكل زائد من طريقة Cells.copyColumns لتكرار أعمدة المصدر على الوجهة. تقبل الطريقة المكشوفة حديثًا 5 معلمات في المجموع ، حيث تكون المعلمات الأربعة الأولى مماثلة للطريقة الشائعة Cells.copyColumns. ومع ذلك ، فإن المعلمة الأخيرة من النوع int تحدد عدد أعمدة الوجهة التي يجب تكرار أعمدة المصدر عليها.

يوضح مقتطف التعليمات البرمجية التالي كيفية استخدام طريقة Cells.copyColumns المكشوفة حديثًا.

**Java**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.copyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **حقول التعداد PasteType.DEFAULT & PasteType.ALL_EXCEPT_BORDERS مضافة**
مع إصدار v8.4.2 ، أضاف Aspose.Cells API حقلي تعداد جديدين لـ PasteType كما هو مفصل أدناه.

- PasteType.DEFAULT: يعمل بشكل مشابه لوظيفة "الكل" في Excel للصق نطاق الخلايا.
- PasteType.ALL_إلا_الحدود: تعمل بشكل مشابه لوظيفة "الكل باستثناء الحدود" في Excel للصق نطاق من الخلايا.

يوضح نموذج التعليمات البرمجية التالي استخدام حقل PasteType.DEFAULT.

**Java**

{{< highlight "csharp" >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Create source & destination ranges

Range source = cells.createRange("A1:B6");

Range destination = cells.createRange("D1:E6");

//Create an instance of PasteOptions and set its PasteType property

PasteOptions options = new PasteOptions();

options.setPasteType(PasteType.DEFAULT);

//Copy the source range onto the destination range with everything except column widths

destination.copy(source, options);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

بدءًا من إصدار for Java for Java Aspose.Cells 8.4.2 ، قدم التعداد PasteType.ALL يتصرف بشكل مختلف مقارنة بوظيفة "الكل" في Excel للصق نطاق الخلايا. الآن ، يقوم PasteType.ALL أيضًا بنسخ عرض العمود إلى النطاق الوجهة بدلاً من وظيفة "الكل" في Excel. لتقليد سلوك "الكل" في Excel ، يرجى استخدام PasteType.DEFAULT.

{{% /alert %}}
