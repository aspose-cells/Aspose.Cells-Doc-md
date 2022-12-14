---
title: API العام التغييرات في Aspose.Cells 8.3.1
type: docs
weight: 120
url: /ar/java/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.3.0 إلى 8.3.1 والتي قد تهم مطوري الوحدة / التطبيق.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة خاصية DataLabels.ShowCellRange**
تمت إضافة أداة الإدخال / الضبط للخاصية ShowCellRange إلى فئة DataLabels لتقليد وظيفة Excel الخاصة بتنسيق تسميات بيانات المخطط في وقت التشغيل. يرجى ملاحظة أن Excel يوفر هذه الميزة من خلال الخطوات التالية.

1. حدد تسميات البيانات للسلسلة وانقر بزر الماوس الأيمن لفتح القائمة المنبثقة.
1.  انقر على**تنسيق تسميات البيانات ...** وسوف تظهر**خيارات التسمية**.
1.  حدد خانة الاختيار أو ألغِ تحديدها**يحتوي الملصق على - القيمة من Cells**.

 يصل نموذج التعليمات البرمجية أدناه إلى تسميات البيانات الخاصة بسلسلة التخطيطات ثم قم بتعيين طريقة DataLabels.setShowCellRange () إلى true لتقليد ميزة Excel الخاصة بـ**يحتوي الملصق على - القيمة من Cells**.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from the source spreadsheet containing an existing chart

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.getNSeries().get(0).getDataLabels();

dataLabels.setShowCellRange(true);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 يرجى مراجعة المقال[عرض Cell المدى كعناوين بيانات](/cells/ar/java/showing-cell-range-as-the-data-labels/) للمزيد من المعلومات.

{{% /alert %}} 

### **تمت إضافة الطرق Cell.getTable & ListObject.putCellValue**
تمت إضافة الطريقتين Cell.getTable & ListObject.putCellValue مع Aspose.Cells for Java 8.3.1 لتسهيل وصول المستخدمين إلى ListObject من خلية وإضافة قيم بداخلها باستخدام إزاحة الصف والعمود. يقوم نموذج التعليمات البرمجية التالي بتحميل جدول البيانات المصدر ، وإضافة القيم داخل الجدول.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell D5 which lies inside the table

Cell cell = worksheet.getCells().get("D5");

//Put value inside the cell D5

cell.putValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.getTable();

//Add some value using Row and Column Offset

table.putCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 يرجى مراجعة المقال[الوصول إلى الجدول من Cell وإضافة القيم بداخله باستخدام إزاحة الصف والعمود](/cells/ar/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) للمزيد من المعلومات.

{{% /alert %}} 

### **طرق OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11 مضاف**
تمت إضافة الطرق هي StrictSchema11 & setStrictSchema11 إلى فئة OdsSaveOptions للسماح للمطورين بحفظ جدول البيانات بتنسيق يتوافق مع مواصفات ODF v1.2. القيمة الافتراضية لخاصية setStrictSchema11 خاطئة ، وهذا يعني أنه من الإصدار 8.3.1 لواجهات برمجة التطبيقات Aspose.Cells سيتم حفظ ملفات ODS كنسق ODF الإصدار 1.2 افتراضيًا.

مقتطف الشفرة الوارد أدناه يحفظ ملف ODS بتنسيق ODF 1.2.

**Java**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some value in cell A1

Cell cell = worksheet.getCells().get("A1");

cell.putValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.setStrictSchema11(true);

workbook.save("ODF1.1.ods", options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 يرجى مراجعة المقال[حفظ ملف ODS في مواصفات ODF 1.1 و 1.2](/cells/ar/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) للمزيد من المعلومات.

{{% /alert %}} 

### **طريقة SparklineCollection.add المضافة**
 كشفت واجهات برمجة التطبيقات Aspose.Cells طريقة SparklineCollection.add (String dataRange ، int row ، int column) لتحديد نطاق البيانات وموقع مجموعة Sparkline. يرجى ملاحظة أن Excel يوفر نفس الميزة من خلال الخطوات التالية.

1. حدد الخلية التي تحتوي على خط المؤشر الخاص بك.
1.  يختار**تحرير البيانات من خط المؤشر** قسم داخل**تصميم** التبويب
1.  يختار**تحرير موقع المجموعة والبيانات**.
1. حدد**نطاق البيانات** & **موقع**.

 يقوم نموذج التعليمات البرمجية التالي بتحميل جدول البيانات المصدر ، والوصول إلى أول مجموعة خط مؤشر وإضافة نطاقات بيانات ومواقع جديدة لمجموعة خط المؤشر.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first sparkline group

SparklineGroup group = worksheet.getSparklineGroupCollection().get(0);

//Add Data Ranges and Locations inside this sparkline group

group.getSparklineCollection().add("D5:O5", 4, 15);

group.getSparklineCollection().add("D6:O6", 5, 15);

group.getSparklineCollection().add("D7:O7", 6, 15);

group.getSparklineCollection().add("D8:O8", 7, 15);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 يرجى مراجعة المقال[انسخ Sparkline عن طريق تحديد نطاق البيانات وموقع مجموعة Sparkline](/cells/ar/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) للمزيد من المعلومات.

{{% /alert %}}
