---
title: Pdf
type: docs
weight: 220
url: /it/python-net/convert-excel-to-pdf/
description: Scopri come convertire Excel in PDF con Aspose.Cells for Python via .NET API.
keywords: Python converT Excel to PDF, ConverT Excel to PDF using Python, Python save Excel to PDF, Excel to PDF in Python
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET supporta la conversione della cartella di lavoro di Excel in PDF. In questo esempio, vedremo la conversione completa di una cartella di lavoro di Excel in PDF.

{{% /alert %}}

##  **Conversione della cartella di lavoro Excel in PDF**

I file PDF sono ampiamente utilizzati per scambiare documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e agli sviluppatori di software viene spesso chiesto di trovare un modo per convertire i file Excel Microsoft in documenti PDF.

Aspose.Cells for Python via .NET supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET scrive direttamente le informazioni su API e il numero di versione nei documenti di output. Ad esempio, dopo aver eseguito il rendering del documento su PDF, Aspose.Cells for Python via .NET viene popolato**PDF Produttore** campo con valore, ad esempio 'Aspose.Cells for Python via .NET v23.2'.

 Tieni presente che puoi modificare queste informazioni nei documenti di output tramite**[PdfSaveOptions.producer](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/)** proprietà.

{{% /alert %}}

