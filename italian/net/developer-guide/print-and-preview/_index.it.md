---
title: Stampa e visualizza in anteprima la cartella di lavoro
linktitle: Stampa e Anteprima
type: docs
weight: 70
url: /it/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells supporta la stampa e l'anteprima dei file Excel senza l'installazione di Microsoft Excel.
---
{{% alert color="primary" %}}

Dopo aver creato un foglio di lavoro, spesso si desidera stamparne una copia cartacea. Questo articolo spiega come stampare fogli di calcolo con Aspose.Cells.

{{% /alert %}}

## **Stampa Introduzione**

Microsoft Excel presuppone che si desidera stampare l'intera area del foglio di lavoro a meno che non si specifichi una selezione. Per stampare utilizzando Aspose.Cells, importare prima lo spazio dei nomi Aspose.Cells.Rendering nel programma. Ha diverse classi utili, ad esempio,[**FoglioRendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) e[**Workbook Render**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **Stampa utilizzando SheetRender**

 Il[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class rappresenta un foglio di lavoro e ha l'estensione[**Alla stampante**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index)metodo che può stampare un foglio di lavoro. Il codice di esempio seguente mostra come stampare un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **Stampa utilizzando WorkbookRender**

 Per stampare un'intera cartella di lavoro, scorrere i fogli e stamparli oppure utilizzare il file[**Workbook Render**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)classe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

 Aspose.Cells fornisce anche i sovraccarichi per il[**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) e[**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) metodi, quindi è possibile impostare il nome del lavoro di stampa durante la stampa di fogli di calcolo Excel. Per impostazione predefinita, tutti i lavori di stampa vengono creati con il nome "Documento".

{{% /alert %}}

## **Anteprima di stampa**

Potrebbero esserci casi in cui i file Excel con milioni di pagine devono essere convertiti in PDF o immagini. L'elaborazione di tali file richiederà molto tempo e risorse. In questi casi, la funzione Anteprima di stampa della cartella di lavoro e del foglio di lavoro potrebbe rivelarsi utile. Prima di convertire tali file, l'utente può controllare il numero totale di pagine e quindi decidere se il file deve essere convertito o meno. Questo articolo si concentra sull'utilizzo di[**Cartella di lavoroStampaAnteprima**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)e[**FoglioStampaAnteprima**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)classi per scoprire il numero totale di pagine.

 Aspose.Cells fornisce la funzione di anteprima di stampa. Per questo, l'API fornisce[**Cartella di lavoroStampaAnteprima**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) e[**FoglioStampaAnteprima**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) classi. Per creare l'anteprima di stampa dell'intera cartella di lavoro, creare un'istanza di[**Cartella di lavoroStampaAnteprima**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) classe passando[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) e[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) oggetti al costruttore. Il[**Cartella di lavoroStampaAnteprima**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) la classe fornisce un[**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) metodo che restituisce il numero di pagine nell'anteprima generata. Simile a[**Cartella di lavoroStampaAnteprima**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)classe, il[**FoglioStampaAnteprima**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)class viene utilizzata per generare un'anteprima di stampa per un foglio di lavoro specifico. Per creare l'anteprima di stampa di un foglio di lavoro, creare un'istanza di[**FoglioStampaAnteprima**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)classe passando[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)e[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)oggetti al costruttore. Il[**FoglioStampaAnteprima**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)class fornisce anche un[**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)metodo che restituisce il numero di pagine nell'anteprima generata.

Il seguente frammento di codice illustra l'uso di entrambi[**Cartella di lavoroStampaAnteprima**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)e[**FoglioStampaAnteprima**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) classi utilizzando il[file excel di esempio](94896177.xlsx).

### **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

Di seguito è riportato l'output generato dall'esecuzione del codice precedente.

### **Uscita console**

Numero di pagine della cartella di lavoro: 1
Numero di pagine del foglio di lavoro: 1


## **Argomenti avanzati**
- [Configurazione dei caratteri per il rendering di fogli di calcolo](/cells/it/net/configuring-fonts-for-rendering-spreadsheets/)
- [Converti foglio di lavoro in immagine: rimuovi gli spazi bianchi intorno ai dati](/cells/it/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Conversione del foglio di lavoro in immagine e del foglio di lavoro in immagine per pagina](/cells/it/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Conversione del foglio di lavoro in immagine utilizzando le opzioni ImageOrPrint](/cells/it/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Esporta intervallo di Cells in un foglio di lavoro in immagine](/cells/it/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Esporta foglio di lavoro o grafico in immagine con larghezza e altezza desiderate](/cells/it/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Estrai le immagini dai fogli di lavoro utilizzando ImageOrPrintOptions](/cells/it/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Genera miniatura del foglio di lavoro](/cells/it/net/generate-thumbnail-of-the-worksheet/)
- [Stampa pagina vuota quando non c'è niente da stampare](/cells/it/net/output-blank-page-when-there-is-nothing-to-print/)
- [Impostazioni di pagina e opzioni di stampa](/cells/it/net/page-setup-and-printing-options/)
- [Stampa dell'intervallo di pagine utilizzando SheetRender e WorkbookRender](/cells/it/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Eseguire il rendering della sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions](/cells/it/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Renderizza il foglio di lavoro nel contesto grafico](/cells/it/net/render-worksheet-to-graphic-context/)
- [Specifica un set di caratteri individuale o privato per il rendering della cartella di lavoro](/cells/it/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Specificare il nome del lavoro o del documento durante la stampa con Aspose.Cells](/cells/it/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
