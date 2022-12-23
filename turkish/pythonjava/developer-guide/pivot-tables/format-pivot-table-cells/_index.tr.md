---
title: Pivot Tabloyu Biçimlendir Cells
type: docs
weight: 20
url: /tr/python-java/format-pivot-table-cells/
---
{{% alert color="primary" %}}

 Bazen pivot tablo hücrelerini biçimlendirmek istersiniz. Örneğin, pivot tablo hücrelerine bir arka plan rengi uygulamak istiyorsunuz. Aspose.Cells iki yöntem sunar[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) ve[**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)), bu amaçla kullanabilirsiniz.

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) stili pivot tablonun tamamına uygularken[**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) stili pivot tablonun tek bir hücresine uygular.

{{% /alert %}}

Aşağıdaki örnek kod, tüm pivot tabloyu açık mavi renkle biçimlendirir ve ardından ikinci tablo satırını sarı olarak biçimlendirir.

**Kodu çalıştırmadan önce giriş pivot tablosu**

![yapılacaklar:resim_alternatif_metin](format-pivot-table-cells_1.png)

**Kodu çalıştırdıktan sonra çıkış pivot tablosu**

![yapılacaklar:resim_alternatif_metin](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
