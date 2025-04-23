---
title: Zellen mit spezifischem Stil mit C++ finden
linktitle: Zellen mit bestimmtem Stil finden
type: docs
weight: 190
url: /de/cpp/find-cells-with-specific-style/
description: Erfahren Sie, wie Sie Zellen mit einem bestimmten Stil mithilfe der API Aspose.Cells for C++ suchen oder finden.
keywords: Zellen mit einem bestimmten angewendeten Stil finden, Zellen mit einem bestimmten Stil suchen
---

{{% alert color="primary" %}}

Manchmal müssen Sie Zellen mit einem bestimmten angewendeten Stil finden. Sie können Aspose.Cells verwenden, um alle Zellen mit einem gemeinsamen Stil zu finden. Aspose.Cells bietet die [**FindOptions.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/getstyle/) Eigenschaft, die Sie verwenden können, um den Stil anzugeben, nach dem Zellen gesucht werden sollen.

{{% /alert %}}

Der Code in diesem Beispiel sucht alle Zellen, die denselben Stil wie die Zelle A1 haben. Nachdem der Code ausgeführt wurde, enthalten alle Zellen, die denselben Stil wie A1 haben, den Text "Gefunden".

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"TestBook.xlsx";

    Workbook workbook(filePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    FindOptions options;
    options.SetStyle(style);

    Cell nextCell;

    do
    {
        nextCell = worksheet.GetCells().Find(U16String(), nextCell, options);
        if (nextCell.GetRow() == -1)
            break;
        nextCell.PutValue(u"Found");
    } while (true);

    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
