---
title: Impostazioni del carattere con JavaScript tramite C++
linktitle: Impostazioni del carattere
description: Aspose.Cells è una libreria JavaScript per lavorare con i file di fogli di calcolo. Supporta la configurazione delle impostazioni del carattere delle celle, consentendo agli utenti di personalizzare lo stile e le proprietà del carattere delle celle. Questo articolo introdurrà come utilizzare la libreria Aspose.Cells per impostare le impostazioni del carattere della cella.
keywords: Aspose.Cells, Celle, Impostazioni del carattere, Stili, Proprietà, JavaScript tramite C++
type: docs
weight: 30
url: /it/javascript-cpp/cells-font-settings/
---

{{% alert color="primary" %}}  
L'aspetto di un testo può essere controllato modificando le impostazioni del carattere. Le impostazioni del carattere possono includere il nome, lo stile, le dimensioni, il colore e altri effetti dei font. Proprio come Microsoft Excel, Aspose.Cells supporta anche la configurazione delle impostazioni del carattere delle celle.  
{{% /alert %}}  

## **Configurazione delle Impostazioni del Carattere**  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una raccolta [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fornisce una raccolta [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). Ogni elemento nella raccolta [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).  

Aspose.Cells fornisce i metodi [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) e [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) che vengono usati per ottenere e impostare lo stile di formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) fornisce proprietà per la configurazione delle impostazioni di font.  

### **Impostazione del nome del carattere**  

Gli sviluppatori possono applicare qualsiasi carattere al testo all'interno di una cella utilizzando il metodo [**name**](https://reference.aspose.com/cells/javascript-cpp/font/#name-string-) dell'oggetto [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font name to "Times New Roman"
            style.font.name = "Times New Roman";

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **Impostare lo stile del carattere su Grassetto**  

Gli sviluppatori possono rendere il testo in grassetto impostando il metodo [**isBold**](https://reference.aspose.com/cells/javascript-cpp/font/#isBold-boolean-) dell'oggetto [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) su **true**.   

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font weight to bold
            style.font.isBold = true;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and A1 updated. Click the download link to get the file.</p>';
        });
    </script>
</html>
```



### **Impostazione della dimensione del carattere**  

Imposta la dimensione del font con il metodo [**size**](https://reference.aspose.com/cells/javascript-cpp/font/#size-number-) dell'oggetto [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--).  

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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.count;
            workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font size to 14
            style.font.size = 14;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **Impostazione del colore del carattere**  

Usa il metodo [**color**](https://reference.aspose.com/cells/javascript-cpp/font/#color-color-) dell'oggetto [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) per impostare il colore del carattere. Seleziona qualsiasi colore dall'enumerazione Color (parte di JavaScript) e assegnalo al metodo [**color**](https://reference.aspose.com/cells/javascript-cpp/font/#color-color-).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Worksheet and Set Cell Style Example</h1>
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
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font color to blue
            style.font.color = AsposeCells.Color.Blue;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **Impostazione del tipo sottolineato del carattere**  

Usa il metodo [**underline**](https://reference.aspose.com/cells/javascript-cpp/font/#underline-fontunderlinetype-) dell'oggetto [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) per sottolineare il testo. Aspose.Cells offre vari tipi di sottolineatura predefiniti nella enumerazione [**FontUnderlineType**](https://reference.aspose.com/cells/javascript-cpp/fontunderlinetype).  

|**Tipi di sottolineatura del carattere**|**Descrizione**|  
| :- | :- |  
|Accounting|Un solo sottolineatura contabile|  
|Double|Doppia sottolineatura|  
|DoubleAccounting|Doppia sottolineatura contabile|  
|None|Nessuna sottolineatura|  
|Single|Una singola sottolineatura|  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontUnderlineType } = AsposeCells;

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
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font to be underlined
            style.font.underline = FontUnderlineType.Single;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready to download.</p>';
        });
    </script>
</html>
```


### **Impostazione dell'effetto barrato**  

Applicare il sbarrato impostando il metodo [**isStrikeout**](https://reference.aspose.com/cells/javascript-cpp/font/#isStrikeout-boolean-) dell'oggetto [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) su **true**.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the strike out effect on the font
            style.font.isStrikeout = true;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


### **Impostazione dell'effetto pedice**  

Applicare il pedice impostando il metodo [**isSubscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSubscript-boolean-) dell'oggetto [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) su **true**.  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Add Worksheet</h1>
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

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet and get its index
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access the "A1" cell
            const cell = worksheet.cells.get("A1");

            // Set value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtain the style of the cell
            const style = cell.style;

            // Set strikeout on the font
            style.font.isStrikeout = true;

            // Apply the style to the cell
            cell.style = style;

            // Save the workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



### **Impostazione dell'effetto esponente sulla font**  

Gli sviluppatori possono applicare l'effetto apice impostando il metodo [**isSuperscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSuperscript-boolean-) dell'oggetto [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) su **true**.  

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting superscript effect
            style.font.isSuperscript = true;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


## **Argomenti avanzati**  
- [Applica gli effetti esponente e pedice sulle font](/cells/it/javascript-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [Ottieni un elenco di font utilizzati in un foglio di calcolo o di lavoro](/cells/it/javascript-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
