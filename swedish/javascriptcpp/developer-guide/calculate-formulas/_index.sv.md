---
title: Beräkna formulär med JavaScript via C++
linktitle: Beräkna formler
description: Den här artikeln introducerar hur man använder Aspose.Cells biblioteket för att beräkna formler i Microsoft Excel med JavaScript via C++. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda metoder som tillhandahålls av Aspose.Cells för att beräkna formeln och få resultatet. Slutligen sparar vi den modifierade Excel filen till disk.
keywords: Aspose.Cells, Excel, formler, beräkningar, direkt beräkning av formel, beräkna formulär upprepade gånger, lägg till formler JavaScript via C++
type: docs
weight: 125
url: /sv/javascript-cpp/calculate-formulas/
---

## **Lägga till formler och beräkna resultat**

Aspose.Cells har en inbäddad formelberäkningsmotor. Den kan inte bara omberäkna formler importerade från designermallar utan också stödjer beräkning av resultaten av formler som läggs till vid körning.

Aspose.Cells stöder de flesta av de formler eller funktioner som är en del av Microsoft Excel (Läs [en lista över de funktioner som stöds av beräkningsmotorn](/cells/sv/javascript-cpp/supported-formula-functions/)). Dessa funktioner kan användas via API:er eller designer spreadsheets. Aspose.Cells kräver ett stort urval av matematiska, sträng-, boolean-, datum/tid-, statistiska, databas-, uppslags- och referensformler.

Använd [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--)-egenskapen eller [**formula(string, object)**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula-string-object-)-metoderna i [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassen för att lägga till en formel till en cell. När du tillämpar en formel, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel, och använd ett komma (,) för att avgränsa funktionsparametrar.

För att beräkna resultaten av formler kan användaren anropa [**calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)-metoden i [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen som behandlar alla inbäddade formler i en Excel-fil. Eller, användaren kan anropa [**calculateFormula(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-)-metoden i [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen som behandlar alla formler i ett blad. Eller, användaren kan även anropa [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/javascript-cpp/cell/#calculate-calculationoptions-)-metoden i [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassen som behandlar formeln för en Cell:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 1;

            // Adding a value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 2;

            // Adding a value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 3;

            // Adding a SUM formula to "A4" cell
            const cellA4 = worksheet.cells.get("A4");
            cellA4.formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value in A4: ${value}. Click the download link to get the file.</p>`;
        });
    </script>
</html>
```

### **Viktigt att veta för formler**

{{% alert color="primary" %}}

Egenskapen **Formula** och metoderna **formula(...)** i [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassen fungerar annorlunda än **calculate**-metoderna i klasserna [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) och [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). Egenskapen **Formula** och metoderna **formula(...)** lägger helt enkelt till formeln i en cell men beräknar inte resultatet vid körning. För att få resultatet av formlarna, vänligen kalla på **calculate**-metoder.

{{% /alert %}}

## **Direkt beräkning av formel**

Aspose.Cells har en inbyggd formelberäkningsmotor. Förutom att beräkna formler som importerats från en designfil kan Aspose.Cells också beräkna formelresultat direkt.

Ibland måste du beräkna formelresultat direkt utan att lägga till dem i ett kalkylblad. Värdena för cellerna som används i formeln finns redan i ett kalkylblad, och allt du behöver är att hitta resultatet av dessa värden baserat på någon Microsoft Excel-formel utan att lägga till formeln i ett kalkylblad.

Du kan använda Aspose.Cells formelberäknings-API:er för {0} till {1} för att {2} resultaten av sådana formler utan att lägga till dem i kalkylbladet:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Calculate Sum</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put 20 in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 20;

            // Put 30 in cell A2
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 30;

            // Calculate the Sum of A1 and A2
            const results = worksheet.calculateFormula("=Sum(A1:A2)");

            // Prepare output text
            const outputHtml = [
                `<p>Value of A1: ${cellA1.stringValue}</p>`,
                `<p>Value of A2: ${cellA2.stringValue}</p>`,
                `<p>Result of Sum(A1:A2): ${results.toString()}</p>`
            ].join("");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<div style="color: green;">Operation completed successfully!</div>${outputHtml}`;
        });
    </script>
    </body>
</html>
```

Ovanstående kod ger följande utmatning:
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Hur man beräknar formler upprepade gånger**

När det finns många formler i arbetsboken och användaren behöver beräkna dem om och om igen medan endast en liten del förändras, kan det vara fördelaktigt för prestanda att aktivera formelberäkningskedjan: [**formulaSettings.enableCalculationChain**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Calculate Formulas</title>
    </head>
    <body>
        <h1>Calculate Formulas Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Print the time before formula calculation
            console.log(new Date());

            // Set the CreateCalcChain as true
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate the workbook formulas
            workbook.calculateFormula();

            // Print the time after formula calculation
            console.log(new Date());

            // Change the value of one cell (A1 in first worksheet)
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            cell.value = "newvalue";

            // Re-calculate those formulas which depend on cell A1
            workbook.calculateFormula();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas calculated and cell updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Viktigt att veta**

{{% alert color="primary" %}}

Som standard är beräkningskedjan inaktiverad. Eftersom skapandet av kedjan också kräver extra tid, kan den första gångens formelberäkning ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)) ta mer CPU-processor tid och minne jämfört med att beräkna formler utan att skapa en kedja. Om användaren inte behöver kalkylera formler om och om igen, bör standardbeteendet (att beräkna formeln direkt utan att skapa en beräkningskedja) vara det bästa sättet.

{{% /alert %}}

## **Fortsatta ämnen**
- [Lägg till celler i Microsoft Excel Formelövervakningsfönstret](/cells/sv/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Beräkning av IFNA-funktionen med Aspose.Cells](/cells/sv/javascript-cpp/calculating-ifna-function-using-aspose-cells/)
- [Beräkning av Array Formula av Data Tables](/cells/sv/javascript-cpp/calculation-of-array-formula-of-data-tables/)
- [Beräkning av Excel 2016 MINIFS och MAXIFS funktioner](/cells/sv/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Minska beräkningstiden för Cell.calculate-metoden](/cells/sv/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Upptäcka cirkulär referens](/cells/sv/javascript-cpp/detecting-circular-reference/)
- [Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad](/cells/sv/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementera anpassad beräkningsmotor för att förlänga standardberäkningsmotorn för Aspose.Cells](/cells/sv/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Avbryt eller avbryt formelberäkningen i arbetsbok](/cells/sv/javascript-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Returnera en rad med värden med hjälp av AbstractCalculationEngine](/cells/sv/javascript-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Inställning av Formelberäkningsläge för Arbetsbok](/cells/sv/javascript-cpp/setting-formula-calculation-mode-of-workbook/)
- [Användning av FormulaText-funktionen i Aspose.Cells](/cells/sv/javascript-cpp/using-formulatext-function-in-aspose-cells/)
