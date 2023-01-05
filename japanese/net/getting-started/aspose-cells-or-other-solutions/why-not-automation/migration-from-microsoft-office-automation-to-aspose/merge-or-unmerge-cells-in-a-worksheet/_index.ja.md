---
title: ワークシートで Cells をマージまたはマージ解除する
type: docs
weight: 40
url: /ja/net/merge-or-unmerge-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

ワークシートで作業しているときに、ワークシートの上部にまたがる単一のセルにタイトル/見出しを作成する必要があることがよくあります。請求書を作成していて、合計値または要約値の列を少なくしたい場合があります。 2 つ以上のセルから 1 つのセルを作成する場合は、セルを結合します。 VSTO と Aspose.Cells for .NET を個別に使用してタスクを実行します。

{{% /alert %}}

## **説明**

既存の Excel ファイルを開き、ワークブックの最初のワークシートのいくつかのセルを結合して、Excel ファイルを保存します。

## **合併 Cells**

以下は、VSTO (C#、VB) および Aspose.Cells for .NET (C#、VB) の並列コード スニペットです。

### **1) VSTO**

**C#**

{{< highlight "csharp" >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath=@"d:\test\MyBook.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the range of cells i.e.., A1:C1.

Excel.Range rng1 = excelApp.get_Range("A1", "C1");

//Merge the cells.

rng1.Merge(Missing.Value);

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template excel file path.

string myPath=@"d:\test\MyBook.xls";

//Open the excel file.

workbook.Open(myPath);

//Get the range of cells i.e.., A1:C1.

Aspose.Cells.Range rng1 = workbook.Worksheets[0].Cells.CreateRange("A1", "C1");

//Merge the cells.

rng1.Merge();

//Save the file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **Cells のマージ解除**

セルの結合を解除するには、VSTO (C#、VB) および Aspose.Cells for .NET (C#、VB) の次のコード行を使用します。

### **1) VSTO**

**C#**

{{< highlight "csharp" >}}

 //Get the A1 cell (Merged Cell).

Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

//UnMerge the cell.

rng1.UnMerge();     



{{< /highlight >}}

### **2) Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Get the A1 cell (Merged Cell).

Cells rng1 = workbook.Worksheets[0].Cells;

//UnMerge the cell.

rng1.UnMerge(0, 0, 1, 3); 

{{< /highlight >}}
