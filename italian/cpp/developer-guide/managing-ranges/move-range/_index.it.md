---
title: Sposta l intervallo di celle in un foglio di lavoro con C++
linktitle: Sposta intervallo di celle in un foglio di lavoro
type: docs
weight: 370
url: /it/cpp/move-range-of-cells-in-a-worksheet/
description: Impara come spostare un intervallo di celle in un foglio di lavoro usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Questo articolo mostra come spostare un intervallo di celle in un foglio di lavoro.

{{% /alert %}}

## **Sposta Intervallo di Celle in un Foglio di Lavoro**
Il codice di esempio utilizza un file modello per dimostrare il compito.

**Il file di input**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

Si prega di vedere il file generato seguente con l'intervallo da A1:B5 spostato in C1:D5.

**Il file di output

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the workbook object. Open the Excel file
    U16String inputFilePath = u"book1.xlsx";
    Workbook workbook(inputFilePath);

    // Access the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create a range from A1 to B5
    Range range = cells.CreateRange(u"A1", u"B5");

    // Move the range to the right by 2 columns
    range.MoveTo(0, 2);

    Aspose::Cells::Cleanup();
}
```
