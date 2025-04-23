---
title: Чтение CSV файла с несколькими кодировками с помощью C++
linktitle: Чтение CSV файла с несколькими кодировками
type: docs
weight: 200
url: /ru/cpp/reading-csv-file-with-multiple-encodings/
description: Узнайте, как читать CSV файлы с несколькими кодировками, используя Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда ваш CSV-файл содержит несколько кодировок (Unicode, ANSI, UTF8, UTF7 и др.). Aspose.Cells позволяет загружать такие файлы и преобразовывать их в другие форматы, например, PDF или XLSX.

{{% /alert %}}

Для этого используйте свойство [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/), установив его в значение **true** для правильной загрузки CSV с несколькими кодировками.

Следующий снимок показывает пример CSV-файла, содержащего две строки. Первая строка в кодировке **ANSI**, вторая — в кодировке **Unicode**.

|**Входной файл**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Следующий снимок показывает файл XLSX, преобразованный из вышеуказанного CSV-файла без установки свойства [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) в **true**. Как видите, Unicode-текст был преобразован неправильно.

|**Файл вывода 1: не предусмотрены множественные кодировки**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Следующий снимок показывает файл XLSX, преобразованный из вышеуказанного CSV-файла после установки свойства [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/) в **true**. Как видите, Unicode-текст теперь преобразован правильно.

|**Файл вывода 2: IsMultiEncoded установлен в true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Ниже приведен образец кода, преобразующий вышеуказанный файл CSV в формат XLSX правильно.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input CSV file
    U16String filePath = srcDir + u"MultiEncoded.csv";

    // Create TxtLoadOptions and set MultiEncoded property to true
    TxtLoadOptions options;
    options.SetIsMultiEncoded(true);

    // Load the CSV file into Workbook with the specified options
    Workbook workbook(filePath, options);

    // Save the workbook in XLSX format
    workbook.Save(filePath + u".out.xlsx", SaveFormat::Xlsx);

    std::cout << "File converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Связанные статьи

- [Открытие файлов CSV](/cells/ru/cpp/opening-files-with-different-formats/#opening-csv-files)
