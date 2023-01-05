---
title: 連結機能
type: docs
weight: 20
url: /ja/net/consolidation-function/
---
## **連結機能**

Aspose.Cells を使用して、ConsolidationFunction をピボット テーブルのデータ フィールド (または値フィールド) に適用できます。 Microsoft Excel では、値フィールドを右クリックして、**値フィールドの設定...**オプションを選択し、タブを選択します**値の集計基準**.そこから、Sum、Count、Average、Max、Min、Product、Distinct Count などの任意の ConsolidationFunction を選択できます。

Aspose.Cells提供[**連結機能**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction)次の連結関数をサポートするための列挙。

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

### **ConsolidationFunction をピボット テーブルのデータ フィールドに適用する**

次のコードが適用されます**平均**連結関数を最初のデータ フィールド (または値フィールド) に適用し、**DistinctCount** 2 番目のデータ フィールド (または値フィールド) への連結関数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

DistinctCount 連結関数は、Microsoft Excel 2013 のみでサポートされています。

{{% /alert %}}
