---
title: Hantera formler i Excel filer med Node.js via C++
linktitle: Formler
type: docs
weight: 122
url: /sv/nodejs-cpp/using-formulas-or-functions-to-process-data/
description: Lär dig hur du hanterar formler i Excel filer genom Aspose.Cells for Node.js via C++. Aspose.Cells kan enkelt hämta, ställa in och beräkna formler i Excel filer.
keywords: Hur man beräknar formler i Node.js via C++, Formler och funktioner med Node.js via C++, Node.js via C++ Hantera inbyggda funktioner, Hur man använder tilläggsfunktioner med Node.js via C++, Hur man använder array formler via Node.js via C++, Hur man använder R1C1 formel i Node.js via C++.
---

## **Introduktion**

En av Microsoft Excels kraftfulla funktioner är dess möjlighet att bearbeta data med hjälp av formler och funktioner. Microsoft Excel ger ett set av inbyggda funktioner och formler som hjälper användare att snabbt utföra komplexa beräkningar. Aspose.Cells tillhandahåller också ett stort antal inbyggda funktioner och formler som hjälper utvecklare att enkelt beräkna värden. Aspose.Cells stöder också tilläggsfunktioner. Dessutom stöder Aspose.Cells array- och R1C1-formler.

## **Hur man Använder formler och funktioner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller en [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samling. Varje objekt i Cells-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen.

Det är möjligt att använda formler på celler med egenskaper och metoder som erbjuds av [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen, som diskuteras mer detaljerat nedan.

- Använda inbyggda funktioner.
- Använda tilläggsfunktioner.
- Arbeta med matrisformler.
- Skapa en R1C1-formel.

## **Hur man Använder Inbyggda Funktioner**

Inbyggda funktioner eller formler tillhandahålls som färdiga funktioner för att minska utvecklares insats och tid. Se [en lista över inbyggda funktioner](/cells/sv/nodejs-cpp/supported-formula-functions/) som stöds av Aspose.Cells. Funktionerna är listade i alfabetisk ordning. Fler funktioner kommer att stödjas i framtiden.

Aspose.Cells stödjer de flesta av de funktioner eller formler som erbjuds av Microsoft Excel. Utvecklare kan använda dessa formler via API:et eller [designer spreadsheet](/cells/sv/nodejs-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells stöder ett stort set av matematiska, sträng-, Booleska, datum/tid-, statistiska, databas-, uppslags- och referensformler.

Använd [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassens [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--)-egenskap för att lägga till en formula i en cell. **Komplexa formler**, till exempel

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, stöds också i Aspose.Cells. När du tillämpar en formel på en cell, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel och använd ett kommatecken (,) för att avgränsa funktionsparametrar.

I exemplet nedan tillämpas en komplex formula på den första cellen i kalkylbladets [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samling. Formeln använder en inbyggd **OM**-funktion som tillhandahålls av Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A4").setFormula("=SUM(A1:A3)");

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A4").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Hur man Använder Tilläggsfunktioner**

Vi kan ha några användardefinierade formler som vi vill inkludera som en excel-tillägg. När du ställer in cell.Formula-funktionen fungerar inbyggda funktioner bra, men det finns ett behov av att ställa in de anpassade funktionerna eller formlerna med tilläggsfunktionerna.

Aspose.Cells tillhandahåller funktioner för att registrera tilläggsfunktioner med hjälp av [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). Efteråt, när vi ställer in cell.Formula = anyFunctionFromAddIn, innehåller den resulterande Excel-filen det beräknade värdet från tilläggsfunktionen.

Följande XLAM-fil ska laddas ned för att registrera tilläggsfunktionen enligt nedanstående provkod. På samma sätt kan den resulterande filen "test_udf.xlsx" laddas ned för att kontrollera resultatet.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Register macro enabled add-in along with the function name
const id = workbook.getWorksheets().registerAddInFunction(path.join(dataDir, "TESTUDF.xlam"), "TEST_UDF", false);

// Register more functions in the file (if any)
workbook.getWorksheets().registerAddInFunction(id, "TEST_UDF1"); // in this way you can add more functions that are in the same file

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first cell
const cell = worksheet.getCells().get("A1");

// Set formula name present in the add-in
cell.setFormula("=TEST_UDF()");

// Save workbook to output XLSX format.
workbook.save(path.join(outputDir, "test_udf.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Hur man Använder Matrisformel**

Matrisformler är formler som tar matriser, istället för enskilda nummer, som argument till de funktioner som utgör formeln. När en matrisformel visas, omges den av måsvingar ({ }).

Vissa Microsoft Excel-funktioner returnerar matriser med värden. För att beräkna flera resultat med en arrayformel, ange matrisen i en cellintervall med samma antal rader och kolumner som matrisargumenten.

Det är möjligt att tillämpa en matrisformel på en cell genom att anropa [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassens [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-)-metod. [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-)-metoden tar följande parametrar:

- **Arrayformel**, arrayformeln.
- **Antal rader**, antalet rader för att fylla resultatet av arrayformeln.
- **Antal kolumner**, antalet kolumner för att fylla resultatet av matrisformeln.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a value to B1
worksheet.getCells().get("B1").putValue(4);

// Adding a value to "B2" cell
worksheet.getCells().get("B2").putValue(5);

// Adding a value to "B3" cell
worksheet.getCells().get("B3").putValue(6);

// Adding a value to C1
worksheet.getCells().get("C1").putValue(7);

// Adding a value to "C2" cell
worksheet.getCells().get("C2").putValue(8);

// Adding a value to "C3" cell
worksheet.getCells().get("C3").putValue(9);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A6").setArrayFormula("=LINEST(A1:A3,B1:C3,TRUE,TRUE)", 5, 3);

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A6").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Hur man Använder R1C1-formel**

Lägg till en formel med referensstil **R1C1** i en cell med klassens [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) [**getR1C1Formula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getR1C1Formula--)-egenskap.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Setting an R1C1 formula on the "A11" cell, 
// Row and Column indices are relative to destination index
worksheet.getCells().get("A11").setR1C1Formula("=SUM(R[-10]C[0]:R[-7]C[0])");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Fortsatta ämnen**
- [Föregångare och efterföljande](/cells/sv/nodejs-cpp/precedents-and-dependents/)
- [Ange externa länkar i formler](/cells/sv/nodejs-cpp/set-external-links-in-formulas/)
- [Sprid formel i tabell eller listobjekt automatiskt när du matar in data i nya rader](/cells/sv/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Ange formel för namngivet område](/cells/sv/nodejs-cpp/setting-formula-for-named-range/)
- [Inställning av formler - Meddelande för användare som inte talar engelska](/cells/sv/nodejs-cpp/setting-formulas-notice-for-non-english-users/)
- [Inställning av delad formel](/cells/sv/nodejs-cpp/setting-shared-formula/)
- [Ange maximala rader för delad formel](/cells/sv/nodejs-cpp/specify-maximum-rows-of-shared-formula/)
- [Stödda Excel-funktioner](/cells/sv/nodejs-cpp/supported-formula-functions/)

