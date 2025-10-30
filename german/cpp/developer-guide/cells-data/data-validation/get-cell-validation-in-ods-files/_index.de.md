---
title: Zellvalidierung in ODS Dateien mit C++ abrufen
linktitle: Zellvalidierung in ODS Dateien erhalten.
type: docs
weight: 180
url: /de/cpp/get-cell-validation-in-ods-files/
description: Erfahren Sie, wie Sie die Zellvalidierung in ODS Dateien mit der API Aspose.Cells for C++ erhalten.
keywords: Zellvalidierung abrufen, Zellvalidierung erhalten 
---

## **Zellvalidierung in ODS-Dateien erhalten**

Mit Aspose.Cells for C++ können Sie die auf eine Zelle in ODS-Dateien angewendete Validierung erhalten. Die API bietet die [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) Methode der [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) Klasse an.

Das folgende Codebeispiel zeigt, wie die [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) Methode verwendet wird, indem die [Quell-ODS](101089354.ods) Datei geladen und die Validierung der Zelle A9 ausgelesen wird.

### **Beispielcode**

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
