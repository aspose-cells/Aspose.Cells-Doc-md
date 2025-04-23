---
title: Funzionalità di Impostazione Pagina con C++
linktitle: Caratteristiche della configurazione pagina
type: docs
weight: 60
url: /it/cpp/page-setup-features/
description: Impara come configurare le funzionalità di impostazione pagina nei file Excel usando Aspose.Cells con C++.
---

## **Funzionalità Impostazioni pagina**

Aspose.Cells offre un set completo di funzionalità per configurare le opzioni di impostazione della pagina per i file Excel. Queste funzionalità consentono di controllare vari aspetti del layout della pagina, come margini, orientamento, formato della carta e altro ancora.

### **Impostazione Margini di Pagina**

Puoi impostare i margini di pagina per un foglio di lavoro utilizzando la classe `PageSetup`. L'esempio seguente dimostra come impostare i margini superiore, inferiore, sinistro e destro:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageMargins() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set page margins
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetTopMargin(1.0);
    pageSetup.SetBottomMargin(1.0);
    pageSetup.SetLeftMargin(0.75);
    pageSetup.SetRightMargin(0.75);

    // Save the workbook
    workbook.Save("PageMargins.xlsx");
}
```

### **Impostazione Orientamento Pagina**

Puoi impostare l'orientamento della pagina su verticale o orizzontale utilizzando la classe `PageSetup`. L'esempio seguente dimostra come impostare l'orientamento della pagina su orizzontale:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageOrientation() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    workbook.Save("PageOrientation.xlsx");
}
```

### **Impostazione Dimensione Carta**

Puoi impostare la dimensione della carta per la stampa utilizzando la classe `PageSetup`. L'esempio seguente dimostra come impostare la dimensione carta su A4:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPaperSize() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    workbook.Save("PaperSize.xlsx");
}
```

### **Impostazione Area di Stampa**

Puoi definire un intervallo specifico di celle da stampare utilizzando la classe `PageSetup`. L'esempio seguente dimostra come impostare l'area di stampa:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintArea() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea("A1:D10");

    // Save the workbook
    workbook.Save("PrintArea.xlsx");
}
```

### **Impostazione Interruzioni di Pagina**

Puoi inserire interruzioni di pagina in un foglio di lavoro per controllare dove finiscono le pagine e dove iniziano le nuove. L'esempio seguente dimostra come inserire un'interruzione di pagina orizzontale:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageBreaks() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a horizontal page break at row 10
    worksheet.GetHorizontalPageBreaks().Add("A10");

    // Save the workbook
    workbook.Save("PageBreaks.xlsx");
}
```

### **Impostazione Intestazione e Piede di Pagina**

Puoi personalizzare l'intestazione e il piè di pagina di un foglio di lavoro utilizzando la classe `PageSetup`. L'esempio seguente dimostra come impostare un'intestazione e un piè di pagina personalizzati:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetHeaderFooter() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set custom header and footer
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&CHeader Text");
    pageSetup.SetFooter(0, "&CFooter Text");

    // Save the workbook
    workbook.Save("HeaderFooter.xlsx");
}
```

### **Impostazione Titoli di Stampa**

Puoi specificare righe o colonne da ripetere in cima o a sinistra di ogni pagina stampata utilizzando la classe `PageSetup`. L'esempio seguente dimostra come impostare i titoli di stampa:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintTitles() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print titles
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows("$1:$1");
    pageSetup.SetPrintTitleColumns("$A:$A");

    // Save the workbook
    workbook.Save("PrintTitles.xlsx");
}
```

### **Impostazione Qualità di Stampa**

Puoi impostare la qualità di stampa per un foglio di lavoro utilizzando la classe `PageSetup`. L'esempio seguente dimostra come impostare la qualità di stampa:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintQuality() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print quality
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintQuality(600);

    // Save the workbook
    workbook.Save("PrintQuality.xlsx");
}
```

### **Impostazione Ordine di Stampa**

Puoi impostare l'ordine di stampa per un foglio di lavoro utilizzando la classe `PageSetup`. L'esempio seguente dimostra come impostare l'ordine di stampa su "Avanti, poi Giù":

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintOrder() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrder(PrintOrderType::OverThenDown);
    workbook.Save("PrintOrder.xlsx");
}
```

### **Impostazione Griglie di Stampa**

Puoi controllare se le linee della griglia vengono stampate utilizzando la classe `PageSetup`. L'esempio seguente mostra come abilitare la stampa delle linee della griglia:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintGridlines() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of gridlines
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintGridlines(true);

    // Save the workbook
    workbook.Save("PrintGridlines.xlsx");
}
```

