---
title: Afficher et masquer les barres de défilement des classeurs dans xlsx4j
type: docs
weight: 30
url: /fr/java/display-and-hide-scrollbars-of-workbooks-in-xlsx4j/
---

## **Aspose.Cells - Afficher et masquer les barres de défilement des classeurs**
Aspose.Cells fournit une classe, **Workbook** qui représente un fichier Excel. La classe **Workbook** offre un large éventail de propriétés et de méthodes pour gérer un fichier Excel. Mais, pour contrôler la visibilité des barres de défilement dans le fichier Excel, les développeurs peuvent utiliser les méthodes **setVScrollBarVisible** et **setHScrollBarVisible** de la classe **Workbook**.

**Java**

{{< highlight java >}}

 //Instantiating a Excel object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeSrollbarsHide.xls");

// ===============================================================

//Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true);

//Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplaySrollbars.xls");


{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidescrollbars/AsposeDisplayAndHideScrollbars.java)
