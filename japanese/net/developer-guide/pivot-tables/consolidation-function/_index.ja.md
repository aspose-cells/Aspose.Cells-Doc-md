---
title: 統合機能
type: docs
weight: 20
url: /ja/net/consolidation-function/
---

## **統合機能**

Aspose.Cellsを使用して、ピボットテーブルのデータフィールド（または値フィールド）に統合機能を適用できます。Microsoft Excelにおいては、値フィールドを右クリックし、 **「値フィールドの設定...」** を選択し、その後 **「値の集計方法」** タブを選択します。そこから、合計、カウント、平均、最大値、最小値、積、重複排除のような任意の統合機能を選択できます。

Aspose.Cellsは、次の統合機能をサポートするための[**ConsolidationFunction**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction)列挙型を提供します。

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

### **ピボットテーブルのデータフィールドに統合機能を適用する**

次のコードは、最初のデータフィールド（または値フィールド）に **平均** の統合機能を適用し、2番目のデータフィールド（または値フィールド）に **重複排除** の統合機能を適用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

重複排除の統合機能は、Microsoft Excel 2013でのみサポートされています。

{{% /alert %}}
