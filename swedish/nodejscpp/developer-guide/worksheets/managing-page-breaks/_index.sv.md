---
title: Hantera sidbrytningar med Node.js via C++
linktitle: Hantera sidbrytningar
type: docs
weight: 30
url: /sv/nodejs-cpp/managing-page-breaks/
description: Denna artikel ger exempel på kod och förklarar hur man lägger till, rensar eller tar bort specifika sidbrytningar i Excel arbetsblad programmässigt med Aspose.Cells for Node.js via C++.
keywords: sidbrytningar Node.js via C++, Excel sidbrytningar Node.js via C++, rensa sidbrytning Node.js via C++, ta bort specifik sidbrytning Node.js via C++
---

{{% alert color="primary" %}}

Enligt definitionen är en sidbrytning en plats i en textflöde där en sida slutar och den nästa börjar. Microsoft Excel låter användare lägga till sidbrytningar i valfri markerad cell i ett kalkylblad.

Placeringen av cellen där sidbrytningen läggs till, sidan avslutas och resten av datan efter sidbrytningen skrivs ut på nästa sida under utskrift. Med andra ord delar sidbrytningar ditt kalkylblad i flera sidor enligt dina specifikationer. Du kan också lägga till sidbrytningar i dina kalkylblad vid runtime med hjälp av Aspose.Cells. Aspose.Cells tillåter utvecklare att lägga till två typer av sidbrytningar:

- Horisontell sidbrytning
- Vertikal sidbrytning

I resten av diskussionen kommer vi att beskriva hur du kan lägga till horisontella eller vertikala sidbrytningar i dina kalkylblad med hjälp av Aspose.Cells.

{{% /alert %}}

## **Sidbrytningar**

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klass som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder som används för att hantera ett kalkylblad.

Använd [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassens [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) och [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) egenskaper för att lägga till sidbrytningar.

Egenskaperna [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) och [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) är samlingar som kan innehålla flera sidbrytningar. Varje samling innehåller flera metoder för att hantera horisontella och vertikala sidbrytningar.

### **Lägga till sidbrytningar**

För att lägga till en sidbrytning i ett arbetsblad, infoga vertikala och horisontella sidbrytningar vid den angivna cellen genom att anropa [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#add-number-number-number-)- och [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#add-number-number-number-)-metoderna. Varje **add**-metod tar namnet på cellen där brytningen ska läggas till.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Add a page break at cell Y30
workbook.getWorksheets().get(0).getHorizontalPageBreaks().add("Y30");
workbook.getWorksheets().get(0).getVerticalPageBreaks().add("Y30");

// Save the Excel file.
workbook.save(path.join(dataDir, "AddingPageBreaks_out.xls"));
```

{{% alert color="primary" %}}

I sidbrytning förhandsgranskning eller utskriftsförhandsgranskning kan du se hur dessa sidbrytningar fungerar.

{{% /alert %}}

### **Ta bort en specifik sidbrytning**

För att ta bort en specifik sidbrytning, anropa [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#removeAt-number-)- och [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#removeAt-number-)-metoderna. Varje **removeAt**-metod tar indexet för sidbrytningen som ska tas bort.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageBreaks.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Removing a specific page break
workbook.getWorksheets().get(0).getHorizontalPageBreaks().removeAt(0);
workbook.getWorksheets().get(0).getVerticalPageBreaks().removeAt(0);

// Save the Excel file.
workbook.save(path.join(dataDir, "RemoveSpecificPageBreak_out.xls"));
```

## **Viktig information att veta**

När du ställer in **fitToPages**-egenskaper (det vill säga [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) och [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--)) i sidinställningarna påverkas sidbrytningarnas inställningar, så att om du skriver ut arbetsbladet beaktas inte sidbrytningarna även om de fortfarande är inställda.
{{< app/cells/assistant language="nodejs-cpp" >}}
