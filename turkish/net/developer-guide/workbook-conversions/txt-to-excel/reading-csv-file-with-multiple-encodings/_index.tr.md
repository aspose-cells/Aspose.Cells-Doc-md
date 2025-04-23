---
title: Birden Fazla Kodlama ile CSV Dosyasını Okuma
type: docs
weight: 200
url: /tr/net/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}}

Bazı durumlarda, CSV dosyanız birden fazla Kodlama (Unicode, ANSI, UTF8, UTF7, vb.) içerir. Aspose.Cells, bu tür CSV dosyalarını yüklemenize ve bunları diğer formatlara, örneğin PDF veya XSLX'ye dönüştürmenize izin verir.

{{% /alert %}}

Aspose.Cells, CSV dosyanızı çoklu kodlamalarla doğru şekilde yüklemek için [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) özelliğini **true** olarak ayarlamalısınız.

Aşağıdaki ekran görüntüsü, iki satır içeren örnek bir CSV dosyasını gösterir. İlk satır **ANSI** kodlamasındadır ve ikinci satır **Unicode** kodlamasındadır

|**Giriş dosyası**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Yukarıdaki CSV dosyasından dönüştürülen XLSX dosyasını gösteren aşağıdaki ekran görüntüsü, [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) özelliğinin **true** olarak ayarlanmaması durumunda Unicode metninin düzgün şekilde dönüştürülmediğini gösterir.

|**Çıktı dosyası 1: çoklu kodlamalar için herhangi bir düzenleme yapılmamıştır**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Aşağıdaki ekran görüntüsü, [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) özelliğinin **true** olarak ayarlandıktan sonra yukarıdaki CSV dosyasından dönüştürülen XSLX dosyasını gösterir. Bu ekran görüntüsünde, Unicode metninin düzgün şekilde dönüştürüldüğünü görebilirsiniz.

|**Çıktı dosyası 2: IsMultiEncoded true olarak ayarlandı**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Aşağıdaki örnek kod, yukarıdaki CSV dosyasını XLSX formatına uygun bir şekilde dönüştürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## İlgili Makaleler

- [CSV Dosyalarını Açma](/cells/tr/net/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="csharp" >}}
