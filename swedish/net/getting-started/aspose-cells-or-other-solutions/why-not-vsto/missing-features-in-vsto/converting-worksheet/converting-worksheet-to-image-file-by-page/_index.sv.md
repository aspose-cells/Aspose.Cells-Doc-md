---
title: Konvertera arbetsblad till bildfil efter sida
type: docs
weight: 10
url: /sv/net/converting-worksheet-to-image-file-by-page/
---
{{< highlight "csharp" >}}

 Workbook book = new Workbook("Sheet to Image by Page.xls");

Arbetsblad = bok. Arbetsblad[0];

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

optioner.HorizontalResolution = 200;

options.VerticalResolution = 200;

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff;

//Sheet2Image By Page konvertering

SheetRender sr = new SheetRender(ark, optioner);

 för (int j = 0; j< sr.PageCount; j++)

{

	Bitmap pic = sr.ToImage(j);

	pic.Save(sheet.Name + " Page" + (j + 1) + ".tiff");

}


{{< /highlight >}}
## **Ladda ner provkod**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.image.file.by.Page.Aspose.Cells.zip)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20image%20file%20by%20Page%20%28Aspose.Cells%29.zip)
