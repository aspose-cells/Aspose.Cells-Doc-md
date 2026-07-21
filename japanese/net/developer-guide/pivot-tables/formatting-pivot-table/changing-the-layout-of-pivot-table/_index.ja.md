---
title: ピボットテーブルのレイアウトを変更する
type: docs
weight: 10
url: /ja/net/changing-the-layout-of-pivot-table/
---

{{% alert color="primary" %}}

Microsoft Excelでは、*PivotTable Tools > Design > Report Layout*メニューコマンドを使用してピボットテーブルのレイアウトを変更できます。これらの3つの形式でレイアウトを変更できます

- コンパクト形式で表示
- アウトライン形式で表示
- 表形式で表示

Aspose.Cellsは、これらの3つの形式でピボットテーブルのレイアウトを変更する[**PivotTable.ShowInCompactForm()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/showincompactform)、[**PivotTable.ShowInOutlineForm()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/showinoutlineform)、および[**PivotTable.ShowInTabularForm()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/showintabularform)のメソッドも提供しています。

{{% /alert %}}

次のサンプルコードでは、まずPivot Tableを**コンパクト形式**で表示し、次に**アウトライン形式**でPivot Tableを表示し、最後にPivot Tableを**表形式**で表示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-ChangingLayoutOfPivotTable-ChangingLayoutOfPivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}
