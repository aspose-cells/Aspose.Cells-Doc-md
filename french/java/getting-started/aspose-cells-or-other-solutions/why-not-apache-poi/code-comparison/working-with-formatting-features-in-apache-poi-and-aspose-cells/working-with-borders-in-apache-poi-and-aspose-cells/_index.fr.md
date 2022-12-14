---
title: Utilisation des bordures dans Apache POI et Aspose.Cells
type: docs
weight: 10
url: /fr/java/working-with-borders-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Travailler avec les bordures**
Aspose.Cells fournit une classe,[Cahier](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)qui représente un fichier Excel Microsoft. La classe Workbook contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)classer. La classe Worksheet fournit une Cellscollection. Chaque pièce de la collection Cells représente un objet de la[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)classer.

Aspose.Cells fournit la méthode setStyle dans le[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)classe utilisée pour définir le style de formatage d'une cellule. De plus, l'objet Style de la[Style](http://docs.aspose.com:8082/docs/display/cellsjava/Style)La classe est utilisée et fournit des propriétés pour configurer les paramètres de police.

**Java**

{{< highlight "java" >}}

 // Style the cell with borders all around.

Style style = workbook.createStyle();

style.setBorder(BorderType.BOTTOM_BORDER, CellBorderType.THIN, Color.getBlack());

style.setBorder(BorderType.LEFT_BORDER, CellBorderType.THIN, Color.getGreen());

style.setBorder(BorderType.RIGHT_BORDER, CellBorderType.THIN, Color.getBlue());

style.setBorder(BorderType.TOP_BORDER, CellBorderType.MEDIUM_DASH_DOT, Color.getBlack());

// Setting style to the cell

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Utilisation des frontières**
La classe CellStyle fournit des fonctionnalités pour définir les paramètres de bordure à l'aide d'Apache POI SS - HSSF et XSSF.

**Java**

{{< highlight "java" >}}

 //Setting the line of the top border

style.setBorder(BorderType.TOP_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the bottom border

style.setBorder(BorderType.BOTTOM_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the left border

style.setBorder(BorderType.LEFT_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the right border

style.setBorder(BorderType.RIGHT_BORDER,CellBorderType.THICK,Color.getBlack());

//Saving the modified style to the "A1" cell.

cell.setStyle(style);

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Ajout de bordures au Cells](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
