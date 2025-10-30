---
title: Golang ve C++ kullanarak Veri Sıralarken Sıralama Uyarısı Belirtme
linktitle: Veri Sıralaması Yaparken Özel Sıralama Uyarısını Belirtme
type: docs
weight: 140
url: /tr/go-cpp/specifying-sort-warning-while-sorting-data/
description: Aspose.Cells for C++ API’sini kullanarak veriyi sıralarken sıralama uyarısını nasıl belirteceğinizi öğrenin.
keywords: Veri sıralama işlemi yaparken sıralama uyarısı eklemek, veri sıralama sırasında sıralama uyarısı ayarlamak, veri sıralama sırasında sıralama uyarısı seçmek.
---

## **Olası Kullanım Senaryoları**

Lütfen {11, 111, 22} gibi bu metinsel verileri düşünün. Bu metinsel veri, metin olarak sıralandığından 111 22'den önce gelir. Ancak, bu veriyi metin değil, sayı olarak sıralamak istiyorsanız, o zaman bu veri {11, 22, 111} olacak çünkü sayısal olarak 111 22'den sonra gelir. Aspose.Cells, bu sorunu çözmek için {0} özelliğini sağlar. Lütfen bu özelliği **true** olarak ayarlayın ve metinsel verileriniz sayısal veri olarak sıralanacaktır. Aşağıdaki ekran görüntüsü, metinsel veri gibi görünen metinsel verilerin sıralandığında Microsoft Excel tarafından gösterilen sıralama uyarısını göstermektedir.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Örnek Kod**

Aşağıdaki örnek kod, daha önce açıklandığı gibi [**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/go-cpp/datasorter/getsortasnumber/) özelliğinin kullanımını açıklar. Daha fazla yardım için lütfen [örnek Excel dosyasını](43352075.xlsx) ve [çıktı Excel dosyasını](43352076.xlsx) kontrol edin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSortWarningWhileSortingData.go" >}}
