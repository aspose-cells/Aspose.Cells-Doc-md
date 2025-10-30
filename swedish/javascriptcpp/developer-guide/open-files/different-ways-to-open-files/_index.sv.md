---
title: Olika sätt att öppna filer med JavaScript via C++
linktitle: Olika sätt att öppna filer
type: docs
weight: 10
url: /sv/javascript-cpp/different-ways-to-open-files/
description: Denna artikel förklarar hur man öppnar en Excel fil med Aspose.Cells for JavaScript via C++ API.
keywords: JavaScript Öppna en Excel fil utan Excel, Hur öppnar jag en Excel fil med JavaScript.
---

{{% alert color="primary" %}}

 Med Aspose.Cells är det enkelt att öppna filer, till exempel för att hämta data eller använda en designermall för att snabba på utvecklingsprocessen.

{{% /alert %}}

## **Så öppnar du en Excel-fil via en sökväg**

 Utvecklare kan öppna en Microsoft Excel-fil genom att specificera dess sökväg på den lokala datorn i [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) klassens konstruktor. Ange helt enkelt sökvägen som en *sträng* i konstruktorn. Aspose.Cells upptäcker automatiskt filformatet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Open Workbook</title>
    </head>
    <body>
        <h1>Open Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook1 = new Workbook(new Uint8Array(arrayBuffer));
            console.log("Workbook opened using file successfully!");

            // Display basic info about the opened workbook
            document.getElementById('result').innerHTML = `<p style="color: green;">Workbook opened successfully! Worksheets count: ${workbook1.worksheets.count}</p>`;
        });
    </script>
</html>
```

## **Så öppnar du en Excel-fil via en ström**

Det är också enkelt att öppna en Excel-fil som en ström. Använd en överlagrad version av konstruktorn som tar emot *Stream* objektet som innehåller filen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Stream to Workbook</title>
    </head>
    <body>
        <h1>Open Excel Stream Example (Browser)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Read the selected file as an ArrayBuffer (equivalent to reading a stream in JavaScript)
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object from the file content
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Example modification: set A1 to indicate file was loaded (demonstrates cell value setter conversion)
            const cell = worksheet.cells.get(0, 0);
            cell.value = "Loaded from stream";

            // Save the modified workbook as Excel97-2003 (.xls) since original was .xls in JavaScript example
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Så öppnar du en fil med endast data**

För att öppna en fil med endast data, använd klasserna [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) och [**LoadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadfilter) för att ställa in relaterade attribut och alternativ för klassernas mallfil.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells LoadOptions Example</title>
    </head>
    <body>
        <h1>LoadOptions with LoadFilter Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);

            // Set LoadFilter property to load only data & cell formatting
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.CellData);

            // Create a Workbook object and opening the file from the uploaded file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Indicate success
            document.getElementById('result').innerHTML = '<p style="color: green;">File data imported successfully!</p>';

            // Prepare download of the loaded workbook (optional)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

## **Så lastar du bara synliga ark**

När du laddar en [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) kan du ibland bara behöva data i synliga arbetsblad i en arbetsbok. Aspose.Cells gör det möjligt att hoppa över data i osynliga arbetsblad vid inläsning av en arbetsbok. Skapa en anpassad funktion som ärvder [**LoadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadfilter) klassen och passera dess instans till [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) egenskapen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Create if no file selected)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, Utils } = AsposeCells;

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
            let bytes;
            let createdOutputData;

            if (fileInput.files.length) {
                // Load from user-selected file
                const arrayBuffer = await fileInput.files[0].arrayBuffer();
                bytes = new Uint8Array(arrayBuffer);
            } else {
                // Create a sample workbook in memory
                const createWorkbook = new Workbook();

                // Put some data in first cell of all 3 sheets
                createWorkbook.worksheets.get("Sheet1").cells.get("A1").value = "Aspose";
                createWorkbook.worksheets.add("Sheet2").cells.get("A1").value = "Aspose";
                createWorkbook.worksheets.add("Sheet3").cells.get("A1").value = "Aspose";
                createWorkbook.worksheets.get("Sheet3").isVisible = false;

                // Save the created workbook to bytes
                createdOutputData = createWorkbook.save(SaveFormat.Xlsx);
                bytes = createdOutputData instanceof Uint8Array ? createdOutputData : new Uint8Array(createdOutputData);

                // Provide download link for the created workbook
                const blob = new Blob([bytes]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'output.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Created Excel File';
            }

            // Prepare load options and load filter
            const loadOptions = new LoadOptions();
            loadOptions.loadFilter = new LoadFilter();

            // Load the workbook using the bytes and load options
            const loadWorkbook = new Workbook(bytes, loadOptions);

            // Read values from A1 of Sheet1, Sheet2, Sheet3
            const sheet1A1 = loadWorkbook.worksheets.get("Sheet1").cells.get("A1").value;
            const sheet2A1 = loadWorkbook.worksheets.get("Sheet2").cells.get("A1").value;
            const sheet3A1 = loadWorkbook.worksheets.get("Sheet3").cells.get("A1").value;

            // Log to console and show in the page
            console.log(`Sheet1: A1: ${sheet1A1}`);
            console.log(`Sheet2: A1: ${sheet2A1}`);
            console.log(`Sheet3: A1: ${sheet3A1}`);

            document.getElementById('result').innerHTML =
                `<p>Sheet1: A1: ${sheet1A1}</p>
                 <p>Sheet2: A1: ${sheet2A1}</p>
                 <p>Sheet3: A1: ${sheet3A1}</p>
                 <p style="color: green;">Operation completed successfully!</p>`;
        });
    </script>
</html>
```



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>CustomLoad Example</h1>
        <p>Select an Excel file to evaluate sheets with CustomLoad.startSheet()</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadDataFilterOptions } = AsposeCells;

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

        class CustomLoad {
            startSheet(sheet) {
                if (sheet.isVisible()) {
                    // Load everything from visible worksheet
                    this.loadDataFilterOptions = LoadDataFilterOptions.All;
                } else {
                    // Load nothing
                    this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const custom = new CustomLoad();

            let html = '<h2>CustomLoad Results</h2>';
            html += '<ul>';

            for (let i = 0; i < workbook.worksheets.count; i++) {
                const sheet = workbook.worksheets.get(i);
                custom.startSheet(sheet);
                html += `<li><strong>${sheet.name}</strong>: loadDataFilterOptions = ${custom.loadDataFilterOptions}</li>`;
            }

            html += '</ul>';
            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Ett undantag kommer att kastas om du försöker öppna icke-native Excel-filer eller andra filformat (t.ex. PPT/PPTX, DOC/DOCX, etc.) med Aspose.Cells.

{{% /alert %}} 

{{% alert color="primary" %}}

Det finns rättvisa chanser att [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-konstruktören kan kasta *OutOfMemoryError* när stora kalkylblad laddas. Detta undantag tyder på att tillgängligt minne är otillräckligt för att helt ladda kalkylbladet i minnet; därför måste kalkylbladet laddas medan minnesinställningarna är aktiverade.

{{% /alert %}}
