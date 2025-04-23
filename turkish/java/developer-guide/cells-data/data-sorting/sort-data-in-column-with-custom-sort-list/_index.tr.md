---
title: Özel Sıralama Listesi ile Sütunda Verileri Sıralama
type: docs
weight: 210
url: /tr/java/sort-data-in-column-with-custom-sort-list/
---

## **Olası Kullanım Senaryoları**

Verileri özel liste kullanarak sütunda sıralayabilirsiniz. Bunu [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-) yöntemi ile yapabilirsiniz. Ancak, bu yöntem sadece özel listedekindeki öğelerin içinde virgül olmayan durumlar için geçerlidir. Eğer listede "USA, US", "Çin, CN" gibi virgüller varsa, [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-) yöntemini kullanmalısınız. Burada son parametre String değil, Bir Dizidir (Array) of Strings.

## **Özel Sıralama Listesi ile Sütunda Verileri Sıralama**

Aşağıdaki örnek kod, özel sıralama listesi kullanarak verileri özel sıralama listesi ile sıralamanın nasıl yapıldığını açıklar. Bu kodda kullanılan [örnek Excel dosyasını](50528359.xlsx) ve bununla oluşturulan [çıktı Excel dosyasını](50528358.xlsx) kullanarak daha fazla yardım alabilirsiniz. Aşağıdaki ekran görüntüsü, örnek Excel dosyası üzerinde kodun etkisini gösterir.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
{{< app/cells/assistant language="java" >}}
