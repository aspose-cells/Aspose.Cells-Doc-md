---
title: Özel Sıralama Listesi ile Sütunda Verileri Sıralama
type: docs
weight: 290
url: /tr/net/sort-data-in-column-with-custom-sort-list/
description: Aspose.Cells for .NET API sını kullanarak özel bir liste kullanarak sütunda veri nasıl sıralanacağını öğrenin.
keywords: Özel Sıralama Listesi ile Sütunda Veri Sıralama, Özel liste ile veri sırala.
---

## **Olası Kullanım Senaryoları**

Sütunda veri özel bir liste kullanarak sıralanabilir. Bu [**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2) yöntemi kullanılarak yapılabilir. Ancak, özel listedeki öğelerin içinde virgül gibi karakterler bulunmuyorsa. Eğer "ABD,US", "Çin,CN" gibi virgül içeren öğeler varsa, o zaman [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) yöntemini kullanmalısınız. Burada, son parametre String değil, String dizisidir.

## **Özel Sıralama Listesi ile Sütunda Verileri Sıralama**

Aşağıdaki örnek kod, özel sıralama listesi ile veri sıralama işlemini açıklar. Bu kodda kullanılan [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) yöntemini görmek için lütfen bu kodun kullandığı [örnek Excel dosyasını](50528327.xlsx) ve bu işlem sonucunda oluşturulan [çıktı Excel dosyasını](50528328.xlsx) inceleyin.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
{{< app/cells/assistant language="csharp" >}}
