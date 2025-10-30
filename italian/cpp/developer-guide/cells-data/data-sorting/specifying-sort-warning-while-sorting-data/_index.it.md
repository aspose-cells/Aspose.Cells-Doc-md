---
title: Specificare avviso di ordinamento durante l ordinamento dei dati con C++
linktitle: Specificare avviso di ordinamento durante l ordinamento dei dati
type: docs
weight: 140
url: /it/cpp/specifying-sort-warning-while-sorting-data/
description: Scopri come specificare un avviso di ordinamento durante l ordinamento dei dati usando l API Aspose.Cells for C++.
keywords: Aggiungi avviso di ordinamento durante l ordinamento dei dati, imposta l avviso di ordinamento durante l ordinamento dei dati, seleziona l avviso di ordinamento durante l ordinamento dei dati.
---

## **Possibili Scenari di Utilizzo**

Si prega di considerare questi dati testuali, cioè {11, 111, 22}. Questi dati testuali sono ordinati perché, in termini di testo, 111 viene prima di 22. Ma, se si desidera ordinare questi dati non come testo ma come numeri, diventeranno {11, 22, 111} perché numericamente 111 viene dopo 22. Aspose.Cells fornisce la proprietà {0} per gestire questo problema. Si prega di impostare questa proprietà su **true** e i vostri dati testuali verranno ordinati come dati numerici. La seguente schermata mostra l'avviso di ordinamento mostrato da Microsoft Excel quando i dati testuali che sembrano dati numerici vengono ordinati.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Codice di Esempio**

Il seguente codice di esempio illustra l'uso della proprietà [**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortasnumber/) come spiegato in precedenza. Si prega di controllare il [file di esempio Excel](43352075.xlsx) e l' [output Excel file](43352076.xlsx) per ulteriori informazioni.

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

    // Create workbook
    Workbook workbook(srcDir + u"sampleSortAsNumber.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create cell area
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A20");

    // Create data sorter
    DataSorter sorter = workbook.GetDataSorter();

    // Find the index of column A
    int idx = CellsHelper::ColumnNameToIndex(u"A");

    // Add key in sorter for sorting in ascending order
    sorter.AddKey(idx, SortOrder::Ascending);
    sorter.SetSortAsNumber(true);

    // Perform sort
    sorter.Sort(worksheet.GetCells(), ca);

    // Save the output workbook
    workbook.Save(outDir + u"outputSortAsNumber.xlsx");

    std::cout << "Sorting completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