###  **Conversione diretta**

 Aspose.Cells for Python via .NET supporta la conversione da fogli di calcolo a PDF indipendentemente da altri software. Salva semplicemente un file Excel su PDF utilizzando il file**[Cartella di lavoro](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**classe'**[salva](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)** metodo. IL**[salva](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)** il metodo fornisce il file**[SaveFormat.PDF](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**membro di enumerazione che converte i file Excel nativi nel formato PDF.

Segui i passaggi seguenti per convertire direttamente i fogli di calcolo Excel nel formato PDF:

1.  Istanziare un oggetto di**[Cartella di lavoro](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**class chiamando il suo costruttore vuoto.
1. Puoi aprire/caricare un file modello esistente o saltare questo passaggio se stai creando la cartella di lavoro da zero.
1. Esegui qualsiasi operazione (inserisci dati, applica formattazione, imposta formule, inserisci immagini o altri oggetti di disegno e così via) sul foglio di calcolo utilizzando le API Aspose.Cells for Python via .NET'.
1.  Una volta completato il codice del foglio di calcolo, chiamare il**[Cartella di lavoro](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**classe'**[salva](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)**metodo per salvare il foglio di calcolo.

 Il formato del file dovrebbe essere PDF quindi seleziona*PDF* (un valore predefinito) da**[SaveFormat](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**enumerazione per generare il documento finale PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

###  **Conversione avanzata**

 Puoi anche scegliere di utilizzare il file**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** classe per impostare attributi diversi per la conversione. Impostazione di diverse proprietà di**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** ti dà il controllo sulle impostazioni di stampa, carattere, sicurezza e compressione per l'output PDF. La proprietà più importante è**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)**che consente di salvare i file Excel in file PDF conformi a PDF/A.

####  **Salvataggio della cartella di lavoro in file conformi PDF/A**

 Il frammento di codice fornito di seguito illustra come utilizzare il file**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**classe per salvare i file Excel nel formato PDF compatibile con PDF/A.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Si prega di notare che**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)**la proprietà è stata aggiunta con il rilascio di Aspose.Cells for Python via .NET for .NET 5.3.0.

{{% /alert %}}

####  **Imposta l'ora di creazione PDF**

 Con il**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**class, puoi ottenere o impostare l'ora di creazione PDF. Il codice seguente illustra l'utilizzo di**[PdfSaveOptions.created_time](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/)** proprietà per impostare l'ora di creazione del file PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

####  **Imposta l'opzione ContentCopyForAccessibility**

Con il**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** class, puoi ottenere o impostare PDF**[PdfSecurityOptions.accessibility_extract_content](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/)** opzione per controllare l'accesso al contenuto nel convertito PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

####  **Esporta proprietà personalizzate a PDF**

Con il**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** class, è possibile esportare le proprietà personalizzate nella cartella di lavoro di origine in PDF.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/)**viene fornito un enumeratore per specificare il modo in cui le proprietà vengono esportate. Queste proprietà possono essere osservate in Adobe Acrobat Reader facendo clic su File e quindi sull'opzione Proprietà come mostrato nell'immagine seguente. È possibile scaricare il file modello "sourceWithCustProps.xlsx".[Qui](sourceWithCustProps.xlsx) per il test e l'output PDF è disponibile il file "outSourceWithCustProps"[Qui](outSourceWithCustProps.pdf) per analisi.

![cose da fare:immagine_alt_testo](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

###  **Attributi di conversione**

Lavoriamo per migliorare le funzionalità di conversione con ogni nuova versione. La conversione da Excel a PDF di Aspose.Cell presenta ancora un paio di limitazioni. MapChart non è supportato durante la conversione nel formato PDF. Inoltre, alcuni oggetti di disegno non sono supportati correttamente.

La tabella che segue elenca tutte le funzionalità che sono completamente o parzialmente supportate durante l'esportazione a PDF utilizzando Aspose.Cells for Python via .NET. Questa tabella non è definitiva e non copre tutti gli attributi del foglio di calcolo ma identifica le funzionalità che non sono supportate o sono parzialmente supportate per la conversione allo PDF.

|**Elemento del documento**|**Attributo**|**Supportato**|**Appunti**|
| :- | :- | :- | :- |
|Allineamento| |SÌ| |
|Impostazioni dello sfondo| |SÌ| |
|Confine|Colore|SÌ| |
|Confine|Stile della linea|SÌ| |
|Confine|Larghezza della linea|SÌ| |
|Cell Dati| |SÌ| |
|Commenti| |SÌ| |
|Formattazione condizionale| |SÌ| |
|Proprietà del documento| |SÌ| |
|Oggetti di disegno| |Parzialmente|Gli effetti ombra e 3D per gli oggetti di disegno non sono supportati adeguatamente; WordArt e SmartArt sono parzialmente supportati.|
|Font|Misurare|SÌ| |
|Font|Colore|SÌ| |
|Font|Stile|SÌ| |
|Font|Sottolineare|SÌ| |
|Font|Effetti|SÌ||
|immagini| |SÌ| |
|Collegamento ipertestuale| |SÌ| |
|Grafici| |Parzialmente|MapChart non è supportato.|
|Unito Cells| |SÌ| |
|Interruzione di pagina| |SÌ| |
|Impostazione della pagina|Intestazione/piè di pagina|SÌ| |
|Impostazione della pagina|Margini|SÌ| |
|Impostazione della pagina|Orientamento della pagina|SÌ| |
|Impostazione della pagina|Dimensioni della pagina|SÌ| |
|Impostazione della pagina|Area di stampa|SÌ| |
|Impostazione della pagina|Stampa titoli|SÌ| |
|Impostazione della pagina|Ridimensionamento|SÌ| |
|Altezza riga/Larghezza colonna| |SÌ| |
|Lingua RTL (da destra a sinistra).| |SÌ| |

{{% alert color="primary" %}}

 Se il tuo foglio di calcolo contiene formule, è meglio chiamare[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)metodo appena prima di eseguire il rendering del foglio di calcolo nel formato PDF. In questo modo si garantirà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}

##  **Argomenti avanzati**
- [Aggiungi PDF Segnalibri](/cells/it/python-net/add-pdf-bookmarks/)
- [Aggiungi PDF Segnalibri con destinazioni denominate](/cells/it/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Evita la pagina vuota nell'output PDF quando non c'è nulla da stampare](/cells/it/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Converti il file XLSX nel formato PDF](/cells/it/python-net/convert-xlsx-file-to-pdf-format/)
- [Converti file Excel nel formato PDF compatibile con PDFA-1a](/cells/it/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Converti file XLS con immagini o grafici in PDF](/cells/it/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Crea PdfBookmarkEntry per il foglio grafico](/cells/it/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Adatta tutte le colonne del foglio di lavoro sulla singola pagina PDF](/cells/it/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ignora gli errori durante il rendering di Excel su PDF](/cells/it/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limita il numero di pagine generate - Conversione Excel a PDF](/cells/it/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Stampa commenti salvando allo PDF](/cells/it/python-net/print-comments-while-saving-to-pdf/)
- [Eseguire il rendering dei componenti aggiuntivi di Office durante la conversione di Excel in PDF](/cells/it/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Visualizza una pagina PDF per foglio di lavoro Excel - Conversione da Excel a PDF](/cells/it/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Render Unicode Caratteri supplementari nell'output PDF di Aspose.Cells](/cells/it/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Ricampionamento delle immagini aggiunte: conversione da Excel a PDF](/cells/it/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Salva ogni foglio di lavoro in un file PDF diverso](/cells/it/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Salva Excel in PDF con dimensione standard o minima](/cells/it/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Salva i fogli di lavoro specificati al numero PDF](/cells/it/python-net/save-specified-worksheets-to-pdf/)
- [Proteggi i documenti PDF](/cells/it/python-net/secure-pdf-documents/)
- [Specificare come incrociare la stringa nell'output PDF e nell'immagine](/cells/it/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
