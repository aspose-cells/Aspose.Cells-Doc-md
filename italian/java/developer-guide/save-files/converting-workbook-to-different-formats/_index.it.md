---
title: Conversione del foglio di lavoro in formati diversi
type: docs
weight: 20
url: /it/java/converting-workbook-to-different-formats/
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione tra molti formati. Tecnicamente, la conversione significa caricare una cartella di lavoro in un formato di file e salvarla in un altro.

{{% /alert %}}

## **Conversione di Excel in XPS**

Il formato del documento XPS è costituito da markup XML strutturato che definisce la disposizione di un documento e l'aspetto visivo di ogni pagina, insieme a regole di rendering per la distribuzione, l'archiviazione, il rendering, l'elaborazione e la stampa dei documenti.

Il linguaggio di markup per XPS è un sottoinsieme di XAML che consente di incorporare elementi grafici vettoriali nei documenti, utilizzando XAML per contrassegnare i primitivi della Windows Presentation Foundation (WPF). Gli elementi utilizzati sono descritti in termini di percorsi e di altri primitivi geometrici.

Un file XPS è in realtà un archivio ZIP Unicode che utilizza le convenzioni di imballaggio aperto, contenente i file che compongono il documento. Questi includono un file di markup XML per ogni pagina, testo, caratteri di stampa incorporati, immagini raster, grafica vettoriale 2D, nonché le informazioni sulla gestione dei diritti digitali. I contenuti di un file XPS possono essere esaminati semplicemente aprendolo in un'applicazione che supporta i file ZIP.

A partire da Aspose.Cells 6.0.0, è supportata la conversione di Microsoft Excel in XPS.

### **Conversione di un singolo foglio di lavoro in XPS**

L'esempio seguente mostra come convertire un singolo foglio di lavoro in un file Excel in XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Esporta l'intero foglio di lavoro in formato XPS**

L'esempio seguente mostra come convertire l'intero foglio di lavoro nel formato XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Conversione rapida di Excel in XPS**

L'esempio seguente mostra un modo semplice per convertire direttamente il file Excel nel formato XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Conversione di Excel in file MHTML**

[**MHTML**](https://en.wikipedia.org/wiki/MHTML) combina HTML normale con risorse esterne; ovvero, contenuti che di solito vengono collegati come immagini, animazioni, audio e così via in un unico file. Sono utilizzati per le e-mail con l'estensione del file .mht.

{{% alert color="primary" %}}

Aspose.Cells supporta la lettura e la scrittura dei file MHTML.

{{% /alert %}}

La conversione di un foglio di calcolo in MHTML è un'operazione veloce, come mostrato di seguito.

L'esempio di codice sotto mostra come salvare un workbook come file MHTML.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Conversione dei file Excel in HTML**

Le API di Aspose.Cells forniscono supporto per l'esportazione di fogli di calcolo in formato HTML. A questo scopo, Aspose.Cells utilizza la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) che consente ai programmatori di controllare diversi aspetti dell'HTML in uscita.

Il codice sottostante dimostra come utilizzare la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) per esportare file Microsoft Excel nel formato HTML senza specificare parametri aggiuntivi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

Si possono ottenere gli stessi risultati passando il [**SaveFormat.HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML) al metodo [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)).

{{% /alert %}}

### **Impostazione delle preferenze dell'immagine per HTML**

A partire dalla versione 8.0.2, Aspose.Cells ha esposto [**ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) per la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions), che consente ai programmatori di specificare le preferenze delle immagini durante il salvataggio dei fogli di calcolo nel formato HTML.

Le impostazioni dell'immagine che possono essere applicate sono:

- [**ImageType**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType): Ottiene o imposta il tipo di immagine. Si noti che tutte le forme, compresi i grafici, vengono renderizzate come immagini nell'HTML di output.
- [**Quality**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality): Ottiene o imposta la qualità delle immagini tra 0 e 100, quando ImageFormat è specificato come Jpeg.
- [**VerticalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution): Ottiene o imposta la risoluzione verticale dell'immagine in punti per pollice.
- [**HorizontalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution): Ottiene o imposta la risoluzione orizzontale dell'immagine in punti per pollice.
- [**TiffCompression**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression): Ottiene o imposta il tipo di compressione per le immagini quando ImageFormat è specificato come Tiff.
- [**Transparent**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent): Indica se lo sfondo di un'immagine dovrebbe essere trasparente quando ImageFormat è specificato come Png.

Il codice seguente dimostra come utilizzare [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) per specificare diverse preferenze.

