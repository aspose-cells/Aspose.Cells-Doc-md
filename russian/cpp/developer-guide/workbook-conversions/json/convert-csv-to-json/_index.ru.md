---
title: Преобразование CSV в JSON с помощью C++
linktitle: Преобразовать CSV в JSON
type: docs
weight: 220
url: /ru/cpp/convert-csv-to-json/
description: Преобразуйте CSV файл в JSON, используя простое API Aspose.Cells for C++.
keywords: Преобразование, Конвертация CSV в JSON, CSV в JSON, CSV, JSON, Преобразование CSV в JSON C++, код C++ для преобразования CSV в JSON
---

## **Преобразовать CSV в JSON**

Поддержка Aspose.Cells для преобразования CSV в JSON. Для этого API предоставляет классы [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) и [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) предоставляет опции для экспорта диапазона в JSON. Класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) содержит следующие свойства.

- [**GetExportAsString()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/getexportasstring/): Это экспортирует строковое значение ячеек в JSON.
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/gethasheaderrow/): Указывает, содержит ли диапазон строку заголовка.
- [**GetIndent()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/getindent/): Указывает отступ.

Класс [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) экспортирует JSON с использованием настроек экспорта, установленных через класс [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/).

Следующий пример кода демонстрирует использование классов [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/) и [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) для загрузки [исходного CSV-файла](104398879.csv) и вывода JSON в консоль.

### **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create load options for CSV format
    LoadOptions loadOptions(LoadFormat::Csv);

    // Load CSV file
    Workbook workbook(srcDir + u"SampleCsv.csv", loadOptions);

    // Get the last cell in the worksheet
    Cell lastCell = workbook.GetWorksheets().Get(0).GetCells().GetLastCell();

    // Set JsonSaveOptions
    JsonSaveOptions jsonSaveOptions;

    // Create a range from the first cell to the last cell
    Range range = workbook.GetWorksheets().Get(0).GetCells().CreateRange(0, 0, lastCell.GetRow() + 1, lastCell.GetColumn() + 1);

    // Export the range to JSON
    U16String data = JsonUtility::ExportRangeToJson(range, jsonSaveOptions);

    // Print JSON
    std::cout << data.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Вывод в консоль**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
