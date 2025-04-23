---
title: Özel Sıralama Listesi ile Sütunda Verileri Sıralama
type: docs
weight: 290
url: /tr/nodejs-cpp/sort-data-in-column-with-custom-sort-list/
description: Aspose.Cells for Node.js via C++ API sini kullanarak sütundaki verileri özel bir liste kullanarak nasıl sıralayacağınızı öğrenin.
keywords: Özel Sıralama Listesi ile Sütunda Veri Sıralama, Özel liste ile veri sırala.
---

## **Olası Kullanım Senaryoları**

Sütundaki verileri özel bir liste kullanarak sıralayabilirsiniz. Bu, [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-string-) yöntemi kullanılarak yapılabilir. Ancak, bu yöntem yalnızca özel listedeki öğelerde virgül yoksa çalışır. Eğer virgüller varsa, örneğin "USA,US", "China,CN" gibi, o zaman [**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) yöntemini kullanmanız gerekir. Burada, son parametre String değil, String dizisidir.

## **Özel Sıralama Listesi ile Sütunda Verileri Sıralama**

Aşağıdaki örnek kod, [**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) yönteminin nasıl kullanılacağını açıklamaktadır; özel sıralama listesi ile verilerin nasıl sıralanacağı gösterilir. Lütfen bu kodda kullanılan [örnek Excel dosyasını](50528327.xlsx) ve kod tarafından oluşturulan [çıktı Excel dosyasını](50528328.xlsx) görün. Aşağıdaki ekran görüntüsü, kodun yürütülmesi sırasında örnek Excel dosyasındaki etkisini gösterir.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithCustomSortList.js" >}}

