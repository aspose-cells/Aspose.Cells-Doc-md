---
title: Özel Sıralama Listesi ile Sütunda Verileri Sıralama
type: docs
weight: 290
url: /tr/python-net/sort-data-in-column-with-custom-sort-list/
description: Aspose.Cells for Python via .NET API sını kullanarak özel sıralı listeyi kullanarak sütunda veri sıralamayı öğrenin.
keywords: Python Excel Kütüphanesi, Python da Özel Sıralı Listeyle Sütunda Veri Sıralaması, Python da özel listeye göre veri sıralama.
---

## **Olası Kullanım Senaryoları**

Sütunda veri sıralama işleminiz için özel bir liste kullanabilirsiniz. Bu, [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) metodu kullanılarak yapılabilir. Ancak bu metod, özel listedeki öğelerin içinde virgül bulunmuyorsa çalışır. Eğer öğeler içinde "ABD,US", "Çin,CN" gibi virgül bulunuyorsa [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) metodu kullanmalısınız. Burada, son parametre String değil, bir String Dizisi.

## **Özel Sıralama Listesi ile Sütunda Verileri Sıralama**

Aşağıdaki örnek kod, özel sıralı listeyi kullanarak verileri sıralamanızı öğretir. Bu kodun kullanıldığı [örnek Excel dosyasını](50528327.xlsx) ve bu kod tarafından oluşturulan [çıktı Excel dosyasını](50528328.xlsx) incelemek için lütfen bakın. Aşağıda yer alan ekran görüntüsü, kodun örnek Excel dosyası üzerinde uygulanmasının etkisini göstermektedir.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithCustomSortList.py" >}}
