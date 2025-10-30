---
title: Föregångare och beroenden med JavaScript via C++
linktitle: Precedenser och beroende
type: docs
weight: 230
url: /sv/javascript-cpp/precedents-and-dependents/
description: Lär dig att spåra föregångare och beroende celler i kalkylblad med Aspose.Cells for JavaScript via C++. Förstå hur man identifierar länkar celler i komplexa finansiella kalkylblad.
---

{{% alert color="primary" %}} 

Komplexa finansiella arbetsblad, särskilt de som utvecklats i samarbete, kan dölja de mest pinsamma felen. Att kontrollera formler för noggrannhet och hitta felets källa kan vara svårt när formeln använder precedens- och beroendeceller.

{{% /alert %}} 
## **Introduktion**
- **Precedensceller** är celler som hänvisas till av en formel i en annan cell. Till exempel, om cell D10 innehåller formeln =B5, är cell B5 en precedens till cell D10.
- **Beroende celler** innehåller formler som hänvisar till andra celler. Till exempel, om cell D10 innehåller formeln =B5, är D10 beroende av cell B5.

För att göra kalkylarket lättläst vill du kanske tydligt visa vilka celler på ett kalkylblad som används i en formel. På liknande sätt kan du vilja extrahera de beroende cellerna för andra celler.

Aspose.Cells låter dig spåra celler och ta reda på vilka som är länkade.
## **Spåra precedens- och beroendeceller: Microsoft Excel**
Formler kan ändras baserat på ändringar som görs av en klient. Till exempel, om cell C1 är beroende av C3 och C4 som innehåller en formel, och C1 ändras (så formeln åsidosätts), måste C3 och C4, eller andra celler, ändras för att balansera kalkylarket baserat på affärsregler.

På liknande sätt, anta att C1 innehåller formeln "=(B1*22)/(M2*N32)". Jag vill hitta de celler som C1 är beroende av, dvs. precedenscellerna B1, M2 och N32.

Du kan behöva spåra beroendet för en specifik cell till andra celler. Om affärsregler är inbäddade i formler vill vi ta reda på beroendet och utföra några regler baserat på det. På liknande sätt, om värdet på en specifik cell ändras, vilka celler i arbetsbladet påverkas av den ändringen?

Microsoft Excel tillåter användare att spåra precedenser och beroenden.

1. På **Visa verktygsfältet**, välj **Formelgranskning**. Dialogrutan för formelgranskning visas.
1. Spåra Precedenser:
   1. Välj den cell som innehåller formeln för vilken du vill hitta precedensceller.
   1. För att visa en spårpil till varje cell som direkt tillhandahåller data till den aktiva cellen, klicka på **Spåra Precedenser** på verktygsfältet för formelgranskning.
1. Spåra formler som refererar till en specifik cell (beroenden)
   1. Välj den cell för vilken du vill identifiera de beroende cellerna.
   1. För att visa en spårarepil till varje cell som är beroende av den aktiva cellen, klicka på **Trace Dependents** på Formulaspårningsverktygsfältet.
## **Spårar föregående och beroende celler: Aspose.Cells**
### **Spårar föregående**
Aspose.Cells gör det enkelt att få föregående celler. Den kan inte bara hämta celler som ger data till enkla formelföregångare utan också hitta celler som ger data till komplexa formelföregångare med namngivna områden.

I exemplet nedan används en template excelfil, Book1.xls. Kalkylarket har data och formler på den första arbetsbladet.

Aspose.Cells tillhandahåller [Cell](https://reference.aspose.com/cells/javascript-cpp/cell) klassens metod [Cell.precedents()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedents--) som används för att spåra en cells föregångare. Den returnerar en samling av refererade områden. Som du kan se ovan, i Book1.xls, innehåller cell B7 en formel "=SUM(A1:A3)". Så cellerna A1:A3 är förekommande celler för cell B7. Följande exempel visar funktionaliteten för att spåra föregångare med hjälp av mallfilen Book1.xls.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Precedents Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet's cells
            const cells = workbook.worksheets.get(0).cells;

            // Get cell B4
            const cell = cells.get("B4");

            if (cell) {
                // Get precedents (converted from getPrecedents)
                const ret = cell.precedents;

                if (!ret.isNull() && ret.count > 0) {
                    const area = ret.get(0);

                    const sheetName = area.sheetName;
                    const startAddress = AsposeCells.CellsHelper.cellIndexToName(area.startRow, area.startColumn);
                    const endAddress = AsposeCells.CellsHelper.cellIndexToName(area.endRow, area.endColumn);

                    console.log(sheetName);
                    console.log(startAddress);
                    console.log(endAddress);

                    document.getElementById('result').innerHTML = `<pre>Sheet: ${sheetName}\nStart: ${startAddress}\nEnd: ${endAddress}</pre>`;
                } else {
                    document.getElementById('result').innerHTML = '<p style="color: red;">No precedents found for the cell.</p>';
                }
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Cell B4 is null.</p>';
            }
        });
    </script>
