---
title: إضافة أوراق عمل جديدة إلى المصنف وتفعيل ورقة
type: docs
weight: 10
url: /ar/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/
---
{{% alert color="primary" %}} 

عند العمل باستخدام ملف قالب ، في بعض الأحيان ، هناك حاجة لإضافة أوراق عمل إضافية إلى المصنف لجمع البيانات. سيتم ملء الخلايا الجديدة ببيانات في مواقع ومواقع محددة في كل ورقة عمل.

وبالمثل ، قد تحتاج إلى ورقة عمل معينة لتكون نشطة ويتم عرضها أولاً عند فتح الملف في Microsoft Excel. "الورقة النشطة" هي الورقة التي تعمل عليها في مصنف. يكون الاسم الموجود في علامة تبويب الورقة النشطة غامقًا بشكل افتراضي.

 تعد إضافة أوراق العمل وتعيين الورقة النشطة من المهام الشائعة والبسيطة التي يحتاج المطورون إلى معرفة كيفية تنفيذها. في هذه المقالة ، نقوم بتنفيذ هذه المهام باستخدام[VSTO](/cells/ar/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/) و[Aspose.Cells for .NET](/cells/ar/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/).

{{% /alert %}} 
## **إضافة أوراق العمل وتفعيل ورقة**
لأغراض إرشادات الترحيل هذه:

1. قم بإضافة أوراق عمل جديدة إلى ملف Excel Microsoft موجود.
1. املأ البيانات في خلايا كل ورقة عمل جديدة.
1. تنشيط ورقة في المصنف.
1. حفظ كملف Microsoft Excel.

فيما يلي مقتطفات التعليمات البرمجية المتوازية لـ VSTO (C# ، VB) و Aspose.Cells for .NET (C# ، VB) ، والتي توضح كيفية تحقيق هذه المهام.
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 .......

باستخدام Microsoft.VisualStudio.Tools.Applications.Runtime ؛

باستخدام Excel = Microsoft.Office.Interop.Excel ؛

باستخدام Office = Microsoft.Office.Core ؛

باستخدام System.Reflection.

.......

// إنشاء كائن التطبيق.

Excel.Application excelApp = new Excel.ApplicationClass () ؛

// حدد مسار ملف Excel للقالب.

سلسلة myPath = @ "d: \ test \ My_Book1.xls"؛

// افتح ملف Excel.

excelApp.Workbooks.Open (myPath، Missing.Value، Missing.Value،

مفقودة ، قيمة ، مفقودة ، قيمة ،

مفقودة ، قيمة ، مفقودة ، قيمة ،

مفقودة ، قيمة ، مفقودة ، قيمة ،

مفقودة ، قيمة ، مفقودة ، قيمة ،

مفقودة ، قيمة ، مفقودة ، قيمة ،

مفقودة .Value، Missing.Value) ؛

// قم بتعريف كائن ورقة عمل.

Excel.Worksheet newWorksheet ؛

// أضف 5 أوراق عمل جديدة إلى المصنف واملأ بعض البيانات

// في الخلايا.

 لـ (int i = 1 ؛ i< 6; i++)

{

//Add a worksheet to the workbook.

newWorksheet = Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value);

//Name the sheet.

newWorksheet.Name ="New_Sheet" + i.ToString();

//Get the Cells collection.

Excel.Range cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells.set_Item(i, i,"New_Sheet" + i.ToString());

}

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs(@"d:\test\out_My_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 .......

Imports Microsoft.VisualStudio.Tools.Applications.Runtime

Imports Excel = Microsoft.Office.Interop.Excel

Imports Office = Microsoft.Office.Core

Imports System.Reflection

.......

'Instantiate the Application object.

Dim excelApp As Excel.Application = New Excel.ApplicationClass()

'Specify the template excel file path.

Dim myPath As String = "d:\test\My_Book1.xls"

'Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value)

'Declare a Worksheet object.

Dim newWorksheet As Excel.Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 1 To 5 Step 1

'Add a worksheet to the workbook.

newWorksheet = CType(excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value), Excel.Worksheet)

'Name the sheet.

newWorksheet.Name ="New_Sheet" & i.ToString()

'Get the Cells collection.

Dim cells As Excel.Range = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells.Item(i, i) = "New_Sheet" & i.ToString()

Next

'Activate the first worksheet by default.

CType(excelApp.ActiveWorkbook.Sheets(1), Excel.Worksheet).Activate()

'Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("d:\test\out_My_Book1.xls")

'Quit the Application.

excelApp.Quit()



{{< /highlight >}}
### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 .......

باستخدام Aspose.Cells ؛

.......

// إنشاء مثيل ترخيص وتعيين ملف الترخيص

// من خلال طريقها

Aspose.Cells. رخصة الترخيص = Aspose.Cells.License جديد () ؛

License.SetLicense ("Aspose.Cells.lic") ؛

// حدد مسار ملف Excel للقالب.

سلسلة myPath = @ "d: \ test \ My_Book1.xls"؛

// إنشاء مصنف جديد.

// افتح ملف Excel.

مصنف المصنف = مصنف جديد (myPath) ؛

// قم بتعريف كائن ورقة عمل.

ورقة عمل جديدة

// أضف 5 أوراق عمل جديدة إلى المصنف واملأ بعض البيانات

// في الخلايا.

 لـ (int i = 0 ؛ i< 5; i++)

{

//Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

//Name the sheet.

newWorksheet.Name = "New_Sheet" + (i+1).ToString();

//Get the Cells collection.

Cells cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells[i, i].PutValue("New_Sheet" + (i+1).ToString());

}

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save(@"d:\test\out_My_Book1.xls");



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 .......

Imports Aspose.Cells

.......

'Instantiate an instance of license and set the license file

'through its path

Dim license As Aspose.Cells.License = New Aspose.Cells.License

license.SetLicense("Aspose.Cells.lic")

'Specify the template excel file path.

Dim myPath As String ="d:\test\My_Book1.xls"

'Instantiate a new Workbook.

'Open the excel file.

Dim workbook As Workbook = New Workbook(myPath)

'Declare a Worksheet object.

Dim newWorksheet As Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 0 To 4 Step 1

'Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets(workbook.Worksheets.Add())

'Name the sheet.

newWorksheet.Name = "New_Sheet" + (i + 1).ToString()

'Get the Cells collection.

Dim cells As Cells = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells(i, i).PutValue("New_Sheet" + (i + 1).ToString())

Next

'Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0

'Save As the excel file.

workbook.Save("c:\test\out_My_Book1.xls")



{{< /highlight >}}
