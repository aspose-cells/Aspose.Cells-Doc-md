---
title: Définir les titres d'impression
type: docs
weight: 30
url: /fr/net/set-print-titles/
---
## **Aspose.Cells - Définir les titres d'impression**
Aspose.Cells vous permet de désigner des en-têtes de ligne et de colonne à répéter sur toutes les pages d'une feuille de calcul imprimée. Pour ce faire, utilisez le[Mise en page](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)propriétés de classe PrintTitleColumns et PrintTitleRows.

Les lignes ou les colonnes qui seront répétées sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme $1:$2 et les colonnes sont définies comme $A:$B.

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Définir les titres d'impression** forment l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Définition des options d'impression](/cells/fr/net/setting-print-options/).

{{% /alert %}}
