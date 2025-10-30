---  
title: Infoga bilder och former i Excel filer med Node.js via C++  
linktitle: Former  
type: docs  
weight: 140  
url: /sv/nodejs-cpp/insert-shapes/  
description: Hantera bilder, OLE objekt och former i Excel filer med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Ibland måste du infoga vissa nödvändiga former i kalkylbladet. Du kan behöva infoga samma form på olika positioner i kalkylbladet. Eller så måste du batchinfoga former i kalkylbladet.  
Var inte orolig! [Aspose.Cells](https://products.aspose.com/cells/) stöder alla dessa operationer.  
{{% /alert %}}  

Former i Excel är huvudsakligen indelade i följande typer:  
- **Bilder**  
- **OleObjekt**  
- **Linjer**  
- **Rektanglar**  
- **Grundformer**  
- **Blockpilar**  
- **Ekvationformer**  
- **Flödesscheman**  
- **Stjärnor och banderoller**  
- **Inrop**  

Detta guide-dokument kommer att välja en eller två former från varje typ för att skapa exempel. Genom dessa exempel kommer du att lära dig hur du använder [Aspose.Cells](https://products.aspose.com/cells/) för att infoga den specificerade formen i kalkylbladet.  

## **Lägga till bilder i Excel-kalkylblad med Node.js**  

Att lägga till bilder i ett kalkylblad är mycket enkelt. Det tar bara några rader kod:  
 Anropa helt enkelt [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-)-metoden för [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) objektet). [**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-number-number-uint8array-)-metoden tar följande parametrar:  

- **Övre vänstra radindex**, indexet för den övre vänstra raden.  
- **Övre vänstra kolumnindex**, indexet för den övre vänstra kolumnen.  
- **Bildfilnamn**, namnet på bildfilen, komplett med sökväg.  

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

## **Infoga OLE-objekt i Excel-kalkylblad med Node.js**  

Aspose.Cells stöder tillägg, extrahering och manipulation av OLE-objekt i kalkylblad. Av denna anledning har Aspose.Cells klassen [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection), som används för att lägga till ett nytt OLE-objekt till listan. En annan klass, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), representerar ett OLE-objekt. Den har några viktiga medlemmar:  

- Egenskapen [**OleObject.getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) specificerar bild (ikonen) data av typ byte-array. Bilden kommer att visas för att visa OLE-objektet i kalkbladet.  
- Egenskapen [**OleObject.getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) specificerar objektets data i form av en byte-array. Denna data kommer att visas i det relaterade programmet när du dubbelklickar på OLE-objektets ikon.  

Följande exempel visar hur man lägger till en OLE-objekt/-objekt i ett arbetsblad.  

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

## **Infoga en linje i Excel-kalkylblad med Node.js**  

Linjens form tillhör kategorin **lines**.  

***I Microsoft Excel (till exempel 2007):***  

- Välj cellen där du vill infoga linjen  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan linjen från 'Senast använda former' eller 'Lines'  

![](line.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga en linje i kalkylarket.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Metoden returnerar ett [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape) objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar en linje i ett kalkylblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](line2.png)  

## **Infoga en linjepil i Excel-kalkylblad med Node.js**  

Formen av linjepilen tillhör kategorin **Lines**. Det är ett specialfall av linje.  

***I Microsoft Excel (till exempel 2007):***  

- Välj cellen där du vill infoga linjepilen  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan linjepilen från 'Senast använda former' eller 'Lines'  

