---
title: Конвертация CSV, TSV и TXT в Excel с помощью C++
linktitle: Конвертация CSV, TSV и TXT в Excel
type: docs
weight: 30
url: /ru/cpp/convert-csv-tsv-and-txt-to-excel/
description: Узнайте, как конвертировать файлы CSV, TSV и TXT в Excel, используя Aspose.Cells for C++.
---

{{% alert color="primary" %}}

С помощью Aspose.Cells for C++ вы можете конвертировать файлы CSV в Excel, OpenOffice, PDF, JSON и многие другие форматы.

{{% /alert %}}

## **Открытие файлов CSV**

Файлы Значения, разделённые запятыми (CSV), содержат записи, где значения разделены запятыми. Данные хранятся в виде таблицы, где каждый столбец разделён запятой и заключён в двойные кавычки. Если значение поля содержит двойную кавычку, она экранируется парой двойных кавычек. Также можно экспортировать данные таблицы в CSV с помощью Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions4(LoadFormat::Csv);

    // Create a Workbook object and open the file from its path
    Workbook wbCSV(srcDir + u"Book_CSV.csv", loadOptions4);

    std::cout << "CSV file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Открытие CSV-файлов и замена недопустимых символов**

В Excel при открытии CSV-файла с специальными символами символы автоматически заменяются. То же самое делает API Aspose.Cells, как показано в приведенном ниже коде.

```c++
// Fix BOM issue
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filename = srcDir + u"[20180220142533][ASPOSE_CELLS_TEST].csv";

    TxtLoadOptions options;
    options.SetSeparator(u';');
    options.SetCheckExcelRestriction(false);
    options.SetConvertNumericData(false);
    options.SetConvertDateTimeData(false);

    LoadFilter* filter = new LoadFilter(LoadDataFilterOptions::CellData);
    options.SetLoadFilter(filter);

    Workbook workbook(filename, options);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::cout << worksheet.GetName().ToUtf8() << std::endl;
    std::cout << worksheet.GetName().GetLength() << std::endl;
    std::cout << "CSV file opened successfully!" << std::endl;

    delete filter;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Использование предпочтительного парсера**

Не всегда необходимо использовать настройки парсера по умолчанию для открытия CSV-файлов. Иногда импорт CSV файла не создает ожидаемый результат, например, формат даты не такой, как ожидается, или пустые поля обрабатываются иначе. Для этого предназначен **TxtLoadOptions.PreferredParsers**, который позволяет указать ваш собственный парсер для обработки различных типов данных в соответствии с вашими требованиями. В следующем примере показано, как использовать предпочтительный парсер.

Исходный файл и выходные файлы для примера можно скачать по следующим ссылкам для тестирования этой функции.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
	Aspose::Cells::Startup();

	U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
	U16String outDir(u"..\\Data\\02_OutputDirectory\\");

	TxtLoadOptions loadOptions(LoadFormat::Csv);
	loadOptions.SetSeparator(u',');
	loadOptions.SetConvertDateTimeData(true);

	Workbook workbook(srcDir + u"sample.csv", loadOptions);

	Worksheet worksheet = workbook.GetWorksheets().Get(0);
	Cells cells = worksheet.GetCells();

	Cell cell = cells.Get(u"A1");
	std::cout << "A1: " << static_cast<int>(cell.GetType())
		<< " - " << cell.GetDisplayStringValue().ToUtf8() << std::endl;

	cell = cells.Get(u"B1");
	std::cout << "B1: " << static_cast<int>(cell.GetType())
		<< " - " << cell.GetDisplayStringValue().ToUtf8() << std::endl;

	workbook.Save(outDir + u"outputsample.xlsx");

	std::cout << "OpeningCSVFilesWith executed successfully." << std::endl;

	Aspose::Cells::Cleanup();
	return 0;
}
```

### **Открытие текстовых файлов с пользовательским разделителем**

Текстовые файлы используются для хранения данных электронных таблиц без форматирования. Файл является своего рода обычным текстовым файлом, в котором могут быть использованы некоторые настраиваемые разделители.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input CSV file
    U16String filePath = srcDir + u"Book11.csv";

    // Instantiate Text File's LoadOptions
    TxtLoadOptions txtLoadOptions;

    // Specify the separator
    txtLoadOptions.SetSeparator(u',');

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath, txtLoadOptions);

    // Save file
    wb.Save(outDir + u"output.txt");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Открытие файлов с разделителем табуляции**

Файлы с разделителем табуляции (текстовые) содержат данные таблицы без форматирования. Данные расположены в строках и столбцах, как в таблицах и электронных таблицах. В основном, файл с разделителем табуляции является особым видом простого текстового файла с табулятором между столбцами.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions(LoadFormat::TabDelimited);

    // Create a Workbook object and open the file from its path
    Workbook wbTabDelimited(srcDir + u"Book1TabDelimited.txt", loadOptions);

    std::cout << "Tab delimited file opened successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Открытие файлов со значениями, разделенными табуляцией (TSV)**

Файлы с разделителями значений (TSV) содержат данные таблицы без форматирования. Это то же, что и файл с разделителем табуляции, где данные расположены в строках и столбцах, как в таблицах и электронных таблицах.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate LoadOptions specified by the LoadFormat
    LoadOptions loadOptions(LoadFormat::Tsv);

    // Create a Workbook object and open the file from its path
    Workbook workbook(srcDir + u"SampleTSVFile.tsv", loadOptions);

    // Using the Sheet 1 in Workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing a cell using its name
    Cell cell = worksheet.GetCells().Get(u"C3");

    // Output the cell name and value
    std::cout << "Cell Name: " << cell.GetName().ToUtf8() << " Value: " << cell.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Расширенные темы**
- [Загрузка или импорт CSV-файла с формулами](/cells/ru/cpp/load-or-import-csv-file-with-formulas/)
- [Чтение файла CSV с различными кодировками](/cells/ru/cpp/reading-csv-file-with-multiple-encodings/)
{{< app/cells/assistant language="cpp" >}}
