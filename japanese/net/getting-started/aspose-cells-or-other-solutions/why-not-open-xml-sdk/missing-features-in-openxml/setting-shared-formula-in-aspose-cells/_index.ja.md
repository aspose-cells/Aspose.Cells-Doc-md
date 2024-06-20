---
title: Aspose.Cellsでの共有フォーミュラの設定
type: docs
weight: 110
url: /ja/net/setting-shared-formula-in-aspose-cells/
---

{{% alert color="primary" %}} 

データで埋められたワークシートがあるとします。

B2に関数を追加し、最初のデータ行の売上税を計算したいとします。税金は9%です。売上税を計算する式は次のとおりです:"=A2*0.09"。この記事では、Aspose.Cellsでこの式を適用する方法について説明します。

{{% /alert %}} 

Aspose.Cellsを使用すると、Cell.Formulaプロパティを使用して式を指定できます。

列の他のセル（B3、B4、B5など）に数式を追加するための2つのオプションがあります。

最初のセルに実行したことと同様に、各セルの式を設定し、セル参照を更新する必要があります（A3*0.09、A4*0.09、A5*0.09など）。各行のためにセル参照を更新する必要があります。また、Aspose.Cellsが個々の式を解析する必要があり、大きなスプレッドシートや複雑な式の場合は時間がかかる場合があります。また、ループはそれらを削減できますが、余分なコード行が追加されます。

別の方法は**共有フォーミュラ**を使用することです。共有フォーミュラを使用すると、各行のセル参照に対して自動的に式が更新され、税金が正しく計算されます。Cell.SetSharedFormulaメソッドは、最初の方法よりも効率的です。

次の例では、その使用方法を示しています。

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Shared Formula.xlsx";

//Instantiate a Workbook from existing file

Workbook workbook = new Workbook(FileName);

//Get the cells collection in the first worksheet

Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

//Apply the shared formula in the range i.e.., B2:B14

cells["B2"].SetSharedFormula("=A2*0.09", 13, 1);

//Save the excel file

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **実行例のダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
