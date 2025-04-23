---
title: Impostazioni del bordo con C++
linktitle: Impostazioni bordo
description: Come usare la libreria Aspose.Cells in C++ per impostare lo stile e il colore del bordo delle celle. Regolando larghezza, stile e colore del bordo, si ha un maggiore controllo sull aspetto delle celle.
keywords: Aspose.Cells, Impostazioni del bordo della cella, C++, Larghezza del bordo, Stile del bordo, Colore del bordo
type: docs
weight: 40
url: /it/cpp/cells-border-settings/
---

## **Aggiungere Bordi alle Celle**

Microsoft Excel permette agli utenti di formattare le celle aggiungendo i bordi. Il tipo di bordo dipende da dove viene aggiunto. Ad esempio, un bordo superiore viene aggiunto alla posizione superiore di una cella. Gli utenti possono anche modificare lo stile di linea e il colore dei bordi.

Con Aspose.Cells, gli sviluppatori possono aggiungere bordi e personalizzarne l'aspetto in modo flessibile come in Microsoft Excel.

### **Aggiungere Bordi alle Celle**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente di accedere a ogni foglio di calcolo nel file Excel. Un foglio di calcolo viene rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce la collezione [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells fornisce il metodo [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) nella classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Il metodo [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) viene utilizzato per impostare lo stile di formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) offre proprietà per aggiungere bordi alle celle.

#### **Aggiunta di bordi a una cella**

Gli sviluppatori possono aggiungere bordi a una cella utilizzando la raccolta [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) dell'oggetto [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/). Il tipo di bordo viene passato come indice alla raccolta [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/). Tutti i tipi di bordo sono predefiniti nell'enumerazione [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/).

**Enumerazione Border**

| **Tipi di bordo** | **Descrizione** |
|------------------|-----------------|
| BottomBorder     | Una linea di bordo inferiore |
| DiagonaleInGiù | Una linea diagonale dall'angolo superiore sinistro a quello inferiore destro |
| DiagonaleSu | Una linea diagonale dall'angolo inferiore sinistro a quello superiore destro |
| BordoSinistro | Una linea del bordo sinistro |
| BordoDestro | Una linea del bordo destro |
| BordoSuperiore | Una linea del bordo superiore |

La raccolta [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) memorizza tutti i bordi. Ogni bordo nella raccolta [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) è rappresentato da un oggetto [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/) che fornisce due proprietà, [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/) e [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/), per impostare rispettivamente colore e stile della linea del bordo.

Per impostare il colore della linea di un bordo, seleziona un colore utilizzando l'enumerazione Colore e assegnalo alla proprietà Colore dell'oggetto Border.

Lo stile della linea del bordo viene impostato selezionando uno stile di linea dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellbordertype/).

**Enumerazione CellBorderType**

| **Stili di Linea** | **Descrizione** |
|------------------------|-------------------------------|
| TrattoPunto | Linea sottile tratteggiata |
| TrattoPuntoPunto | Linea sottile trattino-punto |
| Tratteggiata | Linea tratteggiata |
| Punteggiata | Linea punteggiata |
| Doppia | Linea doppia |
| Capelli |Linea sottile di capelli |
| TrattoPuntoPuntoMedio | Linea tratto-punto di spessore medio |
| TrattoPuntoPuntoMedio | Linea trattino-punto di spessore medio |
| TrattoTratteggiatoMedio | Linea tratteggiata di spessore medio |
| Nessuno | Nessuna linea |
| Medio | Linea di spessore medio |
| TrattoInclinatoPunto | Linea tratto-punto inclinata di medio spessore |
| Spesso | Linea spessa |
| Sottile | Linea sottile |

Seleziona uno degli stili di linea e assegnalo alla proprietà [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) dell'oggetto [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/).

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
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Visit Aspose!");

    Style style = cell.GetStyle();

    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());

    cell.SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls");
    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Dovresti impostare sia lo stile di linea che il colore contemporaneamente. Le due linee diagonali del bordo dovrebbero avere lo stesso stile e colore.

{{% /alert %}}

#### **Aggiunta di bordi a un intervallo di celle**

È anche possibile aggiungere bordi a un intervallo di celle piuttosto che a una singola cella. Per farlo, prima crea un intervallo di celle chiamando il metodo [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) della raccolta [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Accetta i seguenti parametri:

- Prima riga, la prima riga dell'intervallo.
- Prima colonna, rappresenta la prima colonna dell'intervallo.
- Numero di righe, il numero di righe nell'intervallo.
- Numero di colonne, il numero di colonne nell'intervallo.

Il metodo [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) restituisce un oggetto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/), che contiene l'intervallo di celle specificato. L'oggetto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) fornisce un metodo [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) che prende i seguenti parametri per aggiungere un bordo all'intervallo di celle:

- **Tipo di Bordi**, il tipo di bordo, selezionato dall'enumerazione [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/).
- **Stile di Linea**, lo stile della linea del bordo, selezionato dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellbordertype/).
- **Colore**, il colore della linea, selezionato dall'enumerazione Colore.

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

    // Create workbook
    Workbook workbook;

    // Obtain the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello World From Aspose");

    // Creating a range of cells starting from "A1" cell to 3rd column in a row
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 3);

    // Adding a thick top border with blue line
    range.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick bottom border with blue line
    range.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick left border with blue line
    range.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick right border with blue line
    range.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Thick, Color::Blue());

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
