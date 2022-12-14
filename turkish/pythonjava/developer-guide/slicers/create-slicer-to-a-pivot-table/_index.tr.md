---
title: Pivot Tablo için Dilimleyici Oluşturma
type: docs
weight: 10
url: /tr/python-java/create-slicer-to-a-pivot-table/
---
## **Olası Kullanım Senaryoları**
Dilimleyiciler, verileri hızlı bir şekilde filtrelemek için kullanılır. Hem tablodaki hem de pivot tablodaki verileri filtrelemek için kullanılabilirler. Microsoft Excel, bir tablo veya pivot tablo seçip ardından*Ekle > Dilimleyici*Java aracılığıyla Python için Aspose.Cells, dilimleyici oluşturmak için Worksheet.getSlicers().add() yöntemini sağlar.
## **Pivot Tablo için Dilimleyici Oluşturma**
Aşağıdaki kod parçacığı,[örnek excel dosyası](106364966.xlsx)pivot tabloyu içerir. Ardından, ilk temel pivot alanını temel alarak dilimleyiciyi oluşturur. Son olarak, çalışma kitabını şuraya kaydeder:[çıktı XLSX](106364967.xlsx)biçim. Aşağıdaki ekran görüntüsü, çıktı Excel dosyasında Aspose.Cells tarafından oluşturulan dilimleyiciyi göstermektedir.

![yapılacaklar:resim_alternatif_Metin](create-slicer-to-a-pivot-table_1.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
