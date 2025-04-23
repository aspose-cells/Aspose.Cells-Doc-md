---
title: Ottieni la larghezza del testo del valore della cella con C++
linktitle: Ottieni larghezza testo del valore della cella
type: docs
weight: 50
url: /it/cpp/get-text-width-of-cell-value/
description: Impara come ottenere la larghezza del testo del valore della cella tramite l API Aspose.Cells for C++.
keywords: Ottieni la larghezza del testo del valore della cella, Ottieni la larghezza del testo del valore della cella
---

## **Ottieni larghezza testo del valore della cella**

A volte, gli sviluppatori potrebbero aver bisogno di calcolare la larghezza del valore della cella per organizzare i dati in un certo layout. Aspose.Cells fornisce il metodo [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) che consente agli sviluppatori di ottenere la larghezza del testo del valore della cella. Il seguente esempio illustra come usare [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) per accedere alla larghezza del testo del valore della cella.

Il file di origine utilizzato nello snippet di codice seguente è allegato per il tuo riferimento.

[File di origine](96928090.xlsx)

## Codice di esempio

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory path for source files
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from the specified Excel file
    Workbook workbook(sourceDir + u"GetTextWidthSample.xlsx");

    // Calculate the text width for the string value of cell A1
    double textWidth = CellsHelper::GetTextWidth(workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue(), workbook.GetDefaultStyle().GetFont(), 1);

    // Output the text width
    std::wcout << u"Text width: " << textWidth << std::endl;

    Aspose::Cells::Cleanup();
}
```
