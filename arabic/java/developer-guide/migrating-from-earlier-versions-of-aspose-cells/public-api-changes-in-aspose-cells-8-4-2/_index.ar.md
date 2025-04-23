---
title: تغيرات واجهة برمجة التطبيقات العامة في Aspose.Cells 8.4.2
type: docs
weight: 160
url: /ar/java/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات في واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.4.1 إلى 8.4.2 التي قد تكون مثيرة للاهتمام لمطوري الوحدة/التطبيقات. يتضمن ليس فقط الطرق العامة الجديدة والمحدثة، [الفصول المضافة الخ.](/cells/ar/java/public-api-changes-in-aspose-cells-8-4-2/), ولكن أيضًا وصفًا لأي تغييرات في السلوك وراء الكواليس في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **آلية إنشاء المخططات المحسنة**
تمتكشاف الفئة com.aspose.cells.charts.Chart عن طريقة setChartDataRange لتسهيل عملية إنشاء المخططات. تقبل طريقة setChartDataRange معاملين، حيث يكون المعامل الأول من نوع سلسلة يحدد منطقة الخلايا التي يتم من خلالها تخطيط سلاسل البيانات. المعامل الثاني من نوع بوليان يحدد الاتجاه البياني، أي؛ ما إذا كان تخطيط سلاسل بيانات المخطط من مجموعة القيم الخلية عبر الصفوف أم عبر الأعمدة.

يظهر الشق المشفر التالي كيفية إنشاء مخطط عمودي ببضع أسطر من الشيفرة بشرط أن بيانات سلسلة مخططها موجودة على نفس ورقة العمل من الخلية A1 إلى D4.

**Java**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **تمت إضافة طريقة VbaModuleCollection.add**
Aspose.Cells for Java 8.4.2 قد كشف عن طريقة VbaModuleCollection.add لإضافة وحدة VBA جديدة إلى نسخة من الدفتر. تقبل طريقة VbaModuleCollection.add معلمة من نوع ورقة العمل لإضافة وحدة خاصة بورقة العمل.

يوضح المقطع البرمجي التالي كيفية استخدام طريقة VbaModuleCollection.add

**Java**

{{< highlight csharp >}}

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

### **تمت إضافة الطريقة المتعددة الأحمال Cells.copyColumns**
Aspose.Cells for Java 8.4.2 قد كشف عن إصدار متعدد الأحمال لطريقة Cells.copyColumns لتكرار أعمدة المصدر على الوجهة. تقبل الطريقة الجديدة المعرضة 5 معلمات بإجمالي، حيث تكون أول 4 معلمات هي نفسها كما هو الحال في الطريقة العامة Cells.copyColumns. ومع ذلك، فإن المعلمة الأخيرة من نوع int تحدد عدد الأعمدة الوجهة التي يجب تكرار أعمدة المصدر عليها.

يوضح المقطع البرمجي التالي كيفية استخدام طريقة Cells.copyColumns المعرضة حديثًا.

**Java**

{{< highlight csharp >}}

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

### **تمت إضافة تعداد حقول PasteType.DEFAULT & PasteType.ALL_EXCEPT_BORDERS**
مع إصدار v8.4.2، قام API Aspose.Cells بإضافة 2 حقل تعداد جديد لـ PasteType كما هو مفصل أدناه.

- PasteType.DEFAULT: تعمل بنفس الطريقة كوظيفة "كل" في Excel للصق مدى الخلايا.
- PasteType.ALL_EXCEPT_BORDERS: تعمل بنفس الطريقة كوظيفة "الكل باستثناء الحدود" في Excel للصق مدى الخلايا.

يوضح الكود النموذجي التالي استخدام حقل PasteType.DEFAULT.

**Java**

{{< highlight csharp >}}

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

ابتداءً من إصدار Aspose.Cells for Java 8.4.2، يتصرف الحقل التابع للتعداد PasteType.ALL بشكل مختلف عن وظيفة "الكل" في Excel للصق مدى الخلايا. الآن، ينسخ PasteType.ALL أيضًا عرض الأعمدة على نطاق الوجهة عكس وظيفة "الكل" في Excel. لتقليد سلوك "الكل" في Excel، يُرجى استخدام PasteType.DEFAULT.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
