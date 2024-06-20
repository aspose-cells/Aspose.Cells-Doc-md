---
title: Pdf
type: docs
weight: 220
url: /it/net/convert-excel-to-pdf/
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione del workbook di Excel in PDF. In questo esempio, vedremo la completa conversione di un workbook di Excel in PDF.

{{% /alert %}}

## **Conversione di un Workbook Excel in PDF**

I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e spesso agli sviluppatori software viene chiesto di trovare un modo per convertire i file Microsoft Excel in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{% alert color="primary" %}}

Aspose.Cells for .NET scrive direttamente le informazioni sull'API e il numero di versione nei documenti di output. Ad esempio, al momento del rendering del documento in PDF, Aspose.Cells for .NET popola il campo **Produttore PDF** con il valore, ad es. 'Aspose.Cells v23.2'.

Si noti che è possibile modificare queste informazioni nei documenti di output tramite la proprietà [**PdfSaveOptions.Producer**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/).

{{% /alert %}}

### **Conversione Diretta**

Aspose.Cells for .NET supporta la conversione da fogli di calcolo a PDF indipendentemente da altri software. Basta salvare un file di Excel in PDF utilizzando il metodo [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Il metodo [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) fornisce il membro di enumerazione [**SaveFormat.Pdf**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) che converte i file nativi di Excel nel formato PDF.

Seguire i seguenti passi per convertire direttamente i fogli di calcolo Excel in formato PDF:

1. Istituire un oggetto della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) chiamando il suo costruttore vuoto.
2. È possibile aprire/caricare un file di modello esistente o saltare questo passo se si sta creando il workbook da zero.
3. Eseguire qualsiasi lavoro (inserire dati, applicare formattazione, inserire formule, inserire immagini o altri oggetti grafici, ecc.) sul foglio di calcolo utilizzando le API di Aspose.Cells.
1. Quando il codice del foglio di calcolo è completo, chiamare il metodo [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) per salvare il foglio di calcolo.

Il formato del file dovrebbe essere PDF, quindi selezionare *Pdf* (un valore predefinito) dall'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) per generare il documento PDF finale.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **Conversione Avanzata**

È anche possibile optare per utilizzare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) per impostare attributi diversi per la conversione. Impostare diverse proprietà della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) consente di esercitare il controllo sulle impostazioni di stampa, carattere, sicurezza e compressione per l'output in PDF. 

La proprietà più importante è [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) che consente di impostare il livello di conformità agli standard PDF. Attualmente è possibile salvare in formati PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab e PDF/A-3u. Si noti che con il formato PDF/A, le dimensioni del file di output sono più grandi rispetto a un normale file PDF.

#### **Salvataggio del foglio di lavoro in file PDF/A compilati**

Il frammento di codice fornito di seguito dimostra come utilizzare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) per salvare i file Excel in formato PDF/A conforme.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

Si noti che la proprietà [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) è stata aggiunta con il rilascio di Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

#### **Imposta l'ora di creazione del PDF**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions), è possibile ottenere o impostare l'ora di creazione del PDF. Il codice seguente dimostra l'uso della proprietà [**PdfSaveOptions.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime) per impostare l'ora di creazione del file PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **Imposta l'opzione ContentCopyForAccessibility**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions), è possibile ottenere o impostare l'opzione [**AccessibilityExtractContent**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent) del PDF per controllare l'accesso ai contenuti nel PDF convertito.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **Esporta le proprietà personalizzate in PDF**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions), è possibile esportare le proprietà personalizzate nel foglio di lavoro di origine nel PDF. L'enumeratore [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport) è fornito per specificare il modo in cui vengono esportate le proprietà. Queste proprietà possono essere visualizzate in Adobe Acrobat Reader facendo clic su File e poi sull'opzione proprietà come mostrato nell'immagine seguente. Il file modello "sourceWithCustProps.xlsx" può essere scaricato [qui](sourceWithCustProps.xlsx) per testare, e il file PDF di output "outSourceWithCustProps" è disponibile [qui](outSourceWithCustProps.pdf) per l'analisi.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **Attributi di Conversione**

Lavoriamo per migliorare le funzionalità di conversione con ogni nuova versione. La conversione da Excel a PDF di Aspose.Cell ha ancora un paio di limitazioni. MapChart non è supportato quando si converte in formato PDF. Inoltre, alcuni oggetti grafici non sono ben supportati.

La tabella che segue elenca tutte le caratteristiche che sono completamente o parzialmente supportate durante l'esportazione in PDF utilizzando Aspose.Cells. Questa tabella non è definitiva e non copre tutti gli attributi del foglio di calcolo, ma identifica le funzionalità non supportate o parzialmente supportate per la conversione in PDF.

