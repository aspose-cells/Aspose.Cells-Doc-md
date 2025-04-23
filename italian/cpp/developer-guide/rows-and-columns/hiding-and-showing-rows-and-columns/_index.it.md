---
title: Nascondere e mostrare righe e colonne con C++
linktitle: Nascondere e mostrare righe e colonne
type: docs
weight: 60
url: /it/cpp/hiding-and-showing-rows-and-columns/
description: Impara come nascondere e mostrare righe e colonne nei file Excel programmando con Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte, ha senso nascondere certe righe o colonne in un foglio di lavoro e mostrarle successivamente. Microsoft Excel offre questa funzionalità, e anche Aspose.Cells.

{{% /alert %}}

## **Controllo della visibilità di righe e colonne**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente agli sviluppatori di accedere a ogni foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) che rappresenta tutte le celle nel foglio di lavoro. La raccolta [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi vengono discussi di seguito.

### **Nascondere righe e colonne**

Gli sviluppatori possono nascondere una riga o colonna chiamando rispettivamente i metodi [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) e [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) della collezione [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Entrambi i metodi prendono l'indice della riga e della colonna come parametro per nascondere la riga o colonna specifica.

```c++
#include <iostream>
#include <memory>
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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully. File saved to: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

È anche possibile nascondere una riga o colonna impostando rispettivamente l'altezza della riga e la larghezza della colonna a 0.

{{% /alert %}}

### **Mostrare righe e colonne**

Gli sviluppatori possono mostrare qualsiasi riga o colonna nascosta chiamando rispettivamente i metodi [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) e [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) della collezione [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Entrambi i metodi prendono due parametri:

- **Indice della riga o colonna** - l'indice di una riga o colonna che viene utilizzato per mostrare la riga o colonna specifica.
- **Altezza della riga o larghezza della colonna** - l'altezza della riga o la larghezza della colonna assegnata alla riga o colonna dopo l'annullamento della visualizzazione.

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

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhide the 3rd row and set its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhide the 2nd column and set its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File modified and saved successfully!" << std::endl;

    return 0;
}
```

{{% alert color="primary" %}}

Quando si rende visibile una colonna nascosta, se è necessario ripristinare la larghezza precedentemente assegnata o quella originale, si prega di scoprire la colonna con una larghezza negativa. Per esempio: `worksheet.Cells.UnhideColumn(5, -1)`

{{% /alert %}}

### **Nascondere più righe e colonne**

Gli sviluppatori possono nascondere più righe o colonne contemporaneamente chiamando rispettivamente i metodi [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) e [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) della collezione [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Entrambi i metodi prendono l'indice di partenza della riga o colonna e il numero di righe o colonne che devono essere nascoste come parametri.

```cpp
#include <iostream>
#include <memory>
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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet (zero-based index)
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet (zero-based index)
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

È anche possibile utilizzare i metodi [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) e [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) della classe [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) per rendere visibili più righe e colonne.

{{% /alert %}}
