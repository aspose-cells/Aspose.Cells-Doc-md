---
title: Calcola le formule con C++
linktitle: Calcola le formule
description: Questo articolo introduce come usare la libreria Aspose.Cells per calcolare le formule in Microsoft Excel con C++. Caricando un file Excel esistente o creando un nuovo file, possiamo usare i metodi forniti da Aspose.Cells per calcolare la formula e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, formule, calcoli, Calcolo Diretto della Formula, Calcola le formule ripetutamente, aggiungi formule.
type: docs
weight: 125
url: /it/cpp/calculate-formulas/
---

## **Aggiungere Formule & Calcolare i Risultati**

Aspose.Cells ha un motore di calcolo formule integrato. Non solo può ricalcolare le formule importate da modelli di progettazione, ma supporta anche il calcolo dei risultati delle formule aggiunte in runtime.

Aspose.Cells supporta la maggior parte delle formule o funzioni che fanno parte di Microsoft Excel (Leggi [una lista delle funzioni supportate dal motore di calcolo](/cells/it/cpp/supported-formula-functions/)). Queste funzioni possono essere usate tramite API o fogli di lavoro di progettazione. Aspose.Cells supporta un vasto insieme di formule matematiche, stringa, booleane, data/ora, statistiche, database, ricerca e riferimento.

Usa la proprietà [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/) o i metodi [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) per aggiungere una formula a una cella. Quando applichi una formula, inizia sempre la stringa con un segno di uguale (=) come quando crei una formula in Microsoft Excel e usa una virgola (,) per delimitare i parametri della funzione.

Per calcolare i risultati delle formule, l'utente può chiamare il metodo [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) della classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che elabora tutte le formule incorporate in un file Excel. Oppure, può chiamare il metodo [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) della classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/), che elabora tutte le formule incorporate in un foglio. Oppure, può chiamare anche il metodo [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), che elabora la formula di una singola Cell:

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add values to cells
    worksheet.GetCells().Get(u"A1").PutValue(1);
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(3);

    // Add a SUM formula to cell A4
    worksheet.GetCells().Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Calculate the results of formulas
    workbook.CalculateFormula();

    // Get the calculated value of cell A4
    U16String value = worksheet.GetCells().Get(u"A4").GetStringValue();

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Importante da Sapere per le Formule**

{{% alert color="primary" %}}

La proprietà **GetFormula** e i metodi **SetFormula(...)** della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) funzionano in modo diverso dai metodi **Calculate** delle classi [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) e [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). La proprietà **GetFormula** e i metodi **SetFormula(...)** aggiungono semplicemente la formula a una cella ma non calcolano il risultato in runtime. Per ottenere il risultato delle formule, chiama i metodi **Calculate**.

{{% /alert %}}

## **Calcolo Diretto della Formula**

Aspose.Cells dispone di un motore di calcolo delle formule integrato. Oltre a calcolare le formule importate da un file del progettista, Aspose.Cells può calcolare direttamente i risultati delle formule.

A volte, hai bisogno di calcolare i risultati delle formule direttamente senza aggiungerle a un foglio di calcolo. I valori delle celle usate nella formula esistono già in un foglio di calcolo, e tutto ciò che devi fare è trovare il risultato di quei valori in base a una formula di Microsoft Excel senza aggiungere la formula in un foglio.

Puoi usare le API del motore di calcolo formule di Aspose.Cells per [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) a [**calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) calcolare i risultati di tali formule senza aggiungerle al foglio:

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

    // Create a workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put 20 in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.PutValue(20);

    // Put 30 in cell A2
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.PutValue(30);

    // Calculate the Sum of A1 and A2
    Aspose::Cells::Object results = worksheet.CalculateFormula(u"=Sum(A1:A2)");

    // Print the output
    std::cout << "Value of A1: " << cellA1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Value of A2: " << cellA2.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Result of Sum(A1:A2): " << results.ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

Il codice sopra produce il seguente output:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Come calcolare le formule ripetutamente**

Quando ci sono molte formule nel workbook e l'utente ha bisogno di calcolarle ripetutamente modificando solo una piccola parte di esse, può essere utile per le prestazioni abilitare la catena di calcolo delle formule: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getenablecalculationchain/).

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the template workbook
    Workbook workbook(srcDir + u"book1.xls");

    // Print the time before formula calculation
    auto start = std::chrono::system_clock::now();
    std::time_t start_time = std::chrono::system_clock::to_time_t(start);
    std::cout << "Start time: " << std::ctime(&start_time);

    // Set the CreateCalcChain as true
    workbook.GetSettings().GetFormulaSettings().SetEnableCalculationChain(true);

    // Calculate the workbook formulas
    workbook.CalculateFormula();

    // Print the time after formula calculation
    auto end = std::chrono::system_clock::now();
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    std::cout << "End time: " << std::ctime(&end_time);

    // Change the value of one cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"newvalue");

    // Re-calculate those formulas which depend on cell A1
    workbook.CalculateFormula();

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Importante sapere**

{{% alert color="primary" %}}

Per impostazione predefinita, la catena di calcolo è disattivata. Poiché la creazione della catena richiede anche tempo extra, la prima volta che si calcolano le formule ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)) potrebbe richiedere più tempo di elaborazione CPU e memoria rispetto al calcolo delle formule senza catena. Se l'utente non ha bisogno di calcolare le formule ripetutamente, il comportamento predefinito (calcolare la formula direttamente senza creare una catena di calcolo) dovrebbe essere l'opzione migliore.

{{% /alert %}}

## **Argomenti Avanzati**
- [Aggiungere celle alla finestra di visualizzazione della formula di Microsoft Excel](/cells/it/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calcolare la funzione IFNA utilizzando Aspose.Cells](/cells/it/cpp/calculating-ifna-function-using-aspose-cells/)
- [Calcolo della formula matriciale delle tabelle dei dati](/cells/it/cpp/calculation-of-array-formula-of-data-tables/)
- [Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016](/cells/it/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Ridurre il tempo di calcolo del metodo Cell.Calculate](/cells/it/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementare un motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Restituzione di un intervallo di valori utilizzando AbstractCalculationEngine](/cells/it/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Impostare la modalità di calcolo della formula del foglio di lavoro](/cells/it/cpp/setting-formula-calculation-mode-of-workbook/)
- [Utilizzo della funzione FormulaText in Aspose.Cells](/cells/it/cpp/using-formulatext-function-in-aspose-cells/)