</html>
```
### **Spårar beroende**
Aspose.Cells låter dig få beroende celler i kalkylblad. Aspose.Cells kan inte bara hämta celler som tillhandahåller data för en enkel formel utan också hitta celler som tillhandahåller data till komplexa formelberoenden med namngivna områden.

Aspose.Cells tillhandahåller [Cell](https://reference.aspose.com/cells/javascript-cpp/cell) klassens metod [Cell.dependents(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependents-boolean-) som används för att spåra en cells beroenden. Till exempel, i Book1.xlsx finns formler: "=A1+20" och "=A1+30" i cellerna B2 och C2 respektive. Följande exempel visar hur man spårar beroenden för cell A1 med mallfilen Book1.xlsx.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Get Cell Dependents Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("B2");
            // Ensure dependents is accessed as a property (converted from getDependents)
            const dependents = cell.dependents;

            if (Array.isArray(dependents)) {
                let out = '<p>Dependents found:</p><ul>';
                for (const c of dependents) {
                    console.log(c.name);
                    out += `<li>${c.name}</li>`;
                }
                out += '</ul>';
                resultDiv.innerHTML = out;
            } else {
                console.error("Dependents is not an array");
                resultDiv.innerHTML = '<p style="color: red;">Dependents is not an array</p>';
            }
        });
    </script>
</html>
```
### **Spårning av föregående och beroende celler enligt beräkningskedjan**
Ovan nämnda API:er för att spåra föregångare och beroenden är baserade på själva formeluttrycket. Dessa ger en bekväm metod för användare att spåra mellanliggande beroenden för några formler. Om det finns ett stort antal formler i arbetsboken och användaren behöver spåra föregångare och beroenden för varje cell, kan detta leda till dålig prestanda. I sådana fall bör användaren överväga att använda [Cell.precedentsInCalculation()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedentsInCalculation--) och [Cell.dependentsInCalculation(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependentsInCalculation-boolean-) metoderna. Dessa två metoder spårar beroenden enligt beräkningskedjan. För att använda dem, först måste du aktivera beräkningskedjan med [FormulaSettings.enableCalculationChain()](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--). Sedan bör du utföra fullständig beräkning av arbetsboken med [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--). Efter det kan du spåra föregångare eller beroenden för alla celler du behöver.

För vissa formler kan de slutgiltiga föregångarna vara olika för precedents och precedentsInCalculation, och de slutgiltiga beroende kan vara olika för dependents och dependentsInCalculation. Till exempel, om cell A1:s formel är "=IF(TRUE,B2,C3)", kommer precedents att ge B2 och C3 som A1:s föregångare. Följaktligen har B2 och C3 båda beroendet A1 när man kontrollerar med dependents. Men för beräkningen av denna formel är det självklart att endast B2 kan påverka det beräknade resultatet. Därför kommer precedentsInCalculation inte att ge C3 för A1, och dependentsInCalculation kommer inte att ge A1 för C3. Ibland kan användare ha behov av att spåra de interberoende relationerna som faktiskt påverkar beräkningen av formler baserat på nuvarande data i arbetsboken, då bör de istället använda dependentsInCalculation/precedentsInCalculation i stället för dependents/precedents.

Följande exempel visar hur man spårar föregångare och beroenden enligt beräkningskedjan för celler:


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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;

            // Setting formulas
            cells.get("A1").formula = "=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2";
            cells.get("A2").formula = "=IF(TRUE,B2,B1)";

            // Enable calculation chain
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate formulas
            workbook.calculateFormula();

            // Collect output
            let output = '';

            let en = cells.get("B1").dependentsInCalculation;
            output += "B1's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                // If it's an iterable but doesn't have length
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("B2").dependentsInCalculation;
            output += "B2's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("A1").precedentsInCalculation;
            output += "A1's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }
            output += "\n";

            en = cells.get("A2").precedentsInCalculation;
            output += "A2's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }

            resultDiv.innerHTML = '<pre>' + output.replace(/</g, '&lt;') + '</pre>';

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```
