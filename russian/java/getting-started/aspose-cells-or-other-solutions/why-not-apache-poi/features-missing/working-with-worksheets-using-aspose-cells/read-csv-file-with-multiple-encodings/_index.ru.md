---
title: Чтение файла CSV с несколькими кодировками
type: docs
weight: 70
url: /ru/java/read-csv-file-with-multiple-encodings/
---

## **Aspose.Cells - Чтение файла CSV с несколькими кодировками**
Иногда ваш CSV-файл содержит несколько кодировок (Unicode, ANSI, UTF8, UTF7 и т. д.). Aspose.Cells позволяет загружать такие CSV-файлы и преобразовывать их в другие форматы, например, PDF или XLSX.

**Java**

{{< highlight java >}}

 //Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(dataDir + "MultiEncoded.csv", options);

//Save it in XLSX format

workbook.save(dataDir + "EncodedNewFile_Out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
## **Скачать работающий код**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Чтение файла CSV с несколькими кодировками](/cells/ru/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
