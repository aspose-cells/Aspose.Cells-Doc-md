---
title: ワークブックへの新しいワークシートの追加とシートのアクティブ化
type: docs
weight: 10
url: /ja/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/
---
{{% alert color="primary" %}} 

テンプレート ファイルを使用する場合、データを収集するためにワークシートをワークブックに追加する必要がある場合があります。新しいセルには、各ワークシートの指定された位置と場所にデータが入力されます。

同様に、Microsoft Excel でファイルを開いたときに、特定のワークシートをアクティブにして最初に表示する必要がある場合があります。 "アクティブ シート" は、ワークブックで作業しているシートです。アクティブなシートのタブの名前は、デフォルトで太字になっています。

ワークシートの追加とアクティブなシートの設定は、開発者が実行方法を知る必要がある一般的で単純なタスクです。この記事では、以下を使用してこれらのタスクを実行します。[VSTO](/cells/ja/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/)と[Aspose.Cells for .NET](/cells/ja/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/).

{{% /alert %}} 
## **ワークシートの追加とシートのアクティブ化**
この移行のヒントの目的:

1. 新しいワークシートを既存の Microsoft Excel ファイルに追加します。
1. 新しい各ワークシートのセルにデータを入力します。
1. ワークブックでシートをアクティブにします。
1. Microsoft Excel ファイルとして保存します。

以下は、VSTO (C#、VB) と Aspose.Cells for .NET (C#、VB) の並列コード スニペットで、これらのタスクを実行する方法を示しています。
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 .......

Microsoft.VisualStudio.Tools.Applications.Runtime を使用して;

Excel を使用 = Microsoft.Office.Interop.Excel;

オフィスを使用 = Microsoft.Office.Core;

System.Reflection を使用します。

.......

//Application オブジェクトをインスタンス化します。

Excel.Application excelApp = new Excel.ApplicationClass();

// テンプレートの Excel ファイルのパスを指定します。

string myPath = @"d:\test\My_Book1.xls";

//エクセルファイルを開く。

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value、Missing.Value、

Missing.Value、Missing.Value、

Missing.Value、Missing.Value、

Missing.Value、Missing.Value、

Missing.Value、Missing.Value、

Missing.Value、Missing.Value);

//Worksheet オブジェクトを宣言します。

Excel.Worksheet newWorksheet;

// ワークブックに 5 つの新しいワークシートを追加し、いくつかのデータを入力します

//セルに。

for (int i = 1; i< 6; i++)

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

Aspose.Cells を使用。

.......

//ライセンスのインスタンスをインスタンス化し、ライセンス ファイルを設定します

//そのパスを介して

Aspose.Cells.License ライセンス = 新しい Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

// テンプレートの Excel ファイルのパスを指定します。

string myPath =@"d:\test\My_Book1.xls";

// 新しい Workbook をインスタンス化します。

//エクセルファイルを開く。

ワークブック ワークブック = 新しいワークブック(myPath);

//Worksheet オブジェクトを宣言します。

ワークシート newWorksheet;

// ワークブックに 5 つの新しいワークシートを追加し、いくつかのデータを入力します

//セルに。

for (int i = 0; i< 5; i++)

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
