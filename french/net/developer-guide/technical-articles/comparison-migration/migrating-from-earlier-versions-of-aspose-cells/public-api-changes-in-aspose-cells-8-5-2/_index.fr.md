---
title: Changements de l API publique dans Aspose.Cells 8.5.2
type: docs
weight: 180
url: /fr/net/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.5.1 à la version 8.5.2 qui pourraient intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, [classes ajoutées, etc.](/cells/fr/net/changements-de-l-api-publique-dans-aspose-cells-8-5-2/), mais également une description de tout changement dans le comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Rendre la feuille de calcul dans le contexte graphique**
Cette version de Aspose.Cells for .NET API a exposé deux nouvelles surcharges de la méthode SheetRender.ToImage qui permet désormais d'accepter une instance de la classe System.Drawing.Graphics pour [rendre dans le contexte Graphics](/cells/fr/net/render-worksheet-to-graphic-context/). Les signatures des méthodes nouvellement ajoutées sont les suivantes.

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Create empty Bitmap

Bitmap bmp = new Bitmap(800, 800);

//Create Graphics Context

Graphics g = Graphics.FromImage(bmp);

g.Clear(Color.Blue);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.OnePagePerSheet = true;

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.ToImage(0, g, 0, 0);

//Save the graphics context image in Png format

bmp.Save("test.png", ImageFormat.Png);

{{< /highlight >}}


### **Méthode PivotTable.GetCellByDisplayName ajoutée**
Aspose.Cells for .NET 8.5.2 a exposé la méthode PivotTable.GetCellByDisplayName qui peut être utilisée pour [récupérer l'objet Cell par le nom du PivotField](/cells/fr/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Cette méthode pourrait être utile dans des scénarios où vous souhaitez mettre en évidence ou formater l'en-tête du PivotField.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.PivotTables[0];

//Access cell by display name of 2nd data field of the pivot table

Cell cell = pivotTable.GetCellByDisplayName(pivotTable.DataFields[1].DisplayName);

//Access cell style and set its fill color and font color

Style style = cell.GetStyle();

style.ForegroundColor = Color.LightBlue;

style.Font.Color = Color.Black;

//Set the style of the cell

pivotTable.Format(cell.Row, cell.Column, style);

//Save workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Ajout de la propriété SaveOptions.MergeAreas**
Aspose.Cells for .NET 8.5.2 a exposé la propriété SaveOptions.MergeAreas qui peut accepter une valeur de type booléen. La valeur par défaut est fausse cependant, si elle est définie sur vrai, l'API Aspose.Cells for .NET tente de fusionner les CellArea individuelles avant d'enregistrer le fichier.

{{% alert color="primary" %}} 

Si une feuille de calcul comporte trop de cellules individuelles avec une validation appliquée, il y a des chances que la feuille de calcul résultante soit corrompue. Une solution possible est de fusionner les cellules avec des règles de validation identiques ou vous pouvez maintenant utiliser la propriété SaveOptions.MergeAreas pour indiquer à l'API de fusionner automatiquement les CellAreas avant l'opération de sauvegarde.

{{% /alert %}} 
### **Propriété Shape.Geometry.ShapeAdjustValues ajoutée**
Avec la version 8.5.2, l'API Aspose.Cells a exposé la propriété Shape.Geometry.ShapeAdjustValues qui peut être utilisée pour [apporter des modifications aux points d'ajustement de différentes formes](/cells/fr/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Dans l'interface Microsoft Excel, les points d'ajustement s'affichent sous forme de nœuds de diamants jaunes.

{{% /alert %}} 

Par exemple,

1. Le rectangle arrondi a un ajustement pour changer l'arc.
1. Le triangle a un ajustement pour changer l'emplacement du point.
1. Le trapèze a un ajustement pour changer la largeur du haut.
1. Les flèches ont deux ajustements pour changer la forme de la tête et de la queue.

Voici le scénario d'utilisation le plus simple.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first three shapes of the worksheet

Shape shape1 = worksheet.Shapes[0];

Shape shape2 = worksheet.Shapes[1];

Shape shape3 = worksheet.Shapes[2];

//Change the adjustment values of the shapes

shape1.Geometry.ShapeAdjustValues[0].Value = 0.5d;

shape2.Geometry.ShapeAdjustValues[0].Value = 0.8d;

shape3.Geometry.ShapeAdjustValues[0].Value = 0.5d;

//Save the workbook

workbook.Save("output.xls);

{{< /highlight >}}


### **Énumération Field ConsolidationFunction.DistinctCount ajoutée**
Aspose.Cells for .NET 8.5.2 a exposé le champ ConsolidationFunction.DistinctCount qui peut être utilisé pour [appliquer la fonction de consolidation de dénombrement distinct](/cells/fr/net/consolidation-function/) sur le DataField d'un tableau croisé dynamique.

{{% alert color="primary" %}} 

La fonction de consolidation de comptage distinct est prise en charge uniquement par Microsoft Excel 2013.

{{% /alert %}} 
### **Meilleure gestion des événements pour GridDesktop**
Cette version de Aspose.Cells.GridDesktop a exposé 4 nouveaux événements. 2 de ces événements se déclenchent à différents états du chargement des fichiers de feuille de calcul dans GridDesktop tandis que les 2 autres se déclenchent lors du calcul des formules.

Les événements sont listés comme suit.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
{{< app/cells/assistant language="csharp" >}}
