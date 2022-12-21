---
title: Aspose.Cells に共有数式を設定する
type: docs
weight: 110
url: /ja/net/setting-shared-formula-in-aspose-cells/
---
{{% alert color="primary" %}} 

データが入力されたワークシートがあるとします。

データの最初の行の消費税を計算する関数を B2 に追加します。税金は**9%**.売上税を計算する式は次のとおりです。**「=A2*0.09」**.この記事では、この式を Aspose.Cells に適用する方法について説明します。

{{% /alert %}} 

Aspose.Cells では、Cell.Formula プロパティを使用して数式を指定できます。

列の他のセル (B3、B4、B5 など) に数式を追加するには、2 つのオプションがあります。

最初のセルに対して行ったことを実行し、各セルの数式を効果的に設定し、それに応じてセル参照を更新します (A3*0.09、A4*0.09、A5*0.09 など)。これには、各行のセル参照を更新する必要があります。また、各数式を個別に解析するには Aspose.Cells が必要です。これは、大きなスプレッドシートや複雑な数式では時間がかかる可能性があります。また、コードの余分な行を追加しますが、ループを使用すると多少削減できます。

別のアプローチは、**共有式**.共有数式を使用すると、税金が適切に計算されるように、各行のセル参照の数式が自動的に更新されます。 Cell.SetSharedFormula メソッドは、最初のメソッドより効率的です。

次の例は、その使用方法を示しています。

**C#**

{{< highlight "csharp" >}}

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
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **実行例をダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
