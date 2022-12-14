---
title: Özel Sıralama Listesi ile Verileri Sütunda Sırala
type: docs
weight: 210
url: /tr/java/sort-data-in-column-with-custom-sort-list/
---
## **Olası Kullanım Senaryoları**

Özel bir liste kullanarak sütundaki verileri sıralayabilirsiniz. Bu kullanılarak yapılabilir[DataSorter.AddKey(int anahtarı, SortOrder düzeni, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) yöntem. Ancak, bu yöntem yalnızca özel listedeki öğelerin içinde virgül yoksa çalışır. "USA, US", "China, CN" vb. gibi virgüller varsa, o zaman kullanmanız gerekir.[DataSorter.AddKey(int anahtarı, SortOrder düzeni, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) yöntem. Burada, son parametre String değil, bir String of String'dir.

## **Özel Sıralama Listesi ile Verileri Sütunda Sırala**

Aşağıdaki örnek kod, verileri özel sıralama listesiyle sıralamak için DataSorter.AddKey(int key, SortOrder order, String[]customList) yönteminin nasıl kullanılacağını açıklar. Lütfen bkz[örnek excel dosyası](50528359.xlsx)Bu kodda kullanılan ve[çıktı excel dosyası](50528358.xlsx)onun tarafından oluşturulur. Aşağıdaki ekran görüntüsü, örnek Excel dosyasındaki kodun yürütme üzerindeki etkisini gösterir.

![yapılacaklar:resim_alternatif_Metin](sort-data-in-column-with-custom-sort-list_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
