---
title: Copier les feuilles de calcul à l intérieur d un classeur
type: docs
weight: 20
url: /fr/net/copy-worksheets-within-a-workbook/
---

**Aspose.Cells** fournit une méthode surchargée, **Aspose.Cells.WorksheetCollection.AddCopy()**, qui est utilisée pour ajouter une feuille de calcul à la collection et copie les données à partir d'une feuille de calcul existante. Une version de la méthode prend l'index de la feuille de calcul source en tant que paramètre. L'autre version prend le nom de la feuille de calcul source en tant que paramètre.

L'exemple suivant montre comment copier une feuille existante dans un classeur.

{{< highlight csharp >}}

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
## **Télécharger le code source d'exemple**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)
