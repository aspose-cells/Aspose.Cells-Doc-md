---
title: ワークシートから表示される行データをエクスポート
type: docs
weight: 10
url: /ja/net/export-visible-rows-data-from-worksheet/
description: Aspose.Cells for .NET API を介してワークシートから表示される行データをエクスポートする方法を学びます。
keywords: データテーブルに表示される行データをエクスポート, 非表示行データをデータテーブルにエクスポート, 行データをデータテーブルにエクスポートして非表示行を除外, ワークシートデータをデータテーブルにエクスポートする際に非表示行を無視
---

{{% alert color="primary" %}}

Aspose.Cells を使用してワークシートからデータテーブルにデータをエクスポートできます。時々、表示される行のデータのみをエクスポートしたい場合があります。Aspose.Cells では、これを実現する方法が用意されています。[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) を使用して、表示される行のデータのみをエクスポートすることを指定します。

{{% /alert %}}

この例では、以下のワークシートからデータをエクスポートする方法を示しています。5行目、6行目、7行目が非表示になっています。

|**ワークシートのサンプルデータ、5行目、6行目、7行目が非表示です**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

表示される行データのみをエクスポートする際に、データは [**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)メソッドと [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)オプションを使用してデータテーブルにエクスポートされます。非表示の行は空行としてプロットされます

|**非表示の行はデータテーブルに空行としてエクスポートされます**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