![](line_arrow1.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga en linjepil i kalkylarket.  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
Metoden returnerar ett [LineShape](https://reference.aspose.com/cells/nodejs-cpp/lineshape) objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar en linje pil i ett kalkylblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](line_arrow2.png)  

## **Infoga ett rektangel i Excel-kalkylblad med Node.js**  

Formen av rektangeln tillhör kategorin **Rectangles**.  

***I Microsoft Excel (till exempel 2007):***  

- Välj cellen där du vill infoga rektangeln  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan rektangeln från 'Senast använda former' eller 'Rectangles'  

![](rectangle.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga en rektangel i kalkylarket.  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
Metoden returnerar ett [RectangleShape](https://reference.aspose.com/cells/nodejs-cpp/rectangleshape) objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar ett rektangel i ett kalkylblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](rectangle2.png)  

## **Infoga en Kub i Excel-Arbetsblad med Node.js**  

Kubens form tillhör kategorin **Grundformer**.  

***I Microsoft Excel (till exempel 2007):***  

- Välj cellen där du vill infoga kuben  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan Kuben från **Grundformer**  

![](cube.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga en kub i kalkylarket.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Metoden returnerar ett [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape) objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar en kub i ett arbetsblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](cube2.png)  

## **Infoga ett callout-quad-kommando i Excel-Arbetsblad med Node.js**  

Formen av callout-quad-kommando tillhör kategorin **Blockpilar**.  

***I Microsoft Excel (till exempel 2007):***  

- Välj cellen där du vill infoga återuppringningspilar  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan callout-quad-kommando från **Blockpilar**  

![](callout_quad_arrow.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga återuppringningspilar i kalkylarket.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Metoden returnerar ett [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape) objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar ett callout-quad-kommando i ett arbetsblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](callout_quad_arrow2.png)  

## **Infoga ett multiplikations-tecken i Excel-Arbetsblad med Node.js**  

Formen av multiplikationstecknet tillhör kategorin **Ekvationsformer**.  

***I Microsoft Excel (till exempel 2007):***  

- Välj cellen där du vill infoga multiplikationstecknet  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan multiplikationstecknet från **Ekvationsformer**  

![](multiplication_sign.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga ett multiplikationstecken i kalkylarket.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Metoden returnerar ett [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape) objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar ett multiplikations-tecken i ett arbetsblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](multiplication_sign2.png)  

## **Infoga ett flerdokument i Excel-Arbetsblad med Node.js**  

Formen av flerdokumentet tillhör kategorin **Flödesscheman**.  

***I Microsoft Excel (till exempel 2007):***  

- Välj cellen där du vill infoga multi-dokument  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan flerdokumentet från **Flödesscheman**  

![](multidocument.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga ett multi-dokument i arbetsbladet.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Metoden returnerar ett [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape) objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar ett flerdokument i ett arbetsblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](multidocument2.png)  

## **Infoga en femuddig stjärna i Excel-Arbetsblad med Node.js**  

Formen av femuddig stjärna tillhör kategorin **Stjärnor och Band**.  

***I Microsoft Excel (till exempel 2007):***  

- Välj cellen där du vill infoga Femuddig stjärna  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan femuddig stjärna från **Stjärnor och Band**  

![](star_5_points.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga en Femuddig stjärna i arbetsbladet.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Metoden returnerar ett [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape) objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar en femuddig stjärna i ett arbetsblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](star_5_points2.png)  

## **Infoga en tankebubbla i Excel-Arbetsblad med Node.js**  

Formen av tankebubblan tillhör kategorin **Callouts**.  

***I Microsoft Excel (till exempel 2007):***  

- Välj cellen där du vill infoga pratbubblan  
- Klicka på Infoga-menyn och klicka på Former.  
- Välj sedan tankebubblan från **Callouts**  

![](thought_bubble_cloud.png)  

***Använda Aspose.Cells***  

Du kan använda följande metod för att infoga en pratbubbla i arbetsbladet.  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
Metoden returnerar ett [Shape](https://reference.aspose.com/cells/nodejs-cpp/shape) objekt.  
{{% /alert %}}  

Följande exempel visar hur man infogar en tankebubbla i ett arbetsblad.  

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

Exekvera ovanstående kod, kommer du att få följande resultat:  

![](thought_bubble_cloud2.png)  

## **Fortsatta ämnen**  
- [Ändra justeringsvärden för formen](/cells/sv/nodejs-cpp/change-adjustment-values-of-the-shape/)  
- [Kopiera former mellan kalkylblad](/cells/sv/nodejs-cpp/copy-shapes-between-worksheets/)  
- [Data i icke-primitiv form](/cells/sv/nodejs-cpp/data-in-non-primitive-shape/)  
- [Hitta absolut position av formen inuti kalkylbladet](/cells/sv/nodejs-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [Hämta anslutningspunkter från formen](/cells/sv/nodejs-cpp/get-connection-points-from-shape/)  
- [Hantera kontroller](/cells/sv/nodejs-cpp/managing-controls/)  
- [Lägg till ikoner i kalkylbladet](/cells/sv/nodejs-cpp/insert-svg-to-excel/)  
- [Hantera OLE-objekt](/cells/sv/nodejs-cpp/managing-ole-objects/)  
- [Hantera bilder](/cells/sv/nodejs-cpp/managing-pictures/)  
- [Hantera SmartArt](/cells/sv/nodejs-cpp/managing-smartart/)  
- [Hantera TextBox](/cells/sv/nodejs-cpp/managing-textbox-of-excel/)  
- [Lägg till WordArt-vattenstämpel på arbetsbladet](/cells/sv/nodejs-cpp/add-wordart-watermark-to-worksheet/)  
- [Uppdatera värdena i länkade former](/cells/sv/nodejs-cpp/refresh-values-of-linked-shapes/)  
- [Skicka form framåt eller bakåt inne i Arbetsbladet](/cells/sv/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [Hantera formalternativ](/cells/sv/nodejs-cpp/managing-shape-options/)  
- [Hantera textalternativ för formen](/cells/sv/nodejs-cpp/managing-shape-text-options/)  
- [Webbutökningar - Office-tillägg](/cells/sv/nodejs-cpp/web-extensions-office-add-ins/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
