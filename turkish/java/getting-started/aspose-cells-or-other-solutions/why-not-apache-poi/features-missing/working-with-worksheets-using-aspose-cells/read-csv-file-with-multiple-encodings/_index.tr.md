---
title: Birden Çok Kodlamayla CSV Dosyasını Okuyun
type: docs
weight: 70
url: /tr/java/read-csv-file-with-multiple-encodings/
---
## **Aspose.Cells - Birden Çok Kodlama İçeren CSV Dosyasını Oku**
Bazen, CSV dosyanız birden çok Kodlama içerir (Unicode, ANSI, UTF8, UTF7 vb.). Aspose.Cells, bu tür CSV dosyalarını yüklemenize ve bunları örneğin PDF veya XLSX gibi diğer biçimlere dönüştürmenize olanak tanır.

**Java**

{{< highlight "java" >}}

 //Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(dataDir + "MultiEncoded.csv", options);

//Save it in XLSX format

workbook.save(dataDir + "EncodedNewFile_Out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Birden Çok Kodlamayla CSV Dosyasını Okuma](/cells/tr/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
