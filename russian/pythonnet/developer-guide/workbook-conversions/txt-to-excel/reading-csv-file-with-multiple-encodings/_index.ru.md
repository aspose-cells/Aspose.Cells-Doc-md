---
title: Чтение CSV файла с несколькими кодировками
type: docs
weight: 200
url: /ru/python-net/reading-csv-file-with-multiple-encodings/
description: Чтение файла CSV с несколькими кодировками с помощью Aspose.Cells для Python via .NET API.
keywords: Чтение файла CSV с несколькими кодировками в Python, Преобразуйте файл CSV с несколькими кодировками в Excel в Python via NET, Преобразуйте файл CSV с несколькими кодировками в xlsx в Python, Загрузите файл CSV с несколькими кодировками в файл Excel.
---

{{% alert color="primary" %}}

Иногда ваш CSV-файл содержит несколько кодировок (Unicode, ANSI, UTF8, UTF7 и т. д.). Aspose.Cells позволяет загружать такие CSV-файлы и преобразовывать их в другие форматы, например, PDF или XLSX.

{{% /alert %}}

Aspose.Cells предоставляет свойство [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/), которое вам нужно установить в **true**, чтобы корректно загрузить ваш CSV-файл с несколькими кодировками.

На следующем скриншоте показан пример CSV-файла, который содержит две строки. Первая строка в кодировке **ANSI**, а вторая строка в кодировке **Unicode**.

|**Входной файл**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

На следующем скриншоте показано файл XLSX, преобразованный из указанного CSV-файла без установки свойства [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) в **true**. Как видите, текст Unicode не был преобразован правильно.

|**Файл вывода 1: не предусмотрены множественные кодировки**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Ниже показан снимок экрана XSLX-файла, преобразованного из приведенного выше CSV-файла после установки свойства [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) в **true**. Как видите, Юникод-текст теперь конвертирован правильно.

|**Файл вывода 2: IsMultiEncoded установлен в true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Ниже приведен образец кода, преобразующий вышеуказанный файл CSV в формат XLSX правильно.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
