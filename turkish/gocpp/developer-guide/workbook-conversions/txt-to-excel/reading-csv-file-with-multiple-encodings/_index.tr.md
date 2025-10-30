---
title: Golangkullanarak Çoklu Kodlamalarla CSV Dosyasını Okuma
linktitle: Birden Fazla Kodlama ile CSV Dosyasını Okuma
type: docs
weight: 200
url: /tr/go-cpp/reading-csv-file-with-multiple-encodings/
description: Çoklu kodlama kullanarak Aspose.Cells for C++ ile CSV dosyalarını okuma yöntemini öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, çoklu kodlama ile CSV'yi düzgün yüklemek için {0} özelliğini **true** yapmanızı sağlar.

{{% /alert %}}

Aspose.Cells, [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) özelliği sağlar, bu özelliği doğru şekilde yüklemek için **true** olarak ayarlamanız gerekir.

Aşağıdaki ekran görüntüsü, iki satır içeren örnek bir CSV dosyasını gösterir. Birinci satır **ANSI** kodlamasında ve ikinci satır **Unicode** kodlamasındadır.

|**Giriş dosyası**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Aşağıdaki ekran görüntüsü, yukarıdaki CSV dosyasından dönüştürülmüş XLSX dosyasını gösterir, [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) özelliği **true** olarak ayarlanmamıştır. Görüldüğü gibi, Unicode metni düzgün çevrilmemiştir.

|**Çıktı dosyası 1: çoklu kodlamalar için herhangi bir düzenleme yapılmamıştır**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Aşağıdaki ekran görüntüsü, yukarıdaki CSV dosyasından dönüştürülmüş XLSX dosyasını gösterir, [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) özelliği **true** olarak ayarlandıktan sonra. Görüldüğü gibi, Unicode metni düzgün şekilde çevrilmiştir.

|**Çıktı dosyası 2: IsMultiEncoded true olarak ayarlandı**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Aşağıdaki örnek kod, yukarıdaki CSV dosyasını XLSX formatına uygun bir şekilde dönüştürür.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadingCsvFileWithMultipleEncodings.go" >}}
## İlgili Makaleler

- [CSV Dosyalarını Açma](/cells/tr/cpp/opening-files-with-different-formats/#opening-csv-files)
