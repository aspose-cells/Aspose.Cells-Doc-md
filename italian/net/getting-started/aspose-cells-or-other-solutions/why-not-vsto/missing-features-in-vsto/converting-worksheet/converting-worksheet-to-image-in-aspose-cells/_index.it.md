---
title: Convertire un Foglio di Lavori in un Immagine in Aspose.Cells
type: docs
weight: 20
url: /it/net/converting-worksheet-to-image-in-aspose-cells/
---

Questo documento è progettato per fornire agli sviluppatori una comprensione dettagliata su come convertire un foglio di lavoro in un file immagine e un foglio di lavoro con più pagine in un file immagine per pagina.
A volte potresti avere bisogno di presentare i fogli di lavoro come immagini, ad esempio per utilizzarli in applicazioni o pagine web. Potresti aver bisogno di inserire le immagini in un documento Word, un file **PDF**, una presentazione PowerPoint o utilizzarle in qualche altro scenario. In poche parole, vuoi rendere il foglio di lavoro come un'immagine. Aspose.Cells supporta la conversione dei fogli di lavoro nei file di Microsoft Excel in immagini. Inoltre, **Aspose.Cells** supporta la conversione di un libro in più file immagine, uno per pagina.

Potresti usare l'automazione di Office per ottenere questo, ma l'automazione di Office ha i suoi svantaggi. Ci sono diversi motivi e problemi coinvolti: ad esempio sicurezza, stabilità, scalabilità/velocità, prezzo e funzionalità. In sintesi, ci sono molte ragioni, ma la principale è che Microsoft stessa sconsiglia fortemente l'automazione di Office.

Questo articolo mostra come creare un'applicazione console in Visual Studio.Net, convertire un foglio di lavoro in un'immagine e un foglio di lavoro in un'unica immagine per ogni foglio di lavoro con poche e semplici righe di codice utilizzando l'API Aspose.Cells. È necessario importare il namespace Aspose.Cells.Rendering nel tuo programma/progetto. Ha diverse classi importanti, ad esempio SheetRender, ImageOrPrintOptions, WorkbookRender ecc. La classe Aspose.Cells.Rendering.SheetRender rappresenta un foglio di lavoro per renderizzare immagini per il foglio di lavoro, ha un metodo sovraccaricato **ToImage** che può convertire direttamente un foglio di lavoro in un file immagine specificato con i tuoi attributi o opzioni desiderati. Può restituire un oggetto **System.Drawing.Bitmap** e puoi salvare un file immagine sul disco/stream. Ci sono diversi formati immagine supportati, ad esempio .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf ecc.

{{< highlight csharp >}}

//Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image type

imgOptions.ImageType = ImageType.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
