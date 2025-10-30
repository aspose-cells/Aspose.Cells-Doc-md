---
title: Inserire o eliminare righe in un foglio di lavoro Excel con C++
linktitle: Inserire o eliminare righe
type: docs
weight: 20
url: /it/cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Questo articolo fornisce il codice C++ per inserire ed eliminare righe in un foglio di lavoro Excel.
keywords: Inserisci o elimina righe in C++ in un foglio di lavoro excel, inserisci o elimina righe in Excel con C++, inserisci righe in Excel con C++, elimina righe in Excel con C++
---

{{% alert color="primary" %}}

Quando si crea un nuovo foglio di lavoro, o si lavora con un foglio di lavoro esistente, potresti aver bisogno di aggiungere righe o colonne aggiuntive per ospitare i dati. Altre volte, potresti dover eliminare righe o colonne da posizioni specifiche nel foglio di lavoro.

{{% /alert %}}

Aspose.Cells offre due metodi per inserire ed eliminare righe: [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) e [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/). Questi metodi sono ottimizzati per le prestazioni e svolgono il lavoro molto rapidamente.

Per inserire o rimuovere un numero di righe, ti consigliamo di utilizzare sempre i metodi [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) e [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) invece di usare i metodi [**Cells.InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) o [**DeleteRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterow/) in un loop.

Aspose.Cells funziona allo stesso modo di Microsoft Excel. Quando vengono aggiunte righe o colonne, i contenuti del foglio di lavoro vengono spostati verso il basso e verso destra. Quando vengono rimosse righe o colonne, i contenuti del foglio di lavoro vengono spostati verso l'alto o verso sinistra. Eventuali riferimenti in altri fogli di lavoro e celle vengono aggiornati quando vengono aggiunte o rimosse righe.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_book1.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows at row index 2 (insertion starts at 3rd row)
    sheet.GetCells().InsertRows(2, 10);

    // Delete 5 rows now. (8th row - 12th row)
    sheet.GetCells().DeleteRows(7, 5);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted and deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
