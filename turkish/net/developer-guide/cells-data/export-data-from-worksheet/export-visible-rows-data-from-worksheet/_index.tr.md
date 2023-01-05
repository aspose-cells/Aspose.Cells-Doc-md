---
title: Görünür Satır Verilerini Çalışma Sayfasından Dışa Aktarma
type: docs
weight: 10
url: /tr/net/export-visible-rows-data-from-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells'i kullanarak çalışma sayfalarındaki verileri veri tablolarına aktarabilirsiniz. Bazen yalnızca görünür satırların verilerini dışa aktarmak istersiniz. Aspose.Cells, bunu başarmanın bir yolunu sunar. Kullan[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) yalnızca görünür satır verilerini dışa aktarmak istediğinizi belirtmek için.

{{% /alert %}}

Bu örnek, aşağıdaki çalışma sayfasından verilerin nasıl dışa aktarılacağını gösterir. 5, 6 ve 7. satırlar gizlenir.

|**Çalışma sayfasındaki örnek veriler, 5, 6 ve 7. satırlar gizlenir**|
|:- |
|![yapılacaklar:resim_alternatif_metin](export-visible-rows-data-from-worksheet_1.png)|

Veriler kullanılarak bir veri tablosuna aktarıldıktan sonra[**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) ile yöntem[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)seçeneği, bu gibi görünecektir. Gizli satırlar boş satırlar olarak çizilir

|**Gizli satırlar veri tablosuna boş satırlar olarak aktarılır**|
|:- |
|![yapılacaklar:resim_alternatif_metin](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
