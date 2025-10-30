---
title: Veri Sıralaması Yaparken Özel Sıralama Uyarısını Belirtme
type: docs
weight: 140
url: /tr/nodejs-cpp/specifying-sort-warning-while-sorting-data/
description: Verileri sıralarken sıralama uyarısını nasıl belirleyeceğinizi Aspose.Cells for Node.js via C++ API’sini kullanarak öğrenin.
keywords: Veri sıralama işlemi yaparken sıralama uyarısı eklemek, veri sıralama sırasında sıralama uyarısı ayarlamak, veri sıralama sırasında sıralama uyarısı seçmek.
---

## **Olası Kullanım Senaryoları**

Lütfen bu metinsel veriyi göz önünde bulundurun: {11, 111, 22}. Bu veriler metin olarak sıralanırsa, 111 22'den önce gelir. Ancak, bu veriyi sayısal olarak sıralamak istiyorsanız, sonuç {11, 22, 111} olur, çünkü sayısal olarak 111 22'den sonra gelir. Aspose.Cells for Node.js via C++, bu durumu {0} özelliği ile çözüm sağlar. Bu özelliği **true** olarak ayarlayın ve metinsel veriniz sayısal olarak sıralanacaktır. Aşağıdaki ekran görüntüsü, sayısal gibi görünen metinsel veriler sıralandığında Microsoft Excel tarafından gösterilen uyarıyı gösterir.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Örnek Kod**

Aşağıdaki örnek kod, daha önce açıklandığı gibi [**DataSorter.setSortAsNumber**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortAsNumber-boolean-) özelliğinin kullanımını açıklar. Daha fazla yardım için lütfen [örnek Excel dosyasını](43352075.xlsx) ve [çıktı Excel dosyasını](43352076.xlsx) kontrol edin.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SpecifyingSortWarningWhileSortingData.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
