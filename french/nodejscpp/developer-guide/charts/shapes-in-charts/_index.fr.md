---
title: Formes dans les graphiques avec Node.js via C++
linktitle: Formes dans les graphiques
description: Apprenez à utiliser Aspose.Cells for Node.js via C++ pour ajouter des contrôles et personnaliser les graphiques dans Microsoft Excel. Ce guide montre comment manipuler les éléments du graphique, ajuster le formatage et améliorer l’aspect général et l’utilisabilité de vos graphiques.
keywords: Aspose.Cells for Node.js via C++, Contrôles de graphique, Personnalisation de graphique, Microsoft Excel, Éléments de graphique, Formatage.
type: docs
weight: 70
url: /fr/nodejs-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
Parfois, vous avez besoin d'insérer des objets de dessin comme des étiquettes, des boîtes de texte, des images, etc. dans un graphique. Aspose.Cells peut ajouter les contrôles à un graphique à l'exécution.
{{% /alert %}}

## **Ajout de contrôle d'étiquette au graphique**

Les étiquettes fournissent un moyen de fournir des informations aux utilisateurs sur le contenu d'une feuille de calcul. Aspose.Cells vous permet d'ajouter et de manipuler des étiquettes même dans les graphiques.

La classe [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) fournit une méthode nommée [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLabelInChart-number-number-number-number-), utilisée pour ajouter un contrôle d'étiquette à un graphique. Voici une liste des paramètres utilisés pour la méthode :

- **haut** – le décalage vertical de l'étiquette depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **gauche** – le décalage horizontal de l'étiquette depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **hauteur** – la hauteur de l'étiquette, en unités de 1/4000 de la zone du graphique.
- **largeur** – la largeur de l'étiquette, en unités de 1/4000 de la zone du graphique.

La méthode retourne un objet [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/). La classe [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) représente une étiquette dans le graphique. Elle a quelques membres importants :

- [**getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) (propriété) - spécifie la chaîne de légende d'une étiquette.
- [**getFill()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getFill--) (propriété) - spécifie les attributs de couleur de remplissage.

L'exemple suivant montre comment ajouter une étiquette au graphique. L'exemple utilise un fichier de concepteur (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une étiquette dans le graphique. Ci-dessous se trouve le code d'origine pour ajouter une étiquette au graphique. La sortie suivante est générée lors de l'exécution du code.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new label to the chart.
const label = chart.getShapes().addLabelInChart(100, 100, 350, 900);

// Set the caption of the label.
label.setText("A Label In Chart");

// Set the Placement Type, the way the Label is attached to the cells.
label.setPlacement(AsposeCells.PlacementType.FreeFloating);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Ajout d'un contrôle TextBox au graphique**

Une manière de mettre en évidence des informations importantes dans un rapport est d'utiliser une zone de texte. Par exemple, saisissez du texte pour mettre en valeur le nom de l'entreprise ou pour indiquer la région géographique avec le plus de ventes. La classe [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) fournit une méthode appelée [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-), qui est utilisée pour ajouter un contrôle de zone de texte à un graphique. Voici la liste des paramètres utilisés pour la méthode :

- **top** - le décalage vertical de la zone de texte depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **left** - le décalage vertical de la zone de texte depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **height** - la hauteur de la zone de texte, en unités de 1/4000 de la zone du graphique.
- **width** - la largeur de la zone de texte, en unités de 1/4000 de la zone du graphique.

La méthode renvoie un objet [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/). La classe [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) représente une zone de texte dans le graphique.

L'exemple suivant montre comment ajouter une zone de texte à un graphique. L'exemple utilise le fichier de concepteur précédent (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une zone de texte dans le graphique pour afficher le titre du graphique. Ci-dessous se trouve le code d'origine pour ajouter une zone de texte au graphique.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xls"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Add a new textbox to the chart.
const textbox0 = chart.getShapes().addTextBoxInChart(100, 1100, 350, 2550);

// Fill the text.
textbox0.setText("Sales By Region");

// Get the textbox text frame.
// const textframe0 = textbox0.getTextFrame();

// Set the textbox to adjust it according to its contents.
// textframe0.setAutoSize(true);

// Set the font color.
textbox0.getFont().setColor(AsposeCells.Color.Maroon);

// Set the font to bold.
textbox0.getFont().setIsBold(true);

// Set the font size.
textbox0.getFont().setSize(14);

// Set font attribute to italic.
textbox0.getFont().setIsItalic(true);

// Get the fill format of the textbox.
const fillformat = textbox0.getFill();

// Get the line format type of the textbox.
const lineformat = textbox0.getLine();

// Set the line weight.
lineformat.setWeight(2);

// Set the dash style to solid.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Ajout d'une image au graphique**

Aspose.Cells vous permet d'insérer des images dans un graphique. Par exemple, ajoutez une image pour mettre en avant ou donner plus de sens à un graphique ou à son contenu, ou insérez un fichier image de marque.

La classe [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) fournit une méthode nommée [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-), qui est utilisée pour ajouter un objet image au graphique. Voici la liste des paramètres utilisés pour la méthode :

- **top** - le décalage vertical de l'image depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **left** - le décalage vertical de l'image depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **stream** - un objet flux qui contient les données de l'image.
- **widthScale** - l'échelle de la largeur de l'image, une valeur en pourcentage.
- **heightScale** - l'échelle de la hauteur de l'image, une valeur en pourcentage.

La méthode renvoie un objet [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). La classe [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) représente un objet image dans le graphique.

L'exemple suivant montre comment ajouter une image au graphique. L'exemple utilise le fichier de conception précédent (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une image dans le graphique. Ci-dessous se trouve le code d'origine pour ajouter une image au graphique.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart_shapes.xls"));

// Get an image file to the stream.
const stream = fs.readFileSync(path.join(dataDir, "logo.jpg"));

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(0);
const chart = sheet.getCharts().get(0);

// Add a new picture to the chart.
const pic0 = chart.getShapes().addPictureInChart(50, 50, stream, 40, 40);

// Get the lineformat type of the picture.
const lineformat = pic0.getLine();          

// Set the dash style.
lineformat.setDashStyle(AsposeCells.MsoLineDashStyle.Solid);

// Set the line weight.
lineformat.setWeight(4);    

// Save the excel file.
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Ajout d'une case à cocher dans le graphique**

Aspose.Cells vous permet d'insérer des cases à cocher dans une feuille de graphique en utilisant l'énumération [**MsoDrawingType**](https://reference.aspose.com/cells/nodejs-cpp/msodrawingtype/). L'exemple suivant montre comment ajouter une case à cocher à une feuille de graphique.

L'image suivante montre la feuille de graphique avec la case à cocher dans le fichier de sortie.

![todo:image_alt_text](controls-in-charts_1.jpg)

Le [fichier de sortie](101089316.xlsx) généré par le snippet de code suivant est joint à titre de référence.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a chart to the worksheet
const index = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);

const sheet = workbook.getWorksheets().get(index);
sheet.getCharts().addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);
sheet.getCharts().get(0).getNSeries().add("{1,2,3}", false);

// Add checkbox to the chart.
sheet.getCharts().get(0).getShapes().addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);
sheet.getCharts().get(0).getShapes().get(0).setText("CheckBox 1");

// Save the excel file.
workbook.save(outputDir +"InsertCheckboxInChartSheet_out.xlsx");
```

## **Sujets avancés**
- [Ajouter un filigrane WordArt au graphique](/cells/fr/nodejs-cpp/add-wordart-watermark-to-chart/)

