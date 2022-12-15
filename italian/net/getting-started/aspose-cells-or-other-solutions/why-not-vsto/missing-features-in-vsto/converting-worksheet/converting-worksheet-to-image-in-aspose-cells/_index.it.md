---
title: Conversione del foglio di lavoro in immagine in Aspose.Cells
type: docs
weight: 20
url: /it/net/converting-worksheet-to-image-in-aspose-cells/
---
Questo documento è progettato per fornire agli sviluppatori una comprensione dettagliata su come convertire un foglio di lavoro in un file immagine e un foglio di lavoro con più pagine in un file immagine per pagina.
 A volte, potrebbe essere necessario presentare i fogli di lavoro come immagini, ad esempio per utilizzarli in applicazioni o pagine Web. Potrebbe essere necessario inserire le immagini in un documento Word, a**PDF**file, una presentazione PowerPoint o utilizzarli in qualche altro scenario. Semplicemente, vuoi rendere il foglio di lavoro come un'immagine. Aspose.Cells supporta la conversione di fogli di lavoro in file Microsoft Excel in immagini. Anche,**Aspose.Cells** supporta la conversione di una cartella di lavoro in più file immagine, uno per pagina.

È possibile utilizzare Office Automation per raggiungere questo obiettivo, ma l'automazione di Office ha i suoi svantaggi. Ci sono diversi motivi e problemi coinvolti: ad esempio sicurezza, stabilità, scalabilità/velocità, prezzo e funzionalità. Insomma, i motivi sono tanti, ma il principale è che la stessa Microsoft sconsiglia vivamente l'automazione di Office.

 Questo articolo mostra come creare un'applicazione console in Visual Studio.Net, convertire un foglio di lavoro in un'immagine e un foglio di lavoro in un'immagine per ogni foglio di lavoro con poche e semplici righe di codice utilizzando l'API Aspose.Cells. Devi importare Aspose.Cells.Rendering spazio dei nomi al tuo programma/progetto. Ha diverse classi preziose, ad esempio SheetRender, ImageOrPrintOptions, WorkbookRender ecc.Aspose.Cells.La classe Rendering.SheetRender rappresenta un foglio di lavoro per il rendering delle immagini per il foglio di lavoro, ha un sovraccarico**Immaginare** metodo che può convertire direttamente un foglio di lavoro in file immagine specificati con gli attributi o le opzioni desiderati. Può tornare**System.Drawing.Bitmap**oggetto e puoi salvare un file immagine sul disco/stream. Sono supportati diversi formati di immagine, ad esempio .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf ecc.

{{< highlight "csharp" >}}

 //Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image format

imgOptions.ImageFormat = System.Drawing.Imaging.ImageFormat.Jpeg;

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
