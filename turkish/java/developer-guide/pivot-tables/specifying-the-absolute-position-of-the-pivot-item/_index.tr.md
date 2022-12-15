---
title: Pivot Öğesinin mutlak konumunu belirtme
type: docs
weight: 40
url: /tr/java/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

Bazen kullanıcının pivot öğelerinin mutlak konumunu belirtmesi gerekir, Aspose.Cells API birkaç yeni özellik ve bu kullanıcı ihtiyacını karşılamak için bir yöntem ortaya koymuştur.

-  Katma[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) üst düğümden bağımsız olarak tüm PivotItem'lerdeki konum dizinini belirtmek için kullanılabilen özellik. Katma[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) aynı üst düğüm altındaki PivotItems içindeki konum dizinini belirtmek için kullanılabilen özellik.
-  Katma[**PivotItem.move(int sayısı, boole isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)yöntemi, sayım değerine bağlı olarak öğeyi yukarı veya aşağı taşımak için kullanılır; burada sayı, Özet Öğeyi yukarı veya aşağı hareket ettirmek için konumların sayısıdır. Sayım değeri sıfırdan küçükse, öğe yukarı taşınırken, sayım değeri sıfırdan büyükse, PivotItem aşağı hareket eder, taşıma işleminin aynı üst düğümde mi yoksa aynı üst düğümde mi gerçekleştirileceğini belirten Boolean isSameParent parametresi olumsuzluk.
-  Eskimiş*PivotItem.move(int sayısı)* yöntemi, bu nedenle, yeni eklenen yöntemin kullanılması önerilir.[**PivotItem.move(int sayısı, boole isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) yerine.

 Lütfen dikkat, aramanız gerekir.[**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) ve[**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData() ) yöntemleri kullanmadan önce[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) özellikler ve[**PivotItem.move(int sayısı, boole isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) yöntem.

{{% /alert %}}

## Basit kod

Aşağıdaki örnek kod, bir Pivot Tablo oluşturur ve ardından aynı üst düğümdeki Pivot Öğeleri konumlarını belirtir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
