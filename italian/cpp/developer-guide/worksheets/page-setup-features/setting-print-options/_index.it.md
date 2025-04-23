---
title: Impostare le opzioni di stampa con C++
linktitle: Impostazione delle opzioni di stampa
type: docs
weight: 40
url: /it/cpp/setting-print-options/
description: Questo articolo dimostra come impostare programmaticamente le opzioni di stampa della funzione di configurazione della pagina del foglio di Excel usando l API C++ e la libreria. È possibile impostare l area di stampa, i titoli di stampa e l ordine delle pagine.
keywords: impostare l area di stampa di Excel c++, impostare i titoli di stampa di Excel c++, impostare l ordine delle pagine di Excel c++
---

{{% alert color="primary" %}}

Le impostazioni di pagina di Microsoft Excel forniscono diverse opzioni di stampa (anche chiamate opzioni di foglio) che consentono agli utenti di controllare come vengono stampate le pagine del foglio di lavoro.

{{% /alert %}}

## **Opzioni di stampa**

Queste opzioni di stampa consentono agli utenti di:

- Selezionare un'area di stampa specifica su un foglio di lavoro.
- Stampare i titoli.
- Stampare le linee di griglia.
- Stampare gli intitoli di riga/colonna.
- Ottenere una qualità di bozza.
- Stampare commenti.
- Stampare errori di cella.
Definire l'ordinamento delle pagine.

Aspose.Cells supporta tutte le opzioni di stampa offerte da Microsoft Excel, e gli sviluppatori possono facilmente configurare queste opzioni per i fogli di lavoro usando le proprietà offerte dalla classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). Come vengono usate queste proprietà è discusso più dettagliatamente di seguito.

### **Impostare l'area di stampa**

Per impostazione predefinita, l'area di stampa incorpora tutte le aree del foglio di lavoro che contengono dati. Gli sviluppatori possono stabilire un'area di stampa specifica del foglio di lavoro.

Per selezionare un'area di stampa specifica, utilizzare la proprietà [**GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) della classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). Assegnare un intervallo di celle che definisce l'area di stampa a questa proprietà.

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set the print area to the range A1:T35
    pageSetup.SetPrintArea(u"A1:T35");

    // Save the workbook
    workbook.Save(outDir + u"SetPrintArea_out.xls");

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Impostare i titoli di stampa**

Aspose.Cells consente di designare intitoli di riga e colonna da ripetere su tutte le pagine di un foglio di lavoro stampato. Per farlo, utilizzare le proprietà [**GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) e [**GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) della classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/).

Le righe o le colonne che verranno ripetute sono definite passando il loro numero di riga o colonna. Ad esempio, le righe sono definite come $1:$2 e le colonne sono definite come $A:$B.

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"SetPrintTitle_out.xls";

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Define column numbers A & B as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$B");

    // Define row numbers 1 & 2 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Impostare altre opzioni di stampa**

La classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) fornisce anche diverse altre proprietà per impostare opzioni di stampa generali come segue:

- [**GetPrintGridlines()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintgridlines/): proprietà Booleana che definisce se stampare le linee della griglia o meno.
- [**GetPrintHeadings()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintheadings/): una proprietà booleana che definisce se stampare o meno gli intitoli di riga e colonna.
- [**GetBlackAndWhite()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getblackandwhite/): una proprietà booleana che definisce se stampare o meno il foglio di lavoro in modalità bianco e nero.
- [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/): definisce se visualizzare i commenti di stampa sul foglio di lavoro o alla fine del foglio di lavoro.
- [**GetPrintDraft()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintdraft/): proprietà booleana che definisce se stampare il foglio senza grafici.
- [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/): definisce se stampare gli errori nelle celle come visualizzati, vuoti, trattino o N/A.

Per impostare le proprietà [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) e [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/), Aspose.Cells fornisce anche due enumerazioni, [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) e [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) che contengono valori predefiniti da assegnare rispettivamente alle proprietà [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) e [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/).

I valori predefiniti nell'enumerazione [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) sono elencati di seguito con le loro descrizioni.

|**Tipi di Commenti di Stampa**|**Descrizione**|
| :- | :- |
|PrintInPlace|Specifica di stampare i commenti come visualizzati sul foglio di lavoro.|
|PrintNoComments|Specifica di non stampare i commenti.|
|PrintSheetEnd| Specifica di stampare i commenti alla fine del foglio di lavoro.

I valori predefiniti dell'enumerazione [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) sono elencati di seguito con le loro descrizioni.

|**Tipi di Errori di Stampa**|**Descrizione**|
| :- | :- |
|PrintErrorsBlank| Specifica di non stampare gli errori.
|PrintErrorsDash| Specifica di stampare gli errori come "--".
|PrintErrorsDisplayed| Specifica di stampare gli errori come visualizzato.
|PrintErrorsNA| Specifica di stampare gli errori come "#N/A".

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set print options
    pageSetup.SetPrintGridlines(true);  // Allow printing gridlines
    pageSetup.SetPrintHeadings(true);   // Allow printing row/column headings
    pageSetup.SetBlackAndWhite(true);   // Allow printing in black & white mode
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);  // Print comments as displayed
    pageSetup.SetPrintDraft(true);      // Print with draft quality
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);  // Print cell errors as N/A

    // Save the workbook
    U16String outputPath = outDir + u"OtherPrintOptions_out.xls";
    workbook.Save(outputPath);

    std::cout << "Workbook saved with print options successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Imposta l'Ordine delle Pagine**

La classe [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) fornisce la proprietà [**GetOrder()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getorder/) che viene utilizzata per ordinare la stampa di più pagine del foglio di lavoro. Ci sono due possibilità per ordinare le pagine come segue.

- **In basso poi a destra:** stampa tutte le pagine in basso prima di stampare eventuali pagine a destra.
- **A destra poi in basso:** stampa le pagine da sinistra a destra prima di stampare le pagine sottostanti.

Aspose.Cells fornisce un'enumerazione, [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/), che contiene tutti i tipi di ordinamento predefiniti.

I valori predefiniti dell'enumerazione [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) sono elencati di seguito.

|**Tipi di Ordine di Stampa**|**Descrizione**|
| :- | :- |
|DownThenOver|Rappresenta l'ordine di stampa come in basso e poi sopra.|
|OverThenDown|Rappresenta l'ordine di stampa come sopra e poi in basso.|

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

    // Obtain the reference of the PageSetup of the first worksheet
    PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

    // Set the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outDir + u"SetPageOrder_out.xls");

    std::cout << "Page order set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
