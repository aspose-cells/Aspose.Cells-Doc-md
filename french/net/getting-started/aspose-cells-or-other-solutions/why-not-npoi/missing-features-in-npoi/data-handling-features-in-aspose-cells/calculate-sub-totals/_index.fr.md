---
title: Calculer les sous totaux
type: docs
weight: 10
url: /fr/net/calculate-sub-totals/
---

## **Aspose.Cells - Calculer des sous-totaux**
Vous pouvez créer automatiquement des sous-totaux pour toutes les valeurs répétées dans une feuille de calcul. Aspose.Cells offre des fonctionnalités API qui vous aident à ajouter des sous-totaux aux feuilles de calcul de manière programmée.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the Cells collection in the first worksheet

Cells cells = workbook.Worksheets[0].Cells;

//Create a cellarea i.e.., B3:C19

CellArea ca = new CellArea();

ca.StartRow = 2;

ca.StartColumn = 1;

ca.EndRow = 18;

ca.EndColumn = 2;

//Apply subtotal, the consolidation function is Sum and it will applied to

//Second column (C) in the list

cells.Subtotal(ca, 0, ConsolidationFunction.Sum, new int[] { 1 });

//Save the excel file

workbook.Save("AsposeTotal.xls"); 

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Calculer les sous-totaux** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Créer des sous-totaux](/cells/fr/net/creating-subtotals/).

{{% /alert %}}
