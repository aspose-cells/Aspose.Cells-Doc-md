---
title: Ordinamento dati con C++
linktitle: Ordinamento dei dati
type: docs
weight: 130
url: /it/cpp/sort-data-of-excel/
description: Impara come ordinare i dati usando l API Aspose.Cells for C++.
keywords: Ordina i dati in ordine ascendente o discendente, ordina i dati in base al colore di sfondo.
---

{{% alert color="primary" %}}

Il sorting dei dati è una delle molte utili funzionalità di Microsoft Excel. Consente agli utenti di ordinare i dati per renderli più facili da esaminare. Aspose.Cells consente ai programmatori di ordinare i dati del foglio di lavoro in ordine alfabetico o numerico, funzionante allo stesso modo di Microsoft Excel per ordinare i dati.

{{% /alert %}}

## **Ordinare i dati in Microsoft Excel**

Per ordinare i dati in Microsoft Excel:

1. Seleziona **Dati** dal menu **Ordina**. Verrà visualizzata la finestra di dialogo Ordina.
1. Seleziona un'opzione di ordinamento.

In genere, l'ordinamento viene eseguito su un elenco - definito come un gruppo contiguo di dati in cui i dati sono visualizzati in colonne.

## **Ordinare i dati con Aspose.Cells**

Aspose.Cells fornisce la classe [**DataSorter**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/) utilizzata per ordinare i dati in ordine ascendente o discendente. La classe ha alcuni membri importanti, ad esempio, proprietà come Key1 ... Key3 e Order1 ... Order3. Questi membri vengono utilizzati per definire le chiavi ordinate e specificare l'ordine di ordinamento della chiave.

È necessario definire le chiavi e impostare l'ordine di ordinamento prima di implementare l'ordinamento dei dati. La classe fornisce il metodo [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) utilizzato per eseguire l'ordinamento dei dati in base ai dati della cella in un foglio di lavoro.

Il metodo [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) accetta i seguenti parametri:

- [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), le celle per il foglio di lavoro sottostante.
- [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/), l'intervallo di celle. Definire l'area delle celle prima di applicare l'ordinamento dei dati.

Questo esempio utilizza il file di modello "Book1.xls" creato in Microsoft Excel. Dopo l'esecuzione del codice seguente, i dati vengono ordinati in modo appropriato.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the workbook datasorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Set the first order for datasorter object
    sorter.SetOrder1(SortOrder::Descending);

    // Define the first key
    sorter.SetKey1(0);

    // Set the second order for datasorter object
    sorter.SetOrder2(SortOrder::Ascending);

    // Define the second key
    sorter.SetKey2(1);

    // Create a cells area (range)
    CellArea ca = CellArea::CreateCellArea(0, 0, 13, 1);

    // Sort data in the specified data range (A1:B14)
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), ca);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Se si desidera ordinare *DaSinistraADestra*, utilizzare l'attributo [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortlefttoright/).

{{% /alert %}}

### **Ordinamento dati con il colore di sfondo**

Excel fornisce funzionalità per ordinare i dati in base al colore di sfondo. La stessa funzionalità viene fornita utilizzando Aspose.Cells utilizzando DataSorter dove [**SortOnType**](https://reference.aspose.com/cells/cpp/aspose.cells/sortontype/).CellColor può essere utilizzato in [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) per ordinare i dati in base al colore di sfondo. Tutte le celle che contengono il colore specificato nella [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/), sono posizionate in cima o in fondo in base all'impostazione di SortOrder e l'ordine delle altre celle non viene affatto cambiato.

Di seguito sono riportati i file di esempio che possono essere scaricati per testare questa funzionalità:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

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
    U16String inputFilePath = srcDir + u"CellsNet46500.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outputSortData_CustomSortList.xlsx";

    // Create a workbook object and load template file
    Workbook workbook(inputFilePath);

    // Instantiate data sorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Add key for second column for red color
    sorter.AddColorKey(1, SortOnType::CellColor, SortOrder::Descending, Color::Red());

    // Sort the data based on the key
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), CellArea::CreateCellArea(u"A2", u"C6"));

    // Save the output file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Ordina dati nella colonna con elenco di ordinamenti personalizzati](/cells/it/cpp/sort-data-in-column-with-custom-sort-list/)
- [Specifica dell'avviso di ordinamento durante l'ordinamento dei dati](/cells/it/cpp/specifying-sort-warning-while-sorting-data/)
