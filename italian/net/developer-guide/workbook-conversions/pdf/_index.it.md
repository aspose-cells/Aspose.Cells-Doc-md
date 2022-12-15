---
title: PDF
type: docs
weight: 220
url: /it/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells supporta la conversione della cartella di lavoro di Excel in PDF. In questo esempio, vedremo la conversione completa di una cartella di lavoro Excel in PDF.

{{% /alert %}}

## **Conversione della cartella di lavoro di Excel in PDF**

I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e agli sviluppatori di software viene spesso chiesto di trovare un modo per convertire i file Microsoft Excel in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{% alert color="primary" %}}

 Aspose.Cells for .NET scrive direttamente le informazioni sull'API e il numero di versione nei documenti di output. Ad esempio, dopo il rendering del documento in PDF, Aspose.Cells for .NET viene popolato**Applicazione** campo con valore 'Aspose.Cells' e**Produttore PDF**campo con valore, ad esempio 'Aspose.Cells v17.9'.

Si prega di notare che non è possibile incaricare Aspose.Cells for .NET di modificare o rimuovere queste informazioni dai documenti di output.

{{% /alert %}}

### **Conversione diretta**

 Aspose.Cells for .NET supporta la conversione da fogli di calcolo a PDF indipendentemente da altri software. Basta salvare un file Excel in PDF utilizzando il formato**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** classe'**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** metodo. Il**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** metodo fornisce il**[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**membro di enumerazione che converte i file Excel nativi in formato PDF.

Segui i passaggi seguenti per convertire direttamente i fogli di calcolo Excel in formato PDF:

