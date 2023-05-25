---
title: Pdf
type: docs
weight: 220
url: /it/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells supporta la conversione della cartella di lavoro di Excel in PDF. In questo esempio, vedremo la conversione completa di una cartella di lavoro di Excel in PDF.

{{% /alert %}}

##  **Conversione della cartella di lavoro di Excel in PDF**

file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e agli sviluppatori di software viene spesso chiesto di trovare un modo per convertire i file Excel Microsoft in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{% alert color="primary" %}}

 Aspose.Cells for .NET scrive direttamente le informazioni su API e il numero di versione nei documenti di output. Ad esempio, dopo aver reso Document to PDF, Aspose.Cells for .NET popola**PDF Produttore** campo con valore, ad esempio 'Aspose.Cells v23.2'.

 Si prega di notare che è possibile modificare queste informazioni nei documenti di output di**[PdfSaveOptions.Producer](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/)** proprietà.

{{% /alert %}}

###  **Conversione diretta**

Aspose.Cells for .NET supporta la conversione da fogli di calcolo a PDF indipendentemente da altri software. Basta salvare un file Excel in PDF utilizzando il file**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** classe'**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** metodo. IL**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** metodo fornisce il**[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**membro di enumerazione che converte i file Excel nativi nel formato PDF.

Segui i passaggi seguenti per convertire direttamente i fogli di calcolo Excel nel formato PDF:

1.  Istanziare un oggetto di**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)**class chiamando il suo costruttore vuoto.
1. Puoi aprire/caricare un file modello esistente o saltare questo passaggio se stai creando la cartella di lavoro da zero.
1. Eseguire qualsiasi lavoro (dati di input, applicare formattazione, impostare formule, inserire immagini o altri oggetti di disegno e così via) sul foglio di calcolo utilizzando le API Aspose.Cells.
1.  Quando il codice del foglio di calcolo è completo, chiama il**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** classe'**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**metodo per salvare il foglio di calcolo.

 Il formato del file dovrebbe essere PDF, quindi selezionalo*Pdf* (un valore predefinito) da**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**enumerazione per generare il documento PDF finale.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

###  **Conversione avanzata**

 Puoi anche scegliere di utilizzare il**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class per impostare diversi attributi per la conversione. Impostazione di diverse proprietà del file**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class ti dà il controllo sulle impostazioni di stampa, carattere, sicurezza e compressione per l'output PDF. La proprietà più importante è**[Conformità](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**che consente di salvare i file Excel in file PDF compatibili con PDF/A.

####  **Salvataggio della cartella di lavoro nei file conformi PDF/A**

 Il frammento di codice fornito di seguito mostra come utilizzare il file**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**class per salvare i file Excel nel formato PDF compatibile con PDF/A.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

 Si prega di notare, il**[Conformità](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**proprietà è stata aggiunta con il rilascio di Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

####  **Impostare l'ora di creazione PDF**

 Con il**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**class, puoi ottenere o impostare l'ora di creazione PDF. Il codice seguente illustra l'uso di**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** proprietà per impostare l'ora di creazione del file PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

####  **Imposta l'opzione ContentCopyForAccessibility**

Con il**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** classe, puoi ottenere o impostare lo PDF**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)**opzione per controllare l'accesso ai contenuti nel convertito PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

####  **Esporta proprietà personalizzate in PDF**

Con il**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class, è possibile esportare le proprietà personalizzate nella cartella di lavoro di origine nel file PDF.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)** enumeratore viene fornito per specificare il modo in cui le proprietà vengono esportate. Queste proprietà possono essere osservate in Adobe Acrobat Reader facendo clic su File e quindi sull'opzione proprietà come mostrato nell'immagine seguente. È possibile scaricare il file modello "sourceWithCustProps.xlsx".[Qui](sourceWithCustProps.xlsx) per il test e l'output PDF è disponibile il file "outSourceWithCustProps"[Qui](outSourceWithCustProps.pdf) per analisi.

