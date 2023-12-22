---
title: Verileri Sıralarken Sıralama Uyarısını Belirtme
type: docs
weight: 140
url: /tr/net/specifying-sort-warning-while-sorting-data/
description: Aspose.Cells for .NET API'i kullanarak verileri sıralarken sıralama uyarısını nasıl belirleyeceğinizi öğrenin.
keywords: Add sort warning when sorting data, set sort warning while sorting data, select sort warning when sorting data.
---
##  **Olası Kullanım Senaryoları**

Lütfen bu metin verilerini (ör. {11, 111, 22}) dikkate alın. Bu metinsel veriler sıralanmıştır çünkü metin açısından 111 22'den önce gelir. Ancak bu verileri metin olarak değil sayı olarak sıralamak isterseniz {11, 22, 111} olur çünkü sayısal olarak 111 22'den sonra gelir. Aspose.Cells sağlar[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)Bu sorunla başa çıkmak için mülk. Lütfen bu özelliği ayarlayın**doğru**ve metinsel verileriniz sayısal veriler olarak sıralanacaktır. Aşağıdaki ekran görüntüsünde sayısal verilere benzeyen metinsel veriler sıralandığında Microsoft Excel'in gösterdiği sıralama uyarısı görülmektedir.

![yapılacak şey:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

##  **Basit kod**

 Aşağıdaki örnek kod kullanımını göstermektedir:[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber) daha önce açıklandığı gibi mülk. Lütfen kontrol edin[örnek Excel dosyası](43352075.xlsx) Ve[Excel dosyasının çıktısı](43352076.xlsx) daha fazla yardım için.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
