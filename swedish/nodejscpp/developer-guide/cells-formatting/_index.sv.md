---
title: Formatera celler med Node.js via C++
description: Lär dig hur du formaterar och stilar celler i Aspose.Cells for Node.js via C++, inklusive numreringsformat, datumformat, teckensnittsstilar och andra cellstilalternativ. Vår guide hjälper dig att skapa attraktiva och professionella kalkylblad.
keywords: Aspose.Cells for Node.js via C++, cellformat, styling, nummerformat, datumformat, teckenstils, cellstilalternativ, kalkylblad, skapa, professionellt utseende, formatera rader och kolumner.
linktitle: Formatera celler
type: docs
weight: 120
url: /sv/nodejs-cpp/cells-formatting/
---

## **Introduktion**

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) och [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) metoderna av [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen, för att få/ställa in formatstilen för en cell. Aspose.Cells tillhandahåller också en [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) klass.

{{% /alert %}}

## **Hur man formaterar celler med hjälp av GetStyle och SetStyle-metoderna**

Tillämpa olika typer av formateringsstilar på celler för att ställa in bakgrund eller förgrundsfärger, ramar, typsnitt, horisontell och vertikal justering, indenteringsnivå, textriktning, rotationsvinkel och mycket mer.

### **Hur man använder GetStyle och SetStyle-metoderna**

Om utvecklare behöver tillämpa olika formateringsstilar på olika celler är det bättre att få [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) av cellen med hjälp av [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--)-metoden, specificera stilde attributes och sedan tillämpa formateringen med [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)-metoden. Ett exempel ges nedan för att demonstrera detta tillvägagångssätt för att tillämpa olika formatering på en cell.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Defining a Style object
let style;

// Get the style from A1 cell
style = cell.getStyle();

// Setting the vertical alignment
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text
style.getFont().setColor(AsposeCells.Color.Green);

// Setting to shrink according to the text contained in it
style.setShrinkToFit(true);

// Setting the bottom border color to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Applying the style to A1 cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Hur man använder Style-objektet för att formatera olika celler**

Om utvecklare behöver tillämpa samma formateringsstil på olika celler kan de använda [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektet. Följ stegen nedan för att använda [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektet:

1. Lägg till ett [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objekt genom att anropa [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--)-metoden av [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen
2. Åtkomst till det nyss tillagda [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektet
3. Sätt de önskade egenskaperna/attributen för [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektet för att tillämpa önskad formateringsinställning
4. Tilldela det konfigurerade [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektet till dina önskade celler

Denna metod kan avsevärt förbättra effektiviteten i dina applikationer och spara minne också.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the first worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Adding a new Style
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Assigning the Style object to the "A1" cell
cell.setStyle(style);

// Apply the same style to some other cells
worksheet.getCells().get("B1").setStyle(style);
worksheet.getCells().get("C1").setStyle(style);
worksheet.getCells().get("D1").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Hur man använder Microsoft Excel 2007 Fördefinierade Stilar**

Om du behöver tillämpa olika formateringsstilar för Microsoft Excel 2007, tillämpa stilar med hjälp av Aspose.Cells API. Ett exempel ges nedan för att visa denna metod att tillämpa en fördefinierad stil på en cell.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");


// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Create a style object.
const style = workbook.createStyle();

// Input a value to A1 cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Test");

// Apply the style to the cell.
workbook.getWorksheets().get(0).getCells().get("A1").setStyle(style);

// Save the Excel 2007 file.
workbook.save(path.join(dataDir, "book1.out.xlsx"));
```



## **Hur man formaterar valda tecken i en cell**

Hantera typsnittsinställningar förklarar hur man formaterar text i celler, men det förklarar bara hur man formaterar allt cellinnehåll. Vad händer om du vill formatera endast utvalda tecken?

Aspose.Cells stöder också denna funktion. Denna guide förklarar hur man använder denna funktion effektivt.

### **Hur man formaterar valda tecken**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som tillåter åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller en [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samling. Varje objekt i [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen.

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen tillhandahåller [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-)-metoden som tar följande parametrar för att välja ett teckenintervall inom en cell:

- **Startindex**, index för tecknet som urvalet börjar från.
- **Antal tecken**, antalet tecken att välja.

'[**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-)'-metoden returnerar en instans av [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)-klassen som tillåter utvecklare att formatere tecknen på samma sätt som de skulle formatera en cell, som visas nedan i kodexemplet. I utdatafilen kommer ordet 'Visit' i cell A1 att formateras med standardteckensnitt men 'Aspose!' är fetstilt och blå.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first(default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the font of selected characters to bold
const font = cell.characters(6, 7).getFont();
font.isBold = true;

// Setting the font color of selected characters to blue
font.color = AsposeCells.Color.Blue;

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

{{% alert color="primary" %}}

Om du är intresserad av att formatera en del av Rich Text i en cell, överväg att använda [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) & [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-)-metoderna. [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--)-metoden används för att komma åt textdelarna och sedan kan ändringar göras med [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-)-metoden medan 'Get'-metoden returnerar en array av [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)-objekt som kan manipuleras för att ställa in olika egenskaper såsom teckensnittnamn, teckenfärg, fetstil m.m. och 'Set'-metoden kan användas för att tillämpa ändringarna.

{{% /alert %}}

## **Hur man formaterar rader och kolumner**

Ibland behöver utvecklare tillämpa samma formatering på rader eller kolumner. Att tillämpa formatering på celler en i taget tar ofta längre tid och är inte en bra lösning.
För att lösa detta problem tillhandahåller Aspose.Cells ett enkelt, snabbt sätt som diskuteras utförligt i den här artikeln.

### **Formatering av rader & kolumner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen ger en [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samling. [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen ger en [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--)-samling.

### **Hur man formaterar en rad**

Varje objekt i [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--)-samlingen representerar ett [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)-objekt. [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)-objektet erbjuder [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-)-metoden som används för att ställa in radens formatering. För att tillämpa samma formatering på en rad, använd [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektet. Stegen nedan visar hur man använder det.

1. Lägg till ett [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objekt till [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen genom att anropa dess [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--)-metod.
2. Sätt egenskaperna för [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektet för att tillämpa formateringsinställningarna.
3. Gör de relevanta attributen ON för [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)-objektet.
4. Tilldela det konfigurerade [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektet till [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)-objektet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a row from the Rows collection
const row = worksheet.getCells().getRows().get(0);

// Assigning the Style object to the Style property of the row
row.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Hur man formaterar en kolumn**

[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen ger också en [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--)-samling. Varje objekt i [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--)-samlingen representerar ett [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column)-objekt. Liknande ett [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)-objekt, erbjuder [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column)-objektet också [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-)-metoden för att formatera en kolumn.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a column from the Columns collection
const column = worksheet.getCells().getColumns().get(0);

// Applying the style to the column
column.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Fortsatta ämnen**
- [Justering inställningar](/cells/sv/nodejs-cpp/cells-alignment-settings/)
- [Kantinställningar](/cells/sv/nodejs-cpp/cells-border-settings/)
- [Ställa in villkorlig formatering av Excel och ODS-filer.](/cells/sv/nodejs-cpp/conditional-formatting/)
- [Excel-teman och färger](/cells/sv/nodejs-cpp/excel-themes-and-colors/)
- [Fyllinställningar](/cells/sv/nodejs-cpp/cells-fill-settings/)
- [Typsnittinställningar](/cells/sv/nodejs-cpp/cells-font-settings/)
- [Formatera kalkylbladsceller i en arbetsbok](/cells/sv/nodejs-cpp/format-worksheet-cells-in-a-workbook/)
- [Implementera 1904 Datasystem](/cells/sv/nodejs-cpp/implement-1904-date-system/)
- [Sammanfoga och dela upp celler](/cells/sv/nodejs-cpp/merging-and-unmerging-cells/)
- [Antalseinställningar](/cells/sv/nodejs-cpp/cells-number-settings/)
- [Hämta och ange stil för celler](/cells/sv/nodejs-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

