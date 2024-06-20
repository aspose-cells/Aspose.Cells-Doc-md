---
title: Pivot Tablosuna Dilimleyici Oluştur
type: docs
weight: 10
url: /tr/java/create-slicer-to-a-pivot-table/
---

## **Olası Kullanım Senaryoları**
Dilimleyici verileri hızlıca filtrelemek için kullanılır. Tablo veya pivot tabloda verileri filtrelemek için kullanılabilir. Microsoft Excel, bir tablo veya pivot tabloyu seçip *Ekle > Dilimleyici* yi tıklarak dilimleyici oluşturmanıza olanak tanır. Aspose.Cells de aynı şekilde [Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)) yöntemini kullanarak dilimleyici oluşturmanıza olanak tanır.
## **Pivot Tablosuna Dilimleyici Oluştur**
Lütfen aşağıdaki örnek kodu görün. Pivot tabloyu içeren [örnek Excel dosyasını](67338498.xlsx) yükler. Ardından ilk temel pivot alanına dayalı dilimleyiciyi oluşturur ve son olarak çalışma kitabını [çıktı XLSX](67338497.xlsx) ve [çıktı XLSB](67338496.xlsb) formatlarında kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından oluşturulan dilimleyiciyi göstermektedir.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
