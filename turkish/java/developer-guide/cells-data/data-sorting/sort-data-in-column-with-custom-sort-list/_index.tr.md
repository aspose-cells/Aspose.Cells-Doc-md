---
title: Özel Sıralama Listesi ile Sütunda Verileri Sıralama
type: docs
weight: 210
url: /tr/java/sort-data-in-column-with-custom-sort-list/
---

## **Olası Kullanım Senaryoları**

Özel sıralama listesi kullanarak sütundaki verileri sıralayabilirsiniz. Bu, [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) yöntemi kullanılarak yapılabilir. Ancak, bu yöntem özel listedeki öğelerin içinde virgül bulunmuyorsa çalışır. Eğer "ABD, US", "Çin, CN" gibi virgül içeren öğeler varsa, o zaman [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) yöntemini kullanmalısınız. Burada, son parametre String değil, bir Dizi String'dir.

## **Özel Sıralama Listesi ile Sütunda Verileri Sıralama**

Aşağıdaki örnek kod, özel sıralama listesi kullanarak verileri özel sıralama listesi ile sıralamanın nasıl yapıldığını açıklar. Bu kodda kullanılan [örnek Excel dosyasını](50528359.xlsx) ve bununla oluşturulan [çıktı Excel dosyasını](50528358.xlsx) kullanarak daha fazla yardım alabilirsiniz. Aşağıdaki ekran görüntüsü, örnek Excel dosyası üzerinde kodun etkisini gösterir.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
