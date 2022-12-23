---
title: Conversione della cartella di lavoro in diversi formati
type: docs
weight: 20
url: /it/java/converting-workbook-to-different-formats/
---
{{% alert color="primary" %}}

Aspose.Cells supporta la conversione tra molti formati. Tecnicamente, la conversione significa caricare una cartella di lavoro in un formato di file e salvarla in un altro.

{{% /alert %}}

## **Conversione di Excel in XPS**

Il formato del documento XPS consiste in un markup XML strutturato che definisce il layout di un documento e l'aspetto visivo di ogni pagina, insieme alle regole di rendering per la distribuzione, l'archiviazione, il rendering, l'elaborazione e la stampa dei documenti.

Il linguaggio di markup per XPS è un sottoinsieme di XAML che consente di incorporare elementi grafici vettoriali nei documenti, utilizzando XAML per contrassegnare le primitive Windows Presentation Foundation (WPF). Gli elementi utilizzati sono descritti in termini di percorsi e altre primitive geometriche.

Un file XPS è di fatto un archivio ZIP Unicoded che utilizza le Open Packaging Conventions, contenente i file che compongono il documento. Questi includono un file di markup XML per ogni pagina, testo, caratteri incorporati, immagini raster, grafica vettoriale 2D, nonché informazioni sulla gestione dei diritti digitali. Il contenuto di un file XPS può essere esaminato semplicemente aprendolo in un'applicazione che supporti i file ZIP.

Da Aspose.Cells 6.0.0, Microsoft Excel tp XPS la conversione è supportata.

### **Conversione di un singolo foglio di lavoro in XPS**

L'esempio seguente mostra come convertire un singolo foglio di lavoro in un file Excel in XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Esporta l'intera cartella di lavoro in XPS**

L'esempio seguente mostra come convertire l'intera cartella di lavoro nel formato XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Conversione rapida da Excel a XPS**

L'esempio seguente mostra un modo semplice per convertire direttamente il file Excel nel formato XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Conversione di Excel in file MHTML**

