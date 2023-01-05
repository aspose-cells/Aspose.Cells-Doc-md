---
title: ワークブック内のワークシートを非表示および再表示する
type: docs
weight: 80
url: /ja/net/hide-and-unhide-worksheets-in-a-workbook/
---
{{% alert color="primary" %}}

ワークブックを顧客に提示するとき、またはプレゼンテーションを行うとき、ワークブック内のワークシートを非表示にすると便利な場合があります。スプレッドシート モデリングへの構造化されたアプローチでは、データ、数式、グラフなどの視覚化を別のシートに保存することをお勧めします。このアプローチにより、レイアウトがすっきりとシンプルに保たれ、ワークブックのナビゲートが容易になります。結果を表示するときは、気が散らないように、データまたは数式シートを非表示にすることができます。

Microsoft Excel で作業しているユーザーは、ワークシートを簡単に非表示にしてから再表示 (表示) できます。 Excel スプレッドシートでプログラミングする開発者は、同じ機能を利用できます。ソフトウェア アプリケーション内からスプレッドシートを操作するには、さまざまな方法があります。 1 つは VSTO を使用する方法で、もう 1 つは Aspose.Cells for .NET です。

{{% /alert %}}

## **ワークシートの非表示と再表示**

この記事で比較する[隠蔽](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)と[再表示](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)ワークシート[VSTO](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)、C# または Visual Basic を使用して、同じタスクを[Aspose.Cells](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)、再び C# または Visual Basic を使用します。 Aspose.Cells では、Microsoft Excel がインストールされていなくても作業できます。

ワークシートを非表示にする手順は次のとおりです。

1. ファイルを開きます。
1. ワークシートを取得します。
1. ワークシートを非表示にします。
1. ファイルを保存します。

に[再表示する](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)非表示のシートの表示をオンに切り替えるだけです。

以下のコード サンプルは、最初にワークシートを非表示にする方法を示しています。最初のサンプルは、プロセスを示しています[VSTO](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)、C# または Visual Basic を使用する場合と比較して[Aspose.Cells](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)、再び C# または Visual Basics を使用します。

コード サンプルの 2 番目のセットは、ワークシートを再表示するために使用される行を示しています。[VSTO](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)また[Aspose.Cells](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/).

## **ワークシートを非表示にする**

以下は、ブック内のワークシートを非表示にする方法を示す VSTO および Aspose.Cells のコード サンプルです。

### **VSTO でワークシートを非表示にする**

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



//Specify the template Excel file path.

string myPath=@"d:\test\MyBook.xls";



//Open the Excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);



//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)excelApp.ActiveWorkbook.Sheets["Sheet1"];

//Hide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **Aspose.Cells for .NET でワークシートを非表示にする**

**C#**

{{< highlight "csharp" >}}



.......



using Aspose.Cells;



.......



//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = @"d:\test\MyBook.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **ワークシートの再表示**

以下は、VSTO と Aspose.Cells のコード サンプルで、ブック内のワークシートを再表示する方法を示しています。

### **VSTO でワークシートを再表示する**

**C#**

{{< highlight "csharp" >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Aspose.Cells for .NET でワークシートを再表示する**

**C#**

{{< highlight "csharp" >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
