---
title: Copier des feuilles de calcul dans un classeur
type: docs
weight: 20
url: /fr/net/copy-worksheets-within-a-workbook/
---
**Aspose.Cells** fournit une méthode surchargée,**Aspose.Cells.WorksheetCollection.AddCopy()**, qui est utilisé pour ajouter une feuille de calcul à la collection et copier les données d'une feuille de calcul existante. Une version de la méthode prend l'index de la feuille de calcul source comme paramètre. L'autre version prend le nom de la feuille de calcul source comme paramètre.

L'exemple suivant montre comment copier une feuille de calcul existante dans un classeur.

{{< highlight "csharp" >}}

 //Create a new Workbook.

//Open an existing Excel file.

Workbook wb = new Workbook("ResultedBook.xls");

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Copy data to a new sheet from an existing

//sheet within the Workbook.

sheets.AddCopy("MySheet");

//Save the Excel file.

wb.Save("Copy Worksheet.xls");

{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
