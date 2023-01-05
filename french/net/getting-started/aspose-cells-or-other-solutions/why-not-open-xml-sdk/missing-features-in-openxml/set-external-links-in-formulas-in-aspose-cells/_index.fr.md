---
title: Définir les liens externes dans les formules dans Aspose.Cells
type: docs
weight: 90
url: /fr/net/set-external-links-in-formulas-in-aspose-cells/
---
{{% alert color="primary" %}} 

Parfois, il est nécessaire d'inclure des liens vers des fichiers externes dans les formules, par exemple pour évaluer une valeur de cellule ou de plage par rapport à eux. Aspose.Cells fournit cette fonctionnalité et ce document explique comment l'utiliser.

{{% /alert %}} 

L'exemple de code ci-dessous montre comment inclure des fichiers externes dans des formules.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Set External Links in Formula.xlsx";

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get first Worksheet

Worksheet sheet = workbook.Worksheets[0];

//Get Cells collection

Aspose.Cells.Cells cells = sheet.Cells;

//Set formula with external links

cells["A1"].Formula = "=SUM('[book1.xls]Sheet1'!A2, '[book1.xls]Sheet1'!A4)";

//Set formula with external links

cells["A2"].Formula = "='[book1.xls]Sheet1'!A8";

//Save the workbook

workbook.Save(FileName);

{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Set%20External%20Links%20in%20Formula)
## **Télécharger l'exemple d'exécution**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
