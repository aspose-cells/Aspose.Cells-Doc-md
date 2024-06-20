---
title: Pivot Tablosunda Alanları Gruplandırın
type: docs
weight: 90
url: /tr/java/group-pivot-fields-in-the-pivot-table/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, pivot tablosunun alanlarını gruplamanıza olanak tanır. Bir pivot alanıyla ilgili büyük miktarda veri olduğunda, bunları bölümlere gruplamak sık ​​sık faydalıdır. Aspose.Cells, bunu [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) yöntemini kullanarak sağlar.

## **Pivot Tablosunda Alanları Gruplandırın**

Aşağıdaki örnek kod, [örnek Excel dosyasını](64716838.xlsx) yükler ve [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) yöntemini kullanarak ilk pivot alanında gruplama yapar. Daha sonra pivot tablonun verilerini yeniler ve hesaplar ve çalışma kitabını [çıktı Excel dosyası](64716837.xlsx) olarak kaydeder. Ekran görüntüsü, örnek Excel dosyası üzerinde örnek kodun etkisini gösterir. Ekran görüntüsünde, ilk pivot alanının artık aylara ve çeyizlere göre gruplandığını görebilirsiniz.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
