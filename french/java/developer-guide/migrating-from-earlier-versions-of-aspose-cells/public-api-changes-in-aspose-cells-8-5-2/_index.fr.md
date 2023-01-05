---
title: Public API Changements dans Aspose.Cells 8.5.2
type: docs
weight: 190
url: /fr/java/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.5.1 à 8.5.2 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour,[classes ajoutées, etc.](/cells/fr/java/public-api-changes-in-aspose-cells-8-5-2/), mais aussi une description de tout changement de comportement dans les coulisses du Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Rendre la feuille de calcul dans le contexte graphique**
Cette version de Aspose.Cells for Java API a exposé une autre surcharge de la méthode SheetRender.toImage qui permet désormais d'accepter une instance de la classe Graphics2D pour[rendre la feuille de calcul dans le contexte graphique](/cells/fr/java/render-worksheet-to-graphic-context/). Les signatures de la méthode nouvellement ajoutée sont les suivantes.

- SheetRender.toImage(int pageIndex, graphique Graphics2D)

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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
### **Méthode PivotTable.getCellByDisplayName ajoutée**
 Aspose.Cells for Java 8.5.2 a exposé la méthode PivotTable.getCellByDisplayName qui peut être utilisée pour[récupérer l'objet Cell par le nom du PivotField](/cells/fr/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Cette méthode peut être utile dans les scénarios où vous souhaitez mettre en surbrillance ou formater l'en-tête PivotField.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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
### **Propriété SaveOptions.MergeAreas ajoutée**
Aspose.Cells for Java 8.5.2 a exposé la propriété SaveOptions.MergeAreas qui peut accepter une valeur de type booléen. La valeur par défaut est false cependant, si elle est définie sur true, le Aspose.Cells for Java API essaie de fusionner la CellArea individuelle avant d'enregistrer le fichier.

{{% alert color="primary" %}} 

Si une feuille de calcul contient trop de cellules individuelles avec validation appliquée, il est possible que la feuille de calcul résultante soit corrompue. Une solution possible consiste à fusionner les cellules avec des règles de validation identiques ou vous pouvez maintenant utiliser la propriété SaveOptions.MergeAreas pour demander au API de fusionner automatiquement les CellAreas avant l'opération d'enregistrement.

{{% /alert %}} 
### **Propriété Geometry.ShapeAdjustValues ajoutée**
 Avec la version v8.5.2, le Aspose.Cells API a exposé la méthode Geometry.getShapeAdjustValues qui peut être utilisée pour[accéder et modifier les points de réglage de différentes formes](/cells/fr/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Dans l'interface Excel Microsoft, les points de réglage s'affichent sous forme de nœuds en losange jaune.

{{% /alert %}} 

 Par exemple,

1. Le rectangle arrondi a un ajustement pour changer l'arc
1. Triangle a un ajustement pour changer l'emplacement du point
1. Le trapèze a un ajustement pour changer la largeur du haut
1. Les flèches ont deux ajustements pour changer la forme de la tête et de la queue

Voici le scénario d'utilisation le plus simple.

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells for Java 8.5.2 a exposé le champ ConsolidationFunction.DISTINCT_COUNT qui peut être utilisé pour appliquer la fonction consolidée Distinct Count sur DataField d'un tableau croisé dynamique.

{{% alert color="primary" %}} 

La fonction de consolidation Distinct Count est prise en charge par Microsoft Excel 2013 uniquement.

{{% /alert %}}
