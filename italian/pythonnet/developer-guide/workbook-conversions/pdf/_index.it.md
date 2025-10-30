---
title: Pdf
type: docs
weight: 220
url: /it/python-net/convert-excel-to-pdf/
description: Scopri come convertire Excel in PDF con l API Aspose.Cells for Python via .NET.
keywords: Converti Excel in PDF con Python, Converti Excel in PDF usando Python, Salva Excel in PDF in Python, Excel in PDF con Python
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET supporta la conversione di un Workbook di Excel in PDF. In questo esempio, vedremo la completa conversione di un Workbook di Excel in PDF.

{{% /alert %}}

## **Conversione di un Workbook Excel in PDF**

I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e spesso agli sviluppatori software viene chiesto di trovare un modo per convertire i file Microsoft Excel in documenti PDF.

Aspose.Cells for Python via .NET supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET scrive direttamente le informazioni sull'API e sul numero di versione nei documenti di output. Ad esempio, al momento del rendering di un Document in PDF, Aspose.Cells for Python via .NET popola il campo **Produttore PDF** con il valore, ad es. 'Aspose.Cells for Python via .NET v23.2'.

Si noti che è possibile modificare queste informazioni nei documenti di output tramite la proprietà [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/).

{{% /alert %}}

### **Conversione Diretta**

Aspose.Cells for Python via .NET supporta la conversione da fogli di calcolo a PDF indipendentemente da altri software. Basta salvare un file Excel in PDF utilizzando il metodo [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Il metodo [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) fornisce l'elemento di enumerazione [**SaveFormat.PDF**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) che converte i file nativi di Excel nel formato PDF.

Seguire i seguenti passi per convertire direttamente i fogli di calcolo Excel in formato PDF:

1. Istituire un oggetto della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) chiamando il suo costruttore vuoto.
2. È possibile aprire/caricare un file di modello esistente o saltare questo passo se si sta creando il workbook da zero.
1. Eseguire qualsiasi lavoro (inserire dati, applicare formattazione, impostare formule, inserire immagini o altri oggetti grafici e così via) nel foglio di calcolo utilizzando le API Aspose.Cells per Python via .NET.
1. Quando il codice del foglio di calcolo è completo, chiamare il metodo [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) della classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) per salvare il foglio di calcolo.

Il formato del file dovrebbe essere PDF, quindi selezionare *PDF* (un valore predefinito) dall'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) per generare il documento PDF finale.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

### **Conversione Avanzata**

È anche possibile scegliere di utilizzare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) per impostare diversi attributi per la conversione. Impostare diverse proprietà della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) ti offre il controllo sulle impostazioni di stampa, font, sicurezza e compressione per il PDF in uscita. La proprietà più importante è [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/), che consente di salvare i file Excel in file PDF/A conformi.

#### **Salvataggio del foglio di lavoro in file PDF/A compilati**

Il frammento di codice fornito di seguito dimostra come utilizzare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) per salvare i file Excel in formato PDF/A conforme.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Si prega di notare che la proprietà [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) è stata aggiunta con il rilascio di Aspose.Cells per Python via .NET per .NET 5.3.0.

{{% /alert %}}

#### **Imposta l'ora di creazione del PDF**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions), è possibile ottenere o impostare l'ora di creazione del PDF. Il codice seguente dimostra l'uso della proprietà [**PdfSaveOptions.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/) per impostare l'ora di creazione del file PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

#### **Imposta l'opzione ContentCopyForAccessibility**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions), è possibile ottenere o impostare l'opzione [**PdfSecurityOptions.accessibility_extract_content**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/) del PDF per controllare l'accesso ai contenuti nel PDF convertito.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

#### **Esporta le proprietà personalizzate in PDF**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions), è possibile esportare le proprietà personalizzate nel foglio di lavoro di origine nel PDF. L'enumeratore [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/) è fornito per specificare il modo in cui vengono esportate le proprietà. Queste proprietà possono essere visualizzate in Adobe Acrobat Reader facendo clic su File e poi sull'opzione proprietà come mostrato nell'immagine seguente. Il file modello "sourceWithCustProps.xlsx" può essere scaricato [qui](sourceWithCustProps.xlsx) per testare, e il file PDF di output "outSourceWithCustProps" è disponibile [qui](outSourceWithCustProps.pdf) per l'analisi.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

### **Attributi di Conversione**

Lavoriamo per migliorare le funzionalità di conversione con ogni nuova versione. La conversione da Excel a PDF di Aspose.Cell ha ancora un paio di limitazioni. MapChart non è supportato quando si converte in formato PDF. Inoltre, alcuni oggetti grafici non sono ben supportati.

La tabella che segue elenca tutte le funzionalità completamente o parzialmente supportate quando si esporta in PDF utilizzando Aspose.Cells per Python via .NET. Questa tabella non è definitiva e non copre tutti gli attributi del foglio di calcolo, ma identifica le funzionalità non supportate o parzialmente supportate per la conversione in PDF.

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

Se il tuo foglio di calcolo contiene formule, è meglio chiamare il metodo [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) appena prima di rappresentare il foglio di calcolo nel formato PDF. Così facendo, garantirai che i valori dipendenti dalla formula vengano ricalcolati e i valori corretti vengano rappresentati nel PDF.

{{% /alert %}}

## **Argomenti avanzati**
- [Aggiungi segnalibri PDF](/cells/it/python-net/add-pdf-bookmarks/)
- [Aggiungi Segnalibri PDF con Destinazioni con Nome](/cells/it/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Evitare Pagina Vuota nel PDF di Output quando non c'è Nulla da Stampare](/cells/it/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Converti file XLSX in formato PDF](/cells/it/python-net/convert-xlsx-file-to-pdf-format/)
- [Convertire file Excel in formato PDF compatibile con PDFA-1a](/cells/it/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Converti file XLS con immagini o grafici in PDF](/cells/it/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Crea PdfBookmarkEntry per Chart Sheet](/cells/it/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Adatta tutte le colonne del foglio di calcolo in una singola pagina PDF](/cells/it/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ignora gli errori durante la conversione di Excel in PDF](/cells/it/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limita il numero di pagine generate - Conversione da Excel a PDF](/cells/it/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Stampa commenti durante il salvataggio in PDF](/cells/it/python-net/print-comments-while-saving-to-pdf/)
- [Render Office Add-Ins durante la conversione di Excel in PDF](/cells/it/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendi una pagina PDF per ogni foglio di lavoro Excel - Conversione da Excel a PDF](/cells/it/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rende i Caratteri Unicode Supplementari nell'output PDF con Aspose.Cells](/cells/it/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Ridimensionamento delle immagini aggiunte - Conversione da Excel a PDF](/cells/it/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Salva ciascun foglio di calcolo in un file PDF separato](/cells/it/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Salva Excel in PDF con dimensioni standard o minime](/cells/it/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Salva fogli specificati in PDF](/cells/it/python-net/save-specified-worksheets-to-pdf/)
- [Documenti PDF sicuri](/cells/it/python-net/secure-pdf-documents/)
- [Specificare come incrociare la stringa nel PDF e nell'immagine di output](/cells/it/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="python-net" >}}
