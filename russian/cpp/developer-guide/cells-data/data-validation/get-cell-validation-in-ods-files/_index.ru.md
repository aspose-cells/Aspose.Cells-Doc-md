---
title: Получить проверку данных ячейки в файлах ODS с помощью C++
linktitle: Получить проверку ячейки в файлах ODS
type: docs
weight: 180
url: /ru/cpp/get-cell-validation-in-ods-files/
description: Узнайте, как получить проверку данных ячейки в файлах ODS с помощью API Aspose.Cells for C++.
keywords: Получение проверки ячейки, Получение проверки ячейки 
---

## **Получить проверку ячейки в файлах ODS**

С помощью API Aspose.Cells for C++ можно получить примененную проверку к ячейке в файлах ODS. API предоставляет метод [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Следующий пример демонстрирует использование метода [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/), загружая [исходный файл ODS](101089354.ods) и читаюа проверку ячейки A9.

### **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    U16String inputFilePath = srcDir + u"SampleBook1.ods";
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access cell A9
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(U16String(u"A9"));

    // Check validation existence
    Validation validation = cell.GetValidation();
    if (validation.IsNull() == false)
    {
        std::cout << "Validation type: " << static_cast<int>(validation.GetType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
