---
title: Shapes in Charts mit Node.js über C++
linktitle: Formen in Diagrammen
description: Lernen Sie, wie Sie mit Aspose.Cells for Node.js via C++ Steuerelemente hinzufügen und Diagramme in Microsoft Excel anpassen. Dieser Leitfaden zeigt, wie man Diagrammelemente manipuliert, Formatierungen anpasst und das Gesamtbild sowie die Benutzerfreundlichkeit Ihrer Diagramme verbessert.
keywords: Aspose.Cells for Node.js via C++, Diagrammsteuerungen, Diagrammansage, Microsoft Excel, Diagrammelemente, Formatierung.
type: docs
weight: 70
url: /de/nodejs-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
Manchmal müssen Sie Zeichenobjekte wie Beschriftungen, Textfelder, Bilder usw. in ein Diagramm einfügen. Aspose.Cells kann die Steuerelemente zur Laufzeit zu einem Diagramm hinzufügen.
{{% /alert %}}

## **Hinzufügen von Beschriftungssteuerung zum Diagramm**

Labels bieten eine Möglichkeit, Benutzern Informationen über den Inhalt eines Tabellenblatts zu geben. Aspose.Cells ermöglicht es Ihnen, Labels hinzuzufügen und zu manipulieren, sogar in Diagrammen.

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) stellt eine Methode namens [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLabelInChart-number-number-number-number-) zur Verfügung, die verwendet wird, um dem Diagramm eine Beschriftungssteuerung hinzuzufügen. Im Folgenden finden Sie eine Liste der Parameter, die für die Methode verwendet werden:

- **top** – der vertikale Versatz der Beschriftung von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Versatz der Beschriftung von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **height** – die Höhe der Beschriftung, in Einheiten von 1/4000 des Diagrammbereichs.
- **width** – die Breite der Beschriftung, in Einheiten von 1/4000 des Diagrammbereichs.

Die Methode gibt ein [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/)-Objekt zurück. Die Klasse [**Label**](https://reference.aspose.com/cells/nodejs-cpp/label/) stellt eine Beschriftung im Diagramm dar. Sie verfügt über einige wichtige Elemente:

- [**getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) (Eigenschaft) – gibt einen Beschriftungszeichenfolgenwert an.
- [**getFill()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getFill--) (Eigenschaft) – gibt die Farbfüllungseigenschaften an.

Im folgenden Beispiel wird gezeigt, wie eine Beschriftung dem Diagramm hinzugefügt wird. Das Beispiel verwendet eine Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um eine Beschriftung in das Diagramm einzufügen. Unten finden Sie den ursprünglichen Code zum Hinzufügen einer Beschriftung zum Diagramm. Die folgende Ausgabe wird beim Ausführen des Codes generiert.

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

## **Hinzufügen einer Textfeldsteuerung zum Diagramm**

Eine Möglichkeit, wichtige Informationen in einem Bericht hervorzuheben, besteht darin, einen Textbereich zu verwenden. Geben Sie beispielsweise Text ein, um den Firmennamen hervorzuheben oder das geografische Gebiet mit den höchsten Verkäufen anzuzeigen. Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) stellt eine Methode namens [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-) zur Verfügung, die verwendet wird, um dem Diagramm eine Textfeldsteuerung hinzuzufügen. Im Folgenden finden Sie die verwendete Parameterliste für die Methode:

- **top** – der vertikale Versatz des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Versatz des Textfelds von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **height** – die Höhe des Textfelds, in Einheiten von 1/4000 des Diagrammbereichs.
- **width** – die Breite des Textfelds, in Einheiten von 1/4000 des Diagrammbereichs.

Die Methode gibt ein [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/)-Objekt zurück. Die Klasse [**TextBox**](https://reference.aspose.com/cells/nodejs-cpp/textbox/) stellt ein Textfeld im Diagramm dar.

Im folgenden Beispiel wird gezeigt, wie ein Textfeld zu einem Diagramm hinzugefügt wird. Das Beispiel verwendet die vorherige Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um ein Textfeld in das Diagramm einzufügen, um den Diagrammtitel anzuzeigen. Unten finden Sie den ursprünglichen Code zum Hinzufügen eines Textfelds zum Diagramm.

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

## **Hinzufügen eines Bilds zum Diagramm**

Mit Aspose.Cells können Sie Bilder in ein Diagramm einfügen. Fügen Sie beispielsweise ein Bild hinzu, um ein Diagramm oder seine Inhalte zu betonen oder mehr Bedeutung zu verleihen oder fügen Sie eine Markenbild-Datei ein.

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/) stellt eine Methode namens [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-) zur Verfügung, die verwendet wird, um ein Bildobjekt dem Diagramm hinzuzufügen. Im Folgenden finden Sie die verwendete Parameterliste für die Methode:

- **top** – der vertikale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **left** – der horizontale Abstand des Bildes von der oberen linken Ecke in Einheiten von 1/4000 des Diagrammbereichs.
- **stream** – ein Stream-Objekt, das die Bilddaten enthält.
- **widthScale** – die Skalierung der Bildbreite, ein Prozentsatz.
- **heightScale** – die Skalierung der Bildhöhe, ein Prozentsatz.

Die Methode gibt ein [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)-Objekt zurück. Die Klasse [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) stellt ein Bildobjekt im Diagramm dar.

Das folgende Beispiel zeigt, wie Sie ein Bild zum Diagramm hinzufügen. Das Beispiel verwendet die vorige Designerdatei (**exp_piechart.xls**), die ein Diagramm enthält. Wir verwenden diese Datei, um ein Bild in das Diagramm einzufügen. Unten finden Sie den ursprünglichen Code zum Hinzufügen eines Bildes zum Diagramm.

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

## **Checkbox in das Diagramm einfügen**

Aspose.Cells ermöglicht es Ihnen, Checkboxen in ein Diagrammblatt einzufügen, indem Sie die [**MsoDrawingType**](https://reference.aspose.com/cells/nodejs-cpp/msodrawingtype/)-Aufzählung verwenden. Das folgende Beispiel zeigt das Hinzufügen einer Checkbox zu einem Diagrammblatt.

Das folgende Bild zeigt das Diagrammblatt mit der Checkbox in der Ausgabedatei.

![todo:image_alt_text](controls-in-charts_1.jpg)

Die [Ausgabedatei](101089316.xlsx), die durch den folgenden Code-Schnipsel generiert wurde, ist als Referenz angehängt.

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

## **Erweiterte Themen**
- [Fügen Sie dem Diagramm ein WordArt-Wasserzeichen hinzu](/cells/de/nodejs-cpp/add-wordart-watermark-to-chart/)

