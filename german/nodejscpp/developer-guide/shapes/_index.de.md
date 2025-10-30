---  
title: Bilder und Formen in Excel Dateien mit Node.js über C++ einfügen  
linktitle: Formen  
type: docs  
weight: 140  
url: /de/nodejs-cpp/insert-shapes/  
description: Verwalten Sie Bilder, OLE Objekte und Formen in Excel Dateien mit Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Manchmal müssen Sie einige notwendige Formen in das Arbeitsblatt einfügen. Sie müssen möglicherweise die gleiche Form an verschiedenen Positionen des Arbeitsblatts einfügen. Oder Sie müssen Stapel von Formen in das Arbeitsblatt einfügen.  
Keine Sorge! [Aspose.Cells](https://products.aspose.com/cells/) unterstützt all diese Operationen.  
{{% /alert %}}  

Die Formen in Excel werden hauptsächlich in die folgenden Typen unterteilt:  
- **Bilder**  
- **OLE-Objekte**  
- **Linien**  
- **Rechtecke**  
- **Grundformen**  
- **Blockpfeile**  
- **Gleichungsformen**  
- **Flussdiagramme**  
- **Sterne und Banner**  
- **Legenden**  

Dieses Leitfadendokument wählt eine oder zwei Formen aus jedem Typ aus, um Muster zu erstellen. Durch diese Beispiele lernen Sie, wie man [Aspose.Cells](https://products.aspose.com/cells/) benutzt, um die angegebene Form in das Arbeitsblatt einzufügen.  

## **Bilder in Excel-Arbeitsblatt mit Node.js hinzufügen**  

Das Hinzufügen von Bildern zu einer Tabelle ist sehr einfach. Es dauert nur wenige Zeilen Code:  
Rufen Sie einfach die [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-)-Methode der [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection)-Sammlung auf (verkapselt im [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Objekt). Die [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-)-Methode nimmt folgende Parameter:   

- **Index der oberen linken Zeile**, der Index der oberen linken Zeile.  
- **Index der oberen linken Spalte**, der Index der oberen linken Spalte.  
- **Bilddateiname**, der Name der Bilddatei inklusive des Pfads.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **OLE-Objekte in Excel-Arbeitsblatt mit Node.js einfügen**  

Aspose.Cells unterstützt das Hinzufügen, Extrahieren und Verwalten von OLE-Objekten in Arbeitsblättern. Zu diesem Zweck enthält Aspose.Cells die [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection)-Klasse, die verwendet wird, um ein neues OLE-Objekt zur Sammlungsliste hinzuzufügen. Eine andere Klasse, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), stellt ein OLE-Objekt dar. Sie besitzt einige wichtige Mitglieder:  

- Die [**OleObject.getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--)-Eigenschaft gibt die Bild- (Symbol-) Daten vom Typ Byte-Array an. Das Bild wird angezeigt, um das OLE-Objekt im Arbeitsblatt zu zeigen.  
- Die [**OleObject.getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--)-Eigenschaft gibt die Objekt-Daten in Form eines Byte-Arrays an. Diese Daten werden in ihrem zugehörigen Programm angezeigt, wenn Sie doppelt auf das OLE-Objekt-Icon klicken.  

Das folgende Beispiel zeigt, wie man OLE-Objekte in ein Arbeitsblatt einfügt.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const excelFilePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(excelFilePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Linie in das Excel-Arbeitsblatt mit Node.js einfügen**  

Die Form der Linie gehört zur Kategorie **Linien**.  

***In Microsoft Excel (zum Beispiel 2007):***  

- Wählen Sie die Zelle aus, in die Sie die Linie einfügen möchten.  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Wählen Sie dann die Linie aus 'Kürzlich verwendete Formen' oder 'Linien'  

![](line.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um eine Linie im Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Die Methode gibt ein [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape)-Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man eine Linie in ein Arbeitsblatt einfügt.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line to the worksheet
sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// sheet.getShapes().addAutoShape(AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// sheet.getShapes().addShape(MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// Save. You can check your line in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](line2.png)  

## **Einen Linienpfeil in das Excel-Arbeitsblatt mit Node.js einfügen**  

Der Form des Linienpfeils gehört zur Kategorie **Linien**. Es ist eine Spezialform der Linie.  

***In Microsoft Excel (zum Beispiel 2007):***  

- Wählen Sie die Zelle aus, in der Sie den Linienpfeil einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Wählen Sie dann den Linienpfeil aus 'Kürzlich verwendete Formen' oder 'Linien'  

![](line_arrow1.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um einen Linienpfeil in das Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Die Methode gibt ein [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape)-Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man einen Linienpfeil in ein Arbeitsblatt einfügt.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the line arrow to the worksheet
let s = sheet.getShapes().addLine(2, 0, 2, 0, 100, 300); // method 1
// let s = sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
// let s = sheet.getShapes().addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

// add a arrow at the line begin
s.getLine().setBeginArrowheadStyle(AsposeCells.MsoArrowheadStyle.Arrow); // arrow type
s.getLine().setBeginArrowheadWidth(AsposeCells.MsoArrowheadWidth.Wide); // arrow width
s.getLine().setBeginArrowheadLength(AsposeCells.MsoArrowheadLength.Short); // arrow length

// add a arrow at the line end
s.getLine().setEndArrowheadStyle(AsposeCells.MsoArrowheadStyle.ArrowOpen); // arrow type
s.getLine().setEndArrowheadWidth(AsposeCells.MsoArrowheadWidth.Narrow); // arrow width
s.getLine().setEndArrowheadLength(AsposeCells.MsoArrowheadLength.Long); // arrow length

// Save. You can check your arrow in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](line_arrow2.png)  

## **Rechteck in das Excel-Arbeitsblatt mit Node.js einfügen**  

Die Form des Rechtecks gehört zur Kategorie **Rechtecke**.  

***In Microsoft Excel (zum Beispiel 2007):***  

- Wählen Sie die Zelle, in die Sie das Rechteck einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Wählen Sie dann das Rechteck aus 'Kürzlich verwendete Formen' oder 'Rechtecke'  

![](rectangle.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um ein Rechteck im Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
Die Methode gibt ein [RectangleShape](https://reference.aspose.com/cells/nodejs-cpp/rectangleshape)-Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man ein Rechteck in ein Arbeitsblatt einfügt.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the rectangle to the worksheet
sheet.getShapes().addRectangle(2, 0, 2, 0, 100, 300);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](rectangle2.png)  

## **In das Excel-Arbeitsblatt mit Node.js einen Würfel einfügen**  

Die Form des Würfels gehört zur Kategorie **Grundformen**.  

***In Microsoft Excel (zum Beispiel 2007):***  

- Wählen Sie die Zelle, in die Sie den Würfel einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Wählen Sie dann den Würfel aus **Grundformen**  

![](cube.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um einen Würfel im Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Die Methode gibt ein [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape)-Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man einen Würfel in ein Arbeitsblatt einfügt.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the cube to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

// Save. You can check your cube in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](cube2.png)  

## **Einen Callout-Quadratpfeil in das Excel-Arbeitsblatt mit Node.js einfügen**  

Die Form des Callout-Quadratpfeils gehört zur Kategorie **Blockpfeile**.  

***In Microsoft Excel (zum Beispiel 2007):***  

- W�hlen Sie die Zelle aus, in die Sie den Callout-Quad-Pfeil einf�gen m�chten.  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Wählen Sie dann den Callout-Quadratpfeil aus **Blockpfeile**  

![](callout_quad_arrow.png)  

***Mit Aspose.Cells verwenden***  

Sie k�nnen die folgende Methode verwenden, um einen Callout-Quad-Pfeil in das Arbeitsblatt einzuf�gen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Die Methode gibt ein [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape)-Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man eine Callout-Quadratapplikation in ein Arbeitsblatt einfügt.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the callout quad arrow to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

//Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](callout_quad_arrow2.png)  

## **Einfügen eines Multiplikationszeichens in das Excel-Arbeitsblatt mit Node.js**  

Die Form des Multiplikationszeichens gehört zur Kategorie **Gleichungsformen**.  

***In Microsoft Excel (zum Beispiel 2007):***  

- Wählen Sie die Zelle aus, in der Sie das Multiplikationszeichen einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Dann wählen Sie das Multiplikationszeichen aus **Gleichungsformen**  

![](multiplication_sign.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um ein Multiplikationszeichen im Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Die Methode gibt ein [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape)-Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man ein Multiplikationszeichen in ein Arbeitsblatt einfügt.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multiplication sign to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

// Save. You can check your multiplication in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](multiplication_sign2.png)  

## **Einfügen eines Multi-Dokument in das Excel-Arbeitsblatt mit Node.js**  

Die Form des Multi-Dokuments gehört zur Kategorie **Flowcharts**.  

***In Microsoft Excel (zum Beispiel 2007):***  

- Wählen Sie die Zelle aus, in der Sie das Multi-Dokument einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Dann wählen Sie das Multi-Dokument aus **Flowcharts**  

![](multidocument.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um ein Multidokument in das Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Die Methode gibt ein [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape)-Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man ein Multi-Dokument in ein Arbeitsblatt einfügt.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the multidocument to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](multidocument2.png)  

## **Einfügen eines fünfzackigen Sterns in ein Excel-Arbeitsblatt mit Node.js**  

Die Form des fünfzackigen Sterns gehört zur Kategorie **Sterne und Banner**.  

***In Microsoft Excel (zum Beispiel 2007):***  

- Wählen Sie die Zelle aus, in die Sie den Fünfzackigen Stern einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Dann wählen Sie den fünfzackigen Stern aus **Sterne und Banner**  

![](star_5_points.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um einen Fünfzackigen Stern in das Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Die Methode gibt ein [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape)-Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man einen fünfzackigen Stern in ein Arbeitsblatt einfügt.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create workbook from sample file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the Five-pointed star to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

// Save. You can check your icon in this way.
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](star_5_points2.png)  

## **Einfügen einer Gedankenblasenwolke in das Excel-Arbeitsblatt mit Node.js**  

Die Form der Gedankenblasenwolke gehört zur Kategorie **Callouts**.  

***In Microsoft Excel (zum Beispiel 2007):***  

- Wählen Sie die Zelle aus, in die Sie die Gedankenblasenwolke einfügen möchten  
- Klicken Sie auf das Menü 'Einfügen' und dann auf 'Formen'.  
- Dann wählen Sie die Gedankenblasenwolke aus **Callouts**  

![](thought_bubble_cloud.png)  

***Mit Aspose.Cells verwenden***  

Sie können die folgende Methode verwenden, um eine Gedankenblasenwolke in das Arbeitsblatt einzufügen.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Die Methode gibt ein [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape)-Objekt zurück.  
{{% /alert %}}  

Das folgende Beispiel zeigt, wie man eine Gedankenblasenwolke in ein Arbeitsblatt einfügt.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the thought bubble cloud to the worksheet
sheet.getShapes().addAutoShape(AsposeCells.AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

// Save
workbook.save("sample.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

Führen Sie den obigen Code aus, und Sie erhalten die folgenden Ergebnisse:  

![](thought_bubble_cloud2.png)  

## **Erweiterte Themen**  
- [Ändern der Anpassungswerte der Form](/cells/de/nodejs-cpp/change-adjustment-values-of-the-shape/)  
- [Formen zwischen Arbeitsblättern kopieren](/cells/de/nodejs-cpp/copy-shapes-between-worksheets/)  
- [Daten in nicht primitiver Form](/cells/de/nodejs-cpp/data-in-non-primitive-shape/)  
- [Absolute Position der Form im Arbeitsblatt finden](/cells/de/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Verbindungspunkte von Form erhalten](/cells/de/nodejs-cpp/get-connection-points-from-shape/)  
- [Steuerungen verwalten](/cells/de/nodejs-cpp/managing-controls/)  
- [Symbole zum Arbeitsblatt hinzufügen](/cells/de/nodejs-cpp/insert-svg-to-excel/)  
- [OLE-Objekte verwalten](/cells/de/nodejs-cpp/managing-ole-objects/)  
- [Bilder verwalten](/cells/de/nodejs-cpp/managing-pictures/)  
- [SmartArt verwalten](/cells/de/nodejs-cpp/managing-smartart/)  
- [TextBox verwalten](/cells/de/nodejs-cpp/managing-textbox-of-excel/)  
- [Fügen Sie dem Arbeitsblatt eine WordArt-Wasserzeichen hinzu](/cells/de/nodejs-cpp/add-wordart-watermark-to-worksheet/)  
- [Werte verlinkter Formen aktualisieren](/cells/de/nodejs-cpp/refresh-values-of-linked-shapes/)  
- [Form nach vorn oder hinten im Arbeitsblatt senden](/cells/de/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Formoptionen verwalten](/cells/de/nodejs-cpp/managing-shape-options/)  
- [Textoptionen der Form verwalten](/cells/de/nodejs-cpp/managing-shape-text-options/)  
- [Weberweiterungen - Office-Add-Ins](/cells/de/nodejs-cpp/web-extensions-office-add-ins/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
