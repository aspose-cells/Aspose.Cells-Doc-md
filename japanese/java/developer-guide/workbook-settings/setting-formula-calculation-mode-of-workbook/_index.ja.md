---
title: ワークブックの数式計算モードの設定
type: docs
weight: 130
url: /ja/java/setting-formula-calculation-mode-of-workbook/
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

 Aspose.Cells を設定することもできます**式計算モード**を使用して[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode)財産。あなたはそれを割り当てることができます[**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType)次のいずれかの値を持つ列挙型:

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

次のサンプル コードでは、最初にワークブックを作成し、次に数式計算モードを**マニュアル**ワークブックを出力 Excel ファイルとしてディスクに保存します。

**出力ファイル。数式計算モードに注意してください。**

![todo:画像_代替_文章](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
