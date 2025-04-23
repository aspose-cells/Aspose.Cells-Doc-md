---
title: Crea, accedi e copia intervalli nominati con C++
linktitle: Crea, accedi e copia intervalli nominati
type: docs
weight: 200
url: /it/cpp/create-access-and-copy-named-ranges/
description: Impara come creare, accedere e copiare intervalli nominati nei file Excel usando Aspose.Cells con C++.
---

## **Introduzione**

Normalmente, le etichette di colonna e riga vengono usate per riferirsi a celle individuali. È possibile creare nomi descrittivi per rappresentare celle, intervalli di celle, formule o valori costanti. La parola **nome** può riferirsi a una sequenza di caratteri che rappresenta una cella, un intervallo di celle, una formula o un valore costante. Assegnare un nome a un intervallo significa che quell'intervallo di celle può essere chiamato con il suo nome. Usa nomi facili da capire, come Prodotti, per riferirti a intervalli difficili da interpretare, come Vendite!C20:C30. Le etichette possono essere usate in formule che si riferiscono ai dati sullo stesso foglio di lavoro; se vuoi rappresentare un intervallo su un altro foglio, puoi usare un nome. *Gli intervalli nominati sono tra le caratteristiche più potenti di Microsoft Excel, specialmente quando usati come intervallo di origine per controlli elenco, tabelle pivot, grafici, ecc.

## **Lavorare con l'intervallo con nome usando Microsoft Excel**

### **Creare intervalli con nome**

I passaggi seguenti descrivono come denominare una cella o un intervallo di celle usando **MS Excel**. Questo metodo si applica a **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000**, e **2002**.

1. Seleziona la cella o l'intervallo di celle che vuoi denominare.
1. Fai clic sulla **Casella di nome** all'estremità sinistra della barra della formula.
1. Digita il nome delle celle.
1. Premi INVIO.

{{% alert color="primary" %}}

Non è possibile nominare una cella mentre si sta modificando il contenuto della cella.

{{% /alert %}}

## **Lavorare con l'intervallo nominato utilizzando Aspose.Cells**

Qui, utilizziamo l'API Aspose.Cells per svolgere il compito.
Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che permette l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

### **Creare intervallo nominato**

È possibile creare un intervallo nominato chiamando il metodo sovraccarico [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) della raccolta [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Una versione tipica del metodo [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) prende i seguenti parametri:

- Nome della cella in alto a sinistra, il nome della cella in alto a sinistra nell'intervallo.
- Nome della cella in basso a destra, il nome della cella in basso a destra nell'intervallo.

Quando il metodo [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) è chiamato, restituisce il nuovo intervallo creato come un'istanza della classe [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). Utilizzare questo oggetto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) per configurare l'intervallo nominato. Ad esempio, impostare il nome dell'intervallo utilizzando la proprietà [**GetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getname/). L'esempio seguente mostra come creare un intervallo nominato di celle che si estende da B4:G14.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating a named range
    Range range = worksheet.GetCells().CreateRange(u"B4", u"G14");

    // Setting the name of the named range
    range.SetName(u"TestRange");

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Named range created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Inserimento dei dati nelle celle dell'intervallo nominato**

È possibile inserire dati nelle singole celle di un intervallo seguendo lo schema:

- **C++**: Range(riga, colonna)

Supponi di avere un intervallo di celle chiamato che si estende da A1 a C4. La matrice comprende 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte sequenzialmente: Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).

Usa le seguenti proprietà per identificare le celle nell'intervallo:

- FirstRow restituisce l'indice della prima riga nell'intervallo nominato.
- FirstColumn restituisce l'indice della prima colonna nell'intervallo nominato.
- RowCount restituisce il numero totale di righe nell'intervallo nominato.
- ColumnCount restituisce il numero totale di colonne nell'intervallo nominato.

L'esempio seguente mostra come inserire alcuni valori nelle celle di un intervallo specificato.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Create a range of cells based on H1:J4
    Range range = worksheet1.GetCells().CreateRange(u"H1", u"J4");

    // Name the range
    range.SetName(u"MyRange");

    // Input some data into cells in the range
    range.Get(0, 0).PutValue(u"USA");
    range.Get(0, 1).PutValue(u"SA");
    range.Get(0, 2).PutValue(u"Israel");
    range.Get(1, 0).PutValue(u"UK");
    range.Get(1, 1).PutValue(u"AUS");
    range.Get(1, 2).PutValue(u"Canada");
    range.Get(2, 0).PutValue(u"France");
    range.Get(2, 1).PutValue(u"India");
    range.Get(2, 2).PutValue(u"Egypt");
    range.Get(3, 0).PutValue(u"China");
    range.Get(3, 1).PutValue(u"Philipine");
    range.Get(3, 2).PutValue(u"Brazil");

    // Save the excel file
    workbook.Save(outDir + u"rangecells.out.xls");

    std::cout << "Range cells created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Identifica le celle nell'intervallo nominato**

È possibile inserire dati nelle singole celle di un intervallo seguendo lo schema:

- **C++**: Range(riga, colonna)

Se hai un intervallo chiamato che si estende da A1 a C4. La matrice comprende 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte sequenzialmente: Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).

Usa le seguenti proprietà per identificare le celle nell'intervallo:

- FirstRow restituisce l'indice della prima riga nell'intervallo nominato.
- FirstColumn restituisce l'indice della prima colonna nell'intervallo nominato.
- RowCount restituisce il numero totale di righe nell'intervallo nominato.
- ColumnCount restituisce il numero totale di colonne nell'intervallo nominato.

L'esempio seguente mostra come inserire alcuni valori nelle celle di un intervallo specificato.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    // Identify range cells
    std::cout << "First Row : " << range.GetFirstRow() << std::endl;
    std::cout << "First Column : " << range.GetFirstColumn() << std::endl;
    std::cout << "Row Count : " << range.GetRowCount() << std::endl;
    std::cout << "Column Count : " << range.GetColumnCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Accedi agli intervalli nominati**

#### **Accedi a un intervallo nominato specifico**

Chiama il metodo [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) della collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) per ottenere un intervallo con il nome specificato. Un tipico metodo [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) prende il nome dell'intervallo nominato e restituisce l'intervallo nominato specificato come un'istanza della classe [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). L'esempio seguente mostra come accedere a un intervallo specificato per nome.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Getting the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    if (range)
    {
        std::cout << "Named Range : " << range.GetRefersTo().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

#### **Accedi a tutti gli intervalli nominati in un foglio di calcolo**

Chiama il metodo [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) della raccolta [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) per ottenere tutti gli intervalli denominati in un foglio di calcolo. Il metodo [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) restituisce un array di tutti gli intervalli denominati nella collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).

L'esempio seguente mostra come accedere a tutti i nomi definiti in un libro.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    WorksheetCollection sheets = workbook.GetWorksheets();
    Vector<Range> ranges = sheets.GetNamedRanges();

    std::cout << "Total Number of Named Ranges: " << ranges.GetLength() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Copiare i Nomi Definiti**

Aspose.Cells fornisce il metodo [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) per copiare un intervallo di celle con formattazione in un altro intervallo.

L'esempio seguente mostra come copiare un intervallo di celle di origine in un altro nome definito.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");
    range1.SetName(u"MyRange");

	Color borderColor = Color{ 0,0, 0, 128 };
    range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, borderColor);

    range1.Get(0, 0).PutValue(u"Test");
    range1.Get(0, 4).PutValue(u"123");

    Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");
    range2.SetName(u"testrange");
    range2.Copy(range1);

    workbook.Save(outDir + u"copyranges.out.xls");

    std::cout << "Ranges copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
