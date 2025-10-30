---
title: Veri Sıralaması Yaparken Özel Sıralama Uyarısını Belirtme
type: docs
weight: 140
url: /tr/python-net/specifying-sort-warning-while-sorting-data/
description: Aspose.Cells for Python via .NET API sını kullanarak veri sıralama sırasında sıralama uyarısını belirtmeyi öğrenin.
keywords: Python Excel Kütüphanesi, Python Veri sıralama sırasında sıralama uyarısı ekleme, Python veri sıralarken sıralama uyarısı ayarlama, Python veri sıralarken sıralama uyarısını seçme.
---

## **Olası Kullanım Senaryoları**

Lütfen bu metin verilerini göz önünde bulundurun; örneğin {11, 111, 22}. Bu metin verileri, metin açısından 111'in 22'den önce olmasından dolayı sıralanmıştır. Ancak eğer bu verileri metin olarak değil de sayılar olarak sıralamak istiyorsanız, o zaman {11, 22, 111} olacak çünkü sayısal olarak 111, 22'den sonra gelir. Aspose.Cells for Python via .NET, bu sorunu {0} özelliği ile çözmek için sağlar. Lütfen bu özelliği **true** olarak ayarlayın ve metin verileriniz sayısal veri olarak sıralanacaktır. Aşağıdaki ekran görüntüsü, sayısal veri gibi görünen metin verileri sıralandığında Microsoft Excel tarafından gösterilen sıralama uyarısını gösterir.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Örnek Kod**

Aşağıdaki örnek kod, daha önce açıklandığı gibi [**DataSorter.sort_as_number**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_as_number/) özelliğinin kullanımını açıklar. Daha fazla yardım için lütfen [örnek Excel dosyasını](43352075.xlsx) ve [çıktı Excel dosyasını](43352076.xlsx) kontrol edin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SpecifyingSortWarningWhileSortingData.py" >}}
{{< app/cells/assistant language="python-net" >}}
