---
title: Formattare e modificare intervalli denominati con Node.js tramite C++
linktitle: Formattare e modificare intervalli con nome
type: docs
weight: 85
url: /it/nodejs-cpp/format-and-modify-named-ranges/
description: Impara come formattare e modificare intervalli denominati usando Aspose.Cells for Node.js via C++. 
---

## **Formattare intervalli**

### **Impostazione del colore di sfondo e degli attributi del carattere su un intervallo nominato**

Per applicare la formattazione, definisci un oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) per specificare le impostazioni di stile e applicalo all'oggetto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).

Nell'esempio seguente viene mostrato come impostare il colore di riempimento solido (colore ombreggiatura) con impostazioni del carattere a un intervallo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const WS = workbook.getWorksheets().get(0);

// Create a range of cells.
const range = WS.getCells().createRange(1, 1, 1, 18);

// Name the range.
range.setName("MyRange");

// Declare a style object.
let stl;

// Create/add the style object.
stl = workbook.createStyle();

// Specify some Font settings.
stl.getFont().setName("Arial");
stl.getFont().setIsBold(true);

// Set the font text color
stl.getFont().setColor(AsposeCells.Color.Red);

// To Set the fill color of the range, you may use ForegroundColor with
// Solid Pattern setting.
stl.setForegroundColor(AsposeCells.Color.Yellow);
stl.setPattern(AsposeCells.BackgroundType.Solid);

// Create a StyleFlag object.
let flg = new AsposeCells.StyleFlag();
// Make the corresponding attributes ON.
flg.setFont(true);
flg.setCellShading(true);

// Apply the style to the range.
range.applyStyle(stl, flg);

// Save the excel file.
workbook.save(path.join(dataDir, "rangestyles.out.xls"));
```

### **Aggiunta di bordi a un intervallo nominato**

È possibile aggiungere bordi a un intervallo di celle invece di una singola cella. L'oggetto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) offre un metodo [**setOutlineBorder(BorderType, CellBorderType, CellsColor)**](https://reference.aspose.com/cells/nodejs-cpp/range/#setOutlineBorder-bordertype-cellbordertype-cellscolor-) che accetta i seguenti parametri per aggiungere un bordo all'intervallo di celle:

- Tipo di bordo, il tipo di bordo, selezionato dall'enumerazione [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype).
- Stile linea, lo stile della linea, selezionato dall'enumerazione [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype).
- Colore, il colore della linea, selezionato dall'enumerazione dei Colori.

L'esempio seguente mostra come impostare un bordo di contorno a un intervallo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Clears the worksheets
workbook.getWorksheets().clear();

// Adding a new worksheet to the Workbook object
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello World From Aspose");

// Creating a range of cells starting from "A1" cell to 3rd column in a row
const range = worksheet.getCells().createRange(0, 0, 1, 3);

// Adding a thick top border with blue line
range.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Thick, AsposeCells.Color.Blue);

// Adding a thick bottom border with blue line
range.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Thick, AsposeCells.Color.Blue);

// Adding a thick left border with blue line
range.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Thick, AsposeCells.Color.Blue);

// Adding a thick right border with blue line
range.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Thick, AsposeCells.Color.Blue);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

Il seguente esempio mostra come impostare i bordi intorno ad ogni cella nell'intervallo.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the cells in the first worksheet.
const cells = workbook.getWorksheets().get(0).getCells();

// Create a range of cells.
const range = cells.createRange("A6", "P216");

// Declare style.
let stl;

// Create the style adding to the style collection.
stl = workbook.createStyle();

// Specify the font settings.
stl.getFont().setName("Arial");
stl.getFont().setIsBold(true);
stl.getFont().setColor(AsposeCells.Color.Blue);

// Set the borders
stl.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
stl.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Blue);
stl.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
stl.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Blue);
stl.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
stl.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Blue);
stl.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
stl.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Blue);

// Create StyleFlag object.
const flg = new AsposeCells.StyleFlag();
// Make the corresponding formatting attributes ON.
flg.setFont(true);
flg.setBorders(true);

// Apply the style with format settings to the range.
range.applyStyle(stl, flg);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

## **Rinomina un intervallo nominato**

Aspose.Cells consente di rinominare un intervallo denominato secondo le proprie esigenze. Puoi ottenere l'intervallo denominato e rinominarlo utilizzando l'attributo [**Name.getText()**](https://reference.aspose.com/cells/nodejs-cpp/name/#getText--). Il seguente esempio mostra come rinominare un intervallo denominato.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an existing Excel file that has a (global) named range "TestRange" in it
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Get the Cells of the sheet
const cells = sheet.getCells();

// Get the named range "MyRange"
const name = workbook.getWorksheets().getNames().get("TestRange");

// Rename it
name.setText("NewRange");

// Save the Excel file
workbook.save(path.join(dataDir, "RenamingRange.out.xlsx"));
```

## **Unione di intervalli**

