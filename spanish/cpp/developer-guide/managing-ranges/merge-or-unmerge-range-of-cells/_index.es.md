---
title: Combinar o deshacer la combinación de un rango de celdas con C++
linktitle: Combinar o dividir rango de celdas
type: docs
weight: 190
url: /es/cpp/merge-or-unmerge-range-of-cells/
description: Combina y descombina celdas en un rango en Excel con código en C++.
keywords: combinar y descombinar celdas en rangos en C++, combinar y descombinar celdas en rango, combinar y descombinar celdas en rango con C++, combinar y descombinar celdas en rango usando C++, combinar y descombinar celdas en Excel usando C++, combinar y descombinar celdas en Excel con C++, combinar y descombinar celdas en Excel en C++, combinar celdas en Excel en C++, descombinar celdas en Excel en C++, combinar celdas en rango con C++
---

{{% alert color="primary" %}}

Puede utilizar Aspose.Cells para combinar o dividir un rango de celdas. Aspose.Cells ofrece los métodos [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) y [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) para este propósito. Este artículo explica cómo combinar un rango de celdas en una sola celda.

{{% /alert %}}

## **Ejemplo**

El siguiente código de ejemplo primero crea un rango - A1:D4 - luego combina las celdas del rango en una sola usando el método [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/). De manera similar, puedes dividir celdas creando un rango y llamando al método [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/).

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
