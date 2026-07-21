---
title: Pivot Öğesi nin mutlak konumunu belirtme
type: docs
weight: 40
url: /tr/java/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Kullanıcı bazen pivot öğelerin mutlak konumunu belirlemek isteyebilir, Aspose.Cells API bu kullanıcı gereksinimini karşılamak için birkaç yeni özellik ve bir yöntem sunar.

- Tüm ebeveyn düğümün bağımsızında PivotItems içindeki pozisyon indeksini belirlemek için kullanılabilecek [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) özelliği eklendi. - Aynı ebeveyn düğümdeki PivotItems içindeki pozisyon indeksini belirlemek için kullanılabilecek [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) özelliği eklendi.
- PivotItem'ı yukarı veya aşağı hareket ettirmek için [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) yöntemi eklenmiştir, burada sayım, PivotItem'ın yukarı veya aşağı hareket edilecek pozisyon sayısıdır. Eğer sayım değeri sıfırdan küçükse, öğe yukarı taşınacak, eğer sayım değeri sıfırdan büyükse, PivotItem aşağı taşınacak, Boolean tipi isSameParent parametresi taşıma işleminin aynı üst düğümde gerçekleştirilmesi gerekip gerekmediğini belirtir.
- *PivotItem.move(int sayım)* yöntemi kullanılmayacak, bu nedenle yeni eklenen yöntemin [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) kullanılması önerilir.

Lütfen, [**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) ve [**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) yöntemlerini kullanmadan önce [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) özelliklerini ve [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) yöntemini kullanmak gereklidir.

{{% /alert %}}

## Örnek Kod

Aşağıdaki örnek kod bir pivot tablo oluşturur ve daha sonra aynı üst düğümdeki Pivot Öğelerinin pozisyonlarını belirtir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
{{< app/cells/assistant language="java" >}}
