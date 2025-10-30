---
title: Åtkomst till kalkylbladets celler
type: docs
weight: 10
url: /sv/javascript-cpp/accessing-cells-of-a-worksheet/
description: Denna artikel visar hur man får maximalt visningsintervall för arbetsblad och kommer åt celler via API et Aspose.Cells for JavaScript via C++.
keywords: Få Cell objekt, Åtkomst till celler, Få maximalt visningsområde på arbetsbladet. 
---

{{% alert color="primary" %}}

Vi vet att alla arbetsblad kan innehålla data som i grunden lagras i celler (vilka ett arbetsblad är uppbyggt av). En cell är en grundläggande del av ett arbetsblad som används för att konstruera hela arbetsbladet som en sekvens av rader och kolumner. Innan vi försöker få åtkomst till data från ett arbetsblad, måste vi få tillgång till dess celler. Så, i denna ämne, diskuterar vi några grundläggande tillvägagångssätt för att komma åt arbetsbladsceller vid körning med Aspose.Cells for JavaScript via C++.

{{% /alert %}}

## **Hur man får åtkomst till celler**

Aspose.Cells for JavaScript via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) som tillåter åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad är representerat av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) samling som representerar alla celler i arbetsbladet.

Vi kan använda [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) samlingen för att få åtkomst till celler i ett arbetsblad. Aspose.Cells for JavaScript via C++ tillhandahåller tre grundläggande tillvägagångssätt för att komma åt celler i ett arbetsblad:

1. Genom att använda cellnamnet.
2. Genom att använda cellens rad- och kolumnindex.
1. Använda en cellindex i [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen

 1. Genom att använda en cellindex i [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen

### **Hur man får Cell-objekt genom Cellnamn**

Utvecklare kan få tillgång till vilken cell som helst genom att föra in dess cellnamn i [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) som ett index.

Om du skapar ett tomt arbetsblad i början, är antalet [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen noll. När du använder detta tillvägagångssätt för att komma åt en cell, kommer det att kontrollera om cellen finns i samlingen eller inte. Om ja, returnerar det cellobjektet i samlingen, annars skapar det ett nytt [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)-objekt, lägger till objektet i [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen och returnerar det. Detta är det enklaste sättet att komma åt en cell om du är bekant med Microsoft Excel, men det är det långsammaste jämfört med andra metoder.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Read Cell Example</h1>
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

            // Using the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its name
            const cell = worksheet.cells.get("A1");

            // Output the cell's string value to the page
            document.getElementById('result').innerHTML = `<p>Cell A1 value: ${cell.stringValue}</p>`;
        });
    </script>
</html>
```

### **Hur man får Cell-objekt genom rad- och kolumnindex för cellen**

Utvecklare kan få tillgång till vilken cell som helst genom att skicka dess rad- och kolumnindextal till [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

Det här tillvägagångssättet fungerar på samma sätt som det första tillvägagångssättet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell Value</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the first worksheet in workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column (A1 -> 0,0)
            const cell = worksheet.cells.get(0, 0);

            // Printing the string value of the cell
            const value = cell.stringValue;
            console.log(value);
            resultDiv.innerHTML = `<p>Cell A1 value: ${value}</p>`;
        });
    </script>
</html>
```

### **Hur man får cellobjekt efter cellindex i cellsamlingen**

En cell kan också nås genom att skicka cellens numeriska index till [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen.

Om du använder detta tillvägagångssätt för att komma åt celler, kan ett undantag kastas om cellens numeriska index är utanför räckvidden. Detta tillvägagångssätt är det snabbaste att komma åt cellerna, men en viktig sak att veta är att om du använder detta för att komma åt en cell, kan det numeriska indexet ändras efter att nya celler har lagts till i [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen. Cellobjekten i [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen är internt sorterade efter rad- och kolumnindextal.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Read Cell String Value</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Using the Sheet 1 in Workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing a cell using its row and column.
            const cell = worksheet.cells.get(0, 0);

            // Output the string value of the cell
            console.log(cell.stringValue);
            resultDiv.innerHTML = `<p>Cell (0,0) string value: <strong>${cell.stringValue}</strong></p>`;
        });
    </script>
</html>
```

## **Hur man får maximal visningsområde för arbetsblad**

Aspose.Cells for JavaScript via C++ tillåter utvecklare att få åtkomst till ett arbetsblads maximala visningsintervall. Det maximala visningsintervallet - området av celler mellan den första och den sista cellen med innehåll - är användbart när du behöver kopiera, markera eller visa hela innehållet i ett arbetsblad som en bild.

Du kan få åtkomst till ett arbetsbladets maximala visningsintervall med [**Cells.maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--). Följande exempel visar hur man får åtkomst till egenskapen [**maxDisplayRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDisplayRange--).

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the Maximum Display Range
            const range = worksheet.cells.maxDisplayRange;

            // Print / display the Maximum Display Range RefersTo property
            const refersTo = range.refersTo;
            resultDiv.innerHTML = `<p style="color: green;">Maximum Display Range: ${refersTo}</p>`;
        });
    </script>
</html>
```
