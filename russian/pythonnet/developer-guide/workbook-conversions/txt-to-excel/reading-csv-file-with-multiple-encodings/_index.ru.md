---
title: Чтение файла CSV с несколькими кодировками
type: docs
weight: 200
url: /ru/python-net/reading-csv-file-with-multiple-encodings/
description: Чтение файла CSV с несколькими кодировками с помощью Aspose.Cells for Python via .NET API.
keywords: Python Reading CSV File with Multiple Encodings, Convert CSV File with Multiple Encodings to Excel in Python via NET, Python convert CSV File with Multiple Encodings to xlsx, Load CSV File with Multiple Encodings to Excel file.
---
{{% alert color="primary" %}}

Иногда ваш файл CSV содержит несколько кодировок (Unicode, ANSI, UTF8, UTF7 и т. д.). Aspose.Cells позволяет загружать такие файлы CSV и конвертировать их в другие форматы, например, PDF или XLSX.

{{% /alert %}}

 Aspose.Cells обеспечивает[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) свойство, которое вам нужно установить в**истинный** чтобы правильно загрузить файл CSV с несколькими кодировками.

 На следующем снимке экрана показан пример файла CSV, содержащего две строки. Первая строка находится в**ANSI** кодировка, а вторая строка находится в**Юникод** кодирование

|**Входной файл**|
| :- |
|![задача: image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

На следующем снимке экрана показан файл XLSX, преобразованный из приведенного выше файла CSV без установки[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)свойство в *true**. Как видите, текст Unicode не был преобразован должным образом.

|**Выходной файл 1: не предусмотрено множественное кодирование.**|
| :- |
|![задача: image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

 На следующем снимке экрана показан файл XSLX, преобразованный из приведенного выше файла CSV после установки[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)свойство в *true**. Как видите, текст Unicode теперь преобразуется правильно.

|**Выходной файл 2: для параметра IsMultiEncoded установлено значение true.**|
| :- |
|![задача: image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Ниже приведен пример кода, который правильно преобразует указанный выше файл CSV в формат XLSX.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
