---
title: Чтение CSV файла с несколькими кодировками
type: docs
weight: 140
url: /ru/java/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}} 

Иногда ваш CSV-файл содержит несколько кодировок (Unicode, ANSI, UTF8, UTF7 и т. д.). Aspose.Cells позволяет загружать такие CSV-файлы и преобразовывать их в другие форматы, например, PDF или XLSX.

{{% /alert %}} 

Aspose.Cells предоставляет метод TxtLoadOptions.setMultiEncoded(), который нужно установить в **true**, чтобы правильно загрузить ваш CSV-файл с несколькими кодировками.

Ниже показан снимок экрана - образец файла CSV, содержащий две строки. Первая строка закодирована в **ANSI**, а вторая - в **Unicode**

**Входной файл** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)

Ниже показан снимок экрана - файл XLSX, преобразованный из вышеуказанного файла CSV без установки метода TxtLoadOptions.setMultiEncoded() в true. Как видно, Юникод-текст не был правильно преобразован.

**Выходной файл 1: не сделано никаких упоров на несколько кодировок** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)

Ниже показан снимок экрана - файл XSLX, преобразованный из вышеуказанного файла CSV после установки метода TxtLoadOptions.setMultiEncoded() в true. Как видно, Юникод-текст теперь преобразован правильно.

**Выходной файл 2: IsMultiEncoded установлено в true** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)

Ниже приведен образец кода, преобразующий вышеуказанный файл CSV в формат XLSX правильно.

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
