---
title: Чтение файла CSV с несколькими кодировками
type: docs
weight: 140
url: /ru/java/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}} 

Иногда ваш файл CSV содержит несколько кодировок (Unicode, ANSI, UTF8, UTF7 и т. д.). Aspose.Cells позволяет загружать такие файлы CSV и преобразовывать их в другие форматы, например PDF или XLSX.

{{% /alert %}} 

 Aspose.Cells предоставляет метод TxtLoadOptions.setMultiEncoded(), для которого необходимо установить значение**истинный** чтобы правильно загрузить файл CSV с несколькими кодировками.

 На следующем снимке экрана показан пример файла CSV, который содержит две строки. Первая строка находится в**ANSI** кодировка, а вторая строка находится в**Юникод** кодирование

**Входной файл** 

![дело:изображение_альтернативный_текст](reading-csv-file-with-multiple-encodings_1.png)

На следующем снимке экрана показан файл XLSX, преобразованный из указанного выше файла CSV без установки для метода TxtLoadOptions.setMultiEncoded() значения true. Как видите, текст Unicode не был преобразован должным образом.

**Выходной файл 1: приспособление для многократного кодирования не предусмотрено.** 

![дело:изображение_альтернативный_текст](reading-csv-file-with-multiple-encodings_2.png)

На следующем снимке экрана показан файл XSLX, преобразованный из указанного выше файла CSV после установки для метода TxtLoadOptions.setMultiEncoded() значения true. Как видите, текст Unicode теперь конвертируется правильно.

**Выходной файл 2: IsMultiEncoded имеет значение true** 

![дело:изображение_альтернативный_текст](reading-csv-file-with-multiple-encodings_3.png)

Ниже приведен пример кода, который правильно преобразует вышеуказанный файл CSV в формат XLSX.

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
