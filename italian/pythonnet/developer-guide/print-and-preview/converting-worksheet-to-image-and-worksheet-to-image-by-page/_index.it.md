---
title: Convertire foglio elettronico in immagine e foglio elettronico in immagine per pagina
type: docs
weight: 80
url: /it/python-net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Questo documento è progettato per fornire agli sviluppatori una comprensione dettagliata di come convertire un foglio elettronico in un file immagine e un foglio elettronico con pagine multiple in un file immagine per pagina.

A volte, potrebbe essere necessario presentare i fogli di calcolo come immagini, ad esempio, per usarli in applicazioni o pagine web. Potresti dover inserire le immagini in un documento Word, in un file PDF, in una presentazione PowerPoint o usarle in altri scenari. In modo semplice, vuoi rendere il foglio di lavoro come immagine. Aspose.Cells per Python via .NET supporta la conversione dei fogli di calcolo di file Excel in immagini. Inoltre, supporta la conversione di un workbook in più file immagine, uno per ogni pagina.

Potresti usare l'automazione di Office per ottenere questo, ma l'automazione di Office ha i suoi svantaggi. Ci sono diversi motivi e problemi coinvolti: ad esempio sicurezza, stabilità, scalabilità/velocità, prezzo e funzionalità. In sintesi, ci sono molte ragioni, ma la principale è che Microsoft stessa sconsiglia fortemente l'automazione di Office.

{{% /alert %}}

## **Utilizzare Aspose.Cells per convertire un foglio elettronico in un file immagine**

Questo articolo mostra come creare un'applicazione console in Visual Studio, convertire un foglio di lavoro in un'immagine e convertire un foglio di lavoro in un'immagine per ogni foglio con poche e semplici righe di codice usando l’API Aspose.Cells per Python via .NET.

È necessario importare lo spazio dei nomi [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) nel proprio programma/progetto. Ha diverse classi preziose, come [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender), e così via. La classe [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) rappresenta un foglio elettronico per renderizzare immagini per il foglio e ha un metodo sovraccaricato [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) che può convertire direttamente un foglio elettronico in file immagine con eventuali attributi o opzioni impostate. Può restituire un oggetto System.Drawing.Bitmap e è possibile salvare un file immagine sul disco/flusso. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF, EMF e altri.

Questo articolo spiega come convertire un foglio di lavoro in un'immagine. Questo esempio mostra come utilizzare Aspose.Cells per Python via .NET per convertire un foglio di lavoro da un modello di workbook in un file immagine.


### **Converti Foglio di Lavoro in File Immagine**

Ho creato un nuovo workbook in Microsoft Excel e ho aggiunto alcuni dati al primo foglio di lavoro: **Testbook.xlsx** (1 foglio di lavoro). Successivamente, converti il foglio di lavoro del file modello chiamato Sheet1 in un file immagine chiamato SheetImage.jpg.

Di seguito è riportato il codice utilizzato dal componente per completare il compito. Converte Sheet1 in **Testbook.xlsx** in un file immagine per spiegare quanto sia facile questa conversione.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheettoImageFile-1.py" >}}

## **Utilizzare Aspose.Cells per convertire il foglio di lavoro in un file immagine per pagina**

Questo esempio mostra come usare Aspose.Cells per Python via .NET per convertire un foglio di lavoro da un workbook modello che ha diverse pagine in un file immagine per pagina.

### **Converti Foglio di Lavoro in Immagine per pagina**

Ho creato un nuovo workbook in Microsoft Excel e ho aggiunto alcuni dati al primo foglio di lavoro: **Testbook2.xlsx** (1 foglio di lavoro).

Ora, converti il foglio di lavoro del file modello in file immagine (un file per pagina). Poiché ho già creato l'applicazione console per eseguire il compito di copia, salterò quei passaggi di creazione dell'applicazione console e passerò direttamente ai passaggi di conversione del foglio di lavoro.

Di seguito è riportato il codice utilizzato dal componente per completare il compito. Converte Sheet1 in Testbook2.xls in file immagine per pagina.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheetToImageByPage-1.py" >}}

