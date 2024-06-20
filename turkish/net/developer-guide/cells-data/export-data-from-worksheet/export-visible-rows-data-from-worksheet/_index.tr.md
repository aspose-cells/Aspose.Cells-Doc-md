---
title: Çalışma Sayfasından Görünür Satırların Verilerini Aktar
type: docs
weight: 10
url: /tr/net/export-visible-rows-data-from-worksheet/
description: Aspose.Cells for .NET API si aracılığıyla Çalışma Sayfasından Görünür Satırların Verilerini Nasıl Aktarılacağını Öğrenin
keywords: Görünen Satırların Verilerini DataTable a Aktar, Gizlenmemiş Satırların Verilerini DataTable a Aktar, Satırların Verilerini DataTable a Aktar ve Gizli satırları hariç tut, Çalışma Sayfasından Veri Tablosuna Veri Aktarırken Gizli Satırları Yoksay
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak çalışma sayfasından verileri veri tablolarına aktarabilirsiniz. Bazı durumlarda yalnızca görünür satırların verilerini aktarmak isteyebilirsiniz. Aspose.Cells, bunu gerçekleştirmenin bir yolunu sağlar. Yalnızca görünür satırlar verilerini aktarmak istediğinizi belirtmek için [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) kullanın

{{% /alert %}}

Bu örnek, aşağıdaki çalışma sayfasından verileri nasıl aktaracağını göstermektedir. 5, 6 ve 7. satırlar gizlidir.

|**Çalışma sayfasındaki örnek veri, 5, 6 ve 7. satırlar gizlidir**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

Veri [**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) yöntemi ve [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) seçeneği ile veri tablosuna aktarıldığında, aşağıdaki gibi olacaktır. Gizli satırlar boş satırlar olarak çizilmiştir

|**Gizli satırlar veri tablosuna boş satırlar olarak aktarılır**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
