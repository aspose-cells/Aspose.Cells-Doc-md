---
title: 統合機能
type: docs
weight: 20
url: /ja/java/consolidation-function/
description: ピボットテーブルのデータフィールドに ConsolidationFunction を適用します。
---

## **統合機能**

Aspose.Cellsを使用して、ピボットテーブルのデータフィールド（または値フィールド）に統合機能を適用できます。Microsoft Excelにおいては、値フィールドを右クリックし、 **「値フィールドの設定...」** を選択し、その後 **「値の集計方法」** タブを選択します。そこから、合計、カウント、平均、最大値、最小値、積、重複排除のような任意の統合機能を選択できます。

Aspose.Cellsは、次の統合機能をサポートするための[**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction)列挙型を提供します。

- ConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP
- ConsolidationFunction.DISTINCT_COUNT

### **ピボットテーブルのデータフィールドに統合機能を適用する**

次のコードは、最初のデータフィールド（または値フィールド）に **AVERAGE** の集約関数を適用し、2 番目のデータフィールド（または値フィールド）に **STD_DEV** の集約関数を適用します。

サンプルソースファイルと出力ファイルは、テスト用のサンプルコードをダウンロードできます:

[元のExcelファイル](source.xlsx)

[出力のExcelファイル](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

重複排除の統合機能は、Microsoft Excel 2013でのみサポートされています。

{{% /alert %}}

