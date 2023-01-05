---
title: Conversion d'une feuille de calcul en fichier image par page
type: docs
weight: 10
url: /fr/net/converting-worksheet-to-image-file-by-page/
---
{{< highlight "csharp" >}}

 Workbook book = new Workbook("Feuille à Image par Page.xls");

Feuille de calcul = livre. Feuilles de travail [0] ;

Aspose.Cells.Rendering.ImageOrPrintOptions options = nouveau Aspose.Cells.Rendering.ImageOrPrintOptions();

options.HorizontalResolution = 200;

options.VerticalResolution = 200;

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Tiff ;

// Conversion Sheet2Image par page

SheetRender sr = new SheetRender(feuille, options);

 pour (int j = 0; j< sr.PageCount; j++)

{

	Bitmap pic = sr.ToImage(j);

	pic.Save(sheet.Name + " Page" + (j + 1) + ".tiff");

}


{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.image.file.by.Page.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20image%20file%20by%20Page%20%28Aspose.Cells%29.zip)
