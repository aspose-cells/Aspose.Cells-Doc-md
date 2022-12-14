---
title: Utilisation des couleurs dans Apache POI et Aspose.Cells
type: docs
weight: 20
url: /fr/java/working-with-colors-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Travailler avec les couleurs**
Aspose.Cells fournit une classe,[Cahier](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), qui représente un fichier Excel Microsoft. La classe Workbook contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)classer. La classe Worksheet fournit une Cellscollection. Chaque pièce de la collection Cells représente un objet de la[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)classer.

Aspose.Cells fournit la méthode setStyle dans la classe Cell qui est utilisée pour définir la mise en forme d'une cellule. En outre, l'objet Style de la classe Style peut être utilisé pour configurer les paramètres de police.

**Java**

{{< highlight "java" >}}

 //Accessing cell from the worksheet

Cell cell = cells.get("B2");

Style style = cell.getStyle();

//Setting the foreground color to yellow

style.setBackgroundColor(Color.getYellow());

//Setting the background pattern to vertical stripe

style.setPattern(BackgroundType.VERTICAL_STRIPE);

//Saving the modified style to the "A1" cell.

cell.setStyle(style);

// === Setting Foreground ===

//Adding custom color to the palette at 55th index

Color color = Color.fromArgb(212,213,0);

workbook.changePalette(color,55);

//Accessing cell from the worksheet

cell = cells.get("B3");

//Adding some value to the cell

cell.setValue("Hello Aspose!");

//Setting the custom color to the font

style = cell.getStyle();

Font font = style.getFont();

font.setColor(color);

cell.setStyle(style);


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Travailler avec les couleurs**
La classe CellStyle est disponible pour définir les paramètres d'arrière-plan et de motif de remplissage.

**Java**

{{< highlight "java" >}}

 // Aqua background

CellStyle style = wb.createCellStyle();

style.setFillBackgroundColor(IndexedColors.AQUA.getIndex());

style.setFillPattern(CellStyle.BIG_SPOTS);

Cell cell = row.createCell((short) 1);

cell.setCellValue("X");

cell.setCellStyle(style);

// Orange "foreground", foreground being the fill foreground not the font color.

style = wb.createCellStyle();

style.setFillForegroundColor(IndexedColors.ORANGE.getIndex());

style.setFillPattern(CellStyle.SOLID_FOREGROUND);

cell = row.createCell((short) 2);

cell.setCellValue("X");

cell.setCellStyle(style);

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Couleurs et motifs de fond](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns).

{{% /alert %}}
