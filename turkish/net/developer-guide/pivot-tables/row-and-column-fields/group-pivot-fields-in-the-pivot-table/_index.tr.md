---
title: Pivot Tablosunda Alanları Gruplandırın
type: docs
weight: 80
url: /tr/net/group-pivot-fields-in-the-pivot-table/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, pivot tablosunun pivot alanlarını gruplamanıza olanak tanır. Bir pivot alanına ilişkin büyük miktarda veri olduğunda, bunları bölümlere ayırmak genellikle faydalıdır. Aspose.Cells, [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/) yöntemini kullanarak bu özelliği sağlar.

## **Pivot Tablosunda Alanları Gruplandırın**

Aşağıdaki örnek kod, [örnek Excel dosyasını](64716818.xlsx) yükler ve ilk pivot alanında [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/) yöntemini kullanarak gruplama yapar. Ardından pivot tablosunun verilerini yeniler ve hesaplar ve çalışma kitabını [çıktı Excel dosyası olarak](64716817.xlsx) kaydeder. Ekran görüntüsü, örnek kodun örneğin Excel dosyası üzerindeki etkisini göstermektedir. Ekran görüntüsünde gördüğünüz gibi, ilk pivot alanı artık aylara ve çeyreklere göre gruplandırılmış durumda.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}