|**Elemento del Documento**|**Attributo**|**Supportato**|**Note**|
| :- | :- | :- | :- |
|Allineamento| |Sì| |
|Impostazioni sfondo| |Sì| |
|Bordo|Colore|Sì| |
|Bordo|Stile di linea|Sì| |
|Bordo|Spessore linea|Sì| |
|Dati della cella| |Sì| |
|Commenti| |Sì| |
|Formattazione condizionale| |Sì| |
|Proprietà del documento| |Sì| |
|Oggetti disegno| |Parzialmente|Effetti ombra e 3-D per gli oggetti di disegno non sono ben supportati; WordArt e SmartArt sono supportati parzialmente.|
|Carattere|Dimensione|Sì| |
|Carattere|Colore|Sì| |
|Carattere|Stile|Sì| |
|Carattere|Sottolineato|Sì| |
|Carattere|Effetti|Sì||
|Immagini| |Sì| |
|Collegamento ipertestuale| |Sì| |
|Grafici| |Parzialmente|MapChart non è supportato.|
|Celle unite| |Sì| |
|Interruzione di pagina| |Sì| |
|Impostazioni pagina|Intestazione/Piè di pagina|Sì| |
|Impostazioni pagina|Margini|Sì| |
|Impostazioni pagina|Orientamento pagina|Sì| |
|Impostazioni pagina|Formato pagina|Sì| |
|Impostazioni pagina|Area di stampa|Sì| |
|Impostazioni pagina|Titoli di stampa|Sì| |
|Impostazioni pagina|Scalatura|Sì| |
|Altezza riga/Larghezza colonna| |Sì| |
|Lingua RTL (da destra a sinistra)| |Sì| |

{{% alert color="primary" %}}

Se il tuo foglio di calcolo contiene formule, è meglio chiamare [**Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) appena prima di rendere il foglio di calcolo nel formato PDF. In questo modo assicurerai che i valori dipendenti dalle formule siano ricalcolati e i valori corretti siano resi nel PDF.

{{% /alert %}}

## **Argomenti avanzati**
- [Aggiungi segnalibri PDF](/cells/it/net/add-pdf-bookmarks/)
- [Aggiungi Segnalibri PDF con Destinazioni con Nome](/cells/it/net/add-pdf-bookmarks-with-named-destinations/)
- [Evitare Pagina Vuota nel PDF di Output quando non c'è Nulla da Stampare](/cells/it/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Modifica il carattere solo sui caratteri Unicode specifici durante il salvataggio in PDF](/cells/it/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Controlla il caricamento di Risorse Esterne nel Lavoro MS Excel mentre viene convertito in PDF](/cells/it/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Converti file XLSX in formato PDF](/cells/it/net/convert-xlsx-file-to-pdf-format/)
- [Convertire file Excel in formato PDF compatibile con PDFA-1a](/cells/it/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Converti file XLS con immagini o grafici in PDF](/cells/it/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Crea PdfBookmarkEntry per Chart Sheet](/cells/it/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Adatta tutte le colonne del foglio di calcolo in una singola pagina PDF](/cells/it/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ottieni DrawObject e Bound durante il rendering in PDF utilizzando la classe DrawObjectEventHandler](/cells/it/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Ottieni avvisi per la sostituzione del carattere mentre si rende il file Excel](/cells/it/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignora gli errori durante la conversione di Excel in PDF](/cells/it/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limita il numero di pagine generate - Conversione da Excel a PDF](/cells/it/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Stampa commenti durante il salvataggio in PDF](/cells/it/net/print-comments-while-saving-to-pdf/)
- [Render Office Add-Ins durante la conversione di Excel in PDF](/cells/it/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendi una pagina PDF per ogni foglio di lavoro Excel - Conversione da Excel a PDF](/cells/it/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rende i Caratteri Unicode Supplementari nell'output PDF con Aspose.Cells](/cells/it/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Ridimensionamento delle immagini aggiunte - Conversione da Excel a PDF](/cells/it/net/resampling-added-images-excel-to-pdf-conversion/)
- [Salva ciascun foglio di calcolo in un file PDF separato](/cells/it/net/save-each-worksheet-to-a-different-pdf-file/)
- [Salva Excel in PDF con dimensioni standard o minime](/cells/it/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Salva fogli specificati in PDF](/cells/it/net/save-specified-worksheets-to-pdf/)
- [Documenti PDF sicuri](/cells/it/net/secure-pdf-documents/)
- [Specificare come incrociare la stringa nel PDF e nell'immagine di output](/cells/it/net/specify-how-to-cross-string-in-output-pdf-and-image/)
