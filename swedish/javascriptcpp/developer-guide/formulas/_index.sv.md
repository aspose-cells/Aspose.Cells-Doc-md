---
title: Hantera formler i Excel filer med JavaScript via C++
linktitle: Formler
type: docs
weight: 122
url: /sv/javascript-cpp/using-formulas-or-functions-to-process-data/
description: Lär dig hur du hanterar formler i Excel filer genom Aspose.Cells for JavaScript via C++. Aspose.Cells kan enkelt hämta, ställa in och beräkna formler i Excel filer.
keywords: Hur man beräknar formler i JavaScript via C++, formler och funktioner med JavaScript via C++, JavaScript via C++ Hantera inbyggda funktioner, Hur man använder tilläggsfunktioner med JavaScript via C++, Hur man använder matrixformler via JavaScript via C++, Hur man använder R1C1 formel i JavaScript via C++.
---

## **Introduktion**

En av Microsoft Excels kraftfulla funktioner är dess möjlighet att bearbeta data med hjälp av formler och funktioner. Microsoft Excel ger ett set av inbyggda funktioner och formler som hjälper användare att snabbt utföra komplexa beräkningar. Aspose.Cells tillhandahåller också ett stort antal inbyggda funktioner och formler som hjälper utvecklare att enkelt beräkna värden. Aspose.Cells stöder också tilläggsfunktioner. Dessutom stöder Aspose.Cells array- och R1C1-formler.

## **Hur man Använder formler och funktioner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen tillhandahåller en [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samling. Varje objekt i Cells-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassen.

