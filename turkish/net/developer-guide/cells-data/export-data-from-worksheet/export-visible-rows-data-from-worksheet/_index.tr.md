---
title: Görünür Satır Verilerini Çalışma Sayfasından Dışa Aktarma
type: docs
weight: 10
url: /tr/net/export-visible-rows-data-from-worksheet/
description: Aspose.Cells for .NET API numaralı telefondan Görünür Satır Verilerini Çalışma Sayfasından Nasıl Dışa Aktaracağınızı öğrenin.
keywords: Export Visible Rows Data to DataTable, Export unhidden Rows Data to DataTable, Export Rows Data to DataTable and Exclude hidden rows, Ignore Hidden Rows while Exporting Worksheet Data to Data Table
---
{{% alert color="primary" %}}

 Aspose.Cells'i kullanarak çalışma sayfalarındaki verileri veri tablolarına aktarabilirsiniz. Bazen yalnızca görünür satırların verilerini dışa aktarmak isteyebilirsiniz. Aspose.Cells bunu başarmanın bir yolunu sunuyor. Kullan[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)yalnızca görünür satır verilerini dışa aktarmak istediğinizi belirtmek için.

{{% /alert %}}

Bu örnek, aşağıdaki çalışma sayfasındaki verilerin nasıl dışarı aktarılacağını gösterir. 5, 6 ve 7. satırlar gizlidir.

|**Çalışma sayfasındaki örnek veriler, 5, 6 ve 7. satırlar gizlendi**|
| :- |
|![yapılacak şey:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

 Veriler kullanılarak bir veri tablosuna aktarıldıktan sonra[**Çalışma Sayfası.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) yöntemi ile[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)seçeneği şu şekilde görünecektir. Gizli satırlar boş satırlar olarak çizilir

|**Gizli satırlar veri tablosuna boş satırlar olarak aktarılır**|
| :- |
|![yapılacak şey:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
