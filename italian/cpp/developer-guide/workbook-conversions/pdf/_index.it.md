---
title: Converti Excel in PDF con C++
linktitle: Converti Excel in PDF
type: docs
weight: 220
url: /it/cpp/convert-excel-to-pdf/
description: Scopri come Convertire cartelle di lavoro Excel in formato PDF usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione di cartelle di lavoro Excel in PDF. In questo esempio, vedremo la conversione completa di una cartella di lavoro Excel in PDF.

{{% /alert %}}

## **Conversione di un Workbook Excel in PDF**

I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e gli sviluppatori di software spesso devono trovare un modo per convertire i file Microsoft Excel in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{% alert color="primary" %}}

Aspose.Cells for C++ scrive direttamente le informazioni su API e numero di versione nei documenti di output. Ad esempio, durante il rendering di un documento in PDF, Aspose.Cells for C++ popola il campo **Produttore PDF** con un valore, ad esempio 'Aspose.Cells v23.2'.

Si noti che è possibile modificare queste informazioni nei documenti di output utilizzando la proprietà [**PdfSaveOptions.GetProducer()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getproducer/).

{{% /alert %}}

### **Conversione Diretta**

Aspose.Cells for C++ supporta la conversione da fogli di calcolo a PDF indipendentemente da altri software. Basta salvare un file Excel in PDF utilizzando il metodo [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) della classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Il metodo [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) fornisce il membro di enumerazione [**SaveFormat.Pdf**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) che converte i file Excel nativi in formato PDF.

Seguire i seguenti passi per convertire direttamente i fogli di calcolo Excel in formato PDF:

1. Crea un'istanza di un oggetto della classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) chiamando il suo costruttore vuoto.
2. È possibile aprire/caricare un file di modello esistente o saltare questo passo se si sta creando il workbook da zero.
1. Esegui qualsiasi operazione (input dati, applica formattazioni, imposta formule, inserisci immagini o altri oggetti di disegno, e così via) sul foglio di calcolo utilizzando le API di Aspose.Cells.
1. Quando il codice del foglio di calcolo è completo, chiama il metodo [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) della classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) per salvare il foglio di calcolo.

Il formato del file deve essere PDF, quindi seleziona *Pdf* (un valore predefinito) dall'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) per generare il documento PDF finale.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"output.pdf";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the document in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Document saved successfully in PDF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Conversione Avanzata**

Puoi anche optare per usare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) per impostare attributi differenti per la conversione. Impostare proprietà diverse della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) ti dà il controllo su impostazioni di stampa, carattere, sicurezza e compressione per il PDF di output.

La proprietà più importante è [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/), che consente di impostare il livello di conformità agli standard PDF. Attualmente, puoi salvare in formati PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab e PDF/A-3u. Nota che con il formato PDF/A, si ottiene una dimensione del file di output maggiore rispetto a un PDF normale.

#### **Salvataggio del foglio di lavoro in file PDF/A compilati**

