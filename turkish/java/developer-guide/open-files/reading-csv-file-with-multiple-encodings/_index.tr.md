---
title: Birden Fazla Kodlama İçeren CSV Dosyasını Okuma
type: docs
weight: 140
url: /tr/java/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}} 

Bazen, CSV dosyanız birden çok Kodlama (Unicode, ANSI, UTF8, UTF7 vb.) içerir. Aspose.Cells, bu tür CSV dosyalarını yüklemenize ve bunları başka biçimlere, örneğin PDF veya XLSX'e dönüştürmenize olanak tanır.

{{% /alert %}} 

 Aspose.Cells, ayarlamanız gereken TxtLoadOptions.setMultiEncoded() yöntemini sağlar**doğru** CSV dosyanızı birden fazla kodlamayla düzgün şekilde yüklemek için.

 Aşağıdaki ekran görüntüsü, iki satır içeren örnek bir CSV dosyasını göstermektedir. İlk satır içinde**ANSI** kodlama ve ikinci satır**Unicode** kodlama

**Giriş dosyası** 

![yapılacaklar:resim_alternatif_metin](reading-csv-file-with-multiple-encodings_1.png)

Aşağıdaki ekran görüntüsü, TxtLoadOptions.setMultiEncoded() yöntemini true olarak ayarlamadan yukarıdaki CSV dosyasından dönüştürülen XLSX dosyasını gösterir. Gördüğünüz gibi, Unicode metni düzgün bir şekilde dönüştürülmedi.

**Çıktı dosyası 1: çoklu kodlama için herhangi bir düzenleme yapılmadı** 

![yapılacaklar:resim_alternatif_metin](reading-csv-file-with-multiple-encodings_2.png)

Aşağıdaki ekran görüntüsü, TxtLoadOptions.setMultiEncoded() yöntemini true olarak ayarladıktan sonra yukarıdaki CSV dosyasından dönüştürülen XSLX dosyasını gösterir. Gördüğünüz gibi, Unicode metni artık düzgün bir şekilde dönüştürüldü.

**Çıktı dosyası 2: IsMultiEncoded, true olarak ayarlandı** 

![yapılacaklar:resim_alternatif_metin](reading-csv-file-with-multiple-encodings_3.png)

Aşağıda, yukarıdaki CSV dosyasını düzgün bir şekilde XLSX biçimine dönüştüren örnek kod bulunmaktadır.

**Java**

{{< highlight "csharp" >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
