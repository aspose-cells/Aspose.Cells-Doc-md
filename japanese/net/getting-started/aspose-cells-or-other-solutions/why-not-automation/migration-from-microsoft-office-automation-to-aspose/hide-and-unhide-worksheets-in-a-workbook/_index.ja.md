---
title: ワークブック内のワークシートを非表示または表示する
type: docs
weight: 80
url: /ja/net/hide-and-unhide-worksheets-in-a-workbook/
---

{{% alert color="primary" %}}

顧客にワークブックを提示したりプレゼンテーションを行う際に、ワークブック内のワークシートを非表示にすると便利です。スプレッドシートモデリングの構造化されたアプローチでは、データ、数式、チャートなどの視覚化情報を個々のシートに保管することが推奨されます。このアプローチにより、レイアウトが清潔でシンプルになり、ワークブックが操作しやすくなります。結果を提示する際には、データや数式のシートを非表示にして、注意がそれにそれなくなるのを防ぐことができます。

Microsoft Excelで作業するユーザーは、ワークシートを簡単に非表示にしてから再表示（表示）できます。同じ機能は、Excelスプレッドシートでプログラムを作成する開発者にも利用できます。ソフトウェアアプリケーション内でスプレッドシートを操作するさまざまな方法があります。1つの方法はVSTOを使用することであり、もう1つの方法はAspose.Cells for .NETを使用することです。

{{% /alert %}}

## **ワークシートを非表示または表示する**

この記事では、[VSTO](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)を使用してC#またはVisual Basicを使用し、[Aspose.Cells](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)を使用してまたC#またはVisual Basicを使用して、同じタスクを実行する方法を比較しています。Aspose.Cellsを使用すると、Microsoft Excelのインストールがなくても作業できます。

ワークシートを非表示にする手順：

1. ファイルを開く。
1. ワークシートを取得する。
1. ワークシートを非表示にする。
1. ファイルを保存します。

ワークシートを再度[非表示に](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)おくことをやめるには、非表示になっているシートの可視性を単に切り替えます。

以下のコードサンプルでは、まずワークシートを非表示にする方法を示します。最初のサンプルは、[VSTO](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)を使用して、C#またはVisual Basicを使用してこのプロセスをどのように行うかを示し、[Aspose.Cells](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)を使用して、またC#またはVisual Basicを使用して行う方法を比較しています。

次の一連のコードサンプルは、[VSTO](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)または[Aspose.Cells](/cells/ja/net/hide-and-unhide-worksheets-in-a-workbook/)でワークシートの非表示を解除する行を示します。

## **ワークシートを非表示にする**

以下は、VSTOおよびAspose.Cellsのコードサンプルで、ワークブック内のワークシートを非表示にする方法を示しています。

### **VSTOでのワークシートの非表示**

**C#**

{{< highlight csharp >}}



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


### **Aspose.Cells for .NETでのワークシートの非表示**

**C#**

{{< highlight csharp >}}



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

## **ワークシートの表示を解除する**

以下は、VSTOおよびAspose.Cellsのコードサンプルで、ワークブック内のワークシートを非表示から表示する方法を示しています。

### **VSTOでのワークシートの表示を解除**

**C#**

{{< highlight csharp >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Aspose.Cells for .NETでのワークシートの表示を解除**

**C#**

{{< highlight csharp >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
