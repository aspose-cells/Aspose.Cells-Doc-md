---
title: Zusammenführen oder Trennen des Bereichs von Zellen mit C++
linktitle: Bereich von Zellen zusammenführen oder trennen
type: docs
weight: 190
url: /de/cpp/merge-or-unmerge-range-of-cells/
description: Zellen in einem Bereich in Excel mit C++ Code zusammenführen und trennen.
keywords: C++ Zellen in einem Bereich zusammenführen und trennen, C++ Zellen in einem Bereich zusammenführen und trennen, Zellen in einem Bereich mit C++ zusammenführen und trennen, Zellen in einem Bereich mit C++ zusammenführen und trennen, Zellen in Excel mit C++ zusammenführen und trennen, Zellen in Excel mit C++, C++ Zellen in Excel zusammenführen und trennen, C++ Zellen in Excel zusammenführen, C++ Zellen in Excel trennen, Zellen in einem Bereich mit C++ zusammenführen
---

{{% alert color="primary" %}}

Sie können Aspose.Cells verwenden, um einen Bereich von Zellen zusammenzuführen oder aufzuteilen. Aspose.Cells bietet die Methoden [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) und [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) für diesen Zweck. Dieser Artikel erklärt, wie Sie einen Bereich von Zellen in eine einzige Zelle zusammenführen können.

{{% /alert %}}

## **Beispiel**

Der folgende Beispielcode erstellt zuerst einen Bereich - A1:D4 - und führt dann die Zellen im Bereich mit der [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/)-Methode zusammen. Ebenso können Sie Zellen aufteilen, indem Sie einen Bereich erstellen und die [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/)-Methode aufrufen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of output excel file
    U16String outputPath = srcDir + u"output.out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range
    Range range = worksheet.GetCells().CreateRange(u"A1:D4");

    // Merge range into a single cell
    range.Merge();

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
