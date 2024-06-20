---
title: Calcul des sous totaux à l aide d Aspose.Cells
type: docs
weight: 20
url: /fr/java/calculate-sub-totals-using-aspose-cells/
---

## **Aspose.Cells - Calculer des sous-totaux**
Vous pouvez créer automatiquement des sous-totaux pour toutes les valeurs répétées dans une feuille de calcul. Aspose.Cells offre des fonctionnalités API qui vous aident à ajouter des sous-totaux aux feuilles de calcul de manière programmée.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook

Workbook workbook = new Workbook("book1.xls");

//Get the Cells collection in the first worksheet

Cells cells = workbook.getWorksheets().get(0).getCells();

//Create a cellarea i.e.., B3:C19

CellArea ca = new CellArea();

ca.StartRow = 2;

ca.StartColumn =1;

ca.EndRow = 18;

ca.EndColumn = 2;

//Apply subtotal, the consolidation function is Sum and it will applied to

//Second column (C) in the list

cells.subtotal(ca, 0, ConsolidationFunction.SUM, new int[] { 1 });

//Save the excel file

workbook.save("AsposeTotal.xls");

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/formula/AsposeCreateSubTotals.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Créer des sous-totaux](/cells/fr/java/creating-subtotals).

{{% /alert %}}
