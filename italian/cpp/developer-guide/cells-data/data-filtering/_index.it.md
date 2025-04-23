---
title: Filtraggio dei dati con C++
linktitle: Filtraggio dei dati
type: docs
weight: 85
url: /it/cpp/data-filtering/
description: Impara come aggiungere un filtro dati utilizzando l API Aspose.Cells for C++.
keywords: Aggiungi filtro per colore, aggiungi filtri per data, aggiungi filtri per numeri, aggiungi filtro dinamico, aggiungi filtri per testo, aggiungi filtro personalizzato con Contiene, aggiungi filtro personalizzato con NonContiene, aggiungi filtro personalizzato con IniziaCon, aggiungi filtro personalizzato con TerminaCon
---

{{% alert color="primary" %}}

Microsoft Excel fornisce alcune buone funzionalità per filtrare automaticamente i dati del foglio di lavoro. Aspose.Cells supporta pienamente le funzionalità di autofiltro di Microsoft Excel. Questo articolo spiega come utilizzare le funzionalità in Microsoft Excel e come codificarle utilizzando Aspose.Cells.

{{% /alert %}}

## **Dati Autofiltra**

L'auto-filtraggio è il modo più rapido per selezionare solo gli elementi del foglio di lavoro che si desidera visualizzare in un elenco. La funzione di autofiltro consente agli utenti di filtrare gli elementi in un elenco in base a determinati criteri. Filtra in base a testo, numeri o date.

### **Autofiltro in Microsoft Excel**

Per attivare la funzione di autofiltro in Microsoft Excel:

1. Fare clic sulla riga dell'intestazione su un foglio di lavoro.
1. Dal menu **Dati**, selezionare **Filtro** e poi **Autofiltro**.

Quando si applica un autofiltro a un foglio di lavoro, compaiono degli interruttori di filtro (frecce nere) alla destra degli intestazioni delle colonne.

1. Fare clic su una freccia del filtro per visualizzare un elenco di opzioni di filtro.

Alcune delle opzioni di autofiltro sono:

|**Opzioni**|**Descrizione**|
| :- | :- |
|All|Mostra tutti gli elementi nell'elenco una volta.|
|Custom|Personalizza i criteri di filtro come contiene/non contiene|
|Filter by Color|Filtra in base al colore riempito|
|Date Filters|Filtra le righe in base a diversi criteri di data|
|Number Filters|Diversi tipi di filtro sui numeri come confronto, medie e i primi 10 ecc.|
|Text Filters|Diversi filtri come inizia con, termina con, contiene ecc.,|
|Blanks/Non Blanks|Questi filtri possono essere implementati tramite Filtro Testo Vuoto|

Gli utenti filtrano manualmente i dati del foglio di lavoro in Microsoft Excel utilizzando queste opzioni.

### **Filtro automatico con Aspose.Cells**

Aspose.Cells fornisce una classe, `Workbook`, che rappresenta un file Excel. La classe `Workbook` contiene una collezione `Worksheets` che consente l'accesso a ogni foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe `Worksheet`. La classe `Worksheet` offre una vasta gamma di proprietà e metodi per gestire i fogli di lavoro. Per creare un autofiltro, utilizza la proprietà `AutoFilter` della classe `Worksheet`. La proprietà `AutoFilter` è un oggetto della classe `AutoFilter`, che fornisce la proprietà `Range` per specificare l'intervallo di celle che costituiscono una riga di intestazione. Un autofiltro viene applicato all'intervallo di celle che è la riga di intestazione.

In ogni foglio di lavoro, puoi specificare solo un intervallo di filtro. Questo è limitato da Microsoft Excel. Per filtraggio dati personalizzato, utilizza il metodo `AutoFilter.Custom`.

Nell'esempio qui sotto, abbiamo creato lo stesso autofiltro utilizzando Aspose.Cells come abbiamo creato utilizzando Microsoft Excel nella sezione precedente.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range of the heading row
    worksheet.GetAutoFilter().SetRange(u"A1:B1");

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Diversi tipi di filtro**

Aspose.Cells offre molteplici opzioni per applicare diversi tipi di filtri come Filtro colore, Filtro data, Filtro numero, Filtro testo, Filtri vuoti e non vuoti.

##### **Colore di riempimento**