### **Impostazione Intestazioni di Stampa**

Puoi controllare se le intestazioni di riga e colonna vengono stampate utilizzando la classe `PageSetup`. L'esempio seguente mostra come abilitare la stampa delle intestazioni:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintHeadings() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of headings
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintHeadings(true);

    // Save the workbook
    workbook.Save("PrintHeadings.xlsx");
}
```

### **Impostazione Stampa in Bianco e Nero**

Puoi controllare se il foglio di lavoro viene stampato in bianco e nero utilizzando la classe `PageSetup`. L'esempio seguente mostra come abilitare la stampa in bianco e nero:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintBlackAndWhite() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable black and white printing
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetBlackAndWhite(true);

    // Save the workbook
    workbook.Save("PrintBlackAndWhite.xlsx");
}
```

### **Impostazione Stampa in Bozza**

Puoi controllare se il foglio di lavoro viene stampato in modalità bozza utilizzando la classe `PageSetup`. L'esempio seguente mostra come abilitare la stampa in modalità bozza:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintDraft() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintDraft(true);
    workbook.Save("PrintDraft.xlsx");
}
```

### **Impostazione Commenti di Stampa**

Puoi controllare se i commenti vengono stampati utilizzando la classe `PageSetup`. L'esempio seguente mostra come abilitare la stampa dei commenti:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintComments() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);
    workbook.Save("PrintComments.xlsx");
}
```

### **Impostazione Errori di Stampa**

Puoi controllare come vengono stampati gli errori utilizzando la classe `PageSetup`. Il seguente esempio dimostra come impostare l'opzione di stampa degli errori:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintErrors() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsBlank);
    workbook.Save("PrintErrors.xlsx");
}
```

### **Impostare l'adattamento dell'area di stampa a pagine**

Puoi controllare se l'area di stampa viene scalata per adattarsi a un numero specifico di pagine utilizzando la classe `PageSetup`. Il seguente esempio dimostra come impostare l'area di stampa per adattarsi a una pagina di larghezza e una pagina di altezza:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintAreaFitToPages() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area to fit to one page wide and one page tall
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the workbook
    workbook.Save("PrintAreaFitToPages.xlsx");
}
```

### **Impostare la scala di stampa**

Puoi impostare la scala di stampa per un foglio di lavoro usando la classe `PageSetup`. Il seguente esempio dimostra come impostare la scala di stampa al 50%:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintScale() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print scale to 50%
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetZoom(50);

    // Save the workbook
    workbook.Save("PrintScale.xlsx");
}
```

### **Impostare il centramento di stampa orizzontalmente e verticalmente**

Puoi controllare se il foglio di lavoro è centrato orizzontalmente e verticalmente sulla pagina stampata usando la classe `PageSetup`. Il seguente esempio dimostra come centrare il foglio di lavoro orizzontalmente e verticalmente:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintCenterHorizontallyAndVertically() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Center the worksheet horizontally and vertically
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the workbook
    workbook.Save("PrintCenterHorizontallyAndVertically.xlsx");
}
```

### **Impostare il numero della prima pagina di stampa**

Puoi impostare il numero della prima pagina per la stampa usando la classe `PageSetup`. Il seguente esempio dimostra come impostare il numero della prima pagina:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintFirstPageNumber() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the first page number
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save("PrintFirstPageNumber.xlsx");
}
```

### **Impostare il numero di pagina di stampa**

Puoi controllare se il numero di pagina viene stampato usando la classe `PageSetup`. Il seguente esempio dimostra come abilitare la stampa del numero di pagina:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPrintPageNumber() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&P");
    workbook.Save("PrintPageNumber.xlsx");
}
```

### **Impostare l'ordine di stampa delle pagine**

Puoi impostare l'ordine in cui vengono stampate le pagine usando la classe `PageSetup`. Il seguente esempio dimostra come impostare l'ordine delle pagine su "Giù, poi Orizzontale":

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPageOrder() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the page order to "Down, then Over"
    PageSetup
