---
title: Trova o Cerca Dati
type: docs
weight: 50
url: /it/javascript-cpp/find-or-search-data/
description: Impara come trovare o cercare celle in un foglio di lavoro che contengono dati specificati tramite lo Script Aspose.Cells for Java tramite C++.
keywords: Trova dati JavaScript tramite C++, Ricerca dati JavaScript tramite C++, Trova Celle contenenti una Formula JavaScript tramite C++, Ricerca Celle contenenti una Formula JavaScript tramite C++, Trova Dati o Formule usando FindOptions JavaScript tramite C++, Ricerca Dati o Formule usando FindOptions JavaScript tramite C++, Trova o Cerca Celle contenenti Stringa o Numero Specificato JavaScript tramite C++, Trova o Cerca celle contenenti dati specificati
---

{{% alert color="primary" %}}  
Microsoft Excel consente agli utenti di trovare celle in un foglio di lavoro che contengono dati specificati.  
{{% /alert %}}  

## **Ricerca delle celle contenenti dati specificati**  

### **Utilizzando Microsoft Excel**  

Microsoft Excel consente agli utenti di trovare celle in un foglio di lavoro che contengono dati specificati. Se selezioni **Modifica** dal menu **Trova** in Microsoft Excel, vedrai una finestra di dialogo in cui puoi specificare il valore di ricerca.  

Qui stiamo cercando il valore "Arance". Aspose.Cells consente anche agli sviluppatori di trovare celle nel foglio di lavoro contenenti valori specificati.  

### **Usando Aspose.Cells for JavaScript tramite C++**  

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una raccolta [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) che permette di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) fornisce una raccolta [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) che rappresenta tutte le celle del foglio di lavoro. La raccolta [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) offre vari metodi per trovare celle in un foglio di lavoro contenenti dati inseriti dall’utente. Alcuni di questi metodi sono discussi più dettagliatamente di seguito.  

{{% alert color="primary" %}}  
Tutti i metodi di ricerca restituiscono i riferimenti delle celle contenenti i dati specificati da cercare.  
{{% /alert %}}  

## **Ricerca delle celle contenenti una formula**  

Gli sviluppatori possono trovare una formula specifica nel foglio di lavoro chiamando il metodo [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) nella raccolta [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). In genere, il metodo [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) accetta tre parametri:  

-  L'oggetto da cercare. Il tipo dovrebbe essere int, double, DateTime, string, bool.  
-  La cella precedente con lo stesso oggetto. Questo parametro può essere impostato su null se si ricerca dall'inizio.  
-  Opzioni per trovare l'oggetto richiesto.  

Gli esempi seguenti utilizzano i dati del foglio di lavoro per praticare i metodi di ricerca:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Cell Containing Formula</title>
    </head>
    <body>
        <h1>Find Cell Containing Formula</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions, LookInType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Instantiate FindOptions Object and set to look in formulas
            const findOptions = new FindOptions();
            findOptions.lookInType = LookInType.Formulas;

            // Finding the cell containing the specified formula
            const cell = worksheet.cells.find("=SUM(A5:A10)", null, findOptions);

            // Displaying the name of the cell found after searching worksheet
            document.getElementById('result').innerHTML = `<p style="color: green;">Name of the cell containing formula: ${cell.name}</p>`;
        });
    </script>
</html>
```  


## **Ricerca di dati o formule mediante FindOptions**  

È possibile trovare valori specificati utilizzando il metodo [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-) della collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) con vari [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions). Tipicamente, il metodo [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) accetta i seguenti parametri:  

- **Valore di ricerca**, i dati o il valore da cercare.  
- **Celle precedenti**, l'ultima cella che conteneva lo stesso valore. Questo parametro può essere impostato su null durante la ricerca dall'inizio.  
- **Opzioni di ricerca**, le opzioni di ricerca.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Using FindOptions</title>
    </head>
    <body>
        <h1>Find Using FindOptions Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FindOptions, CellArea, LookInType, LookAtType } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Calculate formulas in workbook
            workbook.calculateFormula();

            // Get Cells collection from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Instantiate FindOptions Object
            const findOptions = new FindOptions();

            // Create a Cells Area
            const ca = new CellArea();
            ca.startRow = 8;
            ca.startColumn = 2;
            ca.endRow = 17;
            ca.endColumn = 13;

            // Set cells area for find options
            findOptions.range = ca;

            // Set searching properties
            findOptions.searchBackward = false;
            findOptions.searchOrderByRows = true;

            // Set the lookintype, you may specify, values, formulas, comments etc.
            findOptions.lookInType = LookInType.Values;

            // Set the lookattype, you may specify Match entire content, endswith, startswith etc.
            findOptions.lookAtType = LookAtType.EntireContent;

            // Find the cell with value
            const cell = cells.find(341, null, findOptions);

            if (cell !== null) {
                document.getElementById('result').innerHTML = `<p>Name of the cell containing the value: ${cell.name}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p>Record not found</p>';
            }
        });
    </script>
</html>
```  


## **Ricerca delle celle contenenti un valore di stringa specificato o numero**  

È possibile trovare valori stringa specifici chiamando lo stesso metodo [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) presente nella collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) con vari [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions).  

Specifica le proprietà [**FindOptions.lookInType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookInType-lookintype-) e [**FindOptions.lookAtType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookAtType-lookattype-). Il seguente esempio di codice illustra come utilizzare queste proprietà per trovare celle con un diverso numero di stringhe all'inizio, al centro o alla fine della stringa della cella.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Find Examples</h1>
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

            // Instantiate the workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection
            const cells = workbook.worksheets.get(0).cells;

            const opts = new AsposeCells.FindOptions();
            opts.lookInType = AsposeCells.LookInType.Values;
            opts.lookAtType = AsposeCells.LookAtType.EntireContent;

            let messages = '';

            // Find the cell with the input integer or double
            let cell1 = cells.find(205, null, opts);

            if (cell1 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell1.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell with the input string
            let cell2 = cells.find("Items A", null, opts);

            if (cell2 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell2.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell containing the input string (partial match)
            opts.lookAtType = AsposeCells.LookAtType.Contains;
            let cell3 = cells.find("Data", null, opts);

            if (cell3 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell3.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            document.getElementById('result').innerHTML = messages;
        });
    </script>
</html>
``` 



## **Argomenti avanzati**  
- [Trova celle con stile specifico](/cells/it/javascript-cpp/find-cells-with-specific-style/)  
- [Verifica se il valore della cella inizia con un apice singolo](/cells/it/javascript-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Cerca dati usando valori originali](/cells/it/javascript-cpp/search-data-using-original-values/)
