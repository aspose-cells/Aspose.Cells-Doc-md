---
title: Adatta automaticamente righe e colonne con C++
linktitle: Adatta automaticamente righe e colonne
type: docs
weight: 20
url: /it/cpp/autofit-rows-and-columns/
description: Questo articolo mostra come adattare automaticamente righe, colonne, righe di celle unite e righe in un intervallo di celle utilizzando l API Aspose.Cells for C++.
keywords: Autoadatta righe, autoadatta colonne, autoadatta righe in un intervallo di celle, autoadatta righe di celle unite
---

{{% alert color="primary" %}}

Microsoft Excel permette agli utenti di adattare automaticamente la larghezza e l'altezza delle celle in base al loro contenuto. Questa funzione è disponibile anche tramite Aspose.Cells, in modo che gli sviluppatori possano adattare automaticamente le dimensioni di una cella durante l'esecuzione.

{{% /alert %}}

## **Adattamento automatico**

Aspose.Cells fornisce una classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che permette l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) offre un'ampia gamma di metodi per gestire un foglio di lavoro. Questo articolo esplora l'uso della classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) per adattare automaticamente righe o colonne.

### **Adatta automaticamente la riga - Semplice**

L'approccio più semplice per adattare automaticamente la larghezza e l'altezza di una riga è chiamare il metodo [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) della classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Il metodo [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) accetta come parametro un indice di riga (della riga da ridimensionare).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fit the 2nd row (index 1) of the worksheet
    worksheet.AutoFitRow(1);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Come adattare automaticamente la riga in un intervallo di celle**

Una riga è composta da molte colonne. Aspose.Cells permette agli sviluppatori di adattare automaticamente una riga in base al contenuto in un intervallo di celle all'interno della riga chiamando una versione sovraccaricata del metodo [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/). Prende i seguenti parametri:

- **Indice riga**, l'indice della riga da adattare automaticamente.
- **Primo indice colonna**, l'indice della prima colonna della riga.
- **Ultimo indice colonna**, l'indice dell'ultima colonna della riga.

Il metodo [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) verifica i contenuti di tutte le colonne della riga e quindi la adatta automaticamente.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fitting the 3rd row of the worksheet
    worksheet.AutoFitRow(1, 0, 5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Come adattare automaticamente la colonna in un intervallo di celle**

Una colonna è composta da molte righe. È possibile adattare automaticamente una colonna in base ai contenuti in un intervallo di celle della colonna chiamando una versione sovraccaricata del metodo [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) che prende i seguenti parametri:

- **Indice colonna**, l'indice della colonna da adattare automaticamente.
- **Primo indice riga**, l'indice della prima riga della colonna.
- **Ultimo indice di riga**, l'indice dell'ultima riga della colonna.

Il metodo [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) verifica i contenuti di tutte le righe nella colonna e quindi adatta automaticamente la colonna.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fit the 5th column (index 4) from row 4 to 6
    worksheet.AutoFitColumn(4, 4, 6);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Come adattare automaticamente le righe per le celle unite**

Con Aspose.Cells, è possibile adattare automaticamente le righe anche per celle unite utilizzando l'API [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/). La classe [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) fornisce la proprietà [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) che può essere usata per adattare automaticamente le righe delle celle unite. [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) accetta l'enumerazione [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitmergedcellstype/), che presenta i seguenti membri:

- Nessuno: Ignora le celle unite.
- PrimaLinea: espande solo l'altezza della prima riga.
- UltimaLinea: espande solo l'altezza dell'ultima riga.
- OgniLinea: espande solo l'altezza di ogni riga.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first (default) worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Create a range A1:B1
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 2);

    // Merge the cells
    range.Merge();

    // Insert value to the merged cell A1
    worksheet.GetCells().Get(0, 0).SetValue(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

    // Create a style object
    Style style = worksheet.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style.SetIsTextWrapped(true);

    // Apply the style to the cell
    worksheet.GetCells().Get(0, 0).SetStyle(style);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options;

    // Set auto-fit for merged cells
    options.SetAutoFitMergedCellsType(AutoFitMergedCellsType::EachLine);

    // Autofit rows in the sheet (including the merged cells)
    worksheet.AutoFitRows(options);

    // Save the Excel file
    wb.Save(outDir + u"AutofitRowsforMergedCells.xlsx");

    std::cout << "Autofit rows for merged cells completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Puoi anche provare a utilizzare le versioni sovraccaricate dei metodi [**AutoFitRows**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrows/) e [**AutoFitColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumns/) che accettano un intervallo di righe/colonne e un'istanza di [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) per adattare automaticamente le righe/colonne selezionate con i tuoi [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) desiderati.

Le firme dei metodi sopra indicati sono le seguenti:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)

{{% /alert %}}

## **Importante sapere**

{{% alert color="primary" %}}

Se una cella è unita, i metodi AutoFit non verranno applicati, il che è lo stesso comportamento di Microsoft Excel. Puoi ovviare a questo usando l'API di filtro automatico. Inoltre, se il testo di una cella è avvolto, il metodo [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) non verrà applicato. Un'altra cosa importante da sapere è che i metodi *AutoFit* sono dispendiosi in termini di tempo. Pertanto, dovresti chiamare questi metodi il meno possibile per garantire l'efficienza della tua applicazione.

{{% /alert %}}

## **Argomenti Avanzati**
- [Adattare automaticamente le righe per le celle unite](/cells/it/cpp/autofit-rows-for-merged-cells/)