Il frammento di codice sottostante mostra come usare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) per salvare i file Excel in formato PDF/A conforme allo standard PDF.

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

    // Instantiate new workbook
    Workbook workbook;

    // Insert a value into the A1 cell in the first worksheet
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(U16String(u"Testing PDF/A"));

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set the compliance type
    pdfSaveOptions.SetCompliance(PdfCompliance::PdfA1b);

    // Save the file
    workbook.Save(outDir + u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file created successfully with PDF/A-1b compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Si noti che la proprietà [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/) è stata aggiunta con il rilascio di Aspose.Cells for C++ 5.3.0.

{{% /alert %}}

#### **Imposta l'ora di creazione del PDF**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/), puoi ottenere o impostare l'orario di creazione del PDF. Il seguente codice dimostra l'uso della proprietà [**PdfSaveOptions.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcreatedtime/) per impostare l'orario di creazione del file PDF.

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
    U16String inputPath = srcDir + u"Book1.xlsx";

    // Load excel file containing charts
    Workbook workbook(inputPath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions options;
	options.SetCreatedTime(Date{ 2025,01,01 });

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    workbook.Save(srcDir + u"output.pdf", options);

    std::cout << "Workbook saved to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Imposta l'opzione ContentCopyForAccessibility**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/), puoi ottenere o impostare l'opzione [**GetAccessibilityExtractContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/getaccessibilityextractcontent/) del PDF per controllare l'accesso ai contenuti nel PDF convertito.

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
    U16String inputPath = srcDir + u"BookWithSomeData.xlsx";

    // Load excel file containing some data
    Workbook workbook(inputPath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions pdfSaveOpt;

    // Create an instance of PdfSecurityOptions
    PdfSecurityOptions securityOptions;

    // Set AccessibilityExtractContent to false
    securityOptions.SetAccessibilityExtractContent(false);

    // Set the security option in the PdfSaveOptions
    pdfSaveOpt.SetSecurityOptions(securityOptions);

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    workbook.Save(outDir + u"outFile.pdf", pdfSaveOpt);

    std::cout << "Workbook saved to PDF format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Esporta le proprietà personalizzate in PDF**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/), puoi esportare le proprietà personalizzate del workbook di origine nel PDF. È fornito l'enumeratore [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfcustompropertiesexport/) per specificare il metodo di esportazione delle proprietà. Queste proprietà possono essere osservate in Adobe Acrobat Reader cliccando su File e poi su Proprietà come mostrato nell'immagine seguente. Il file modello "sourceWithCustProps.xlsx" può essere scaricato [qui](sourceWithCustProps.xlsx) per test, e il file PDF di output "outSourceWithCustProps" è disponibile [qui](outSourceWithCustProps.pdf) per analisi.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Load excel file containing custom properties
    U16String inputFilePath(u"sourceWithCustProps.xlsx");
    Workbook workbook(inputFilePath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set CustomPropertiesExport property to PdfCustomPropertiesExport::Standard
    pdfSaveOptions.SetCustomPropertiesExport(PdfCustomPropertiesExport::Standard);

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    U16String outputFilePath(u"outSourceWithCustProps.pdf");
    workbook.Save(outputFilePath, pdfSaveOptions);

    Aspose::Cells::Cleanup();
}
```

### **Attributi di Conversione**

Lavoriamo per migliorare le funzionalità di conversione con ogni nuova versione. La conversione da Excel a PDF di Aspose.Cells presenta ancora alcune limitazioni. MapChart non è supportato nella conversione in PDF. Inoltre, alcuni oggetti di disegno non sono molto supportati.

La tabella che segue elenca tutte le funzionalità completamente o parzialmente supportate nell'esportazione in PDF utilizzando Aspose.Cells. Questa tabella non è definitiva e non copre tutte le caratteristiche del foglio di calcolo, ma identifica quelle funzionalità non supportate o parzialmente supportate nella conversione in PDF.

| Elemento del documento | Attributo | Supportato | Note |
| :- | :- | :- | :- |
| Allineamento |  | Sì |  |
| Impostazioni di sfondo |  | Sì |  |
| Bordo | Colore | Sì |  |
| Bordo | Stile della linea | Sì |  |
| Bordo | Spessore della linea | Sì |  |
| Dati Cella |  | Sì |  |
| Commenti |  | Sì |  |
| Formattazione Condizionale |  | Sì |  |
| Proprietà del Documento |  | Sì |  |
| Oggetti di Disegno |  | Parzialmente | Gli effetti Shadow e 3D per gli oggetti di disegno non sono supportati bene; WordArt e SmartArt sono parzialmente supportati. |
| Font | Dimensione | Sì |  |
| Font | Colore | Sì |  |
| Font | Stile | Sì |  |
| Font | Sottolineatura | Sì |  |
| Font | Effetti | Sì |  |
| Immagini |  | Sì |  |
| Collegamento ipertestuale |  | Sì |  |
| Grafici |  | Parzialmente | MapChart non supportato. |
| Celle unite |  | Sì |  |
| Interruzione di pagina |  | Sì |  |
| Impostazione pagina | Intestazione/Piede | Sì |  |
| Impostazione pagina | Margini | Sì |  |
| Impostazione pagina | Orientamento della pagina | Sì |  |
| Impostazione pagina | Dimensione pagina | Sì |  |
| Impostazione pagina | Area di stampa | Sì |  |
| Impostazione pagina | Titoli di stampa | Sì |  |
| Impostazione pagina | Scala | Sì |  |
| Altezza riga/Larghezza colonna |  | Sì |  |
| Lingua RTL (Da destra a sinistra) |  | Sì |  |

{{% alert color="primary" %}}

Se il tuo foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) subito prima di renderizzarlo in formato PDF. Questo assicura che i valori dipendenti dalle formule siano ricalcolati, e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}

## **Argomenti avanzati**
- [Aggiungi Segnalibri PDF con Destinazioni con Nome](/cells/it/cpp/add-pdf-bookmarks-with-named-destinations/)
- [Modifica il carattere solo sui caratteri Unicode specifici durante il salvataggio in PDF](/cells/it/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Converti file XLSX in formato PDF](/cells/it/cpp/convert-xlsx-file-to-pdf-format/)
- [Convertire file Excel in formato PDF compatibile con PDFA-1a](/cells/it/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Converti file XLS con immagini o grafici in PDF](/cells/it/cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Crea PdfBookmarkEntry per Chart Sheet](/cells/it/cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Adatta tutte le colonne del foglio di calcolo in una singola pagina PDF](/cells/it/cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ottieni DrawObject e Bound durante il rendering in PDF utilizzando la classe DrawObjectEventHandler](/cells/it/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Ottieni avvisi per la sostituzione del carattere mentre si rende il file Excel](/cells/it/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignora gli errori durante la conversione di Excel in PDF](/cells/it/cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Limita il numero di pagine generate - Conversione da Excel a PDF](/cells/it/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Stampa commenti durante il salvataggio in PDF](/cells/it/cpp/print-comments-while-saving-to-pdf/)
- [Render Office Add-Ins durante la conversione di Excel in PDF](/cells/it/cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendi una pagina PDF per ogni foglio di lavoro Excel - Conversione da Excel a PDF](/cells/it/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rende i Caratteri Unicode Supplementari nell'output PDF con Aspose.Cells](/cells/it/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Ridimensionamento delle immagini aggiunte - Conversione da Excel a PDF](/cells/it/cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Salva ciascun foglio di calcolo in un file PDF separato](/cells/it/cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Salva Excel in PDF con dimensioni standard o minime](/cells/it/cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Salva fogli specificati in PDF](/cells/it/cpp/save-specified-worksheets-to-pdf/)
- [Documenti PDF sicuri](/cells/it/cpp/secure-pdf-documents/)
- [Specificare come incrociare la stringa nel PDF e nell'immagine di output](/cells/it/cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="cpp" >}}
