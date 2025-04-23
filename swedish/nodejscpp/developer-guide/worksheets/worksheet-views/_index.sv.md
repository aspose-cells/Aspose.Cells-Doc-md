---
title: Arksvy översikter med Node.js via C++
linktitle: Arbetsboks vy
type: docs
weight: 40
url: /sv/nodejs-cpp/worksheet-views/
description: Denna artikel beskriver hur man använder Node.js och Node.js API för att interagera med sidbrytning av ett Excel arbetsbok och arksnitt. Arbeta med delade paneler, frysta paneler och zoomfaktor också.
---

## **Sidbrytning Förhandsgranskning**

Alla arbetsblad kan visas i två lägen:

- Normal vy.
- Sidbrytningsvy.

Normalvy är ett standardvy för ett arksnitt. Sidbrytning förhandsvisning är en redigeringsvy som visar ett arksnitt som det kommer att skrivas ut. Sidbrytning förhandsvisning visar vilka data som kommer att hamna på varje sida så att du kan justera utskriftsområdet och sidbrytningar. Med Aspose.Cells for Node.js via C++ kan utvecklare aktivera normalvy eller sidbrytning förhandsvisning.

### **Styra vynlägen**

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som möjliggör åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att aktivera normal vy eller sidbrytningsvy används [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassens [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--)-egenskap. [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) är en boolesk egenskap, vilket innebär att den bara kan lagra ett värde **true** eller **false**.

#### **Aktivera normal vy**

Ställ in ett arbetsblad till normal vy genom att ange [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassens [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--)-egenskap till **false**.

#### **Aktivera sidbrytningsvy**

Ställ in valfritt arbetsblad till sidbrytningsvy genom att ange [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassens [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--)-egenskap till **true**. Detta gör att arbetsbladet byts från normal vy till sidbrytningsvy.

Ett komplett exempel visas nedan som demonstrerar hur man använder [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--)-egenskapen för att aktivera sidbrytningsvy för det första arbetsbladet i en Excel-fil.

Filen book1.xls öppnas genom att skapa en instans av klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Vyn byts till sidbrytningsvy för det första arbetsbladet genom att ange att [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--)-egenskapen är **true**. Den modifierade filen sparas som output.xls.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");


// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Displaying the worksheet in page break preview
worksheet.setIsPageBreakPreview(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Zoomfaktor**

### **Använda Microsoft Excel**

Microsoft Excel har en funktion som låter användare sätta en arbetsblads zoom- eller skalfaktor. Denna funktion hjälper användare att se arbetsbladsinnehållet i mindre eller större visningar. Användare kan sätta zoom-faktorn till vilket värde som helst.

### **Aspose.Cells och Zoom Faktor**

Aspose.Cells tillåter utvecklare att sätta arbetsblads zoom-faktor.
Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klassen innehåller en [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) samling som tillåter åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att sätta en arbetsblads zoom-faktor använder man egenskapen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) i [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) klassen. Zoom-faktorn sätts genom att tilldela ett numeriskt (heltals) värde till egenskapen [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--).

Ett komplett exempel ges nedan som demonstrerar hur man använder egenskapen [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) för att ställa in zoomfaktorn för det första arksnittet i Excel-filen.

book1.xls-filen öppnas genom att skapa en instans av [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen. Zoom-faktorn på det första arbetsbladet sätts till 75 och den modifierade filen sparas som output.xls.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the zoom factor of the worksheet to 75
worksheet.setZoom(75);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Frys Fönsterpaneler**

### **Använda Microsoft Excel**

Frysa rutor är en funktion som tillhandahålls av Microsoft Excel. Att frysa rutor gör att man kan välja data som ska förbli synlig när man rullar i ett arbetsblad.

### **Aspose.Cells och Frysa rutor**

Aspose.Cells tillåter utvecklare att applicera frysfönster på arbetsblad vid körning.

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klassen innehåller en [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) samling som tillåter åtkomst till varje arbetsblad i en Excel-fil.

Ett arksnitt representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) klassen. Klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) erbjuder ett brett utbud av egenskaper och metoder för att hantera arksnitt. För att konfigurera frysta paneler, anropa Worksheet-klassens [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) metod. [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) metoden tar följande parametrar:

- **Rad**, radindexet för cellen som frysen ska starta från.
- **Kolumn**, kolumnindexet för cellen som frysen ska starta från.
- **Frusna rader**, antalet synliga rader i toppfönstret.
- **Frysta kolumner**, antalet synliga kolumner i vänsterpanelen.

book1.xls-filen öppnas genom att man kallar på konstruktorn till [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen medan man instansierar den och några rader och kolumner frysas i det första arbetsbladet. Den modifierade filen sparas som output.xls.

Ett komplett exempel nedan visar hur man använder sig av [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) metoden för att frysa rader och kolumner (som börjar från C4, representerat av den fjärde raden och tredje kolumnen, där raderna och kolumnerna börjar från index 0) på det första arbetsbladet i Excel-filen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Applying freeze panes settings
worksheet.freezePanes(3, 2, 3, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// The file stream will be automatically closed after saving
```

## **Dela rutor**

Om du behöver dela skärmen för att få två olika vyer i samma arbetsblad, dela rutor. Microsoft Excel erbjuder en mycket praktisk funktion som gör att du kan se mer än en kopia av ditt arbetsblad och för dig att kunna bläddra igenom varje ruta av ditt arbetsblad oberoende av varandra: dela rutor.

Fönstren fungerar samtidigt. Om du gör en förändring i ett, visas förändringen samtidigt i den andra. Aspose.Cells tillhandahåller split panes-funktionen för användarna.

### **Sätta på och Ta bort Delade paneler**

#### **Dela Fönster**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att implementera split vyer använder man sig av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) metoden. För att ta bort delade rutor, använder man sig av [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--) metoden.

I exemplet använder vi en enkel mallfil som laddas, sedan används inställningar för att dela rutor på en cell i det första arbetsbladet. Den uppdaterade filen sparas.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const book = new AsposeCells.Workbook(filePath);

// Set the active cell
book.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
book.getWorksheets().get(0).split();

// Save the excel file
book.save(path.join(dataDir, "output.xls"));
```

Efter att ovanstående kod har körts, kommer den genererade filen ha en delad vy.

#### **Ta bort rutor**

Ta bort delade rutor med metoden [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const workbook = new AsposeCells.Workbook(filePath);

// Set the active cell
workbook.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
workbook.getWorksheets().get(0).removeSplit();

// Save the excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Fortsatta ämnen**
- [Dölja visning av nollvärden i kalkylbladet](/cells/sv/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Ange färg på kalkylbladsflik](/cells/sv/nodejs-cpp/set-worksheet-tab-color/)
- [Visa och dölj rutnät och radkolumnhuvuden](/cells/sv/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Visa och dölj rader kolumner och skrollbar](/cells/sv/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Visa och dölj arbetsblad och flikar](/cells/sv/nodejs-cpp/show-and-hide-worksheets-and-tabs/)
- [Visa formler istället för värden i ett arbetsblad](/cells/sv/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Använd felkontrollalternativ](/cells/sv/nodejs-cpp/use-error-checking-options/)

