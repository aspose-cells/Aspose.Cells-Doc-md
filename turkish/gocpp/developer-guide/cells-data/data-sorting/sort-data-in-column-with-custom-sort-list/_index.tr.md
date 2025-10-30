---
title: Golang ve C++ ile Özel Sıralama Listesi ile Sütunda Veri Sırala
linktitle: Özel Sıralama Listesi ile Sütunda Verileri Sıralama
type: docs
weight: 290
url: /tr/go-cpp/sort-data-in-column-with-custom-sort-list/
description: Aspose.Cells for C++ API’sini kullanarak özel liste ile sütundaki veriyi nasıl sıralayacağınızı öğrenin.
keywords: Özel Sıralama Listesi ile Sütunda Veri Sıralama, Özel liste ile veri sırala.
---

## **Olası Kullanım Senaryoları**

Sütundaki veriyi özel bir liste kullanarak sıralayabilirsiniz. Bu [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) yöntemiyle yapılabilir. Ancak, bu yöntem yalnızca özel listedeki öğelerde virgül yoksa çalışır. Eğer "USA,US", "Çin,CN" gibi virgüller içeriyorsa, o zaman [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) yöntemini kullanmanız gerekir. Burada, son parametre String değil, bir String Dizisidir.

## **Özel Sıralama Listesi ile Sütunda Verileri Sıralama**

Aşağıdaki örnek kod, [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) yöntemini kullanarak özel sıralama listesi ile veriyi nasıl sıralayacağınızı gösterir. Bu kodda kullanılan [örnek Excel dosyasını](50528327.xlsx) ve bunun tarafından oluşturulan [çıkış Excel dosyasını](50528328.xlsx) inceleyin. Aşağıdaki ekran görüntüsü, kodun çalışma anında örnek Excel dosyasına olan etkisini gösterir.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SortDataInColumnWithCustomSortList.go" >}}
