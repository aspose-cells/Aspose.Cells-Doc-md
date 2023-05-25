---
title: Conversione del foglio di lavoro in immagine utilizzando le opzioni ImageOrPrint
type: docs
weight: 90
url: /it/net/converting-worksheet-to-image-using-imageorprint-options/
---
{{% alert color="primary" %}}

Questo documento è progettato per fornire una comprensione dettagliata di come convertire un foglio di lavoro in un file immagine e applicare diverse opzioni di immagine e stampa per l'immagine, opzioni come risoluzione, compressione TIFF, formato immagine e qualità della pagina.

{{% /alert %}}

##  **Salvataggio di fogli di lavoro in immagini: approcci diversi**

volte, potresti dover presentare i tuoi fogli di lavoro come una rappresentazione pittorica. Devi presentare le immagini del foglio di lavoro nelle tue applicazioni o pagine web. Potrebbe essere necessario inserire le immagini in un documento Word, un file PDF, una presentazione PowerPoint o utilizzarle in qualche altro scenario. Semplicemente vuoi un foglio di lavoro reso come immagine in modo da poterlo usare altrove. Aspose.Cells supporta la conversione di fogli di lavoro in file Excel in immagini. Inoltre, Aspose.Cells supporta l'impostazione di diverse opzioni come il formato dell'immagine, la risoluzione (sia verticale che orizzontale), la qualità dell'immagine e altre opzioni di immagine e stampa.

Potresti provare l'automazione dell'ufficio, ma l'automazione dell'ufficio ha i suoi svantaggi. Ci sono diversi motivi e problemi coinvolti: ad esempio sicurezza, stabilità, scalabilità e velocità, prezzo e funzionalità. In breve, ci sono molte ragioni, la prima delle quali è che gli stessi Microsoft sconsigliano vivamente l'automazione dell'ufficio dalle soluzioni software.

Questo articolo mostra come creare un'applicazione console in Visual Studio .NET, eseguire la conversione di un foglio di lavoro in immagine utilizzando diverse opzioni di immagine e stampa con poche e semplici righe di codice utilizzando Aspose.Cells API.

 Devi importare[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)spazio dei nomi al tuo programma/progetto. Ha diverse classi preziose, ad esempio,[**FoglioRendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**Workbook Render**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)eccetera.

IL[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class rappresenta un foglio di lavoro per il rendering delle immagini per il foglio di lavoro, ha un overload[**Immaginare**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)metodo che può convertire direttamente un foglio di lavoro in file immagine specificati con gli attributi o le opzioni desiderati. Può restituire l'oggetto System.Drawing.Bitmap e puoi salvare un file immagine sul disco/stream. Sono supportati diversi formati immagine, ad esempio BMP, PNG, GIFF, JPEG, TIFF, EMF e così via.

##  **Utilizzo di Aspose.Cells per convertire il foglio di lavoro in immagine utilizzando le opzioni ImageOrPrint.**

###  **Creazione di una cartella di lavoro modello in Microsoft Excel**

Ho creato una nuova cartella di lavoro in MS Excel e ho aggiunto alcuni dati nel primo foglio di lavoro. Ora convertirò il foglio di lavoro del file modello "Sheet1" in un file immagine "SheetImage.tiff" e applicherò diverse opzioni di immagine come risoluzioni orizzontali e verticali, TiffCompression ecc.

###  **Scarica e installa Aspose.Cells**

 Per prima cosa, devi[scaricamento](https://downloads.aspose.com/cells/net) Aspose.Cells per .Net. Installalo sul tuo computer di sviluppo. Tutto[Aspose](http://www.aspose.com/) componenti, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e si limita a inserire filigrane nei documenti prodotti.

###  **Crea un progetto**

Avvia VisualStudio. Net e crea una nuova applicazione console. Questo esempio mostrerà un'applicazione console C#, ma puoi usare anche VB.NET.

###  **Aggiungi riferimenti**

Questo progetto utilizzerà Aspose.Cells. Quindi, devi aggiungere il riferimento al componente Aspose.Cells nel tuo progetto. Ad esempio, aggiungi un riferimento a ….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll

###  **Converti foglio di lavoro in un file immagine**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

##  **Opzioni di conversione**

È possibile salvare pagine specifiche nell'immagine. Il codice seguente converte il primo e il secondo foglio di lavoro in una cartella di lavoro in immagini JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

##  **Conversione di immagini utilizzando WorkbookRender**

Un'immagine TIFF può contenere più di un fotogramma. Puoi salvare l'intera cartella di lavoro in una singola immagine TIFF con più frame o pagine:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

