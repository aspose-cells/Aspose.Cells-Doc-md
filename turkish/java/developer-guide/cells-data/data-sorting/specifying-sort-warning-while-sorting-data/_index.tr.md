---
title: Verileri Sıralarken Sıralama Uyarısı Belirtme
type: docs
weight: 100
url: /tr/java/specifying-sort-warning-while-sorting-data/
---
## **Olası Kullanım Senaryoları**
 Lütfen bu metinsel verileri göz önünde bulundurun, yani {11, 111, 22}. Bu metinsel veri bu şekilde sıralanmıştır çünkü metin olarak 111 22'den önce gelir. Ama bu veriyi yazı olarak değil sayı olarak sıralamak isterseniz o zaman {11, 22, 111} olur çünkü sayısal olarak 111 sonra gelir. 22. Aspose.Cells sağlar[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) Bu sorunla başa çıkmak için mülk. Lütfen bu özelliği ayarlayın**doğru**ve metin verileriniz sayısal veriler olarak sıralanacaktır. Aşağıdaki ekran görüntüsü, sayısal veri gibi görünen metinsel veriler sıralandığında Microsoft Excel tarafından gösterilen sıralama uyarısını göstermektedir.

![yapılacaklar:resim_alternatif_metin](specifying-sort-warning-while-sorting-data_1.png)
## **Basit kod**
 Aşağıdaki örnek kod, kullanımını göstermektedir[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber)özellik daha önce açıklandığı gibi. Lütfen kontrol edin[örnek excel dosyası](43352077.xlsx) ve[çıktı excel dosyası](43352078.xlsx) daha fazla yardım için

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
