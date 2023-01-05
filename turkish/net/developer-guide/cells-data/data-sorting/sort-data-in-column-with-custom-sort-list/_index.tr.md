---
title: Özel Sıralama Listesi ile Verileri Sütunda Sırala
type: docs
weight: 290
url: /tr/net/sort-data-in-column-with-custom-sort-list/
---
## **Olası Kullanım Senaryoları**

 Özel bir liste kullanarak sütundaki verileri sıralayabilirsiniz. Bu kullanılarak yapılabilir[**DataSorter.AddKey(int anahtarı, SortOrder düzeni, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)yöntem. Ancak, bu yöntem yalnızca özel listedeki öğelerin içinde virgül yoksa çalışır. "USA,US", "China,CN" vb. gibi virgülleri varsa [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) yöntemi. Burada, son parametre String değil, bir String of String'dir.

## **Özel Sıralama Listesi ile Verileri Sütunda Sırala**

Aşağıdaki örnek kod, [**DataSorter.AddKey Yöntemi (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey) nasıl kullanılacağını açıklar /methods/3) özel sıralama listesiyle verileri sıralama yöntemi. Lütfen bu kodda kullanılan [örnek Excel dosyasına](50528327.xlsx) ve bunun tarafından oluşturulan [çıktı Excel dosyasına](50528328.xlsx) bakın. Aşağıdaki ekran görüntüsü, örnek Excel dosyasındaki kodun yürütme üzerindeki etkisini gösterir.

![yapılacaklar:resim_alternatif_metin](sort-data-in-column-with-custom-sort-list_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
