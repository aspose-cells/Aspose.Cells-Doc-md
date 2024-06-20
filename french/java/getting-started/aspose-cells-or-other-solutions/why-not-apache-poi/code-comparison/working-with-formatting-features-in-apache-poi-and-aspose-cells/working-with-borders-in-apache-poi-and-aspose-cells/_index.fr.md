---
title: Travailler avec les bordures dans Apache POI et Aspose.Cells
type: docs
weight: 10
url: /fr/java/working-with-borders-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Travailler avec les bordures**
Aspose.Cells fournit une classe, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) qui représente un fichier Microsoft Excel. La classe Workbook contient une collection de feuilles de calcul qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). La classe Worksheet fournit une collection de cellules. Chaque élément dans la collection de cellules représente un objet de la classe [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell).

Aspose.Cells fournit la méthode setStyle dans la classe [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) utilisée pour définir le style de mise en forme d'une cellule. De plus, l'objet Style de la classe [Style](http://docs.aspose.com:8082/docs/display/cellsjava/Style) est utilisé et fournit des propriétés pour configurer les paramètres de police.

**Java**

{{< highlight java >}}

 // Style the cell with borders all around.

Style style = workbook.createStyle();

style.setBorder(BorderType.BOTTOM_BORDER, CellBorderType.THIN, Color.getBlack());

style.setBorder(BorderType.LEFT_BORDER, CellBorderType.THIN, Color.getGreen());

style.setBorder(BorderType.RIGHT_BORDER, CellBorderType.THIN, Color.getBlue());

style.setBorder(BorderType.TOP_BORDER, CellBorderType.MEDIUM_DASH_DOT, Color.getBlack());

// Setting style to the cell

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Travailler avec les bordures**
La classe CellStyle fournit des fonctionnalités pour définir les paramètres de bordure à l'aide d'Apache POI SS - HSSF et XSSF.

**Java**

{{< highlight java >}}

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
## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Ajouter des bordures aux cellules](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
