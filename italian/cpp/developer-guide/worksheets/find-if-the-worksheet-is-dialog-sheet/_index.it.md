---
title: Trova se il Foglio del Foglio di Lavoro è un Foglio di Dialogo con C++
linktitle: Verificare se il foglio di lavoro è un foglio di dialogo
type: docs
weight: 90
url: /it/cpp/find-if-the-worksheet-is-dialog-sheet/
description: Il Foglio di Dialogo è un vecchio formato di foglio. Questo articolo fornisce istruzioni e codice esempio per determinare programmaticamente se un foglio di Excel è un Foglio di Dialogo utilizzando l API C++.
keywords: trova tipo dialogo foglio excel c++, foglio dialogo c++
---

## **Possibili Scenari di Utilizzo**

Il foglio di dialogo è un vecchio formato di foglio che contiene una finestra di dialogo. Tale foglio potrebbe essere stato inserito da una versione precedente di Microsoft Excel, ad esempio la versione 2003 come mostrato in questa schermata. Può anche essere inserito con VBA nelle nuove versioni, ad esempio Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Puoi scoprire se il foglio è un foglio di dialogo o un altro tipo di foglio con la proprietà [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) fornita da Aspose.Cells. Se restituisce il valore della enumerazione [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) allora significa che stai trattando con un foglio di dialogo.

## **Trova se il foglio di lavoro è un foglio di dialogo**

Il seguente esempio carica il [file Excel di esempio](64716820.xlsx) che contiene un foglio di dialogo. Controlla la proprietà [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) la confronta con [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) e quindi stampa il messaggio. Si prega di consultare l'output della console del codice esempio di seguito per ulteriori assistenza.

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load Excel file containing Dialog Sheet
    Workbook workbook(u"sampleFindIfWorksheetIsDialogSheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Find if the sheet type is dialog and print the message
    if (ws.GetType() == SheetType::Dialog)
    {
        std::cout << "Worksheet is a Dialog Sheet." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **Output della console**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
