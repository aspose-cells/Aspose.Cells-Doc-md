---
title: Чтение файла CSV с несколькими кодировками
type: docs
weight: 200
url: /ru/net/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}}

Иногда ваш файл CSV содержит несколько кодировок (Unicode, ANSI, UTF8, UTF7 и т. д.). Aspose.Cells позволяет загружать такие файлы CSV и преобразовывать их в другие форматы, например, PDF или XLSX.

{{% /alert %}}

 Aspose.Cells обеспечивает[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)свойство, которое вам нужно установить в**истинный** чтобы правильно загрузить файл CSV с несколькими кодировками.

 На следующем снимке экрана показан пример файла CSV, который содержит две строки. Первая строка находится в**ANSI** кодировка, а вторая строка находится в**Юникод** кодирование

|**Входной файл**|
|:- |
|![дело:изображение_альтернативный_текст](reading-csv-file-with-multiple-encodings_1.png)|

 На следующем снимке экрана показан файл XLSX, преобразованный из вышеуказанного файла CSV без установки[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) собственность на**истинный**. Как видите, текст Unicode не был преобразован должным образом.

|**Выходной файл 1: приспособление для многократного кодирования не предусмотрено.**|
|:- |
|![дело:изображение_альтернативный_текст](reading-csv-file-with-multiple-encodings_2.png)|

 На следующем снимке экрана показан файл XSLX, преобразованный из вышеуказанного файла CSV после установки[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) собственность на**истинный**. Как видите, текст Unicode теперь конвертируется правильно.

|**Выходной файл 2: IsMultiEncoded имеет значение true**|
|:- |
|![дело:изображение_альтернативный_текст](reading-csv-file-with-multiple-encodings_3.png)|

Ниже приведен пример кода, который правильно преобразует вышеуказанный файл CSV в формат XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## Статьи по Теме

- [Открытие CSV-файлов](/cells/ru/net/opening-files-with-different-formats/#opening-csv-files)
