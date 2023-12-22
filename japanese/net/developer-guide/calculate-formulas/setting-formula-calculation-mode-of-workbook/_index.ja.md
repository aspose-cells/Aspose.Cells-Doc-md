---
title: ワークブックの数式計算モードの設定
description: この記事では、Aspose.Cells ライブラリを使用して Microsoft Excel でブックの数式計算モードを設定する方法を紹介します。既存の Excel ファイルをロードするか、新しい Excel ファイルを作成することで、Aspose.Cells が提供するメソッドを使用して数式計算モードを設定し、結果を取得できます。最後に、変更した Excel ファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, workbook, formula calculation mode, settings
type: docs
weight: 110
url: /ja/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel では、数式の計算モード、つまり数式の計算方法を設定できます。可能な値は次の 3 つです。

- 自動 - 何かが変更されるたび、およびワークブックが開かれるたびに再計算します。
- データ テーブルを除いて自動 - 何かが変更されるたびに再計算されますが、データ テーブルは除外されます。
- 手動 - ユーザーが F9 キーまたは CTRL+ALT+F9 キーを押して明示的に要求した場合、またはワークブックが保存された場合にのみ再計算します。

{{% /alert %}}

Microsoft Excel で数式計算モードを設定するには:

1. 選択する**数式**次に、*計算オプション** を選択します。
1. いずれかのオプションを選択します。

 Aspose.Cells を使用すると、**数式計算モード**を使用して[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode)モードプロパティ。それに割り当てることができます[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)次のいずれかの値を持つ列挙:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
