---
title: Pivot Tablosundaki Veri Alanı nın Veri Görüntüleme Biçimleriyle Çalışma
type: docs
weight: 150
url: /tr/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells, DataField'ın tüm veri görüntüleme formatlarını destekler.

{{% /alert %}}

## **"En Küçükten En Büyüğe Sırala" ve "En Büyükten En Küçüğe Sırala" görüntüleme formatı seçeneği**

Aspose.Cells, haraket alanları için görüntüleme formatı seçeneğini ayarlama olanağı sağlar. Bunun için API, [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) özelliğini sağlar. En büyükten en küçüğe sıralamak için, [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) özelliğini [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK_LARGEST_TO_SMALLEST) olarak ayarlayabilirsiniz. Aşağıdaki kod parçası, görüntüleme formatı seçeneklerinin ayarlanmasını göstermektedir.

Örnek kaynak ve çıktı dosyalarını buradan indirebilir ve örnek kodu test etmek için kullanabilirsiniz:

[Kaynak Excel Dosyası](PivotTableSample.xlsx)

[Çıktı Excel Dosyası](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
