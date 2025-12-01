---
title: Get Cell Validation in ODS Files with C++
linktitle: Get Cell Validation in ODS Files
type: docs
weight: 180
url: /cpp/get-cell-validation-in-ods-files/
description: Learn how to Get Cell Validation in ODS Files using Aspose.Cells for C++.
keywords: Get Cell Validation, Obtain Cell Validation 
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Get Cell Validation in ODS Files**

With Aspose.Cells for C++, you can get the validation applied to a cell in ODS files. The API provides the [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) method of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class.

The following code sample demonstrates using the [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) method by loading the [source ODS](101089354.ods) file and reading the validation of cell A9.

### **Sample Code**

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
