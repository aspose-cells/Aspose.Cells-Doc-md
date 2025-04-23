---
title: Mostrare e Nascondere le Linee della Griglia e le Intestazioni delle Righe e Colonne con C++
linktitle: Mostra e nasconde le linee della griglia e gli intestazioni delle righe e delle colonne
type: docs
weight: 30
url: /it/cpp/show-and-hide-gridlines-and-row-column-headers/
description: Questo articolo fornisce un esempio di codice per l uso dell API o della libreria C++ per nascondere o mostrare programmaticamente le linee della griglia, le intestazioni di riga e colonna di un foglio di lavoro Excel.
---

{{% alert color="primary" %}}

Aspose.Cells supporta la visualizzazione e la modifica delle linee della griglia del foglio di calcolo che sono visibili per impostazione predefinita. Fornisce anche il controllo della visibilità delle intestazioni delle righe e delle colonne del foglio di calcolo.

{{% /alert %}}

## **Mostrare e nascondere le linee della griglia**

Tutti i fogli di lavoro di Excel hanno linee di griglia per impostazione predefinita. Aiutano a delimitare le celle in modo che sia facile inserire dati in celle specifiche. Le linee di griglia ci consentono di visualizzare un foglio di calcolo come una collezione di celle, in cui ogni cella è facilmente identificabile.

### **Controllo della visibilità delle linee della griglia**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che permette agli sviluppatori di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) offre un'ampia gamma di proprietà e metodi per la gestione di un foglio di lavoro. Per controllare la visibilità delle linee di griglia, usa la proprietà della classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/). [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) è una proprietà Booleana, il che significa che può contenere solo un valore **vero** o **falso**.

#### **Rendere Visibili le Linee della Griglia**

Rendi visibili le linee della griglia impostando la proprietà {6} della classe {5} su **true**.

#### **Nascondere le Linee della Griglia**

Nascondi le linee della griglia impostando la proprietà {6} della classe {5} su **falso**.

Un esempio completo è mostrato di seguito che dimostra l'uso della proprietà [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) aprendendo un file Excel (book1.xls), nascondendo le linee della griglia sul primo foglio di lavoro e salvando il file modificato come output.xls.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the grid lines of the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Grid lines hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Mostra e nasconde gli intestazioni delle righe e delle colonne**

Tutti i fogli di lavoro in un file Excel sono composti da celle disposte in righe e colonne. Tutte le righe e colonne hanno valori univoci che vengono utilizzati per identificarle e per identificare singole celle. Ad esempio, le righe sono numerate – 1, 2, 3, 4, ecc. – e le colonne sono ordinate in modo alfabetico – A, B, C, D, ecc. I valori delle righe e delle colonne sono visualizzati negli intestazioni. Utilizzando Aspose.Cells, gli sviluppatori possono controllare la visibilità di queste intestazioni delle righe e delle colonne.

### **Controllo della visibilità dei fogli di lavoro**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che permette agli sviluppatori di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) offre un'ampia gamma di proprietà e metodi per la gestione di un foglio di lavoro. Per controllare la visibilità delle intestazioni di riga e colonna, usa la proprietà della classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) è una proprietà Booleana, che significa che può contenere solo un valore **vero** o **falso**.

#### **Rendere visibili le intestazioni di riga/colonna**

Rendi visibili le intestazioni di riga e colonna impostando la proprietà {6} della classe {5} su **true**.

#### **Nascondere le intestazioni di riga/colonna**

Nascondi intestazioni di riga e colonna impostando la proprietà [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) della classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) su **falso**.

Esempio completo mostrato di seguito che illustra come utilizzare la proprietà [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) aprendo un file excel (book1.xls), nascondendo le intestazioni di riga e colonna nel primo foglio di lavoro e salvando il file modificato come output.xls.

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

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the headers of rows and columns
    worksheet.SetIsRowColumnHeadersVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Headers hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

È anche possibile usare i metodi [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) e [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) della classe [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) per rendere visibili più righe e colonne.

{{% /alert %}}
