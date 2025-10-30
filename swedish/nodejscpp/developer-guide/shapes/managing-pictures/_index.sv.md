---  
title: Hantera bilder med Node.js via C++  
linktitle: Hantera bilder  
type: docs  
weight: 10  
url: /sv/nodejs-cpp/managing-pictures/  
description: Lär dig hur du lägger till och placerar bilder i kalkblad med Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells tillåter utvecklare att lägga till bilder i kalkylbladet under körtiden. Dessutom kan placeringen av dessa bilder styras under körtiden, vilket diskuteras mer utförligt i de kommande avsnitten.

Den här artikeln förklarar hur du lägger till bilder och hur du infogar en bild som visar innehållet i vissa celler.

## **Lägga till bilder**

Att lägga till bilder i ett kalkylblad är mycket enkelt. Det tar bara några rader kod:  
 Anropa helt enkelt [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-)-metoden för [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) objektet). [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-)-metoden tar följande parametrar:

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

## **Placering av bilder**

Det finns två möjliga sätt att kontrollera placeringen av bilder med hjälp av Aspose.Cells:

- Proportionell placering: definiera ett läge proportionellt med radhöjden och kolumnbredden.
- Absolut positionering: definiera den exakta positionen på sidan där bilden kommer att infogas, till exempel 40 pixlar till vänster och 20 pixlar under cellens kant.

### **Proportionell placering**

Utvecklare kan positionera bilder proportionellt i förhållande till radhöjd och kolumnbredd med hjälp av [**getUpperDeltaX()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaX--)- och [**getUpperDeltaY()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaY--)-egenskaperna hos [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)-objektet. Ett [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)-objekt kan erhållas från [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection)-samlingen genom att ange dess bildindex. Detta exempel placerar en bild i cellen F6.

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
const pictureIndex = worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Positioning the picture proportional to row height and column width
picture.setUpperDeltaX(200);
picture.setUpperDeltaY(200);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Absolut positionering**

Utvecklare kan också positionera bilder absolut genom att använda [**getLeft()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeft--)- och [**getTop()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTop--)-egenskaperna hos [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)-objektet. Detta exempel placerar en bild i cell F6, 60 pixlar från vänster och 10 pixlar från toppen av cellen.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "logo.jpg");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, filePath);

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Absolute positioning of the picture in unit of pixels
picture.setLeft(60);
picture.setTop(10);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Infoga en bild baserad på cellreferens**

Aspose.Cells låter dig visa innehållet i en arbetsbladscell i en bildform. Du kan länka bilden till cellen som innehåller de data du vill visa. Eftersom cellen eller cellintervallet är länkat till den grafiska objektet, visas ändringar som du gör i data i den cellen eller cellintervallet automatiskt i den grafiska objektet.

Lägg till en bild i kalkbladet genom att anropa [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-)-metoden för [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-objektet). Specificera cellområdet med hjälp av [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--)-attributet hos [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/)-objektet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

const picts = workbook.getWorksheets().get(0).getPictures();
// Add a blank picture to the D1 cell
const picIndex = picts.add(0, 3, 10, 6, null);
const pic = picts.get(picIndex);

// Specify the formula that refers to the source range of cells

pic.setFormula("A1:C10");

// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Fortsatta ämnen**
- [Lägg till villkorliga ikoner inställda med celltexten](/cells/sv/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/)
- [Infoga en Länkbild från Webbadress](/cells/sv/nodejs-cpp/insert-a-linked-picture-from-web-address/)
- [Infoga en Bild Baserat på Cellreferens](/cells/sv/nodejs-cpp/insert-a-picture-based-on-cell-reference/)
- [Ladda en webbbild från en URL till ett Excel-arbetsblad](/cells/sv/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="nodejs-cpp" >}}
