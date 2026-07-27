---
title: Pivot Tablosundaki Veri Alanı nın Veri Görüntüleme Biçimleriyle Çalışma
type: docs
weight: 140
url: /tr/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Python via .NET için Aspose.Cells ile Pivot Tablosundaki DataField ın veri görüntüleme biçimleriyle çalışma
keywords: Python Excel için Aspose.Cells, Excel Python kütüphanesi, Pivot Tablosundaki DataField ın veri görüntüleme biçimleriyle çalışma.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, DataField'ın tüm veri görüntüleme biçimlerini destekler.

{{% /alert %}}

## **"En Küçükten En Büyüğe Sırala" ve "En Büyükten En Küçüğe Sırala" görüntüleme biçimi seçeneğini nasıl ayarlayacağınız**

Aspose.Cells for Python via .NET, pivot alanları için görüntüleme biçimi seçeneğini ayarlama olanağı sağlar. Bunun için API, [**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/) özelliğini sağlar. En büyükten en küçüğe sıralamak için, [**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/) özelliğini [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfielddatadisplayformat/) olarak ayarlayabilirsiniz. Aşağıdaki kod örneği, görüntüleme biçimi seçeneklerinin nasıl ayarlanacağını göstermektedir.

Örnek kaynak ve çıktı dosyalarını buradan indirebilir ve örnek kodu test etmek için kullanabilirsiniz:

[Kaynak Excel Dosyası](101089332.xlsx)

[Çıktı Excel Dosyası](101089333.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTableDataDisplayFormatRanking-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
