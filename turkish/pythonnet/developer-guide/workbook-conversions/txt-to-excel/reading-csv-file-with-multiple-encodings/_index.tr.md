---
title: CSV Dosyasını Çoklu Kodlamalarla Okumak
type: docs
weight: 200
url: /tr/python-net/reading-csv-file-with-multiple-encodings/
description: Aspose.Cells for Python via .NET API kullanarak CSV Çoklu Kodlamalı Dosyayı Okuma.
keywords: Python Reading CSV File with Multiple Encodings, Convert CSV File with Multiple Encodings to Excel in Python via NET, Python convert CSV File with Multiple Encodings to xlsx, Load CSV File with Multiple Encodings to Excel file.
---
{{% alert color="primary" %}}

Bazen CSV dosyanız birden fazla Kodlama (Unicode, ANSI, UTF8, UTF7 vb.) içerir. Aspose.Cells, bu tür CSV dosyalarını yüklemenize ve bunları diğer formatlara (örneğin PDF veya XLSX) dönüştürmenize olanak tanır.

{{% /alert %}}

 Aspose.Cells şunları sağlar[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) ayarlamanız gereken özellik**doğru** CSV dosyanızı birden fazla kodlamayla düzgün şekilde yüklemek için.

 Aşağıdaki ekran görüntüsünde iki satır içeren örnek bir CSV dosyası gösterilmektedir. İlk satır içeride**ANSI** kodlama ve ikinci satır**Unicode** kodlama

|**Giriş dosyası**|
| :- |
|![yapılacak şey:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Aşağıdaki ekran görüntüsü, yukarıdaki CSV dosyasından dönüştürülen XLSX dosyasını,[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)özelliği *true** olarak değiştirin. Gördüğünüz gibi Unicode metni düzgün şekilde dönüştürülmedi.

|**Çıkış dosyası 1: çoklu kodlama için herhangi bir düzenleme yapılmadı**|
| :- |
|![yapılacak şey:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

 Aşağıdaki ekran görüntüsü, yukarıdaki CSV dosyasından dönüştürülen XSLX dosyasını göstermektedir.[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)özelliği *true** olarak değiştirin. Gördüğünüz gibi Unicode metni artık düzgün bir şekilde dönüştürüldü.

|**Çıkış dosyası 2: IsMultiEncoded true olarak ayarlandı**|
| :- |
|![yapılacak şey:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Yukarıdaki CSV dosyasını düzgün bir şekilde XLSX formatına dönüştüren örnek kod aşağıdadır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
