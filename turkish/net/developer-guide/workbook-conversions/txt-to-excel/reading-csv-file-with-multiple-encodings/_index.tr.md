---
title: Birden Fazla Kodlama İçeren CSV Dosyasını Okuma
type: docs
weight: 200
url: /tr/net/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}}

Bazen, CSV dosyanız birden çok Kodlama (Unicode, ANSI, UTF8, UTF7, vb.) içerir. Aspose.Cells, bu tür CSV dosyalarını yüklemenize ve bunları örneğin PDF veya XLSX gibi diğer biçimlere dönüştürmenize olanak tanır.

{{% /alert %}}

 Aspose.Cells şunları sağlar:[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) olarak ayarlamanız gereken özellik**doğru** CSV dosyanızı birden fazla kodlamayla düzgün şekilde yüklemek için.

 Aşağıdaki ekran görüntüsü, iki satır içeren örnek bir CSV dosyasını göstermektedir. İlk satır içinde**ANSI** kodlama ve ikinci satır**Unicode** kodlama

|**Giriş dosyası**|
|:- |
|![yapılacaklar:resim_alternatif_metin](reading-csv-file-with-multiple-encodings_1.png)|

 Aşağıdaki ekran görüntüsü, ayarlanmadan yukarıdaki CSV dosyasından dönüştürülen XLSX dosyasını göstermektedir.[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) mülkiyet**doğru**. Gördüğünüz gibi, Unicode metni düzgün bir şekilde dönüştürülmedi.

|**Çıktı dosyası 1: çoklu kodlama için herhangi bir düzenleme yapılmadı**|
|:- |
|![yapılacaklar:resim_alternatif_metin](reading-csv-file-with-multiple-encodings_2.png)|

 Aşağıdaki ekran görüntüsü, ayarlandıktan sonra yukarıdaki CSV dosyasından dönüştürülen XSLX dosyasını gösterir.[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) mülkiyet**doğru**. Gördüğünüz gibi, Unicode metni artık düzgün bir şekilde dönüştürüldü.

|**Çıktı dosyası 2: IsMultiEncoded, true olarak ayarlandı**|
|:- |
|![yapılacaklar:resim_alternatif_metin](reading-csv-file-with-multiple-encodings_3.png)|

Aşağıda, yukarıdaki CSV dosyasını düzgün bir şekilde XLSX biçimine dönüştüren örnek kod bulunmaktadır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## İlgili Makaleler

- [CSV Dosyalarını Açma](/cells/tr/net/opening-files-with-different-formats/#opening-csv-files)
