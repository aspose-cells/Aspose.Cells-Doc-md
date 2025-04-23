---
title: Чтение CSV файла с несколькими кодировками
type: docs
weight: 200
url: /ru/net/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}}

Иногда ваш CSV-файл содержит несколько кодировок (Unicode, ANSI, UTF8, UTF7 и т. д.). Aspose.Cells позволяет загружать такие CSV-файлы и преобразовывать их в другие форматы, например, PDF или XLSX.

{{% /alert %}}

Aspose.Cells предоставляет свойство [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded), которое вам нужно установить в **true**, чтобы корректно загрузить ваш CSV-файл с несколькими кодировками.

На следующем скриншоте показан пример CSV-файла, который содержит две строки. Первая строка в кодировке **ANSI**, а вторая строка в кодировке **Unicode**.

|**Входной файл**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

На следующем скриншоте показано файл XLSX, преобразованный из указанного CSV-файла без установки свойства [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) в **true**. Как видите, текст Unicode не был преобразован правильно.

|**Файл вывода 1: не предусмотрены множественные кодировки**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Ниже показан снимок экрана XSLX-файла, преобразованного из приведенного выше CSV-файла после установки свойства [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) в **true**. Как видите, Юникод-текст теперь конвертирован правильно.

|**Файл вывода 2: IsMultiEncoded установлен в true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Ниже приведен образец кода, преобразующий вышеуказанный файл CSV в формат XLSX правильно.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## Связанные статьи

- [Открытие файлов CSV](/cells/ru/net/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="csharp" >}}
