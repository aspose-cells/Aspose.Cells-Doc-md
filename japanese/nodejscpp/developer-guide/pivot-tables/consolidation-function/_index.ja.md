---
title: 統合機能
type: docs
weight: 20
url: /ja/nodejs-cpp/consolidation-function/
description: Aspose.Cells for Node.js via C++を使用してピボットテーブルのデータフィールドに集約関数を適用する方法。
keywords: Aspose.Cells for Node.js via C++ Excel、Excel Node.jsライブラリを使用して、ピボットテーブルのデータフィールドに集約関数を適用する方法。
---

## **統合機能**

Aspose.Cells for Node.js via C++は、ピボットテーブルのデータ（または値）フィールドに集約関数を適用するために使用できます。Microsoft Excelでは、値フィールドを右クリックし、「値フィールドの設定...」を選択し、「値の集計方法」タブから選択します。そこから、Sum、Count、Average、Max、Min、Product、Distinct Countなどの集約関数を選択できます。

Aspose.Cells for Node.js via C++は、以下の集約関数をサポートする [**ConsolidationFunction**](https://reference.aspose.com/cells/nodejs-cpp/consolidationfunction/) 列挙を提供します。

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **Aspose.Cells for Node.js via C++を使用してピボットテーブルのデータフィールドに集約関数を適用する方法。**

次のコードは、最初のデータフィールド（または値フィールド）に **平均** の統合機能を適用し、2番目のデータフィールド（または値フィールド）に **重複排除** の統合機能を適用します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ConsolidationFunctions-1.js" >}}

{{% alert color="primary" %}}

**DISTINCT_COUNT**集計関数は、Microsoft Excel 2013でのみサポートされています。

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
