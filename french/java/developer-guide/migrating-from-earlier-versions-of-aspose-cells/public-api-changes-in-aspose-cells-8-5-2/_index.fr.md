---
title: Changements de l API publique dans Aspose.Cells 8.5.2
type: docs
weight: 190
url: /fr/java/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.5.1 à la version 8.5.2 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement les méthodes publiques nouvelles et mises à jour, les [classes ajoutées, etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-5-2/), mais aussi une description de tout changement dans le comportement en coulisse d'Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Rendre la feuille de calcul dans le contexte graphique**
Cette version de l'API Aspose.Cells for Java a exposé une autre surcharge de la méthode SheetRender.toImage qui permet maintenant d'accepter une instance de la classe Graphics2D pour [rendre la feuille de calcul dans le contexte graphique](/cells/fr/java/render-worksheet-to-graphic-context/). Les signatures de la méthode nouvellement ajoutée sont les suivantes.

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Create empty image and fill it with blue color

int width = 800;

int height = 800;

BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

Graphics2D g = image.createGraphics();

g.setColor(java.awt.Color.blue);

g.fillRect(0, 0, width, height);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setOnePagePerSheet(true);

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.toImage(0, g);

//Save the graphics context image in Png format

File outputfile = new File("test.png");

ImageIO.write(image, "png", outputfile);

{{< /highlight >}}
### **Ajout de la méthode PivotTable.getCellByDisplayName**
Aspose.Cells for Java 8.5.2 a exposé la méthode PivotTable.getCellByDisplayName qui peut être utilisée pour [récupérer l'objet Cell par le nom du Champ de la Table Pivot](/cells/fr/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Cette méthode pourrait être utile dans des scénarios où vous souhaitez mettre en surbrillance ou formater l'en-tête du Champ de la Table Pivot.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Access cell by display name of 2nd data field of the pivot table

String displayName = pivotTable.getDataFields().get(1).getDisplayName();

Cell cell = pivotTable.getCellByDisplayName(displayName);

//Access cell style and set its fill color and font color

Style style = cell.getStyle();

style.setForegroundColor(Color.getLightBlue());

style.getFont().setColor(Color.getBlack());

//Set the style of the cell

pivotTable.format(cell.getRow(), cell.getColumn(), style);

//Save workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Ajout de la propriété SaveOptions.MergeAreas**
Aspose.Cells for Java 8.5.2 a exposé la propriété SaveOptions.MergeAreas qui peut accepter une valeur de type booléen. La valeur par défaut est fausse cependant, si elle est définie sur true, l'API Aspose.Cells for Java tente de fusionner les CellArea individuelles avant de sauvegarder le fichier.

{{% alert color="primary" %}} 

Si une feuille de calcul comporte trop de cellules individuelles avec une validation appliquée, il y a des chances que la feuille de calcul résultante soit corrompue. Une solution possible est de fusionner les cellules avec des règles de validation identiques ou vous pouvez maintenant utiliser la propriété SaveOptions.MergeAreas pour indiquer à l'API de fusionner automatiquement les CellAreas avant l'opération de sauvegarde.

{{% /alert %}} 
### **Ajout de la propriété Geometry.ShapeAdjustValues**
Avec la version 8.5.2, l'API Aspose.Cells a exposé la méthode Geometry.getShapeAdjustValues qui peut être utilisée pour [accéder et apporter des modifications aux points d'ajustement de différentes formes](/cells/fr/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Dans l'interface de Microsoft Excel, les points d'ajustement s'affichent sous forme de nœuds en forme de diamant jaune.

{{% /alert %}} 

Par exemple, 

1. Le rectangle arrondi a un ajustement pour changer l'arc.
1. Le triangle a un ajustement pour changer l'emplacement du point.
1. Le trapèze a un ajustement pour changer la largeur du haut.
1. Les flèches ont deux ajustements pour changer la forme de la tête et de la queue.

Voici le scénario d'utilisation le plus simple.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first three shapes of the worksheet

Shape shape1 = worksheet.getShapes().get(0);

Shape shape2 = worksheet.getShapes().get(1);

Shape shape3 = worksheet.getShapes().get(2);

//Change the adjustment values of the shapes

shape1.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

shape2.getGeometry().getShapeAdjustValues().get(0).setValue(0.8d);

shape3.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Champ d'énumération ConsolidationFunction.DISTINCT_COUNT ajouté**
Aspose.Cells for Java 8.5.2 a exposé le champ ConsolidationFunction.DISTINCT_COUNT qui peut être utilisé pour appliquer la fonction consolidée de comptage distinct sur DataField d'un PivotTable.

{{% alert color="primary" %}} 

La fonction de consolidation de comptage distinct est prise en charge uniquement par Microsoft Excel 2013.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
