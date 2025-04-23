---
title: Beräkna formulär med Node.js via C++
linktitle: Beräkna formler
description: Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att beräkna formler i Microsoft Excel med Node.js via C++. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda Aspose.Cells metoder för att beräkna formeln och få resultatet. Slutligen sparar vi den modifierade Excel filen till disk.
keywords: Aspose.Cells, Excel, formler, beräkningar, Direkt beräkning av formel, Upprepad formelberäkning, Lägg till formler med Node.js via C++
type: docs
weight: 125
url: /sv/nodejs-cpp/calculate-formulas/
---

## **Lägga till formler och beräkna resultat**

Aspose.Cells har en inbäddad formelberäkningsmotor. Den kan inte bara omberäkna formler importerade från designermallar utan också stödjer beräkning av resultaten av formler som läggs till vid körning.

Aspose.Cells stöder de flesta formler eller funktioner som ingår i Microsoft Excel (Läs [en lista över funktioner som stöds av beräkningsmotorn](/cells/sv/nodejs-cpp/supported-formula-functions/)). Dessa funktioner kan användas via API:er eller designer-spreadsheetar. Aspose.Cells stöder ett stort antal matematiska, sträng-, boolean-, datum/tid-, statistiska, databashandlings- och referensformler.

Använd [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--)-egenskapen eller [**setFormula(string, object)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setFormula-string-object-)-metoderna i [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen för att lägga till en formel till en cell. När du tillämpar en formel, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel, och använd ett komma (,) för att avgränsa funktionsparametrar.

För att beräkna resultaten av formler kan användaren anropa [**calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)-metoden i [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen som behandlar alla inbäddade formler i en Excel-fil. Eller, användaren kan anropa [**calculateFormula(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-)-metoden i [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen som behandlar alla formler i ett blad. Eller, användaren kan även anropa [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#calculate-calculationoptions-)-metoden i [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen som behandlar formeln för en Cell:

```javascript
const path = require("path");
const fs = require("fs");
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

### **Viktigt att veta för formler**

{{% alert color="primary" %}}

**Formel**-egenskapen och **setFormula(...)**-metoderna i [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen fungerar annorlunda än **calculate**-metoderna i [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) och [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) klasserna. **Formel**-egenskapen och **setFormula(...)**-metoderna lägger helt enkelt till formeln till en cell men beräknar inte resultatet vid körning. För att få formelresultatet, vänligen anropa **calculate**-metoder.

{{% /alert %}}

## **Direkt beräkning av formel**

Aspose.Cells har en inbyggd formelberäkningsmotor. Förutom att beräkna formler som importerats från en designfil kan Aspose.Cells också beräkna formelresultat direkt.

Ibland måste du beräkna formelresultat direkt utan att lägga till dem i ett kalkylblad. Värdena för cellerna som används i formeln finns redan i ett kalkylblad, och allt du behöver är att hitta resultatet av dessa värden baserat på någon Microsoft Excel-formel utan att lägga till formeln i ett kalkylblad.

Du kan använda Aspose.Cells formelberäknings-API:er för {0} till {1} för att {2} resultaten av sådana formler utan att lägga till dem i kalkylbladet:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put 20 in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.putValue(20);

// Put 30 in cell A2
const cellA2 = worksheet.getCells().get("A2");
cellA2.putValue(30);

// Calculate the Sum of A1 and A2
const results = worksheet.calculateFormula("=Sum(A1:A2)");

// Print the output
console.log("Value of A1: " + cellA1.getStringValue());
console.log("Value of A2: " + cellA2.getStringValue());
console.log("Result of Sum(A1:A2): " + results.toString());
```

Ovanstående kod ger följande utmatning:
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Hur man beräknar formler upprepade gånger**

När det finns många formler i arbetsboken och användaren behöver beräkna dem om och om igen medan endast en liten del förändras, kan det vara fördelaktigt för prestanda att aktivera formelberäkningskedjan: [**formulaSettings.getEnableCalculationChain()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load the template workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Print the time before formula calculation
console.log(new Date());

// Set the CreateCalcChain as true
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);

// Calculate the workbook formulas
workbook.calculateFormula();

// Print the time after formula calculation
console.log(new Date());

// Change the value of one cell
workbook.getWorksheets().get(0).getCells().get("A1").putValue("newvalue");

// Re-calculate those formulas which depend on cell A1
workbook.calculateFormula();
```

### **Viktigt att veta**

{{% alert color="primary" %}}

Som standard är beräkningskedjan inaktiverad. Eftersom skapandet av kedjan också kräver extra tid, kan den första gångens formelberäkning ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)) ta mer CPU-processor tid och minne jämfört med att beräkna formler utan att skapa en kedja. Om användaren inte behöver kalkylera formler om och om igen, bör standardbeteendet (att beräkna formeln direkt utan att skapa en beräkningskedja) vara det bästa sättet.

{{% /alert %}}

## **Fortsatta ämnen**
- [Lägg till celler i Microsoft Excel Formelövervakningsfönstret](/cells/sv/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Beräkning av IFNA-funktionen med Aspose.Cells](/cells/sv/nodejs-cpp/calculating-ifna-function-using-aspose-cells/)
- [Beräkning av Array Formula av Data Tables](/cells/sv/nodejs-cpp/calculation-of-array-formula-of-data-tables/)
- [Beräkning av Excel 2016 MINIFS och MAXIFS funktioner](/cells/sv/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Minska beräkningstiden för Cell.calculate-metoden](/cells/sv/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Upptäcka cirkulär referens](/cells/sv/nodejs-cpp/detecting-circular-reference/)
- [Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad](/cells/sv/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementera anpassad beräkningsmotor för att förlänga standardberäkningsmotorn för Aspose.Cells](/cells/sv/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Avbryt eller avbryt formelberäkningen i arbetsbok](/cells/sv/nodejs-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Returnera en rad med värden med hjälp av AbstractCalculationEngine](/cells/sv/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Inställning av Formelberäkningsläge för Arbetsbok](/cells/sv/nodejs-cpp/setting-formula-calculation-mode-of-workbook/)
- [Användning av FormulaText-funktionen i Aspose.Cells](/cells/sv/nodejs-cpp/using-formulatext-function-in-aspose-cells/)
