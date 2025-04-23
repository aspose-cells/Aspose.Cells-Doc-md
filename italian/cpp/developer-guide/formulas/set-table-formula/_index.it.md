---
title: Propagare automaticamente le formule in tabella o oggetto elenco durante l inserimento di nuovi dati con C++
linktitle: Imposta la formula tabella
type: docs
weight: 260
url: /it/cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Impara come propagare automaticamente le formule in tabelle o oggetti elenco quando inserisci nuovi dati usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**
A volte, desideri che una formula nel tuo tabella o oggetto elenco si propaghino automaticamente nelle nuove righe mentre inserisci nuovi dati. Questo è il comportamento predefinito di Microsoft Excel. Per ottenere la stessa funzionalità con Aspose.Cells, usa il metodo [ListColumn::GetFormula](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listcolumn/getformula/).

## **Propagare la formula nella tabella o nell'oggetto elenco automaticamente durante l'inserimento dei dati nelle nuove righe**
Il codice di esempio seguente crea una Tabella o Oggetto Elenco in modo che la formula nella colonna B si propaghi automaticamente alle nuove righe quando inserisci nuovi dati. Verifica il [file Excel generato](5115469.xlsx) con questo codice. Se inserisci un numero nella cella A3, vedrai che la formula nella cella B2 si propaga automaticamente nella cella B3.

```c++
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

    // Create workbook object
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add column headings in cell A1 and B1
    sheet.GetCells().Get(0, 0).PutValue(u"Column A");
    sheet.GetCells().Get(0, 1).PutValue(u"Column B");

    // Add list object, set its name and style
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(0, 0, 1, sheet.GetCells().GetMaxColumn(), true));
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium2);
    listObject.SetDisplayName(u"Table");

    // Set the formula of second column so that it propagates to new rows automatically while entering data
    listObject.GetListColumns().Get(1).SetFormula(u"=[Column A] + 1");

    // Save the workbook in xlsx format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
