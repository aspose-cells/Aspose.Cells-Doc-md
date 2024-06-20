---
title: تغييرات الواجهة البرمجية العامة في Aspose.Cells 8.3.1
type: docs
weight: 110
url: /ar/net/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.3.0 إلى 8.3.1 التي قد تكون مثيرة للاهتمام لمطوري الوحدات/التطبيقات.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة خاصية DataLabels.ShowCellRange**
تمت إضافة خاصية ShowCellRange لفئة DataLabels من أجل تقليد وظيفة تنسيق علامات البيانات في الرسم البياني في وقت التشغيل. يرجى ملاحظة أن Excel يوفر هذه الميزة من خلال الخطوات التالية. 

1. حدد تسميات البيانات للسلسلة ثم انقر بزر الماوس الأيمن لفتح القائمة المنبثقة.
1. انقر **تنسيق تسميات البيانات...** وستظهر **خيارات التسمية**.
1. حدد أو ألغِ تحديد خانة الاختيار **التسمية تحتوي على - القيمة من الخلايا**.

الشفرة النموذجية أدناه تصل إلى تسميات البيانات لسلسلة الرسم البياني ثم تضبط طريقة DataLabels.ShowCellRange إلى true لتقليد ميزة إكسيل **Label Contains - Value From Cells**.

**C#**

{{< highlight csharp >}}

 //Create workbook from the source Excel file

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.NSeries[0].DataLabels;

dataLabels.ShowCellRange = true;

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}



'Create workbook from the source Excel file

Dim m_workbook As Workbook = New Workbook("sample.xlsx")

'Access the first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the chart inside the worksheet

Dim m_chart As Chart = m_worksheet.Charts(0)

'Check the "Label Contains - Value From Cells"

Dim m_dataLabels As DataLabels = m_chart.NSeries(0).DataLabels

m_dataLabels.ShowCellRange = True

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

يرجى التحقق من المقالة [عرض نطاق الخلية كتسميات البيانات](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels) للمزيد من المعلومات.

{{% /alert %}} 

### **أضيفت طرق Cell.GetTable & ListObject.PutCellValue**
تمت إضافة الطرق Cell.GetTable & ListObject.PutCellValue مع Aspose.Cells for .NET 8.3.1 لتيسير وصول المستخدمين إلى ListObject من خلية وإضافة القيم داخلها باستخدام تعويضات الصف والعمود. تحمل الشفرة النموذجية التالية جدول البيانات الأصلي وتضيف القيم داخل الجدول.

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell D5 which lies inside the table

Cell cell = worksheet.Cells["D5"];

//Put value inside the cell D5

cell.PutValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.GetTable();

//Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access cell D5 which lies inside the table

Dim m_cell As Cell = m_worksheet.Cells("D5")

'Put value inside the cell D5

m_cell.PutValue("D5 Data")

'Access the Table from this cell

Dim table As ListObject = m_cell.GetTable()

'Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]")

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

يرجى التحقق من المقالة [الوصول إلى الجدول من الخلية وإضافة القيم داخله باستخدام تعويضات الصف والعمود](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets) للمزيد من المعلومات.

{{% /alert %}} 

### **تمت إضافة OdsSaveOptions.IsStrictSchema11 Property**
تمت إضافة الخاصية IsStrictSchema11 إلى فئة OdsSaveOptions للسماح للمطورين بحفظ جدول البيانات في تنسيق يتوافق مع مواصفات ODF v1.2. القيمة الافتراضية لخاصية IsStrictSchema11 هي false، مما يعني أنه ابتداءً من الإصدار 8.3.1 من واجهات برمجة التطبيقات Aspose.Cells ستتم حفظ ملفات ODS كتنسيق ODF الإصدار 1.2 افتراضيًا.

الكود المقدم أدناه يحفظ ملف ODS بتنسيق ODF 1.2.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some value in cell A1

Cell cell = worksheet.Cells["A1"];

cell.PutValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.Save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.IsStrictSchema11 = true;

workbook.Save("ODF1.1.ods", options);


{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Create workbook 

Dim m_workbook As Workbook = New Workbook()

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Put some value in cell A1

Dim m_cell As Cell = m_worksheet.Cells("A1")

m_cell.PutValue("Welcome to Aspose!")

'Save ODS in ODF 1.2 version which is default

Dim options As OdsSaveOptions = New OdsSaveOptions()

m_workbook.Save("ODF1.2.ods", options)

'Save ODS in ODF 1.1 version

options.IsStrictSchema11 = True

m_workbook.Save("ODF1.1.ods", options)

{{< /highlight >}}

{{% alert color="primary" %}} 

يرجى التحقق من المقالة [حفظ ملف ODS في مواصفات ODF 1.1 و 1.2](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications) للمزيد من المعلومات.

{{% /alert %}} 

### **تمت إضافة الطريقة SparklineCollection.Add**
لقد قامت واجهات برمجة التطبيقات Aspose.Cells بتعريض الطريقة SparklineCollection.Add(string dataRange, int row, int column) لتحديد نطاق البيانات وموقع مجموعة الخطوط الكهربائية. يرجى الملاحظة أن إكسيل يوفر نفس الميزة من خلال الخطوات التالية. 

1. حدد الخلية التي تحتوي على بيانات الرسم البياني.
1. حدد **تحرير البيانات من قسم الرسم البياني** داخل علامة التبويب **تصميم**
1. اختر **تحرير موقع المجموعة والبيانات**.
1. حدد **نطاق البيانات** و**الموقع**.

الكود المعروض أدناه يحمل جدول البيانات المصدر، ويصل إلى أول مجموعة البيانات الرسمية ويضيف نطاقات بيانات جديدة ومواقع لمجموعة البيانات الرسمية. 

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first sparkline group

SparklineGroup group = worksheet.SparklineGroupCollection[0];

//Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15);

group.SparklineCollection.Add("D6:O6", 5, 15);

group.SparklineCollection.Add("D7:O7", 6, 15);

group.SparklineCollection.Add("D8:O8", 7, 15);

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the first sparkline group

Dim group As SparklineGroup = m_worksheet.SparklineGroupCollection(0)

'Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15)

group.SparklineCollection.Add("D6:O6", 5, 15)

group.SparklineCollection.Add("D7:O7", 6, 15)

group.SparklineCollection.Add("D8:O8", 7, 15)

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

يرجى التحقق من المقالة [Copy Sparkline by Specifying Data Range and Location of Sparkline Group](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) لمزيد من المعلومات.

{{% /alert %}}
