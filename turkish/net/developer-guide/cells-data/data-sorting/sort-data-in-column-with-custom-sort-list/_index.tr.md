---
title: Özel Sıralama Listesiyle Sütundaki Verileri Sıralama
type: docs
weight: 290
url: /tr/net/sort-data-in-column-with-custom-sort-list/
description: Aspose.Cells for .NET API'i kullanarak özel bir liste kullanarak sütundaki verileri nasıl sıralayacağınızı öğrenin.
keywords: Sort Data in Column with Custom Sort List, Sort data by custom list.
---
##  **Olası Kullanım Senaryoları**

 Özel bir liste kullanarak sütundaki verileri sıralayabilirsiniz. Bu kullanılarak yapılabilir[**DataSorter.AddKey(int anahtarı, SortOrder sırası, String özelList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)yöntem. Ancak bu yöntem yalnızca özel listedeki öğelerin içinde virgül bulunmadığında çalışır. "USA,US", "China,CN" vb. gibi virgülleri varsa, o zaman [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) yöntemi. Burada son parametre String değil, bir String Dizisidir.

##  **Özel Sıralama Listesiyle Sütundaki Verileri Sıralama**

Aşağıdaki örnek kod, [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey) nasıl kullanılacağını açıklamaktadır Verileri özel sıralama listesiyle sıralamak için /methods/3) yöntemini kullanın. Lütfen bkz[örnek Excel dosyası](50528327.xlsx) Bu kodda kullanılan ve[Excel dosyasının çıktısı](50528328.xlsx) onun tarafından oluşturulmuştur. Aşağıdaki ekran görüntüsü, örnek Excel dosyasındaki kodun yürütme üzerindeki etkisini göstermektedir.

![yapılacak şey:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

##  **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
