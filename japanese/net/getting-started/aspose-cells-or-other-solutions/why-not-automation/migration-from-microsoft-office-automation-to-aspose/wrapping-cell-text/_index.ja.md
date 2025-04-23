---
title: セルテキストの折り返し
type: docs
weight: 130
url: /ja/net/wrapping-cell-text/
---

{{% alert color="primary" %}}

テキストを折り返すと、折り返されたテキストを持つセルが他のセルに表示されないようになり、読みやすくなります。

Aspose.Cells for .NETを使用すると、開発者はMicrosoft Excelでユーザーが実行できるほとんどのタスクをアプリケーションで実行できます。これにはセル内のテキストの折り返しなども含まれます。これは、VSTOおよびAspose.Cellsを使用して同じタスクを説明し、比較する記事です。Aspose.Cellsは効率的なコーディングに最適化されており、Microsoft Automationなしで動作します。

{{% /alert %}}

## **セルのテキストの折り返し**

折り返しテキストおよび折り返しのないテキストを含むワークシートを作成するには:

1. ワークシートを設定します:
   1. ワークブックを作成する。
   1. 最初のワークシートにアクセスします。
1. テキストを追加します:
   1. セルA1にテキストを追加します。
   1. セルA5に折り返しテキストを追加します。
1. スプレッドシートを保存します。

以下のコード例では、[VSTO](/cells/ja/net/wrapping-cell-text/)を使用してこれらの手順を実行する方法と、[Aspose.Cells for .NET](/cells/ja/net/wrapping-cell-text/)を使用して同じことを行う方法を、直後にC#またはVisual Basicを使用して示しています。

コードを実行すると、折り返されていないテキストを含むセルと折り返されたテキストを含むセルのあるスプレッドシートが作成されます。

|<p>**Output wrapping cell text with VSTO** </p><p>![todo:image_alt_text](wrapping-cell-text_1.png)</p>|<p>**Output wrapping cell text with Aspose.Cells for .NET** </p><p>![todo:image_alt_text](wrapping-cell-text_2.png)</p>|
| :- | :- |

### **VSTOを使用してセルのテキストを折り返す**

**C#**

{{< highlight csharp >}}

 //Note: To help you better, the code uses full namespacing

void WrappingCellText()

{

    //Access vsto application

    Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

    //Access workbook 

    Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

    //Access worksheet 

    Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

    //Access vsto worksheet

    Microsoft.Office.Tools.Excel.Worksheet sheet = Globals.Factory.GetVstoObject(m_sheet);

    //Place some text in cell A1 without wrapping

    Microsoft.Office.Interop.Excel.Range cellA1 = sheet.Cells.get_Range("A1");

    cellA1.Value = "Sample Text Unwrapped";

    //Place some text in cell A5 with wrapping

    Microsoft.Office.Interop.Excel.Range cellA5 = sheet.Cells.get_Range("A5");

    cellA5.Value = "Sample Text Wrapped";

    cellA5.WrapText = true;

    //Save the workbook

    workbook.SaveAs("f:\\downloads\\OutputVsto.xlsx");

    //Quit the application

    app.Quit();

}

{{< /highlight >}}

### **Aspose.Cells for .NETを使用してセルのテキストを折り返す**

**C#**

{{< highlight csharp >}}

 void WrappingCellText()

{

    //Create workbook

    Workbook workbook = new Workbook();

    //Access worksheet

    Worksheet worksheet = workbook.Worksheets[0];

    //Place some text in cell A1 without wrapping

    Cell cellA1 = worksheet.Cells["A1"];

    cellA1.PutValue("Some Text Unwrapped");

    //Place some text in cell A5 wrapping

    Cell cellA5 = worksheet.Cells["A5"];

    cellA5.PutValue("Some Text Wrapped");

    Style style = cellA5.GetStyle();

    style.IsTextWrapped = true;

    cellA5.SetStyle(style);

    //Autofit rows

    worksheet.AutoFitRows();

    //Save the workbook

    workbook.Save("f:\\downloads\\OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
