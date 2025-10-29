---
title: Применение эффектов индексного и подстрочного знаков на шрифтах с C++
linktitle: Применение эффектов надстрочного и подстрочного индексов к шрифтам
type: docs
weight: 80
url: /ru/cpp/apply-superscript-and-subscript-effects-on-fonts/
description: Код на C++, применяющий эффект индексного и подстрочного знаков к тексту в Excel с помощью API Aspose.Cells for C++.
keywords: excel superscript c++, excel subscript c++, excel superscript and subscript c++, вставка подстрочного и индексного знаков в Excel c++, добавление подстрочного и индексного в Excel c++, добавление суперкритического и подстрочного знаков в Excel c++, добавление индексных и подстрочных знаков в Excel c++
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет возможность применять эффекты надстрочного (текст над базовой линией) и подстрочного (текст под базовой линией) к тексту.

{{% /alert %}}

## **Работа с надстрочным и подстрочным индексами**

Примените эффект надстрочного, установив свойство [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) объекта [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) в значении **true**. Для применения подстрочного установите свойство [**IsSubscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) объекта [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) в значении **true**.

Приведенные ниже примеры кода показывают, как применить надстрочный и подстрочный текст.

### C++ код для применения эффекта индексного знака к тексту

```cpp
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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Setting the font Superscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSuperscript(true);
    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"Superscript_out.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully with superscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### C++ код для применения эффекта подстрочного знака к тексту

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Set the font Subscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSubscript(true);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"Subscript_out.xls", SaveFormat::Auto);

    std::cout << "File saved successfully with subscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
