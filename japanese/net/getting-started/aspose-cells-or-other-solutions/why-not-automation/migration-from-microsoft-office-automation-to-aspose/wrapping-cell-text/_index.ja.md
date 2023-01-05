---
title: ラッピング Cell テキスト
type: docs
weight: 130
url: /ja/net/wrapping-cell-text/
---
{{% alert color="primary" %}}

テキストを折り返すと、読みやすくなります。折り返されたテキストを含むセルは、テキストが他のセルの上に表示されないように、テキストに合わせて拡大されます。

Aspose.Cells for .NET を使用すると、開発者は、ユーザーが Microsoft Excel で実行できるほとんどのタスクをアプリケーションで実行できます (セル内のテキストの折り返しなど)。この記事では、VSTO と Aspose.Cells を使用してタスクを比較し、その方法を説明します。

{{% /alert %}}

## **ラッピング Cell テキスト**

2 つのセル (折り返されたテキストのあるセルとないセル) を持つワークシートを作成するには:

1. ワークシートを設定します。
 1. ワークブックを作成します。
 1. 最初のワークシートにアクセスします。
1. テキストを追加：
 1. セル A1 にテキストを追加します。
 1. 折り返されたテキストをセル A5 に追加します。
1. スプレッドシートを保存します。

以下のコード サンプルは、これらの手順を実行する方法を示しています。[VSTO](/cells/ja/net/wrapping-cell-text/) C# または Visual Basic で。を使用して同じことを行う方法を示すコード サンプル[Aspose.Cells for .NET](/cells/ja/net/wrapping-cell-text/)、再び C# または Visual Basic を使用して、直後に続きます。

コードを実行すると、2 つのセルを含むスプレッドシートが作成されます。

|<p>**VSTO で折り返しセル テキストを出力する** </p><p>![todo:画像_代替_文章](wrapping-cell-text_1.png)</p>|<p>**Aspose.Cells for .NET で折り返しセル テキストを出力する** </p><p>![todo:画像_代替_文章](wrapping-cell-text_2.png)</p>|
|:- |:- |

### **VSTO を使用した Cell テキストの折り返し**

**C#**

{{< highlight "csharp" >}}

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

### **Aspose.Cells for .NET を使用した Cell テキストの折り返し**

**C#**

{{< highlight "csharp" >}}

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
