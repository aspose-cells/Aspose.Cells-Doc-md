---
title: Conversione di un foglio di lavoro in un file immagine per pagina
type: docs
weight: 10
url: /it/net/converting-worksheet-to-image-file-by-page/
---
{{< highlight "csharp" >}}

 Libro della cartella di lavoro = nuova cartella di lavoro ("Foglio per immagine per pagina.xls");

Foglio di lavoro = libro.Fogli di lavoro[0];

Aspose.Cells.Rendering.ImageOrPrintOptions options = nuovo Aspose.Cells.Rendering.ImageOrPrintOptions();

options.HorizontalResolution = 200;

options.VerticalResolution = 200;

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff;

//Sheet2Image Conversione per pagina

SheetRender sr = new SheetRender(foglio, opzioni);

 per (int j = 0; j< sr.PageCount; j++)

{

	Bitmap pic = sr.ToImage(j);

	pic.Save(sheet.Name + " Page" + (j + 1) + ".tiff");

}


{{< /highlight >}}
## **Scarica il codice di esempio**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.image.file.by.Page.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20image%20file%20by%20Page%20%28Aspose.Cells%29.zip)
