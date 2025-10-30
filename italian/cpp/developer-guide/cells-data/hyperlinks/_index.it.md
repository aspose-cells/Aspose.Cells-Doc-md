---
title: Inserire link ipertestuali in Excel o OpenOffice con C++
linktitle: Gestione dei collegamenti ipertestuali
type: docs
weight: 45
url: /it/cpp/insert-hyperlinks-to-excel/
description: Come inserire link ipertestuali nel file Excel con la libreria Aspose.Cells senza MS Excel usando C++.
keywords: Inserire collegamenti ipertestuali in Excel, Aggiungere o Inserire collegamenti ipertestuali, Aggiungi o Inserisci un collegamento a un URL, Aggiungi o Inserisci un collegamento in una cella, Aggiungi un collegamento a un file esterno
---

{{% alert color="primary" %}} 

Un collegamento ipertestuale viene utilizzato per creare un collegamento tra due entità. Tutti sono familiari con l'uso dei collegamenti ipertestuali, specialmente sui siti web.
Utilizzando Aspose.Cells, gli sviluppatori possono creare diversi tipi di collegamenti ipertestuali nei file Microsoft Excel. Questo argomento discute quali tipi di collegamenti ipertestuali sono supportati da Aspose.Cells e come possono essere utilizzati nei nostri file Excel.

{{% /alert %}} 

## **Aggiunta di Collegamenti Ipotestuali**
Aspose.Cells consente agli sviluppatori di aggiungere collegamenti ipertestuali ai file Excel usando l'API o fogli di calcolo creati manualmente (fogli di calcolo in cui i collegamenti vengono creati manualmente e Aspose.Cells viene usato per importarli in altri fogli).

Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che permette l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce diversi metodi per aggiungere diversi collegamenti ipertestuali ai file Excel.

## **Aggiunta di un link a un URL**
 La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) contiene una collezione [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/). Ogni elemento nella collezione rappresenta un [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/). Aggiungi link ipertestuali agli URL chiamando il metodo [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) della collezione [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). Il metodo [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) richiede i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo URL.

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a hyperlink to cell "A1"
    worksheet.GetHyperlinks().Add(u"A1", 1, 1, u"http://www.aspose.com");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Nell'esempio precedente, è stato aggiunto un collegamento ipertestuale a un URL in una cella vuota, **A1**. In tali casi, se una cella è vuota, l'indirizzo URL viene aggiunto anche a quella cella vuota come suo valore. Se la cella non è vuota e viene aggiunto un collegamento ipertestuale, il valore della cella appare come testo semplice. Per farlo apparire come un collegamento ipertestuale, applicare le impostazioni di formattazione appropriate su quella cella.

{{% /alert %}} 

## **Aggiunta di un link a una cella nello stesso file**
È possibile aggiungere link ipertestuali alle celle nello stesso file Excel chiamando il metodo [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) della collezione [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). Il metodo [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) funziona sia per collegamenti interni che esterni. Una versione del metodo sovraccarico richiede i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo della cella di destinazione.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
    // The same Excel file
    worksheet.GetHyperlinks().Add(u"B3", 1, 1, u"Sheet2!B9");

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aggiunta di un link a un file esterno**
 È possibile aggiungere link ipertestuali a file Excel esterni chiamando il metodo [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) della collezione [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). Il metodo [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) richiede i seguenti parametri:

- Nome della cella, il nome della cella a cui verrà aggiunto il collegamento ipertestuale.
- Numero di righe, il numero di righe in questo intervallo di collegamenti ipertestuali.
- Numero di colonne, il numero di colonne in questo intervallo di collegamenti ipertestuali.
- URL, l'indirizzo di destinazione, file Excel esterno.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Add an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
    worksheet.GetHyperlinks().Add(U16String(u"A5"), 1, 1, srcDir + U16String(u"book1.xls"));

    // Save the Excel file
    workbook.Save(outDir + U16String(u"output.out.xls"));

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Aggiungi collegamenti ipertestuali alle immagini](/cells/it/cpp/add-image-hyperlinks/)
- [Rilevare il tipo di collegamento ipertestuale](/cells/it/cpp/detect-hyperlink-type/)
- [Modifica dei collegamenti ipertestuali del foglio di lavoro](/cells/it/cpp/editing-hyperlinks-of-worksheet/)
- [Ottieni i collegamenti ipertestuali nell'intervallo](/cells/it/cpp/get-hyperlinks-in-range/)
{{< app/cells/assistant language="cpp" >}}
