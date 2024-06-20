---
title: Döşeme Özeti Hücreleri Biçimlendir
type: docs
weight: 20
url: /tr/python-java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

Bazı durumlarda, pivot tablo hücrelerini biçimlendirmek isteyebilirsiniz. Örneğin, pivot tablo hücrelerine arka plan rengi uygulamak isteyebilirsiniz. Aspose.Cells, bu amaçla kullanabileceğiniz iki yöntem [**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) ve [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) sağlar.

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)), tüm pivot tablosuna stili uygularken, [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) pivot tablosunun tek bir hücresine stili uygular.

{{% /alert %}}

Aşağıdaki örnek kod, tüm pivot tablosunu açık mavi renkle biçimlendirir ve ardından ikinci tablo satırını sarıyla biçimlendirir.

**Kodun uygulanmasından önceki girdi pivot tablosu**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**Kodun uygulanmasından sonraki çıktı pivot tablosu**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
