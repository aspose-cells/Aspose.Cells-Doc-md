---
title: Pivot Tablodaki Pivot Alanlarını Gruplandırma
type: docs
weight: 90
url: /tr/java/group-pivot-fields-in-the-pivot-table/
---
## **Olası Kullanım Senaryoları**

Microsoft Excel, pivot tablonun pivot alanlarını gruplandırmanıza olanak tanır. Bir pivot alanıyla ilgili çok miktarda veri olduğunda, bunları bölümler halinde gruplandırmak genellikle yararlıdır. Aspose.Cells ayrıca bu özelliği kullanarak[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) yöntem.

## **Pivot Tablodaki Pivot Alanlarını Gruplandırma**

Aşağıdaki örnek kod,[örnek excel dosyası](64716838.xlsx)kullanarak ilk pivot alanında gruplandırma gerçekleştirir.[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) yöntem. Daha sonra pivot tablonun verilerini yeniler ve hesaplar ve çalışma kitabını[çıktı excel dosyası](64716837.xlsx). Ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini gösterir. Ekran görüntüsünde görebileceğiniz gibi, ilk pivot alanı artık aylara ve çeyreklere göre gruplandırılmıştır.

![yapılacaklar:resim_alternatif_Metin](group-pivot-fields-in-the-pivot-table_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