Det är möjligt att använda formler på celler med egenskaper och metoder som erbjuds av [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassen, som diskuteras mer detaljerat nedan.

- Använda inbyggda funktioner.
- Använda tilläggsfunktioner.
- Arbeta med matrisformler.
- Skapa en R1C1-formel.

## **Hur man Använder Inbyggda Funktioner**

Inbyggda funktioner eller formler tillhandahålls som färdiga funktioner för att minska utvecklares ansträngning och tid. Se [en lista över inbyggda funktioner](/cells/sv/javascript-cpp/supported-formula-functions/) som stöds av Aspose.Cells. Funktionerna är listade i alfabetisk ordning. Fler funktioner kommer att stödjas i framtiden.

Aspose.Cells stöder de flesta av de formler eller funktioner som erbjuds av Microsoft Excel. Utvecklare kan använda dessa formler via API:et eller [designer spreadsheet](/cells/sv/javascript-cpp/what-is-a-designer-spreadsheet/). Aspose.Cells stöder ett stort antal matematiska, sträng-, booleska, datum/tid-, statistiska, databas-, uppslags- och referensformler.

Använd [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassens [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--)-egenskap för att lägga till en formula i en cell. **Komplexa formler**, till exempel

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, stöds också i Aspose.Cells. När du tillämpar en formel på en cell, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel och använd ett kommatecken (,) för att avgränsa funktionsparametrar.

I exemplet nedan tillämpas en komplex formula på den första cellen i kalkylbladets [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samling. Formeln använder en inbyggd **OM**-funktion som tillhandahålls av Aspose.Cells.

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            worksheet.cells.get("A1").putValue(1);

            // Adding a value to "A2" cell
            worksheet.cells.get("A2").putValue(2);

            // Adding a value to "A3" cell
            worksheet.cells.get("A3").putValue(3);

            // Adding a SUM formula to "A4" cell
            worksheet.cells.get("A4").formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated A4 value: ${value}. Click the download link to get the generated file.</p>`;
        });
    </script>
</html>
```

## **Hur man Använder Tilläggsfunktioner**

Vi kan ha några användardefinierade formler som vi vill inkludera som ett excel-tillägg. När du ställer in cell.formula fungerar inbyggda funktioner utmärkt, men det finns ett behov av att ställa in anpassade funktioner eller formler med hjälp av tilläggsfunktioner.

Aspose.Cells erbjuder funktioner för att registrera tilläggsfunktioner med [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). Därefter, när vi ställer in cell.formula = någonFunktionFrånTillägget, innehåller den utgående Excel-filen det beräknade värdet från tilläggsfunktionen.

Följande XLAM-fil ska laddas ned för att registrera tilläggsfunktionen enligt nedanstående provkod. På samma sätt kan den resulterande filen "test_udf.xlsx" laddas ned för att kontrollera resultatet.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Register Add-In Function Example</title>
    </head>
    <body>
        <h1>Register Add-In Function Example</h1>
        <p>Select the add-in file (.xlam/.xla) that contains the UDFs to register:</p>
        <input type="file" id="addInInput" accept=".xlam,.xla" />
        <button id="runExample">Register Add-In & Create Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

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
            const fileInput = document.getElementById('addInInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an add-in file (.xlam/.xla).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const addinData = new Uint8Array(arrayBuffer);

            // Create empty workbook
            const workbook = new Workbook();

            // Register macro enabled add-in along with the function name
            const id = workbook.worksheets.registerAddInFunction(addinData, "TEST_UDF", false);

            // Register more functions in the file (if any)
            workbook.worksheets.registerAddInFunction(id, "TEST_UDF1");

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first cell
            const cell = worksheet.cells.get("A1");

            // Set formula name present in the add-in
            cell.formula = "=TEST_UDF()";

            // Save workbook to output XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_udf.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Add-in registered and formula set successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **Hur man Använder Matrisformel**

Matrisformler är formler som tar matriser, istället för enskilda nummer, som argument till de funktioner som utgör formeln. När en matrisformel visas, omges den av måsvingar ({ }).

Vissa Microsoft Excel-funktioner returnerar matriser med värden. För att beräkna flera resultat med en arrayformel, ange matrisen i en cellintervall med samma antal rader och kolumner som matrisargumenten.

Det är möjligt att tillämpa en matrisformel på en cell genom att anropa [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-klassens [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-)-metod. [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-)-metoden tar följande parametrar:

- **Arrayformel**, arrayformeln.
- **Antal rader**, antalet rader för att fylla resultatet av arrayformeln.
- **Antal kolumner**, antalet kolumner för att fylla resultatet av matrisformeln.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LINEST Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding values to cells
            worksheet.cells.get("A1").value = 1;
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 3;

            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 5;
            worksheet.cells.get("B3").value = 6;

            worksheet.cells.get("C1").value = 7;
            worksheet.cells.get("C2").value = 8;
            worksheet.cells.get("C3").value = 9;

            // Adding a SUM/LINEST array formula to "A6" cell
            worksheet.cells.get("A6").arrayFormula = { formula: "=LINEST(A1:A3,B1:C3,TRUE,TRUE)", rows: 5, cols: 3 };

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A6").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value: ${value}</p>`;
        });
    </script>
</html>
```

## **Hur man Använder R1C1-formel**

Lägg till en formel med referensstil **R1C1** i en cell med klassens [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) [**r1C1Formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#r1C1Formula--)-egenskap.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set R1C1 Formula Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting an R1C1 formula on the "A11" cell,
            // Row and Column indices are relative to destination index
            const cell = worksheet.cells.get("A11");
            cell.r1C1Formula = "=SUM(R[-10]C[0]:R[-7]C[0])";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">R1C1 formula set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Föregångare och efterföljande](/cells/sv/javascript-cpp/precedents-and-dependents/)
- [Ange externa länkar i formler](/cells/sv/javascript-cpp/set-external-links-in-formulas/)
- [Sprid formel i tabell eller listobjekt automatiskt när du matar in data i nya rader](/cells/sv/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Ange formel för namngivet område](/cells/sv/javascript-cpp/setting-formula-for-named-range/)
- [Inställning av formler - Meddelande för användare som inte talar engelska](/cells/sv/javascript-cpp/setting-formulas-notice-for-non-english-users/)
- [Inställning av delad formel](/cells/sv/javascript-cpp/setting-shared-formula/)
- [Ange maximala rader för delad formel](/cells/sv/javascript-cpp/specify-maximum-rows-of-shared-formula/)
- [Stödda Excel-funktioner](/cells/sv/javascript-cpp/supported-formula-functions/)
