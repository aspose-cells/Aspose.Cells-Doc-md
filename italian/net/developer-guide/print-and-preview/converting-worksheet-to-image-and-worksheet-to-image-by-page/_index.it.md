---
title: Conversione del foglio di lavoro in immagine e del foglio di lavoro in immagine per pagina
type: docs
weight: 80
url: /it/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Questo documento è progettato per fornire agli sviluppatori una comprensione dettagliata di come convertire un foglio di lavoro in un file immagine e un foglio di lavoro con più pagine in un file immagine per pagina.

volte, potrebbe essere necessario presentare i fogli di lavoro come immagini, ad esempio per utilizzarli in applicazioni o pagine Web. Potrebbe essere necessario inserire le immagini in un documento Word, un file PDF, una presentazione PowerPoint o utilizzarle in qualche altro scenario. Semplicemente, vuoi rendere il foglio di lavoro come un'immagine. Aspose.Cells supporta la conversione di fogli di lavoro in file Excel Microsoft in immagini. Inoltre, Aspose.Cells supporta la conversione di una cartella di lavoro in più file immagine, uno per pagina.

È possibile utilizzare Office Automation per raggiungere questo obiettivo, ma l'automazione di Office ha i suoi svantaggi. Ci sono diversi motivi e problemi coinvolti: ad esempio sicurezza, stabilità, scalabilità/velocità, prezzo e funzionalità. Insomma, i motivi sono tanti, ma il principale è che gli stessi Microsoft sconsigliano vivamente Office automation.

{{% /alert %}}

## **Utilizzo di Aspose.Cells per convertire il foglio di lavoro in file di immagine**

Questo articolo mostra come creare un'applicazione console in Visual Studio, convertire un foglio di lavoro in un'immagine e convertire un foglio di lavoro in un'immagine per ogni foglio di lavoro con poche e più semplici righe di codice usando Aspose.Cells API.

 Devi importare il file[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) spazio dei nomi al tuo programma/progetto. Ha diverse classi preziose, come[**FoglioRendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**Workbook Render**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), e così via. Il[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class rappresenta un foglio di lavoro per il rendering delle immagini per il foglio di lavoro e ha un overload[**Immaginare**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)metodo che può convertire un foglio di lavoro in file immagine direttamente con qualsiasi attributo o opzione impostata. Può restituire un oggetto System.Drawing.Bitmap ed è possibile salvare un file immagine sul disco/stream. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF, EMF e altri.

Questo articolo spiega come:

- Converti un foglio di lavoro in un'immagine
- Converti ogni pagina di un foglio di lavoro in un'immagine

Questa attività mostra come utilizzare Aspose.Cells per convertire un foglio di lavoro da una cartella di lavoro modello in un file di immagine.

### **Progetto di installazione**

1.  Primo,[scarica Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1.  Installalo sul tuo computer di sviluppo. Tutti[Aspose](http://www.aspose.com/) componenti, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e si limita a inserire filigrane nei documenti prodotti. Ora avvia Visual Studio.Net e crea una nuova applicazione console. Questo esempio utilizza un'applicazione console C#, ma è possibile utilizzare anche VB.NET. Aggiungere il riferimento a Aspose.Cells nel progetto creato.

### **Converti foglio di lavoro in file immagine**

 Ho creato una nuova cartella di lavoro in Microsoft Excel e ho aggiunto alcuni dati nel primo foglio di lavoro:**Testbook.xlsx** (1 foglio di lavoro). Successivamente, converti il foglio di lavoro del file modello Sheet1 in un file immagine chiamato SheetImage.jpg.

 Di seguito è riportato il codice utilizzato dal componente per eseguire l'attività. Converte Foglio1 in**Testbook.xlsx** in un file immagine per spiegare quanto sia facile questa conversione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Utilizzo di Aspose.Cells per convertire il foglio di lavoro in file immagine per pagina**

Questo esempio mostra come usare Aspose.Cells per convertire un foglio di lavoro da una cartella di lavoro modello con diverse pagine in un file di immagine per pagina.

### **Converti foglio di lavoro in immagine per pagina**

 Ho creato una nuova cartella di lavoro in Microsoft Excel e ho aggiunto alcuni dati nel primo foglio di lavoro:**Testbook2.xlsx** (1 foglio di lavoro).

Ora converti il foglio di lavoro del file modello Sheet1 in file immagine (un file per pagina). Poiché ho già creato l'applicazione console per eseguire l'attività di copia, salterò i passaggi di creazione dell'applicazione console e passerò direttamente ai passaggi di conversione del foglio di lavoro.

Di seguito è riportato il codice utilizzato dal componente per eseguire l'attività. Converte Sheet1 in Testbook2.xls in file immagine per pagina.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

