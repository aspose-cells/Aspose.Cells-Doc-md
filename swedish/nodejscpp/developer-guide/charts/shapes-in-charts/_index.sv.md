---
title: Former i diagram med Node.js via C++
linktitle: Former i diagram
description: Lär dig att använda Aspose.Cells for Node.js via C++ för att lägga till kontroller och anpassa diagram i Microsoft Excel. Denna guide visar hur man manipulerar diagramselement, justerar formatering och förbättrar det visuella utseendet och användbarheten av diagram.
keywords: Aspose.Cells for Node.js via C++, Diagramkontroller, Diagramanpassning, Microsoft Excel, Diagramelement, Formatering.
type: docs
weight: 70
url: /sv/nodejs-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
Ibland behöver du infoga ritobjekt som etiketter, textrutor, bilder och så vidare i ett diagram. Aspose.Cells kan lägga till kontroller i ett diagram vid körtid.
{{% /alert %}}

## **Lägga till etikettkontroll i diagrammet**

Etiketter ger ett sätt att ge information till användarna om innehållet i ett kalkylblad. Aspose.Cells låter dig lägga till och manipulera etiketter även i diagram.

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) tillhandahåller en metod med namnet [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLabelInChart-number-number-number-number-), som används för att lägga till en etikettkontroll i ett diagram. Nedan finns en lista över de parametrar som används för metoden:

- **överst** – vertikalt avstånd från etiketten till det övre vänstra hörnet i enheter av 1/4000 av diagramområdet.
- **vänster** – det horisontella avståndet från etiketten till det övre vänstra hörnet i enheter av 1/4000 av diagramområdet.
- **höjd** – etikettens höjd, i enheter av 1/4000 av diagramområdet.
- **bredd** – etikettens bredd, i enheter på 1/4000 av diagramområdet.

Metoden returnerar [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/)-objekt. Klassen [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) representerar en etikett i diagrammet. Den har några viktiga medlemmar:

- [**getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) (egenskap) – specificerar en etiketts bildtext.
- [**getFill()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getFill--) (egenskap) – specificerar färgfyllningsegenskaper.

Följande exempel visar hur man lägger till en etikett i diagrammet. Exemplet använder en designerfil (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en etikett i diagrammet. Nedan finns den ursprungliga koden för att lägga till en etikett i diagrammet. Följande utdata genereras när koden utförs.

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

## **Lägga till textbox-styrenhet i diagrammet**

Ett sätt att markera viktig information i en rapport är att använda en textruta. Till exempel, mata in text för att markera företagsnamnet eller för att ange den geografiska regionen med högst försäljning. Klassen [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) tillhandahåller en metod som heter [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-), som används för att lägga till en textruta styrenhet i ett diagram. Följande är parametrarna som används för metoden:

- **top** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **vänster** – den vertikala avvikelsen för textrutan från det övre vänstra hörnet i enheter på 1/4000 av diagramområdet.
- **höjd** – textrutans höjd, i enheter om 1/4000 av diagramområdet.
- **bredd** – textrutans bredd, i enheter om 1/4000 av diagramområdet.

Metoden returnerar [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/)-objekt. Klassen [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) representerar en textruta i diagrammet.

Följande exempel visar hur man lägger till en textruta i ett diagram. Exemplet använder den tidigare designerfilen (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en textruta i diagrammet för att visa diagramtiteln. Nedan finns den ursprungliga koden för att lägga till en textruta i diagrammet.

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

## **Lägga till bild i diagrammet**

Aspose.Cells gör det möjligt att infoga bilder i ett diagram. Till exempel, lägg till en bild för att betona eller ge mer mening åt ett diagram eller dess innehåll, eller infoga en varumärkesbildfil.

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) tillhandahåller en metod som heter [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-), som används för att lägga till ett bildobjekt i diagrammet. Följande är parametrarna som används för metoden:

- **top** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **vänster** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **ström** – en strömobjekt som innehåller bilddata.
- **breddskala** – bildens breddskala, en procentuell värde.
- **höjdskala** – bildens höjdskala, en procentuell värde.

Metoden returnerar ett [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)-objekt. Klassen [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) representerar en bildobjekt i diagrammet.

Följande exempel visar hur man lägger till en bild i diagrammet. Exemplet använder den tidigare designerfilen (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en bild i diagrammet. Nedan finns den ursprungliga koden för att lägga till en bild i diagrammet.

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

## **Lägger till kryssruta i diagrammet**

Aspose.Cells tillåter dig att infoga kryssrutor i ett diagramblad genom att använda [**MsoDrawingType**](https://reference.aspose.com/cells/nodejs-cpp/msodrawingtype/)-uppräkningen. Följande exempel demonstrerar hur man lägger till en kryssruta i ett diagramblad.

Följande bild visar diagrambladet med kryssrutan i utdatafilen.

![todo:image_alt_text](controls-in-charts_1.jpg)

Den [utdatafilen](101089316.xlsx) som genererats av följande kodsnutt bifogas för din referens.

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

## **Fortsatta ämnen**
- [Lägg till WordArt-vattenstämpel på diagram](/cells/sv/nodejs-cpp/add-wordart-watermark-to-chart/)

