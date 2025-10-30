---
title: Converti Excel in PDF con Golang tramite C++
linktitle: Converti Excel in PDF
type: docs
weight: 220
url: /it/go-cpp/convert-excel-to-pdf/
description: Impara come convertire i fogli di lavoro Excel in formato PDF usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione di cartelle di lavoro Excel in PDF. In questo esempio, vedremo la conversione completa di una cartella di lavoro Excel in PDF.

{{% /alert %}}

## **Conversione di un Workbook Excel in PDF**

I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e gli sviluppatori di software spesso devono trovare un modo per convertire i file Microsoft Excel in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{% alert color="primary" %}}

Aspose.Cells for C++ scrive direttamente le informazioni su API e numero di versione nei documenti di output. Ad esempio, durante il rendering di un documento in PDF, Aspose.Cells for C++ popola il campo **Produttore PDF** con un valore, ad esempio 'Aspose.Cells v23.2'.

Si noti che è possibile modificare queste informazioni nei documenti di output utilizzando la proprietà [**PdfSaveOptions.GetProducer()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getproducer/).

{{% /alert %}}

### **Conversione Diretta**

Aspose.Cells for C++ supporta la conversione da fogli di calcolo a PDF indipendentemente da altri software. Basta salvare un file Excel in PDF utilizzando il metodo [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) della classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/). Il metodo [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) fornisce il membro di enumerazione [**SaveFormat.Pdf**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) che converte i file Excel nativi in formato PDF.

Seguire i seguenti passi per convertire direttamente i fogli di calcolo Excel in formato PDF:

1. Crea un'istanza di un oggetto della classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) chiamando il suo costruttore vuoto.
2. È possibile aprire/caricare un file di modello esistente o saltare questo passo se si sta creando il workbook da zero.
1. Esegui qualsiasi operazione (input dati, applica formattazioni, imposta formule, inserisci immagini o altri oggetti di disegno, e così via) sul foglio di calcolo utilizzando le API di Aspose.Cells.
1. Quando il codice del foglio di calcolo è completo, chiama il metodo [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) della classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) per salvare il foglio di calcolo.

Il formato del file deve essere PDF, quindi seleziona *Pdf* (un valore predefinito) dall'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/) per generare il documento PDF finale.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf.go" >}}
### **Conversione Avanzata**

Puoi anche optare per usare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) per impostare attributi differenti per la conversione. Impostare proprietà diverse della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) ti dà il controllo su impostazioni di stampa, carattere, sicurezza e compressione per il PDF di output.

La proprietà più importante è [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/), che consente di impostare il livello di conformità agli standard PDF. Attualmente, puoi salvare in formati PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab e PDF/A-3u. Nota che con il formato PDF/A, si ottiene una dimensione del file di output maggiore rispetto a un PDF normale.

#### **Salvataggio del foglio di lavoro in file PDF/A compilati**

Il frammento di codice sottostante mostra come usare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) per salvare i file Excel in formato PDF/A conforme allo standard PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-1.go" >}}
{{% alert color="primary" %}}

Si noti che la proprietà [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/) è stata aggiunta con il rilascio di Aspose.Cells for C++ 5.3.0.

{{% /alert %}}

#### **Imposta l'ora di creazione del PDF**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/), puoi ottenere o impostare l'orario di creazione del PDF. Il seguente codice dimostra l'uso della proprietà [**PdfSaveOptions.GetCreatedTime()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcreatedtime/) per impostare l'orario di creazione del file PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-2.go" >}}
#### **Imposta l'opzione ContentCopyForAccessibility**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/), puoi ottenere o impostare l'opzione [**GetAccessibilityExtractContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/getaccessibilityextractcontent/) del PDF per controllare l'accesso ai contenuti nel PDF convertito.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-3.go" >}}
#### **Esporta le proprietà personalizzate in PDF**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/), puoi esportare le proprietà personalizzate del workbook di origine nel PDF. È fornito l'enumeratore [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfcustompropertiesexport/) per specificare il metodo di esportazione delle proprietà. Queste proprietà possono essere osservate in Adobe Acrobat Reader cliccando su File e poi su Proprietà come mostrato nell'immagine seguente. Il file modello "sourceWithCustProps.xlsx" può essere scaricato [qui](sourceWithCustProps.xlsx) per test, e il file PDF di output "outSourceWithCustProps" è disponibile [qui](outSourceWithCustProps.pdf) per analisi.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-4.go" >}}
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

Se il tuo foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) subito prima di renderizzarlo in formato PDF. Questo assicura che i valori dipendenti dalle formule siano ricalcolati, e che i valori corretti vengano visualizzati nel PDF.

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
