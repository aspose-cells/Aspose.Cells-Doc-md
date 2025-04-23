---
title: Convertire foglio elettronico in immagine e foglio elettronico in immagine per pagina
type: docs
weight: 80
url: /it/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Questo documento è progettato per fornire agli sviluppatori una comprensione dettagliata di come convertire un foglio elettronico in un file immagine e un foglio elettronico con pagine multiple in un file immagine per pagina.

A volte potresti dover presentare i fogli elettronici come immagini, ad esempio per utilizzarli in applicazioni o pagine web. Potresti aver bisogno di inserire le immagini in un documento di Word, un file PDF, una presentazione PowerPoint o utilizzarle in qualche altro scenario. In sostanza, desideri rendere il foglio elettronico come un'immagine. Aspose.Cells supporta la conversione dei fogli in file Microsoft Excel in immagini. Inoltre, Aspose.Cells supporta la conversione di un libro di lavoro in più file immagine, uno per pagina.

Potresti usare l'automazione di Office per ottenere questo, ma l'automazione di Office ha i suoi svantaggi. Ci sono diversi motivi e problemi coinvolti: ad esempio sicurezza, stabilità, scalabilità/velocità, prezzo e funzionalità. In sintesi, ci sono molte ragioni, ma la principale è che Microsoft stessa sconsiglia fortemente l'automazione di Office.

{{% /alert %}}

## **Utilizzare Aspose.Cells per convertire un foglio elettronico in un file immagine**

Questo articolo mostra come creare un'applicazione console in Visual Studio, convertire un foglio elettronico in un'immagine e convertire un foglio elettronico in un'immagine per ogni foglio con poche e semplici righe di codice utilizzando l'API Aspose.Cells.

È necessario importare lo spazio dei nomi [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) nel proprio programma/progetto. Ha diverse classi preziose, come [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), e così via. La classe [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) rappresenta un foglio elettronico per renderizzare immagini per il foglio e ha un metodo sovraccaricato [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) che può convertire direttamente un foglio elettronico in file immagine con eventuali attributi o opzioni impostate. Può restituire un oggetto System.Drawing.Bitmap e è possibile salvare un file immagine sul disco/flusso. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF, EMF e altri.

Questo articolo spiega come:

- Convertire un foglio di lavoro in un'immagine
- Convertire ogni pagina in un foglio di lavoro in un'immagine

Questo compito mostra come utilizzare Aspose.Cells per convertire un foglio di lavoro da un modello di cartella di lavoro in un file di immagine.

### **Progetto di installazione**

1. Prima di tutto, [scarica Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Installalo sul tuo computer di sviluppo. Tutti i [componenti Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti. Ora avvia Visual Studio.Net e crea una nuova applicazione console. Questo esempio usa un'applicazione console C#, ma è possibile utilizzare anche VB.NET. Aggiungi riferimento a Aspose.Cells nel progetto creato.

### **Converti Foglio di Lavoro in File Immagine**

Ho creato un nuovo workbook in Microsoft Excel e ho aggiunto alcuni dati al primo foglio di lavoro: **Testbook.xlsx** (1 foglio di lavoro). Successivamente, converti il foglio di lavoro del file modello chiamato Sheet1 in un file immagine chiamato SheetImage.jpg.

Di seguito è riportato il codice utilizzato dal componente per completare il compito. Converte Sheet1 in **Testbook.xlsx** in un file immagine per spiegare quanto sia facile questa conversione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Utilizzare Aspose.Cells per convertire il foglio di lavoro in un file immagine per pagina**

Questo esempio mostra come utilizzare Aspose.Cells per convertire un foglio di lavoro da un modello di cartella di lavoro che ha diverse pagine in un file immagine per pagina.

### **Converti Foglio di Lavoro in Immagine per pagina**

Ho creato un nuovo workbook in Microsoft Excel e ho aggiunto alcuni dati al primo foglio di lavoro: **Testbook2.xlsx** (1 foglio di lavoro).

Ora, converti il foglio di lavoro del file modello in file immagine (un file per pagina). Poiché ho già creato l'applicazione console per eseguire il compito di copia, salterò quei passaggi di creazione dell'applicazione console e passerò direttamente ai passaggi di conversione del foglio di lavoro.

Di seguito è riportato il codice utilizzato dal componente per completare il compito. Converte Sheet1 in Testbook2.xls in file immagine per pagina.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
