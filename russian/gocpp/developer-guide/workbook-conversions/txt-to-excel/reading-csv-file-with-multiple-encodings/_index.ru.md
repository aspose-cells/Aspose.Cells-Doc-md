---
title: Чтение CSV файла с несколькими кодировками с помощью Golang через C++
linktitle: Чтение CSV файла с несколькими кодировками
type: docs
weight: 200
url: /ru/go-cpp/reading-csv-file-with-multiple-encodings/
description: Узнайте, как читать CSV файлы с несколькими кодировками, используя Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда ваш CSV-файл содержит несколько кодировок (Unicode, ANSI, UTF8, UTF7 и др.). Aspose.Cells позволяет загружать такие файлы и преобразовывать их в другие форматы, например, PDF или XLSX.

{{% /alert %}}

Для этого используйте свойство [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/), установив его в значение **true** для правильной загрузки CSV с несколькими кодировками.

Следующий снимок показывает пример CSV-файла, содержащего две строки. Первая строка в кодировке **ANSI**, вторая — в кодировке **Unicode**.

|**Входной файл**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Следующий снимок показывает файл XLSX, преобразованный из вышеуказанного CSV-файла без установки свойства [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) в **true**. Как видите, Unicode-текст был преобразован неправильно.

|**Файл вывода 1: не предусмотрены множественные кодировки**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Следующий снимок показывает файл XLSX, преобразованный из вышеуказанного CSV-файла после установки свойства [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/) в **true**. Как видите, Unicode-текст теперь преобразован правильно.

|**Файл вывода 2: IsMultiEncoded установлен в true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Ниже приведен образец кода, преобразующий вышеуказанный файл CSV в формат XLSX правильно.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadingCsvFileWithMultipleEncodings.go" >}}
## Связанные статьи

- [Открытие файлов CSV](/cells/ru/cpp/opening-files-with-different-formats/#opening-csv-files)
