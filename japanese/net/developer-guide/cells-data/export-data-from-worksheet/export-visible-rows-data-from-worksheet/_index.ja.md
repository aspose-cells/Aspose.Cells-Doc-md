---
title: ワークシートからの可視行データのエクスポート
type: docs
weight: 10
url: /ja/net/export-visible-rows-data-from-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells を使用して、ワークシートからデータ テーブルにデータをエクスポートできます。表示されている行のデータのみをエクスポートしたい場合があります。 Aspose.Cells は、これを実現する方法を提供します。使用[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)表示されている行データのみをエクスポートすることを指定します。

{{% /alert %}}

この例は、次のワークシートからデータをエクスポートする方法を示しています。行 5、6、および 7 は非表示になっています。

|**ワークシートのサンプル データ、行 5、6、および 7 は非表示**|
|:- |
|![todo:画像_代替_文章](export-visible-rows-data-from-worksheet_1.png)|

を使用してデータがデータ テーブルにエクスポートされると、[**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)との方法[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)オプションで、このようになります。非表示の行は空白行としてプロットされます

|**非表示の行は空白行としてデータ テーブルにエクスポートされます**|
|:- |
|![todo:画像_代替_文章](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
