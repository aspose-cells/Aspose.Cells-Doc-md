---
title: Déplacer des feuilles de calcul dans le classeur
type: docs
weight: 30
url: /fr/net/move-worksheets-within-workbook/
---
Aspose.Cells fournit une méthode, Aspose.Cells.Worksheet.MoveTo(), utilisée pour déplacer une feuille de calcul vers un autre emplacement dans la feuille de calcul. La méthode prend l'index de la feuille de calcul cible comme paramètre.

L'exemple suivant montre comment déplacer une feuille de calcul vers un autre emplacement dans le classeur.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Move Worksheet.xlsx";

//Open an existing excel file.

Workbook wb = new Workbook(FileName);

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Get the first worksheet.

Worksheet worksheet = sheets[0];

string test = worksheet.Name;

//Move the first sheet to the third position in the workbook.

worksheet.MoveTo(2);

//Save the excel file.

wb.Save(FileName);

{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Move%20Worksheet%20%28Aspose.Cells%29.zip)
