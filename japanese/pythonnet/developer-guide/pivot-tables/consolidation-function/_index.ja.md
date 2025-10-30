---
title: 統合機能
type: docs
weight: 20
url: /ja/python-net/consolidation-function/
description: Aspose.Cells for Python via .NETを使用してピボットテーブルのデータフィールドに集計関数を適用する方法
keywords: Aspose.Cells for Python Excelライブラリを使用して、ピボットテーブルのデータフィールドに集計関数を適用する
---

## **統合機能**

Aspose.Cells for Python via .NETを使用してデータフィールド（または値フィールド）に集計関数を適用できます。Microsoft Excelでは、値フィールドを右クリックし、**値フィールドの設定...**オプションを選択してから**集計値のサマリズでBy**タブを選択します。そこから、Sum、Count、Average、Max、Min、Product、Distinct Countなどの任意の集計関数を選択できます。

Aspose.Cells for Python via .NETは、以下の集計関数をサポートするための[**ConsolidationFunction**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/)列挙型を提供します。

- ConsolidationFunction.AVERAGE
- ConsolidationFunction.COUNT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.DISTINCT_COUNT
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.SUM
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP

## **Aspose.Cells for Python Excelライブラリを使用してピボットテーブルのデータフィールドに集計関数を適用する方法**

以下のコードは、最初のデータフィールドに**AVERAGE**集計関数を適用し、2番目のデータフィールドに**DISTINCT_COUNT**集計関数を適用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

**DISTINCT_COUNT**集計関数は、Microsoft Excel 2013でのみサポートされています。

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
