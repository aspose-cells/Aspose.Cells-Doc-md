---
title: 集約機能
type: docs
weight: 20
url: /ja/python-net/consolidation-function/
description: Aspose.Cells for Python via .NET を使用してピボット テーブルのデータ フィールドに ConsolidationFunction を適用する方法。
keywords: ConsolidationFunction to Data Fields of Pivot Table.
---
##  **集約機能**

Aspose.Cells for Python via .NET は、ピボット テーブルのデータ フィールド (または値フィールド) に ConsolidationFunction を適用するために使用できます。 Microsoft Excel では、値フィールドを右クリックして、**値フィールドの設定...**オプションを選択し、*値の集計方法** タブを選択します。そこから、Sum、Count、Average、Max、Min、Product、Distinct Count などの任意の ConsolidationFunction を選択できます。

 Aspose.Cells for Python via .NET が提供します[**統合機能**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/)次の統合関数をサポートする列挙型。

- 統合関数.AVERAGE
- 統合関数.COUNT
- 統合関数.COUNT_NUMS
- 統合関数.DISTINCT_COUNT
- 統合関数.MAX
- 統合関数.MIN
- 統合関数.PRODUCT
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.SUM
- 統合関数.VAR
- ConsolidationFunction.VARP

###  **ピボット テーブルのデータ フィールドに ConsolidationFunction を適用する**

次のコードが適用されます**AVERAGE**最初のデータ フィールド (または値フィールド) への統合関数と**DISTINCT_COUNT** 番目のデータ フィールド (または値フィールド) への統合関数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

DISTINCT_COUNT 統合関数は、Microsoft Excel 2013 でのみサポートされます。

{{% /alert %}}
