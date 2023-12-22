---
title: 表示されている行データをワークシートからエクスポート
type: docs
weight: 10
url: /ja/net/export-visible-rows-data-from-worksheet/
description: Aspose.Cells for .NET API を通じてワークシートから可視行データをエクスポートする方法を学習します。
keywords: Export Visible Rows Data to DataTable, Export unhidden Rows Data to DataTable, Export Rows Data to DataTable and Exclude hidden rows, Ignore Hidden Rows while Exporting Worksheet Data to Data Table
---
{{% alert color="primary" %}}

 Aspose.Cells を使用して、ワークシートからデータ テーブルにデータをエクスポートできます。表示されている行のデータのみをエクスポートしたい場合があります。 Aspose.Cells はこれを実現する方法を提供します。使用[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)表示されている行データのみをエクスポートすることを指定します。

{{% /alert %}}

この例では、次のワークシートからデータをエクスポートする方法を示します。行 5、6、7 は非表示になります。

|**ワークシートのサンプル データ、行 5、6、および 7 が非表示になっています**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

データがデータテーブルにエクスポートされると、[**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)を使用したメソッド[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)オプションを選択すると、このようになります。非表示の行は空白の行としてプロットされます

|**非表示の行は空白行としてデータテーブルにエクスポートされます**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
