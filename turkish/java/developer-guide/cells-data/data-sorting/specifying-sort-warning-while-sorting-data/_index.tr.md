---
title: Veri Sıralaması Yaparken Özel Sıralama Uyarısını Belirtme
type: docs
weight: 100
url: /tr/java/specifying-sort-warning-while-sorting-data/
---

## **Olası Kullanım Senaryoları**
Lütfen bu metinsel verileri düşünün yani {11, 111, 22}. Bu metinsel veriler, 111'in 22'den önce geldiği için bu şekilde sıralanır. Ancak, bu verileri metin olarak değil de sayılar olarak sıralamak istiyorsanız, o zaman {11, 22, 111} olur çünkü sayısal olarak 111, 22'den sonra gelir. Aspose.Cells, bu sorunla başa çıkmak için [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) özelliğini sağlar. Lütfen bu özelliği **true** olarak ayarlayın ve metinsel verileriniz sayısal veriler olarak sıralanacaktır. Aşağıdaki ekran görüntüsü, metinsel veri gibi gözüken, aslında sayısal veri olan verilerin sıralandığında Microsoft Excel tarafından gösterilen sıralama uyarısını gösterir.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)
## **Örnek Kod**
Aşağıdaki örnek kod, önceden açıklandığı gibi [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) özelliğinin kullanımını açıklar. Daha fazla yardım için [örnek Excel dosyasını](43352077.xlsx) ve [çıktı Excel dosyasını](43352078.xlsx) kontrol edebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
