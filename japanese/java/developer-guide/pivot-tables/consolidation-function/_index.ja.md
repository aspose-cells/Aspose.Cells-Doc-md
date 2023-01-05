---
title: 連結機能
type: docs
weight: 20
url: /ja/java/consolidation-function/
description: ConsolidationFunction をピボット テーブルのデータ フィールドに適用します。
---
## **連結機能**

Aspose.Cells を使用して、ConsolidationFunction をピボット テーブルのデータ フィールド (または値フィールド) に適用できます。 Microsoft Excel では、値フィールドを右クリックして、**値フィールドの設定...**オプションを選択し、タブを選択します**値の集計基準**.そこから、Sum、Count、Average、Max、Min、Product、Distinct Count などの任意の ConsolidationFunction を選択できます。

Aspose.Cells提供[**連結機能**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction)次の連結関数をサポートするための列挙。

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

### **ConsolidationFunction をピボット テーブルのデータ フィールドに適用する**

次のコードが適用されます**平均**連結関数を最初のデータ フィールド (または値フィールド) に適用し、**STD_DEV** 2 番目のデータ フィールド (または値フィールド) への連結関数。

サンプル ソース ファイルと出力ファイルは、サンプル コードをテストするために、ここからダウンロードできます。

[ソース Excel ファイル](source.xlsx)

[出力 Excel ファイル](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

DistinctCount 連結関数は、Microsoft Excel 2013 のみでサポートされています。

{{% /alert %}}

