---
title: Birden Fazla Kodlama ile CSV Dosyasını Okuma
type: docs
weight: 200
url: /tr/python-net/reading-csv-file-with-multiple-encodings/
description: Aspose.Cells for Python via .NET API sını kullanarak Birden Fazla Kod Çözme Biçimine Sahip CSV Dosyasını Okuma.
keywords: Python da Birden Fazla Kod Çözme Biçimine Sahip CSV Dosyasını Okuma, Python da Birden Fazla Kod Çözme Biçimine Sahip CSV Dosyasını Excel e dönüştürme via NET, Python da Birden Fazla Kod Çözme Biçimine Sahip CSV Dosyasını xlsx ye dönüştürme, Excel dosyasına Birden Fazla Kod Çözme Biçimine Sahip CSV Dosyası Yükleme
---

{{% alert color="primary" %}}

Bazı durumlarda, CSV dosyanız birden fazla Kodlama (Unicode, ANSI, UTF8, UTF7, vb.) içerir. Aspose.Cells, bu tür CSV dosyalarını yüklemenize ve bunları diğer formatlara, örneğin PDF veya XSLX'ye dönüştürmenize izin verir.

{{% /alert %}}

Aspose.Cells, CSV dosyanızı çoklu kodlamalarla doğru şekilde yüklemek için [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) özelliğini **true** olarak ayarlamalısınız.

Aşağıdaki ekran görüntüsü, iki satır içeren örnek bir CSV dosyasını gösterir. İlk satır **ANSI** kodlamasındadır ve ikinci satır **Unicode** kodlamasındadır

|**Giriş dosyası**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Yukarıdaki CSV dosyasından dönüştürülen XLSX dosyasını gösteren aşağıdaki ekran görüntüsü, [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) özelliğinin **true** olarak ayarlanmaması durumunda Unicode metninin düzgün şekilde dönüştürülmediğini gösterir.

|**Çıktı dosyası 1: çoklu kodlamalar için herhangi bir düzenleme yapılmamıştır**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Aşağıdaki ekran görüntüsü, [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) özelliğinin **true** olarak ayarlandıktan sonra yukarıdaki CSV dosyasından dönüştürülen XSLX dosyasını gösterir. Bu ekran görüntüsünde, Unicode metninin düzgün şekilde dönüştürüldüğünü görebilirsiniz.

|**Çıktı dosyası 2: IsMultiEncoded true olarak ayarlandı**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Aşağıdaki örnek kod, yukarıdaki CSV dosyasını XLSX formatına uygun bir şekilde dönüştürür.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
