---
title: Ordinare i dati in una colonna con elenco di ordinamento personalizzato con C++
linktitle: Ordina i dati in una colonna con un elenco di ordinamento personalizzato
type: docs
weight: 290
url: /it/cpp/sort-data-in-column-with-custom-sort-list/
description: Scopri come ordinare i dati nella colonna usando un elenco personalizzato con l API Aspose.Cells for C++.
keywords: Ordina i dati nella colonna con un elenco di ordinamento personalizzato, Ordina i dati per elenco personalizzato.
---

## **Possibili Scenari di Utilizzo**

Puoi ordinare i dati nella colonna usando un elenco personalizzato. Questo può essere fatto usando il metodo [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/). Tuttavia, questo metodo funziona solo se gli elementi nell'elenco personalizzato non contengono virgole. Se contengono virgole come "USA,US", "Cina,CN" ecc., allora devi usare il metodo [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/). Qui, l'ultimo parametro non è una String ma un Array di Stringhe.

## **Ordina dati nella colonna con elenco di ordinamenti personalizzati**

Il seguente esempio di codice spiega come utilizzare il metodo [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) per ordinare i dati con un elenco di ordinamento personalizzato. Si prega di vedere il [file Excel di esempio](50528327.xlsx) usato in questo codice e il [file Excel di output](50528328.xlsx) generato da esso. La seguente schermata mostra l'effetto del codice sul file Excel di esempio all'esecuzione.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Codice di Esempio**

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

    // Load the source Excel file
    Workbook wb(srcDir + u"sampleSortData_CustomSortList.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify cell area - sort from A1 to A40
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A40");

    // Create Custom Sort list
    Vector<U16String> customSortList = { u"USA,US", u"Brazil,BR", u"China,CN", u"Russia,RU", u"Canada,CA" };

    // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
    wb.GetDataSorter().AddKey(0, SortOrder::Ascending, customSortList);
    wb.GetDataSorter().Sort(ws.GetCells(), ca);

    // Save the output Excel file
    wb.Save(outDir + u"outputSortData_CustomSortList.xlsx");

    std::cout << "Data sorted successfully with custom sort list!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
