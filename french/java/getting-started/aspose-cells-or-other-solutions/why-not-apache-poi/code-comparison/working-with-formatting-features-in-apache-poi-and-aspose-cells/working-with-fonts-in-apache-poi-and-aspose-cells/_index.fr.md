---
title: Utilisation des polices dans Apache POI et Aspose.Cells
type: docs
weight: 30
url: /fr/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Travailler avec des polices**
Aspose.Cells fournit une classe,[Cahier](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)qui représente un fichier Excel Microsoft. La classe Workbook contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)classe. La classe Worksheet fournit une collection Cells. Chaque pièce de la collection Cells représente un objet de la[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)classe.

**Java**

{{< highlight "java" >}}

 //Adding some value to cell

Cell cell = cells.get("A1");

cell.setValue("This is Aspose test of fonts!");

//Setting the font name to "Courier New"

Style style = cell.getStyle();

Font font = style.getFont();

font.setName("Courier New");

font.setSize(24);

font.setBold(true);

font.setUnderline(FontUnderlineType.SINGLE);

font.setColor(Color.getBlue());

font.setStrikeout(true);

//font.setSubscript(true);

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Utilisation des polices**
Apache POI SS fournit une classe de police pour définir divers paramètres de police.

**Java**

{{< highlight "java" >}}

 // Create a new font and alter it.

Font font = wb.createFont();

font.setFontHeightInPoints((short)24);

font.setFontName("Courier New");

font.setItalic(true);

font.setStrikeout(true);

// Fonts are set into a style so create a new one to use.

CellStyle style = wb.createCellStyle();

style.setFont(font);

// Create a cell and put a value in it.

Cell cell = row.createCell(1);

cell.setCellValue("This is a test of fonts");

cell.setCellStyle(style);

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/fonts)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Gestion des paramètres de police](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}
