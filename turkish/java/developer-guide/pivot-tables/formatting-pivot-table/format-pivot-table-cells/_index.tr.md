---
title: Döşeme Özeti Hücreleri Biçimlendir
type: docs
weight: 20
url: /tr/java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

Bazı durumlarda, pivot tablo hücrelerini biçimlendirmek isteyebilirsiniz. Örneğin, pivot tablo hücrelerine arka plan rengi uygulamak isteyebilirsiniz. Aspose.Cells, bu amaçla kullanabileceğiniz iki yöntem [**PivotTable.formatAll()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll(com.aspose.cells.Style)) ve [**PivotTable.format()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#format(int,%20int,%20com.aspose.cells.Style)) sağlar.

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll(com.aspose.cells.Style)), tüm pivot tablosuna stili uygularken, [**PivotTable.format()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#format(int,%20int,%20com.aspose.cells.Style)) pivot tablosunun tek bir hücresine stili uygular.

{{% /alert %}}

Aşağıdaki örnek kod, tüm pivot tablosunu açık mavi renkle biçimlendirir ve ardından ikinci tablo satırını sarıyla biçimlendirir.

**Kodun uygulanmasından önceki girdi pivot tablosu**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**Kodun uygulanmasından sonraki çıktı pivot tablosu**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FormatPivotTableCells-FormatPivotTableCells.java" >}}
