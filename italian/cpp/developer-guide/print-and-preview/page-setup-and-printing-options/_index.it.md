---
title: Impostazioni pagina e opzioni di stampa con C++
linktitle: Opzioni di Impostazione Pagina e di Stampa
type: docs
weight: 60
url: /it/cpp/page-setup-and-printing-options/
description: Configura le impostazioni di configurazione della pagina e di stampa per controllare il processo di stampa usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte, gli sviluppatori devono configurare l'impostazione della pagina e le impostazioni di stampa per controllare il processo di stampa. Le impostazioni di configurazione della pagina e di stampa offrono varie opzioni e sono completamente supportate in Aspose.Cells.

Questo articolo mostra come creare un'applicazione console in Visual Studio e applicare impostazioni di configurazione pagina e di stampa a un foglio di lavoro con alcune linee di codice semplici utilizzando l'API di Aspose.Cells.

{{% /alert %}}

## **Lavorare con Impostazioni Pagina e di Stampa**

Per questo esempio, abbiamo creato un libro in Microsoft Excel e utilizzato Aspose.Cells per impostare le opzioni di impostazione pagina e di stampa.

### **Utilizzare Aspose.Cells per impostare le opzioni di impaginazione della pagina**

Prima creare un foglio di lavoro semplice in Microsoft Excel. Quindi applicare le opzioni dell'impostazione pagina ad esso. Eseguendo il codice cambia le opzioni dell'impostazione pagina come nello screenshot sottostante.

|**File di output.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Creare un foglio di lavoro con alcuni dati in Microsoft Excel:
   1. Apri un nuovo foglio di lavoro in Microsoft Excel.
   1. Aggiungi alcuni dati.
1. Imposta opzioni dell'impostazione pagina:
   Applicare le opzioni di impostazione pagina al file. Di seguito è riportata una schermata delle opzioni predefinite, prima che vengano applicate le nuove opzioni.

|**Opzioni di impaginazione predefinite.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. Scarica e installa Aspose.Cells:
   1. [Download](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++.
   1. Installalo sul tuo computer di sviluppo.
      Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. Crea un progetto:
   1. Avvia Visual Studio.
   1. Crea una nuova applicazione console.
      Questo esempio mostrerà un'applicazione console C++.
1. Aggiungi riferimenti:
   1. Questo esempio utilizza Aspose.Cells, quindi aggiungi un riferimento a quel componente al progetto. Ad esempio:
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Scrivi l'applicazione che invoca l'API:

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
    U16String inputFilePath = srcDir + u"CustomerReport.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting the orientation to Portrait
    worksheet.GetPageSetup().SetOrientation(PageOrientationType::Portrait);

    // Setting the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Setting the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Setting the paper size to A4
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Setting the print quality of the worksheet to 1200 dpi
    worksheet.GetPageSetup().SetPrintQuality(1200);

    // Setting the first page number of the worksheet pages
    worksheet.GetPageSetup().SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Impostazione delle opzioni di stampa**

Le impostazioni di impostazione pagina forniscono anche diverse opzioni di stampa (chiamate anche opzioni di foglio) che consentono agli utenti di controllare come vengono stampate le pagine del foglio di lavoro. Consentono agli utenti di:

- Selezionare un'area di stampa specifica di un foglio di lavoro.
- Stampare i titoli.
- Stampare le linee di griglia.
- Stampare gli intitoli di riga/colonna.
- Ottenere una qualità di bozza.
- Stampare commenti.
- Stampare errori di cella.
Definire l'ordinamento delle pagine.

L'esempio che segue applica le opzioni di stampa al file creato nell'esempio precedente (PageSetup.xls). La schermata di seguito mostra le opzioni di stampa predefinite prima che vengano applicate nuove opzioni.

|**Documento di input**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
Eseguendo il codice si modificano le opzioni di stampa.

|**File di output**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

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
    U16String inputFilePath = srcDir + u"PageSetup.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_Print_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get PageSetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specifying the cells range (from A1 cell to E30 cell) of the print area
    pageSetup.SetPrintArea(u"A1:E30");

    // Defining column numbers A & E as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$E");

    // Defining row numbers 1 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Allowing to print gridlines
    pageSetup.SetPrintGridlines(true);

    // Allowing to print row/column headings
    pageSetup.SetPrintHeadings(true);

    // Allowing to print worksheet in black & white mode
    pageSetup.SetBlackAndWhite(true);

    // Allowing to print comments as displayed on worksheet
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);

    // Allowing to print worksheet with draft quality
    pageSetup.SetPrintDraft(true);

    // Allowing to print cell errors as N/A
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);

    // Setting the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