![cose da fare:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

###  **Attributi di conversione**

Lavoriamo per migliorare le funzionalità di conversione con ogni nuova versione. La conversione di Excel da Aspose.Cell a PDF ha ancora un paio di limitazioni. La formattazione di alcuni fogli di calcolo potrebbe andare persa durante la conversione nel formato PDF. Inoltre, alcuni oggetti di disegno non sono ancora supportati.

La tabella che segue elenca tutte le funzionalità supportate in tutto o in parte durante l'esportazione in PDF utilizzando Aspose.Cells. Questa tabella non è definitiva e non copre tutti gli attributi del foglio di calcolo, ma identifica le funzionalità che non sono supportate o parzialmente supportate per la conversione in PDF .

|**Elemento documento**|**Attributo**|**Supportato**|**Appunti**|
| :- | :- | :- | :- |
|Allineamento| |SÌ| |
|Impostazioni dello sfondo| |SÌ| |
|Confine|Colore|SÌ| |
|Confine|Stile linea|SÌ| |
|Confine|Larghezza della linea|SÌ| |
|Cell Dati| |SÌ| |
|Commenti| |SÌ| |
|Formattazione condizionale| |SÌ| |
|Proprietà del documento| |SÌ| |
|Oggetti di disegno| |Parzialmente|Oggetti supportati: TextBox, Line, Rectangle, Oval, GroupBox, Button, CheckBox, RadioButton, ListBox, ComboBox, Label|
|Font|Misurare|SÌ| |
|Font|Colore|SÌ| |
|Font|Stile|SÌ| |
|Font|Sottolineare|SÌ| |
|Font|Effetti|Parzialmente|È supportato solo l'effetto barrato|
|immagini| |SÌ| |
|Collegamento ipertestuale| |SÌ| |
|Grafici| |Parzialmente||
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

 Se il tuo foglio di calcolo contiene formule, è meglio chiamare**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)** appena prima di eseguire il rendering del foglio di calcolo nel formato PDF. In questo modo si assicurerà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}

##  **Argomenti avanzati**
- [Aggiungi segnalibri PDF](/cells/it/net/add-pdf-bookmarks/)
- [Aggiungi segnalibri PDF con destinazioni con nome](/cells/it/net/add-pdf-bookmarks-with-named-destinations/)
- [Evitare pagine vuote nell'output PDF quando non c'è niente da stampare](/cells/it/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Cambia il carattere solo sui caratteri Unicode specifici durante il salvataggio in PDF](/cells/it/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Controlla il caricamento delle risorse esterne nella cartella di lavoro MS Excel durante il rendering su PDF](/cells/it/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Converti il file XLSX nel formato PDF](/cells/it/net/convert-xlsx-file-to-pdf-format/)
- [Converti il file Excel nel formato PDF compatibile con PDFA-1a](/cells/it/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Converti file XLS con immagini o grafici in PDF](/cells/it/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Crea PdfBookmarkEntry per il foglio grafico](/cells/it/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Adatta tutte le colonne del foglio di lavoro su una singola pagina PDF](/cells/it/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ottieni DrawObject e Bound durante il rendering su PDF utilizzando la classe DrawObjectEventHandler](/cells/it/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Ricevi avvisi per la sostituzione dei caratteri durante il rendering del file Excel](/cells/it/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignora gli errori durante il rendering di Excel a PDF](/cells/it/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limita il numero di pagine generate - Excel a PDF Conversione](/cells/it/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Stampa commenti salvando su PDF](/cells/it/net/print-comments-while-saving-to-pdf/)
- [Eseguire il rendering dei componenti aggiuntivi di Office durante la conversione di Excel in PDF](/cells/it/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendering di una pagina PDF per foglio di lavoro Excel - Conversione da Excel a PDF](/cells/it/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Renderizza i caratteri supplementari Unicode nell'output PDF per Aspose.Cells](/cells/it/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Ricampionamento delle immagini aggiunte - Conversione da Excel a PDF](/cells/it/net/resampling-added-images-excel-to-pdf-conversion/)
- [Salva ogni foglio di lavoro in un file PDF diverso](/cells/it/net/save-each-worksheet-to-a-different-pdf-file/)
- [Salva Excel in PDF con dimensione standard o minima](/cells/it/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Salva i fogli di lavoro specificati su PDF](/cells/it/net/save-specified-worksheets-to-pdf/)
- [Sicuro PDF Documenti](/cells/it/net/secure-pdf-documents/)
- [Specificare come incrociare la stringa nell'output PDF e nell'immagine](/cells/it/net/specify-how-to-cross-string-in-output-pdf-and-image/)