|**Visualizzazione del foglio di calcolo prima dell'esportazione**|**Visualizzazione HTML dopo l'esportazione**|
| :- | :- |
|![Visualizzazione del foglio di calcolo prima dell'esportazione](converting-workbook-to-different-formats_1.png)|![Visualizzazione HTML dopo l'esportazione](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Converting Excel in file PDF**

I documenti PDF sono ampiamente utilizzati come formato standard per lo scambio di documenti tra organizzazioni, settori governativi e individui. Spesso gli sviluppatori di software sono chiesti di sviluppare un modo per convertire facilmente i file di Microsoft Excel in documenti PDF. Aspose.Cells supporta queste funzionalità. Questo articolo mostra come farlo.

### **Conversione di Excel in PDF**

La conversione da Microsoft Excel a PDF è stata introdotta con Aspose.Cells for Java 2.3.0. Da tale versione, Aspose.Cells può [convertire i fogli di calcolo direttamente in PDF](#direct-conversion) (incluso [PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files)), senza l'uso di un altro prodotto. Per convertire fogli di calcolo con versioni precedenti di Aspose.Cells, [utilizzare Aspose.PDF per la conversione](#conversion-with-asposepdf-asposecells-prior-to-230).

Aspose.Cells converte i fogli di calcolo in PDF con un elevato grado di accuratezza e fedeltà. Tuttavia, ci sono alcune [limitazioni](/cells/it/java/converting-workbook-to-different-formats/#conversion-attributes), elencate alla fine di questo articolo.

{{% alert color="primary" %}}

Aspose.Cells for Java scrive direttamente le informazioni su API e numero di versione nei documenti di output. Ad esempio, durante la creazione di un documento in PDF, Aspose.Cells for Java popola il campo **Applicazione** con il valore 'Aspose.Cells' e il campo **Produttore PDF** con un valore, ad es. 'Aspose.Cells for Java v17.9'.

Si noti che non è possibile istruire Aspose.Cells for Java a modificare o rimuovere queste informazioni dai documenti di output.

{{% /alert %}}

#### **Conversione Diretta**

Salva direttamente un file Excel in PDF utilizzando il metodo [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) e fornisce il membro dell'interfaccia [**SaveFormat.PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF). La conversione diretta come questa è il metodo di conversione più efficiente. Non perde dati o formattazione ma mantiene il PDF di output simile al file Excel di input.

Per specificare le opzioni di sicurezza durante il salvataggio in PDF, utilizzare [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Conversione Avanzata**

È possibile optare anche per l'utilizzo della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) per impostare diversi attributi per la conversione. L'impostazione di diverse proprietà della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) offrirà il controllo sulla stampa, caratteri, sicurezza e impostazioni di compressione per il file PDF risultante. La proprietà più nota è [**Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance) che consente di salvare i file Excel in file PDF/A conformi.

##### **Salvataggio dei fogli di calcolo di Excel in file PDF/A Compilati**

Il seguente snippet di codice mostra l'uso della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) per salvare i file Excel in formato PDF/A conforme.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Conversione con Aspose.Pdf: Aspose.Cells Prima della versione 2.3.0**

Per le versioni di Aspose.Cells precedenti alla versione 2.3.0 è necessario utilizzare un componente come [Aspose.PDF for Java](/pdf/java/) per convertire i fogli di calcolo in file PDF. Aspose.Cells e Aspose.PDF lavorano insieme per convertire un foglio di calcolo in PDF tramite un passaggio intermedio.

Per convertire fogli di calcolo in PDF con Aspose.Cells e Aspose.PDF:

1. Istituire un oggetto della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) chiamando il suo costruttore vuoto.
1. Svolgere il lavoro desiderato sul foglio di calcolo utilizzando l'API di Aspose.Cells.
1. Chiamare il metodo [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) per salvare il foglio di calcolo:
   1. Impostare il formato del file su XML.
   1. Selezionare Aspose_Pdf (un valore predefinito) dall'interfaccia FileFormatType. Questo indica al metodo di salvataggio di generare un foglio di calcolo nella forma XML compatibile con lo schema di Aspose.PDF in modo che Aspose.PDF for Java possa poi generare un documento PDF.
1. Quando il file XML è stato creato, creare un oggetto della classe Pdf nel pacchetto aspose.pdf.
1. Chiamare il metodo bindXML della classe Pdf e passare il nome del file XML di output.
1. Chiamare il metodo save della classe Pdf per generare il documento PDF.

I passaggi sopra indicati sono implementati di seguito in un esempio.

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) subito prima di rendere il foglio di calcolo in formato PDF. In questo modo si garantirà che i valori dipendenti dalle formule vengano ricalcolati e che i valori corretti siano resi nel PDF.

{{% /alert %}}

#### **Attributi di Conversione**

Lavoriamo sodo per migliorare la conversione e altri aspetti di Aspose.Cells con ogni rilascio. La conversione da Excel a PDF ha alcune limitazioni. Alcune impostazioni di formato specificate in un foglio di calcolo potrebbero andare perse e non tutti gli oggetti disegnati sono supportati.

La tabella sottostante elenca tutte le funzionalità supportate totalmente o parzialmente durante l'esportazione in PDF utilizzando Aspose.Cells. Questa tabella non è definitiva e non copre tutti gli attributi del foglio di calcolo. Può anche identificare quelle funzionalità che potrebbero non essere supportate o sono supportate solo parzialmente per la conversione.

{{% alert color="primary" %}}

|**Elemento del Documento**|**Attributo**|**Supportato**|**Note**|
| :- | :- | :- | :- |
|Allineamento| |Sì| |
|Rotazione| |Parzialmente|Supporta solo 90 e -90.|
|Impostazioni sfondo| |Sì| |
|Bordo|Colore|Sì| |
|Bordo|Stile di linea|Sì| |
|Bordo|Spessore linea|Sì| |
|Dati della cella| |Sì| |
|Commenti| |No| |
|Formattazione condizionale| |Sì| |
|Proprietà del documento| |Sì| |
|Oggetti disegno| |Sì| |
|Carattere|Dimensione|Sì| |
|Carattere|Colore|Sì| |
|Carattere|Stile|Sì| |
|Carattere|Sottolineato|Sì| |
|Carattere|Effetti|Parzialmente|Solo l'effetto barrato è supportato|
|Immagini| |Sì| |
|Collegamento ipertestuale| |Sì| |
|Grafici| |Sì| |
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
{{% /alert %}}
