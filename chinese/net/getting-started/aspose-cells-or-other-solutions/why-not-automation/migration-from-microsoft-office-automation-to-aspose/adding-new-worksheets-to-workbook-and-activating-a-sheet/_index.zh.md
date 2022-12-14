---
title: 将新工作表添加到工作簿并激活工作表
type: docs
weight: 10
url: /zh/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/
---
{{% alert color="primary" %}} 

使用模板文件时，有时需要将额外的工作表添加到工作簿中以收集数据。新单元格将填充每个工作表中指定位置和位置的数据。

同样，当文件在 Microsoft Excel 中打开时，您可能需要首先激活和查看特定工作表。 “活动工作表”是您在工作簿中处理的工作表。默认情况下，活动工作表选项卡上的名称为粗体。

添加工作表和设置哪个工作表处于活动状态是开发人员需要知道如何执行的常见且简单的任务。在本文中，我们使用[VSTO](/cells/zh/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/)和[Aspose.Cells for .NET](/cells/zh/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/).

{{% /alert %}} 
## **添加工作表和激活工作表**
出于此迁移提示的目的：

1. 将新工作表添加到现有 Microsoft Excel 文件。
1. 将数据填充到每个新工作表的单元格中。
1. 激活工作簿中的工作表。
1. 另存为 Microsoft Excel 文件。

下面是 VSTO（C#，VB）和 Aspose.Cells for .NET（C#，VB）的并行代码片段，展示了如何完成这些任务。
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 .......

使用 Microsoft.VisualStudio.Tools.Applications.Runtime；

使用 Excel = Microsoft.Office.Interop.Excel；

使用 Office = Microsoft.Office.Core；

使用 System.Reflection；

.......

//实例化应用对象。

Excel.Application excelApp = new Excel.ApplicationClass();

//指定模板excel文件路径。

string myPath = @"d:\test\My_Book1.xls";

//打开excel文件。

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

缺失值，缺失值，

缺失值，缺失值，

缺失值，缺失值，

缺失值，缺失值，

缺失值，缺失值，

缺失值，缺失值）；

//声明一个工作表对象。

Excel.Worksheet 新工作表；

//向工作簿中添加5个新工作表并填充一些数据

//进入细胞。

对于 (int i = 1; i< 6; i++)

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

**虚拟机**

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

使用 Aspose.Cells；

.......

//实例化一个license实例并设置license文件

//通过它的路径

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

//指定模板excel文件路径。

string myPath =@"d:\test\My_Book1.xls";

//实例化一个新的工作簿。

//打开excel文件。

工作簿工作簿=新工作簿（myPath）；

//声明一个工作表对象。

工作表新工作表；

//向工作簿中添加5个新工作表并填充一些数据

//进入细胞。

对于 (int i = 0; i< 5; i++)

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

**虚拟机**

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