1.  Istanziare un oggetto di**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)**class chiamando il suo costruttore vuoto.
1. Puoi aprire/caricare un file modello esistente o saltare questo passaggio se stai creando la cartella di lavoro da zero.
1. Eseguire qualsiasi lavoro (dati di input, applicare formattazione, impostare formule, inserire immagini o altri oggetti di disegno e così via) sul foglio di calcolo utilizzando le API Aspose.Cells.
1.  Quando il codice del foglio di calcolo è completo, chiama il**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** classe'**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**metodo per salvare il foglio di calcolo.

 Il formato del file deve essere PDF, quindi selezionalo*PDF* (un valore predefinito) da**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**enumerazione per generare il documento PDF finale.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **Conversione avanzata**

 Puoi anche scegliere di utilizzare il**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class per impostare diversi attributi per la conversione. Impostazione di diverse proprietà del file**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class ti dà il controllo sulle impostazioni di stampa, carattere, sicurezza e compressione per il PDF di output. La proprietà più importante è**[Conformità](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**che consente di salvare i file Excel in file PDF compatibili con PDF/A.

#### **Salvataggio della cartella di lavoro in file PDF/A conformi**

 Il frammento di codice fornito di seguito mostra come utilizzare il file**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**class per salvare i file Excel in formato PDF compatibile con PDF/A.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

 Si prega di notare, il**[Conformità](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**proprietà è stata aggiunta con il rilascio di Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

#### **Imposta l'ora di creazione del PDF**

 Con il**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**class, è possibile ottenere o impostare l'ora di creazione del PDF. Il codice seguente illustra l'uso di**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** proprietà per impostare l'ora di creazione del file PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **Imposta l'opzione ContentCopyForAccessibility**

Con il**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class, è possibile ottenere o impostare il PDF**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)** opzione per controllare l'accesso al contenuto nel PDF convertito.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **Esporta le proprietà personalizzate in PDF**

Con il**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class, è possibile esportare le proprietà personalizzate nella cartella di lavoro di origine nel PDF.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**enumeratore viene fornito per specificare il modo in cui le proprietà vengono esportate. Queste proprietà possono essere osservate in Adobe Acrobat Reader facendo clic su File e quindi sull'opzione proprietà come mostrato nell'immagine seguente. È possibile scaricare il file modello "sourceWithCustProps.xlsx".[qui](sourceWithCustProps.xlsx) per il test e l'output è disponibile il file PDF "outSourceWithCustProps".[qui](outSourceWithCustProps.pdf) per analisi.

![cose da fare:immagine_alt_testo](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **Attributi di conversione**

Lavoriamo per migliorare le funzionalità di conversione con ogni nuova versione. La conversione da Excel a PDF di Aspose.Cell ha ancora un paio di limitazioni. La formattazione di alcuni fogli di calcolo potrebbe andare persa durante la conversione in formato PDF. Inoltre, alcuni oggetti di disegno non sono ancora supportati.

La tabella che segue elenca tutte le funzionalità supportate in tutto o in parte durante l'esportazione in PDF utilizzando Aspose.Cells. Questa tabella non è definitiva e non copre tutti gli attributi del foglio di calcolo, ma identifica le funzionalità che non sono supportate o parzialmente supportate per la conversione in PDF .

|**Elemento documento**|**Attributo**|**Supportato**|**Appunti**|
|:- |:- |:- |:- |
|Allineamento||sì||
|Impostazioni dello sfondo||sì||
|Confine|Colore|sì||
|Confine|Stile linea|sì||
|Confine|Larghezza della linea|sì||
|Cell Dati||sì||
|Commenti||sì||
|Formattazione condizionale||sì||
|Proprietà del documento||sì||
|Oggetti di disegno||Parzialmente|Oggetti supportati: TextBox, Line, Rectangle, Oval, GroupBox, Button, CheckBox, RadioButton, ListBox, ComboBox, Label|
|Font|Dimensione|sì||
|Font|Colore|sì||
|Font|Stile|sì||
|Font|Sottolineare|sì||
|Font|Effetti|Parzialmente|È supportato solo l'effetto barrato|
|immagini||sì||
|Collegamento ipertestuale||sì||
|Grafici||Parzialmente||
|Unito Cells||sì||
|Interruzione di pagina||sì||
|Impostazione della pagina|Intestazione/piè di pagina|sì||
|Impostazione della pagina|Margini|sì||
|Impostazione della pagina|Orientamento della pagina|sì||
|Impostazione della pagina|Dimensioni della pagina|sì||
|Impostazione della pagina|Area di stampa|sì||
|Impostazione della pagina|Stampa titoli|sì||
|Impostazione della pagina|Ridimensionamento|sì||
|Altezza riga/Larghezza colonna||sì||
|Lingua RTL (da destra a sinistra).||sì||

{{% alert color="primary" %}}

 Se il tuo foglio di calcolo contiene formule, è meglio chiamare**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)** appena prima di eseguire il rendering del foglio di calcolo in formato PDF. In questo modo si assicurerà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati nel PDF.

{{% /alert %}}

## **Argomenti avanzati**
- [Aggiungi segnalibri PDF](/cells/it/net/add-pdf-bookmarks/)
- [Aggiungi segnalibri PDF con destinazioni denominate](/cells/it/net/add-pdf-bookmarks-with-named-destinations/)
- [Evita la pagina vuota nel PDF di output quando non c'è niente da stampare](/cells/it/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Cambia il carattere solo sui caratteri Unicode specifici durante il salvataggio in PDF](/cells/it/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Controlla il caricamento delle risorse esterne nella cartella di lavoro MS Excel durante il rendering in PDF](/cells/it/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Converti un file XLS in formato PDF](/cells/it/net/convert-an-xls-file-to-pdf-format/)
- [Converti file Excel in formato PDF compatibile con PDFA-1a](/cells/it/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Converti file XLS con immagini o grafici in PDF](/cells/it/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Crea PdfBookmarkEntry per il foglio grafico](/cells/it/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Adatta tutte le colonne del foglio di lavoro su una singola pagina PDF](/cells/it/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ottieni DrawObject e Bound durante il rendering in PDF utilizzando la classe DrawObjectEventHandler](/cells/it/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Ricevi avvisi per la sostituzione dei caratteri durante il rendering del file Excel](/cells/it/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignora gli errori durante il rendering di Excel in PDF](/cells/it/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limita il numero di pagine generate - Conversione da Excel a PDF](/cells/it/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Stampa commenti durante il salvataggio in PDF](/cells/it/net/print-comments-while-saving-to-pdf/)
- [Renderizza i componenti aggiuntivi di Office durante la conversione di Excel in PDF](/cells/it/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendering di una pagina PDF per foglio di lavoro Excel - Conversione da Excel a PDF](/cells/it/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Renderizza i caratteri supplementari Unicode nel PDF di output di Aspose.Cells](/cells/it/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Ricampionamento delle immagini aggiunte - Conversione da Excel a PDF](/cells/it/net/resampling-added-images-excel-to-pdf-conversion/)
- [Salva ogni foglio di lavoro in un file PDF diverso](/cells/it/net/save-each-worksheet-to-a-different-pdf-file/)
- [Salva Excel in PDF con dimensione standard o minima](/cells/it/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Proteggi i documenti PDF](/cells/it/net/secure-pdf-documents/)
- [Specificare come incrociare la stringa nel PDF di output e nell'immagine](/cells/it/net/specify-how-to-cross-string-in-output-pdf-and-image/)
