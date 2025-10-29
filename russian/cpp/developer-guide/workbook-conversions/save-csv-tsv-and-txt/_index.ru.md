---
title: Конвертация Excel в CSV, TSV и Txt с помощью C++
linktitle: Сохранить как CSV, TSV и Txt
type: docs
weight: 40
url: /ru/cpp/convert-excel-to-csv-tsv-and-txt/
description: Легко конвертируйте файлы Excel в форматы CSV, TSV и TXT с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет конвертировать файлы Excel, ODS, JSON и другие форматы в CSV, TSV и TXT.

{{% /alert %}}

## **Сохранение рабочей книги в текстовом или CSV формате**

Иногда вам может потребоваться конвертировать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) как Microsoft Excel, так и Aspose.Cells по умолчанию сохраняют только содержимое активного листа.

В следующем примере кода объясняется, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронных таблиц Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством листов.

При выполнении кода он преобразует данные всех листов рабочей книги в формат TXT

Вы можете изменить тот же пример, чтобы сохранить ваш файл в CSV. По умолчанию [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) — запятая, поэтому не указывайте сепаратор при сохранении в формате CSV.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    U16String outputFilePath = srcDir + u"out.txt";
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully as text file!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Сохранение текстовых файлов с пользовательским разделителем**

Текстовые файлы содержат данные электронных таблиц без форматирования. Файл представляет собой своего рода обычный текстовый файл, который может содержать некоторые настраиваемые разделители между его данными.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';'); // Using U16String for the char

    // Save the file with the options
    workbook.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Сохранять разделители для пустых строк при экспорте таблиц в формат CSV](/cells/ru/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV](/cells/ru/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="cpp" >}}
