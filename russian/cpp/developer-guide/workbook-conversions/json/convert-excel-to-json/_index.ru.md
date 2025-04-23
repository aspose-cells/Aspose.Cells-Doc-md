---
title: Преобразование Excel в JSON с помощью C++
linktitle: Преобразование Excel в JSON
type: docs
weight: 300
url: /ru/cpp/convert-excel-to-json/
description: Узнайте, как преобразовать файл Excel в JSON с помощью Aspose.Cells и C++.
keywords: Экспорт рабочей книги в формат JSON без использования office 2013, office 2016, office 2019 и office 365
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает конвертацию рабочей книги в файл JSON (JavaScript Object Notation).

{{% /alert %}}

## **Конвертировать книгу Excel в JSON**

Не нужно гадать, как преобразовать рабочую книгу Excel в JSON, потому что библиотека Aspose.Cells for C++ предоставляет лучшее решение. API Aspose.Cells поддерживает преобразование таблиц в формат JSON. Чтобы экспортировать рабочую книгу в JSON, передайте [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) как второй параметр метода [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) для задания дополнительных настроек при экспорте листа в JSON.

Следующий пример показывает экспорт рабочей книги Excel в JSON. Ознакомьтесь с кодом для преобразования [исходного файла](sample.xlsx) в JSON, созданный этим кодом.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"sample.xlsx");
    Workbook workbook(inputFilePath);

    // Convert the workbook to JSON file.
    U16String outputFilePath(u"sample_out.json");
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Следующий пример, использующий класс JsonSaveOptions для задания дополнительных настроек, демонстрирует экспорт рабочей книги Excel в JSON. Ознакомьтесь с кодом для преобразования [исходного файла](sample.xlsx) в JSON, созданный этим кодом.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an options of saving the file.
    JsonSaveOptions options;

    // Set the exporting range.
    options.SetExportArea(CellArea::CreateCellArea(u"B1", u"C4"));

    // Load your source workbook
    Workbook workbook(u"sample.xlsx");

    // Convert the workbook to json file.
    workbook.Save(u"sample_out.json", options);

    std::cout << "Workbook successfully converted to JSON!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

