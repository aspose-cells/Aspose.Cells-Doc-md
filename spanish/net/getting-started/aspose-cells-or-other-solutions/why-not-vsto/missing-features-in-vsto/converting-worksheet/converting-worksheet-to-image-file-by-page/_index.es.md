---
title: Conversión de hoja de trabajo a archivo de imagen por página
type: docs
weight: 10
url: /es/net/converting-worksheet-to-image-file-by-page/
---
{{< highlight "csharp" >}}

 Libro de trabajo libro = nuevo Libro de trabajo ("Hoja a imagen por página.xls");

Hoja de trabajo hoja = libro.Hojas de trabajo[0];

Aspose.Cells.Rendering.ImageOrPrintOptions opciones = nuevo Aspose.Cells.Rendering.ImageOrPrintOptions();

opciones.HorizontalResolution = 200;

opciones.VerticalResolution = 200;

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff;

//Sheet2Image por conversión de página

SheetRender sr = new SheetRender(hoja, opciones);

 para (int j = 0; j< sr.PageCount; j++)

{

	Bitmap pic = sr.ToImage(j);

	pic.Save(sheet.Name + " Page" + (j + 1) + ".tiff");

}


{{< /highlight >}}
## **Descargar código de muestra**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.image.file.by.Page.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20image%20file%20by%20Page%20%28Aspose.Cells%29.zip)
