---
title: Birden Fazla Kodlama İçeren CSV Dosyasını Okuyun
type: docs
weight: 70
url: /tr/java/read-csv-file-with-multiple-encodings/
---
## **Aspose.Cells - Birden Fazla Kodlamalı CSV Dosyasını Oku**
Bazen, CSV dosyanız birden çok Kodlama (Unicode, ANSI, UTF8, UTF7 vb.) içerir. Aspose.Cells, bu tür CSV dosyalarını yüklemenize ve bunları başka biçimlere, örneğin PDF veya XLSX'e dönüştürmenize olanak tanır.

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

 Daha fazla ayrıntı için, ziyaret edin[Birden Fazla Kodlama İçeren CSV Dosyasını Okuma](/cells/tr/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