Aspose.Cells fornisce una funzione `AddFillColorFilter` per filtrare i dati in base alla proprietà di riempimento delle celle. Nell'esempio seguente, un file template con diversi colori di riempimento nella prima colonna del foglio viene usato per testare la funzione di filtraggio colore. I file di esempio possono essere scaricati dai link seguenti.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

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
    Workbook workbook(srcDir + u"ColouredCells.xlsx");

    // Instantiating a CellsColor object for foreground color
    CellsColor clrForeground = workbook.CreateCellsColor();
    clrForeground.SetColor(Color::Red());

    // Instantiating a CellsColor object for background color
    CellsColor clrBackground = workbook.CreateCellsColor();
    clrBackground.SetColor(Color::White());

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddFillColorFilter function to apply the filter
    worksheet.GetAutoFilter().AddFillColorFilter(0, BackgroundType::Solid, clrForeground, clrBackground);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredColouredCells.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Data**

Diversi tipi di filtri di data possono essere implementati, come il filtro di tutte le righe con date a gennaio 2018. Il codice di esempio seguente dimostra questo filtro utilizzando la funzione `AddDateFilter`. I file di esempio sono forniti di seguito.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddDateFilter function to apply the filter
    worksheet.GetAutoFilter().AddDateFilter(0, DateTimeGroupingType::Month, 2018, 1, 0, 0, 0, 0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Date filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Data Dinamica**

A volte sono richiesti filtri dinamici basati sulla data, come tutte le celle con date a gennaio, indipendentemente dall'anno. In questo caso, viene usata la funzione `DynamicFilter` come mostrato nel seguente esempio. I file di esempio sono forniti di seguito.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDynamicDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call DynamicFilter function to apply the filter
    worksheet.GetAutoFilter().Dynamic_Filter(0, DynamicFilterType::January);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Dynamic filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Numero**

Filtros personalizzati possono essere applicati usando Aspose.Cells, come la selezione di celle con numeri compresi in un intervallo dato. L'esempio seguente dimostra l'uso della funzione `Custom()` per filtrare numeri. I file di esempio sono forniti di seguito.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

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
    U16String inputFilePath = srcDir + u"Number.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"FilteredNumber.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Custom function to apply the filter
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::GreaterOrEqual, 5, true, FilterOperatorType::LessOrEqual, 10);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Testo**

Se una colonna contiene testo e si vogliono selezionare le celle contenenti un testo particolare, si può usare la funzione `Filter()`. Nell'esempio seguente, il file template contiene una lista di paesi e si desidera selezionare le righe contenenti un nome di paese particolare. Il codice seguente dimostra il filtraggio del testo. I file di esempio sono forniti di seguito.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

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
    U16String inputFilePath = srcDir + u"Text.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredText.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Filter function to apply the filter
    worksheet.GetAutoFilter().Filter(0, u"Angola");

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Vuoti**

Se una colonna contiene testo tale che alcune celle sono vuote e si desidera filtrare solo le righe dove sono presenti celle vuote, si può usare la funzione `MatchBlanks()` come mostrato di seguito. I file di esempio sono forniti di seguito.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

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

    // Instantiating a Workbook object
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredBlank.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Non vuoti**

Quando si desidera filtrare celle con qualsiasi testo, si usa la funzione di filtro `MatchNonBlanks` come mostrato di seguito. I file di esempio sono forniti di seguito.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

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

    // Create workbook object and open the Excel file
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchNonBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outDir + u"FilteredNonBlank.xlsx");

    std::cout << "Non-blank filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Filtro personalizzato con Contiene**

Excel fornisce filtri personalizzati come filtrare le righe che contengono una stringa specifica. Questa funzionalità è disponibile in Aspose.Cells e dimostrata di seguito filtrando i nomi nel file di esempio. Sono forniti file di esempio di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::Contains, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Filtro personalizzato con NonContiene**

Excel fornisce filtri personalizzati come filtrare le righe che non contengono una stringa specifica. Questa funzione è disponibile in Aspose.Cells e dimostrata di seguito filtrando i nomi nel file di esempio fornito di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::NotContains, u"Be");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File filtered and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Filtro personalizzato con IniziaCon**

Excel fornisce filtri personalizzati come filtrare le righe che iniziano con una stringa specifica. Questa funzione è disponibile in Aspose.Cells e dimostrata di seguito filtrando i nomi nel file di esempio fornito di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows starting with string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Filtro personalizzato con TerminaCon**

Excel fornisce filtri personalizzati come filtrare le righe che terminano con una stringa specifica. Questa funzionalità è disponibile in Aspose.Cells e dimostrata di seguito filtrando i nomi nel file di esempio fornito di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows end with string "ia"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"ia");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Applicare il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi](/cells/it/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Ottenere tutti gli indici delle righe nascoste dopo l'aggiornamento dell'autofiltro](/cells/it/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
