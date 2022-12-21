---
title: ワークブックの数式計算モードの設定
type: docs
weight: 110
url: /ja/net/setting-formula-calculation-mode-of-workbook/
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

 Aspose.Cells を設定することもできます**式計算モード**使用して[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode)モード プロパティ。あなたはそれを割り当てることができます[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)次のいずれかの値を持つ列挙型:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
