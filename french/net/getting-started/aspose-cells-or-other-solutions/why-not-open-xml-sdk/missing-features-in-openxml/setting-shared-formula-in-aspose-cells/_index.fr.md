---
title: Définir les formules partagées dans Aspose.Cells
type: docs
weight: 110
url: /fr/net/setting-shared-formula-in-aspose-cells/
---

{{% alert color="primary" %}} 

Supposons que vous ayez une feuille de calcul remplie de données.

Vous souhaitez ajouter une fonction en B2 qui calculera la taxe de vente pour la première ligne de données. La taxe est de **9%**. La formule qui calcule la taxe de vente est: **"=A2*0.09"**. Cet article explique comment appliquer cette formule avec Aspose.Cells.

{{% /alert %}} 

Aspose.Cells vous permet de spécifier une formule en utilisant la propriété Cell.Formula.

Il existe deux options pour ajouter des formules aux autres cellules (B3, B4, B5, etc.) de la colonne.

Soit faites ce que vous avez fait pour la première cellule, en définissant efficacement la formule pour chaque cellule, en mettant à jour la référence de la cellule en conséquence (A3*0.09, A4*0.09, A5*0.09, etc.). Cela nécessite la mise à jour des références de cellules pour chaque ligne. Cela nécessite également à Aspose.Cells de parser chaque formule individuellement, ce qui peut être chronophage pour les feuilles de calcul de grande taille et les formules complexes. Cela ajoute également des lignes de code supplémentaires même si les boucles peuvent les réduire quelque peu.

Une autre approche consiste à utiliser une **formule partagée**. Avec une formule partagée, les formules sont automatiquement mises à jour pour les références de cellules dans chaque ligne de sorte que la taxe soit calculée correctement. La méthode Cell.SetSharedFormula est plus efficace que la première méthode.

L'exemple suivant démontre comment l'utiliser.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Shared Formula.xlsx";

//Instantiate a Workbook from existing file

Workbook workbook = new Workbook(FileName);

//Get the cells collection in the first worksheet

Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

//Apply the shared formula in the range i.e.., B2:B14

cells["B2"].SetSharedFormula("=A2*0.09", 13, 1);

//Save the excel file

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Télécharger le code source d'exemple**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **Télécharger un exemple en cours d'exécution**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
