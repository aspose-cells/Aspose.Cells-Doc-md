---
title: ワークブックの式の計算モードを設定する
type: docs
weight: 130
url: /ja/java/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excelでは、フォーミュラ計算モード、つまりフォーミュラの計算方法を設定できます。3つの可能な値があります。

- 自動 - 何かが変更されるたびに再計算し、ワークブックが開かれるたびに再計算します。
- データテーブル以外自動 - 何かが変更されるたびに再計算しますが、データテーブルを除外します。
- マニュアル - ユーザーがF9またはCTRL+ALT+F9を押すか、ワークブックが保存されたときにのみ再計算します。

{{% /alert %}}

Microsoft Excelでの式計算モードを設定するには:

1. **式**、次に**計算オプション**を選択します。
1つのオプションを選択します。

Aspose.Cellsでは、[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) プロパティを使用して**式計算モード**を設定できます。それには[**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType) 列挙型を代入でき、次のいずれかの値を持ちます:

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC-EXCEPT-TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

以下のサンプルコードはまずワークブックを作成し、次に式計算モードを**マニュアル**に設定し、ワークブックをディスク上の出力Excelファイルとして保存します。

**出力ファイル。式計算モードに注意してください。**

![todo:image_alt_text](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
{{< app/cells/assistant language="java" >}}
