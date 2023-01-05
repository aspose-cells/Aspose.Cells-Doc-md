---
title: Aspose.Cellsでワークブックの数式計算モードを設定する
type: docs
weight: 100
url: /ja/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel では、数式の計算モード、つまり数式の計算方法を設定できます。次の 3 つの値があります。

- 自動 - 何かが変更されるたび、およびワークブックが開かれるたびに再計算します。
- データ テーブルを除いて自動 - 何かが変更されるたびに再計算しますが、データ テーブルは除外します。
- 手動 - ユーザーが F9 キーまたは CTRL + ALT + F9 キーを押して明示的に要求した場合、またはブックが保存された場合にのみ再計算します。

{{% /alert %}} 

Microsoft Excel で数式計算モードを設定するには:

1. 選択する**数式**その後**計算オプション**.
1. いずれかのオプションを選択します。

 Aspose.Cells を設定することもできます**式計算モード**FormulaSettings.CalculationMode モード プロパティを使用します。次のいずれかの値を持つ CalcModeType 列挙を割り当てることができます。

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

次のサンプル コードでは、最初にワークブックを作成し、次に数式計算モードを**マニュアル**ワークブックを出力 Excel ファイルとしてディスクに保存します。

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **実行例をダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
