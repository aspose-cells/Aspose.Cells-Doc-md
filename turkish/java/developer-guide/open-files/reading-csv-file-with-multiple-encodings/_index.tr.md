---
title: Birden Fazla Kodlama ile CSV Dosyasını Okuma
type: docs
weight: 140
url: /tr/java/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}} 

Bazen CSV dosyanız birden fazla Kodlama içerir (Unicode, ANSI, UTF8, UTF7 vb.). Aspose.Cells, bu tür CSV dosyalarını yüklemenize ve bunları diğer formatlara, örneğin PDF veya XLSX'ye dönüştürmenize izin verir.

{{% /alert %}} 

Aspose.Cells, CSV dosyanızı birden fazla kodlama ile doğru bir şekilde yüklemek için **true** olarak ayarlamanız gereken TxtLoadOptions.setMultiEncoded() method'unu sağlar.

Aşağıdaki ekran görüntüsü, iki satır içeren bir örnek CSV dosyasını göstermektedir. İlk satır **ANSI** kodlamadadır ve ikinci satır **Unicode** kodlamadadır.

**Giriş dosyası** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)

Yukarıdaki CSV dosyasından dönüştürülen XLSX dosyasını aşağıdaki ekran görüntüsü göstermektedir. Görebileceğiniz gibi, Unicode metni doğru bir şekilde dönüştürülmemiştir.

**Çıktı dosyası 1: birden fazla kodlama için uyarlama yapılmadı** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)

Yukarıdaki CSV dosyasından dönüştürülen XSLX dosyasını aşağıdaki ekran görüntüsü göstermektedir. Görebileceğiniz gibi, Unicode metni şimdi doğru bir şekilde dönüştürülmüştür.

**Çıktı dosyası 2: IsMultiEncoded true olarak ayarlandı** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)

Aşağıdaki örnek kod, yukarıdaki CSV dosyasını XLSX formatına uygun bir şekilde dönüştürür.

**Java**

{{< highlight csharp >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
