--- 
title: Come controllare lo stato di congelamento senza Excel con C++ 
linktitle: Stato congelato 
type: docs 
weight: 190 
url: /it/cpp/how-to-check-frozen-state-of-excel-worksheet 
description: In questo articolo imparerai come verificare lo stato di congelamento di un foglio di lavoro Excel programmando con C++ utilizzando l API Aspose.Cells. 
--- 

## **Introduzione** 

In questo articolo, impareremo come verificare lo stato di congelamento di un foglio di lavoro Excel tramite programmazione. È semplice capire se il foglio è congelato o diviso in MS Excel. Ma c'è un modo per determinare se è congelato o diviso con C++? Possiamo farlo con Aspose.Cells for C++. 

## **Le riquadri della finestra sono congelati** 
Con Aspose.Cells for C++, possiamo verificare se la finestra è congelata e quante righe e colonne sono bloccate. 

Usa la proprietà [**GetPaneState()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getpanestate/) per controllare lo stato delle ante di finestra e ottenere righe e colonne bloccate con il metodo [**Worksheet::GetFreezedPanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getfreezedpanes/). 
1. Costruire il Workbook per aprire il file. 
2. Verificare se il foglio di lavoro è congelato. 
3. Ottieni le righe e le colonne bloccate. 

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create the workbook from the specified file
    Workbook workbook(u"Frozen.xlsx");

    // Get the first worksheet from the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Check whether the worksheet is frozen
    if (sheet.GetPaneState() == PaneStateType::Frozen || sheet.GetPaneState() == PaneStateType::FrozenSplit)
    {
        int32_t row = 0, column = 0;
        int32_t rows = 0, columns = 0;

        // Get the locked rows and columns
        sheet.GetFreezedPanes(row, column, rows, columns);

        // Output the details if needed (just for demonstration)
        std::cout << "Frozen panes at Row: " << row << ", Column: " << column << ", Total Frozen Rows: " 
                  << rows << ", Total Frozen Columns: " << columns << std::endl;
    }

    Aspose::Cells::Cleanup();
}
``` 

{{< app/cells/assistant language="cpp" >}}
