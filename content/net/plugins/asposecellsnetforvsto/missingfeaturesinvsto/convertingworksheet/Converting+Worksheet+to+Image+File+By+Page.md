+++
title = "Converting Worksheet to Image File By Page" 
description = "" 
weight = 20819 
+++

Aspose.Cells for .NET : Converting Worksheet to Image File By Page  

# Aspose.Cells for .NET : Converting Worksheet to Image File By Page


{{< code lang="cs" >}}
Workbook book = new Workbook("Sheet to Image by Page.xls");
Worksheet sheet = book.Worksheets[0];
Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();
options.HorizontalResolution = 200;
options.VerticalResolution = 200;
options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff;

//Sheet2Image By Page conversion
SheetRender sr = new SheetRender(sheet, options);
for (int j = 0; j < sr.PageCount; j++)
{

	Bitmap pic = sr.ToImage(j);
	pic.Save(sheet.Name + " Page" + (j + 1) + ".tiff");
}

{{< /code >}}

## Download Sample Code

*   [Codeplex](https://asposevsto.codeplex.com/downloads/get/812528)
*   [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.image.file.by.Page.Aspose.Cells.zip)
*   [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20image%20file%20by%20Page%20%28Aspose.Cells%29.zip)