[MHTML](https://en.wikipedia.org/wiki/MHTML) combina il normale HTML con risorse esterne; ovvero contenuto che di solito è collegato in immagini, animazioni, audio e così via in un unico file. Sono utilizzati per le e-mail con estensione file .mht.

{{% alert color="primary" %}}

Aspose.Cells supporta la lettura e la scrittura di file MHTML.

{{% /alert %}}

La conversione di un foglio di calcolo in MHTML è un'operazione rapida, come mostrato di seguito.

L'esempio di codice seguente mostra come salvare una cartella di lavoro come file MHTML.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Conversione di file Excel in HTML**

 Le API Aspose.Cells forniscono supporto per l'esportazione di fogli di calcolo nel formato HTML. A tale scopo Aspose.Cells utilizza il**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**class che consente agli sviluppatori di controllare diversi aspetti dell'output HTML.

Il codice seguente mostra come utilizzare il**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**class per esportare i file Excel Microsoft nel formato HTML senza specificare parametri aggiuntivi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

 Puoi ottenere gli stessi risultati passando il file**[SaveFormat.HTML](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)** al**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** metodo.

{{% /alert %}}

### **Impostazione delle preferenze immagine per HTML**

 A partire dalla 8.0.2, Aspose.Cells ha esposto**[ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**per il**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**class, che consente agli sviluppatori di specificare le preferenze delle immagini durante il salvataggio dei fogli di calcolo nel formato HTML.

Le impostazioni dell'immagine che possono essere applicate sono:

- **[ImageType](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType)**: Ottiene o imposta il tipo di immagine. Tieni presente che tutte le forme, inclusi i grafici, vengono visualizzate come immagini nell'output HTML.
- **[Qualità](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality)**: Ottiene o imposta la qualità delle immagini tra 0 e 100, quando ImageFormat è specificato come Jpeg.
- **[Risoluzione verticale](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution)**: Ottiene o imposta la risoluzione verticale dell'immagine in punti per pollice.
- **[Risoluzione orizzontale](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Risoluzioneorizzontale)**: Ottiene o imposta la risoluzione orizzontale dell'immagine in punti per pollice.
- **[TiffCompression](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression)**Ottiene o imposta il tipo di compressione per le immagini quando ImageFormat è specificato come Tiff.
- **[Trasparente](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)**: Indica se lo sfondo di un'immagine deve essere trasparente quando ImageFormat è specificato come Png.

 Il codice seguente mostra come utilizzare**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)** per specificare preferenze diverse.

|**Visualizzazione foglio di calcolo prima dell'esportazione**|**HTML vista dopo l'esportazione**|
|:- |:- |
|![Visualizzazione foglio di calcolo prima dell'esportazione](converting-workbook-to-different-formats_1.png)|![HTML vista dopo l'esportazione](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Conversione di Excel in file PDF**

I documenti PDF sono ampiamente utilizzati come formato standard per lo scambio di documenti tra organizzazioni, settori governativi e individui. Agli sviluppatori di software viene spesso chiesto di trovare un modo per convertire facilmente i file Excel Microsoft in documenti PDF. Aspose.Cells supporta queste funzionalità. Questo articolo mostra come.

### **Conversione di Excel in PDF**

Microsoft La conversione da Excel a PDF è stata introdotta con Aspose.Cells for Java 2.3.0. Da quella versione, Aspose.Cells può[convertire direttamente i fogli di calcolo in PDF](#direct-conversion) (Compreso[PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files) ), senza un altro prodotto. Per convertire fogli di calcolo con versioni precedenti di Aspose.Cells,[utilizzare Aspose.PDF per la conversione](#conversion-with-asposepdf-asposecells-prior-to-230).

 Aspose.Cell's converte i fogli di calcolo in PDF con un alto grado di accuratezza e fedeltà. Tuttavia, ce ne sono alcuni[limitazioni](/cells/it/java/converting-workbook-to-different-formats/#conversion-attributes), elencati alla fine di questo articolo.

{{% alert color="primary" %}}

 Aspose.Cells for Java scrive direttamente le informazioni su API e il numero di versione nei documenti di output. Ad esempio, dopo aver reso Document to PDF, Aspose.Cells for Java popola**Applicazione** campo con valore 'Aspose.Cells' e**PDF Produttore** campo con un valore, ad esempio 'Aspose.Cells for Java v17.9'.

Si prega di notare che non è possibile incaricare Aspose.Cells for Java di modificare o rimuovere queste informazioni dai documenti di output.

{{% /alert %}}

#### **Conversione diretta**

Salva un file Excel direttamente su PDF utilizzando il**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** metodo e fornire il**[SaveFormat.PDF](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)**membro dell'interfaccia. La conversione diretta come questa è il metodo di conversione più efficiente. Non perde dati o formattazione ma mantiene l'output PDF simile al file Excel di input.

 Per specificare le opzioni di sicurezza durante il salvataggio in PDF, utilizzare**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Conversione avanzata**

Puoi anche scegliere di utilizzare il**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** class per impostare diversi attributi per la conversione. Impostazione di diverse proprietà di**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** class ti darà il controllo sulle impostazioni di stampa, carattere, sicurezza e compressione per il file PDF risultante. La proprietà più notevole è il**[Conformità](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**che consente di salvare i file Excel in file PDF compatibili con PDF/A.

##### **Salvataggio di fogli di calcolo Excel in file conformi PDF/A**

Il frammento di codice fornito di seguito dimostra l'utilizzo di**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** class per salvare i file Excel nel formato PDF compatibile con PDF/A.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Conversione con Aspose.Pdf: Aspose.Cells Prima della 2.3.0**

 Per le versioni Aspose.Cells precedenti alla versione 2.3.0 è necessario utilizzare un componente come[Aspose.PDF for Java](/pdf/java/)per convertire fogli di calcolo in file PDF. Aspose.Cells e Aspose.PDF lavorano insieme per convertire un foglio di calcolo in PDF tramite un passaggio intermedio.

Per convertire i fogli di calcolo in PDF con Aspose.Cells e Aspose.PDF:

1.  Istanziare un oggetto di**[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**class chiamando il suo costruttore vuoto.
1. Esegui il lavoro desiderato sul foglio di calcolo utilizzando Aspose.Cells API.
1. Chiama il**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**metodo per salvare il foglio di calcolo:
 1. Impostare il formato del file su XML.
 1. Selezionare Aspose_Pdf (un valore predefinito) dall'interfaccia FileFormatType. Questo dirige il metodo di salvataggio per generare un foglio di calcolo nel formato XML compatibile con lo schema Aspose.PDF in modo che Aspose.PDF for Java possa quindi generare un documento PDF.
1. Quando il file XML è stato creato, creare un oggetto della classe Pdf nel pacchetto aspose.pdf.
1. Chiama il metodo bindXML della classe Pdf e passa il nome del file XML di output.
1. Chiama il metodo save della classe Pdf per generare il documento PDF.

I passaggi precedenti sono implementati di seguito in un esempio.

{{% alert color="primary" %}}

Se il tuo foglio di calcolo contiene formule, è meglio chiamare**[Workbook.calculateFormula](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())** metodo appena prima di eseguire il rendering del foglio di calcolo nel formato PDF. In questo modo si assicurerà che i valori dipendenti dalla formula vengano ricalcolati e che i valori corretti vengano visualizzati in PDF.

{{% /alert %}}

#### **Attributi di conversione**

Lavoriamo sodo per migliorare la conversione e altri aspetti di Aspose.Cells con ogni versione. La conversione da Excel a PDF presenta alcune limitazioni. Alcune impostazioni di formato specificate in un foglio di calcolo potrebbero andare perdute e non tutti gli oggetti di disegno sono supportati.

La tabella seguente elenca tutte le funzionalità supportate in tutto o in parte durante l'esportazione in PDF utilizzando Aspose.Cells. Questa tabella non è definitiva e non copre tutti gli attributi del foglio di calcolo. Può anche identificare quelle funzionalità che potrebbero non essere supportate o sono parzialmente supportate per la conversione.

{{% alert color="primary" %}}

|**Elemento documento**|**Attributo**|**Rete supportata**|**Appunti**|
|:- |:- |:- |:- |
|Allineamento||sì||
|Rotazione||Parzialmente|Supporta solo 90 e -90.|
|Impostazioni dello sfondo||sì||
|Frontiera|Colore|sì||
|Frontiera|Stile linea|sì||
|Frontiera|Larghezza della linea|sì||
|Cell Dati||sì||
|Commenti||No||
|Formattazione condizionale||sì||
|Proprietà del documento||sì||
|Oggetti di disegno||sì||
|Font|Misurare|sì||
|Font|Colore|sì||
|Font|Stile|sì||
|Font|Sottolineare|sì||
|Font|Effetti|Parzialmente|È supportato solo l'effetto barrato|
|immagini||sì||
|Collegamento ipertestuale||sì||
|Grafici||sì||
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
{{% /alert %}}
