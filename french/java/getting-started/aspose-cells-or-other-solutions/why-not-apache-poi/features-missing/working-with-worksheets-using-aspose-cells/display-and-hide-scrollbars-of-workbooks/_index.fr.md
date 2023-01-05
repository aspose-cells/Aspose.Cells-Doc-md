---
title: Afficher et masquer les barres de défilement des classeurs
type: docs
weight: 40
url: /fr/java/display-and-hide-scrollbars-of-workbooks/
---
## **Aspose.Cells - Afficher et masquer les barres de défilement des classeurs**
 Aspose.Cells fournit une classe,**Cahier** qui représente un fichier Excel.**Cahier** fournit un large éventail de propriétés et de méthodes pour gérer un fichier Excel. Mais, pour contrôler la visibilité des barres de défilement dans le fichier Excel, les développeurs peuvent utiliser**setVScrollBarVisiblesetVScrollBarVisible** & **setHScrollBarVisible** méthodes de la**Cahier** classe.

**Java**

{{< highlight "java" >}}

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
## **Télécharger le code d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideScrollbars.java)