Aspose.Cells fornisce il metodo [**Range.unionRang(Range)**](https://reference.aspose.com/cells/nodejs-cpp/range/#unionRang-range-) per unire intervalli; il metodo restituisce un oggetto [*Array*]. Il seguente esempio mostra come unire intervalli.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Instantiate a workbook object.
// Open an existing excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the named ranges.
const ranges = workbook.getWorksheets().getNamedRanges();

// Create a style object.
const style = workbook.createStyle();

// Set the shading color with solid pattern type.
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Create a styleflag object.
const flag = new AsposeCells.StyleFlag();

// Apply the cellshading.
flag.setCellShading(true);

// Creates an array list.
let al = [];

// Get the array list collection apply the union operation.
al = ranges[0].unionRanges([ranges[1]]);

// Define a range object.
let rng;
let frow, fcol, erow, ecol;

for (let i = 0; i < al.length; i++)
{
// Get a range.
rng = al[i];
frow = rng.getFirstRow();
fcol = rng.getFirstColumn();
erow = rng.getRowCount();
ecol = rng.getColumnCount();

// Apply the style to the range.
rng.applyStyle(style, flag);
}

// Save the excel file.
workbook.save(path.join(dataDir, "rngUnion.out.xls"));
```

## **Intersezione di intervalli**

Aspose.Cells fornisce il metodo [**Range.intersect(Range)**](https://reference.aspose.com/cells/nodejs-cpp/range/#intersect-range-) per l'intersezione di due intervalli. Il metodo restituisce un oggetto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). Per verificare se un intervallo interseca un altro, usa il metodo [**Range.intersect(Range)**](https://reference.aspose.com/cells/nodejs-cpp/range/#intersect-range-) che restituisce un valore Booleano. Il seguente esempio mostra come intersectare gli intervalli.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiate a workbook object.
// Open an existing excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the named ranges.
const ranges = workbook.getWorksheets().getNamedRanges();

// Check whether the first range intersect the second range.
const isIntersect = ranges[0].isIntersect(ranges[1]);

// Create a style object.
const style = workbook.createStyle();

// Set the shading color with solid pattern type.
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Create a styleflag object.
const flag = new AsposeCells.StyleFlag();

// Apply the cell shading.
flag.setCellShading(true);

// If first range intersects second range.
if (isIntersect) {
// Create a range by getting the intersection.
const intersection = ranges[0].intersect(ranges[1]);

// Name the range.
intersection.setName("Intersection");

// Apply the style to the range.
intersection.applyStyle(style, flag);
}

// Save the excel file.
workbook.save(path.join(dataDir, "rngIntersection.out.xls"));
```

## **Unisci celle nell'intervallo nominato**

Aspose.Cells fornisce il metodo [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) per unire le celle nell'intervallo. Il seguente esempio mostra come unire le singole celle di un intervallo denominato.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const wb1 = new AsposeCells.Workbook();

// Get the first worksheet in the workbook.
const worksheet1 = wb1.getWorksheets().get(0);

// Create a range.
const mrange = worksheet1.getCells().createRange("A18", "J18");

// Name the range.
mrange.setName("Details");

// Merge the cells of the range.
mrange.merge();

// Get the range.
const range1 = wb1.getWorksheets().getRangeByName("Details");      

// Define a style object.
const style = wb1.createStyle();

// Set the alignment.
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Create a StyleFlag object.
const flag = new AsposeCells.StyleFlag();
// Make the relative style attribute ON.
flag.setHorizontalAlignment(true);

// Apply the style to the range.
range1.applyStyle(style, flag);

// Input data into range.
range1.get(0, 0).putValue("Aspose");

// Save the excel file.
wb1.save(path.join(dataDir, "mergingrange.out.xls"));
```

## **Rimuovere un intervallo nominato**

Aspose.Cells fornisce il metodo [**NameCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#removeAt-number-) per cancellare il nome dell'intervallo. Per cancellare i contenuti dell'intervallo, usa il metodo [**Cells.clearRange(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#clearRange-cellarea-). Il seguente esempio mostra come rimuovere un intervallo denominato con i suoi contenuti.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = worksheets.get(0);

// Create a range of cells.
const range1 = worksheet.getCells().createRange("E12", "I12");

// Name the range.
range1.setName("MyRange");

// Set the outline border to the range.
range1.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));

// Input some data with some formattings into
// A few cells in the range.
range1.get(0, 0).putValue("Test");            
range1.get(0, 4).putValue("123");

// Create another range of cells.
const range2 = worksheet.getCells().createRange("B3", "F3");

// Name the range.
range2.setName("testrange");

// Copy the first range into second range.
range2.copy(range1);

// Remove the previous named range (range1) with its contents.
worksheet.getCells().clearRange(11, 4, 11, 8);
worksheets.getNames().removeAt(0);

// Save the excel file.
workbook.save(path.join(dataDir, "copyranges.out.xls"));
```
