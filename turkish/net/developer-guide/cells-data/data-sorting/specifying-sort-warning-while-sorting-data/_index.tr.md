---
title: Verileri Sıralarken Sıralama Uyarısı Belirtme
type: docs
weight: 140
url: /tr/net/specifying-sort-warning-while-sorting-data/
---
## **Olası Kullanım Senaryoları**

Lütfen bu metinsel verileri göz önünde bulundurun, yani {11, 111, 22}. Bu metinsel veri sıralanır çünkü metin olarak 111 22'den önce gelir. Ama bu veriyi metin olarak değil sayı olarak sıralamak isterseniz {11, 22, 111} olur çünkü sayısal olarak 111 22'den sonra gelir. Aspose.Cells sağlar[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)Bu sorunla başa çıkmak için mülk. Lütfen bu özelliği ayarlayın**doğru**ve metin verileriniz sayısal veriler olarak sıralanacaktır. Aşağıdaki ekran görüntüsü, sayısal veri gibi görünen metinsel veriler sıralandığında Microsoft Excel tarafından gösterilen sıralama uyarısını göstermektedir.

![yapılacaklar:resim_alternatif_Metin](specifying-sort-warning-while-sorting-data_1.png)

## **Basit kod**

 Aşağıdaki örnek kod, kullanımını göstermektedir[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)özellik daha önce açıklandığı gibi. Lütfen kontrol edin[örnek excel dosyası](43352075.xlsx) ve[çıktı excel dosyası](43352076.xlsx) daha fazla yardım için

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
