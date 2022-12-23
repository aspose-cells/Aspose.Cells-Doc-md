---
title: API العام التغييرات في Aspose.Cells 8.3.1
type: docs
weight: 110
url: /ar/net/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.3.0 إلى 8.3.1 والتي قد تهم مطوري الوحدة / التطبيق.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة خاصية DataLabels.ShowCellRange**
 تمت إضافة الخاصية ShowCellRange إلى فئة DataLabels لتقليد وظيفة Excel لتنسيق تسميات بيانات المخطط في وقت التشغيل. يرجى ملاحظة أن Excel يوفر هذه الميزة من خلال الخطوات التالية.

1. حدد تسميات البيانات للسلسلة وانقر بزر الماوس الأيمن لفتح القائمة المنبثقة.
1.  انقر على**تنسيق تسميات البيانات ...** وسوف تظهر**خيارات التسمية**.
1.  حدد خانة الاختيار أو ألغِ تحديدها**يحتوي الملصق على - القيمة من Cells**.

 يصل نموذج التعليمات البرمجية أدناه إلى تسميات البيانات الخاصة بسلسلة التخطيطات ثم قم بتعيين طريقة DataLabels.ShowCellRange إلى true لتقليد ميزة Excel الخاصة بـ**يحتوي الملصق على - القيمة من Cells**.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}



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

 يرجى مراجعة المقال[عرض Cell المدى كعناوين بيانات](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels) للمزيد من المعلومات.

{{% /alert %}} 

### **تمت إضافة الطرق Cell. GetTable & ListObject.PutCellValue**
تمت إضافة الطريقتين Cell.GetTable & ListObject.PutCellValue مع Aspose.Cells for .NET 8.3.1 لتسهيل وصول المستخدمين إلى ListObject من خلية وإضافة قيم بداخلها باستخدام إزاحة الصف والعمود. يقوم نموذج التعليمات البرمجية التالي بتحميل جدول البيانات المصدر ، وإضافة القيم داخل الجدول.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

 يرجى مراجعة المقال[الوصول إلى الجدول من Cell وإضافة القيم بداخله باستخدام إزاحة الصف والعمود](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets) للمزيد من المعلومات.

{{% /alert %}} 

### **تمت إضافة الخاصية OdsSaveOptions.IsStrictSchema11**
تمت إضافة الخاصية IsStrictSchema11 إلى فئة OdsSaveOptions للسماح للمطورين بحفظ جدول البيانات بتنسيق يتوافق مع مواصفات ODF v1.2. القيمة الافتراضية لخاصية IsStrictSchema11 هي false ، وهذا يعني أنه من الإصدار 8.3.1 من Aspose.Cells APIs ، سيتم حفظ ملفات ODS بتنسيق ODF الإصدار 1.2 افتراضيًا.

يحفظ مقتطف الكود أدناه الملف ODS بتنسيق ODF 1.2.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

 يرجى مراجعة المقال[احفظ ملف ODS في مواصفات ODF 1.1 و 1.2](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications) للمزيد من المعلومات.

{{% /alert %}} 

### **طريقة SparklineCollection.Add added**
 كشفت واجهات برمجة التطبيقات (API) Aspose.Cells طريقة SparklineCollection.Add (سلسلة بيانات السلسلة ، وصف int ، عمود int) لتحديد نطاق البيانات وموقع مجموعة Sparkline. يرجى ملاحظة أن Excel يوفر نفس الميزة من خلال الخطوات التالية.

1. حدد الخلية التي تحتوي على خط المؤشر الخاص بك.
1.  يختار**تحرير البيانات من خط المؤشر** قسم داخل**تصميم** التبويب
1.  أختر**تحرير موقع المجموعة والبيانات**.
1.  حدد**نطاق البيانات** & **موقع**.

 يقوم نموذج التعليمات البرمجية التالي بتحميل جدول البيانات المصدر ، والوصول إلى أول مجموعة خط مؤشر وإضافة نطاقات بيانات ومواقع جديدة لمجموعة خط المؤشر.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

 يرجى مراجعة المقال[انسخ Sparkline عن طريق تحديد نطاق البيانات وموقع مجموعة Sparkline](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) للمزيد من المعلومات.

{{% /alert %}}
