---
title: Arbeitsblatt seitenweise in eine Bilddatei konvertieren
type: docs
weight: 10
url: /de/net/converting-worksheet-to-image-file-by-page/
---
{{< highlight "csharp" >}}

 Arbeitsbuch book = new Workbook("Sheet to Image by Page.xls");

Arbeitsblatt sheet = book.Worksheets[0];

Aspose.Cells.Rendering.ImageOrPrintOptions Optionen = neu Aspose.Cells.Rendering.ImageOrPrintOptions();

options.HorizontalResolution = 200;

options.VerticalResolution = 200;

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff;

//Konvertierung Sheet2Image By Page

SheetRender sr = new SheetRender (Blatt, Optionen);

 für (int j = 0; j< sr.PageCount; j++)

{

	Bitmap pic = sr.ToImage(j);

	pic.Save(sheet.Name + " Page" + (j + 1) + ".tiff");

}


{{< /highlight >}}
## **Beispielcode herunterladen**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.image.file.by.Page.Aspose.Cells.zip)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20image%20file%20by%20Page%20%28Aspose.Cells%29.zip)
