---
title: Merging och ofusing av celler med Node.js via C++
linktitle: Sammanfoga och dela upp celler
description: Aspose.Cells är ett Node.js bibliotek för att arbeta med kalkylbladsfiler, som stöder sammanslagning och ofusing av celler. Den här artikeln introducerar hur man slår ihop och tar bort celler med Aspose.Cells biblioteket, med möjligheter att anpassa den sammanslagna cellens stil.
keywords: Aspose.Cells, Node.js bibliotek, kalkylblad, slå samman celler, ta bort celler, stilinställningar, anpassade stilar
type: docs
weight: 190
url: /sv/nodejs-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells stöder den här funktionen och kan också sammanslå celler i ett kalkylblad. Du kan också dela upp eller splittra de sammanslagna cellerna. En sammanslagen cells cellreferens är referensen för den översta vänstra cellen i det ursprungliga markerade området.

{{% /alert %}} 
## **Introduktion**
Du vill inte alltid ha samma antal celler i varje rad eller kolumn. Till exempel kan du vilja lägga en titel i en cell som spänner över flera kolumner. Eller om du skapar en faktura kan du vilja ha färre kolumner för den totala summan. För att göra en cell från två eller flera celler, sammanslag dem. Microsoft Excel låter användare välja filer och sammanfoga dem för att strukturera kalkylbladet på önskat sätt.

{{% alert color="primary" %}} 

 Observera att när celler sammanfogas behålls endast data i det övre vänstra cellen. Om det finns data i de andra cellerna i området tas denna data bort. Formatering baseras också på referenscellen så att när du sammanfogar celler tillämpas formateringsinställningarna för den övre vänstra cellen i området på den sammanslagna cellen. När cellen delas behåller de nya cellerna sina ursprungliga formateringsinställningar.

{{% /alert %}} 
## **Sammanslagning av celler i ett kalkylblad**
### **Sammanslagning av celler i Microsoft Excel**
Följande steg beskriver hur man sammanslår celler i kalkylbladet med hjälp av MS Excel.

1. Kopiera den data du vill ha till den övre vänstra cellen inom området.
1. Välj cellerna du vill sammanfoga.
1. För att sammanfoga celler i en rad eller kolumn och centrera cellinnehållet klickar du på ikonen **Sammanfoga och centrerat** på verktygsfältet **Formatering**.

### **Sammanslagning av celler med Aspose.Cells**
Aspose.Cells.Cells-klassen har några användbara metoder för uppgiften. Till exempel sammanfogar metoden `merge()` cellerna till en enda cell inom ett specificerat område.

Följande exempel visar hur man slår samman celler (C6:E7) i en arbetsbok.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
const wbk = new AsposeCells.Workbook();

// Create a Worksheet and get the first sheet.
const worksheet = wbk.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Merge some Cells (C6:E7) into a single C6 Cell.
cells.merge(5, 2, 2, 3);

// Input data into C6 Cell.
cells.get(5, 2).putValue("This is my value");

// Create a Style object to fetch the Style of C6 Cell.
const style = cells.get(5, 2).getStyle();

// Create a Font object
const font = style.getFont();

// Set the name.
font.setName("Times New Roman");

// Set the font size.
font.setSize(18);

// Set the font color
font.setColor(AsposeCells.Color.Blue);

// Bold the text
font.setIsBold(true);

// Make it italic
font.setIsItalic(true);

// Set the background color of C6 Cell to Red
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Apply the Style to C6 Cell.
cells.get(5, 2).setStyle(style);

// Save the Workbook.
wbk.save(path.join(dataDir, "mergingcells.out.xls"));
```

## **Avfussning (delning) av sammanslagna celler**
### **Använda Microsoft Excel**
Följande steg beskriver hur man delar sammanslagna celler med hjälp av Microsoft Excel.

1. Välj den sammanslagna cellen.
   När cellerna har kombinerats väljs **Slå samman och centrera** på **Formateringsverktygsfältet**.
1. Klicka på **Slå samman och centrera** på **Formateringsverktygsfältet**.

### **Använda Aspose.Cells**
Aspose.Cells.Cells-klassen har en metod som heter `unmerge()` som delar upp cellerna till deras ursprungliga tillstånd. Metoden avfogar cellerna med hjälp av cellens referens i det sammanslagna cellområdet.

Följande exempel visar hur man delar de sammanslagna cellerna (C6). Exemplet använder filen som skapades i det föregående exemplet och delar de sammanslagna cellerna.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
// Open the excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "mergingcells.xls"));

// Create a Worksheet and get the first sheet.
const worksheet = workbook.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Unmerge the cells.
cells.unMerge(5, 2, 2, 3);

// Save the file.
workbook.save(path.join(dataDir, "unmergingcells.out.xls"));
```

## **Fortsatta ämnen**
- [Identifiera sammanslagna celler i ett kalkylblad](/cells/sv/nodejs-cpp/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="nodejs-cpp" >}}
