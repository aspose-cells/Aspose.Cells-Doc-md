---
title: Pivot Tablo için Dilimleyici Oluşturma
type: docs
weight: 10
url: /tr/java/create-slicer-to-a-pivot-table/
---
## **Olası Kullanım Senaryoları**
Dilimleyici, verileri hızlı bir şekilde filtrelemek için kullanılır. Hem tablodaki hem de pivot tablodaki verileri filtrelemek için kullanılabilir. Microsoft Excel, bir tablo veya pivot tablo seçip ardından*Ekle > Dilimleyici*. Aspose.Cells ayrıca, kullanarak dilimleyici oluşturmanıza olanak tanır.[Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)) yöntem.
## **Pivot Tablo için Dilimleyici Oluşturma**
Lütfen aşağıdaki örnek koda bakın. o yükler[örnek excel dosyası](67338498.xlsx)pivot tabloyu içerir. Ardından, ilk temel pivot alanını temel alarak dilimleyiciyi oluşturur. Son olarak, çalışma kitabını şuraya kaydeder:[çıktı XLSX](67338497.xlsx)ve[çıkış XLSB](67338496.xlsb)biçim. Aşağıdaki ekran görüntüsü, çıktı Excel dosyasında Aspose.Cells tarafından oluşturulan dilimleyiciyi göstermektedir.

![yapılacaklar:resim_alternatif_Metin](create-slicer-to-a-pivot-table_1.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
