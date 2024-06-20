---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.3.1
type: docs
weight: 120
url: /ar/java/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.3.0 إلى 8.3.1 التي قد تكون مثيرة للاهتمام لمطوري الوحدات/التطبيقات.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة خاصية DataLabels.ShowCellRange**
تمت إضافة getter/setter للخاصية ShowCellRange إلى فئة DataLabels من أجل تقليد وظيفة تنسيق تسميات البيانات في الرسوم البيانية في الوقت الفعلي. يرجى ملاحظة أن Excel يوفر هذه الميزة من خلال الخطوات التالية. 

1. حدد تسميات البيانات للسلسلة ثم انقر بزر الماوس الأيمن لفتح القائمة المنبثقة.
1. انقر **تنسيق تسميات البيانات...** وستظهر **خيارات التسمية**.
1. حدد أو ألغِ تحديد خانة الاختيار **التسمية تحتوي على - القيمة من الخلايا**.

يقوم الكود النموذجي أدناه بالوصول إلى تسميات البيانات في سلسلة الرسم البياني ثم يقوم بتعيين طريقة DataLabels.setShowCellRange() على true لتقليد ميزة Excel **التسمية تحتوي على - القيمة من الخلايا**.

**Java**

{{< highlight csharp >}}

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

يرجى التحقق من المقالة [عرض مجال الخلية كعلامات البيانات](/cells/ar/java/showing-cell-range-as-the-data-labels/) للمزيد من المعلومات.

{{% /alert %}} 

### **تمت إضافة طرق Cell.getTable & ListObject.putCellValue.**
تمت إضافة الطرق Cell.getTable & ListObject.putCellValue مع Aspose.Cells for Java 8.3.1 لتسهيل وصول المستخدمين إلى ListObject من الخلية وإضافة القيم داخلها باستخدام تعويضات الصف والعمود. يحمل الكود المعروض أدناه الجدول في جدول بيانات المصدر ويضيف قيم داخل الجدول.

**Java**

{{< highlight csharp >}}

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

يرجى التحقق من المقالة [الوصول إلى الجدول من الخلية وإضافة القيم داخلها باستخدام تأويل الصف والعمود](/cells/ar/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) للمزيد من المعلومات.

{{% /alert %}} 

### **تمت إضافة طرق OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11.**
تمت إضافة الطرق isStrictSchema11 & setStrictSchema11 إلى فئة OdsSaveOptions من أجل السماح للمطورين بحفظ جدول البيانات بالتنسيق المتوافق مع مواصفات ODF v1.2. القيمة الافتراضية لخاصية setStrictSchema11 هي false، وهذا يعني أنه اعتبارا من الإصدار 8.3.1 من واجهات برمجة التطبيقات الخاصة بـ Aspose.Cells، سيتم حفظ ملفات ODS كتنسيق ODF إصدار 1.2 بشكل افتراضي.

الكود المقدم أدناه يحفظ ملف ODS بتنسيق ODF 1.2.

**Java**

{{< highlight csharp >}}

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

يرجى التحقق من المقالة [حفظ ملف ODS بمواصفات ODF 1.1 و 1.2](/cells/ar/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) للمزيد من المعلومات.

{{% /alert %}} 

### **تمت إضافة طريقة SparklineCollection.add.**
تمتك عروض واجهات برمجة التطبيقات لـ Aspose.Cells إضافة طريقة SparklineCollection.add(String dataRange, int row, int column) لتحديد مجال البيانات والموقع لمجموعة بيانات Sparkline. يرجى ملاحظة أن ميزة مماثلة متوفرة في Excel من خلال الخطوات التالية. 

1. حدد الخلية التي تحتوي على بيانات الرسم البياني.
1. حدد **تحرير البيانات من قسم الرسم البياني** داخل علامة التبويب **تصميم**
1. اختر **تحرير موقع المجموعة والبيانات**.
1. حدد **نطاق البيانات** و**الموقع**.

الكود المعروض أدناه يحمل جدول البيانات المصدر، ويصل إلى أول مجموعة البيانات الرسمية ويضيف نطاقات بيانات جديدة ومواقع لمجموعة البيانات الرسمية. 

**Java**

{{< highlight csharp >}}

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

يرجى التحقق من المقالة [نسخ مخططات البيانات عن طريق تحديد نطاق البيانات وموقع مجموعة البيانات الرسمية](/cells/ar/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) للمزيد من المعلومات.

{{% /alert %}}
