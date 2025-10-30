---
title: Daten finden oder suchen
type: docs
weight: 50
url: /de/javascript-cpp/find-or-search-data/
description: Erfahren Sie, wie Sie Zellen in einem Arbeitsblatt finden oder suchen, die bestimmte Daten enthalten, mit dem Aspose.Cells for JavaScript über C++.
keywords: Daten mit C++ in JavaScript finden, Daten mit C++ in JavaScript suchen, Zellen mit einer Formel in JavaScript via C++ finden, Zellen mit einer Formel in JavaScript via C++ suchen, Daten oder Formeln mit FindOptions JavaScript via C++ finden, Daten oder Formeln mit FindOptions JavaScript via C++, Zellen mit einem bestimmten String Wert oder einer Zahl finden oder durchsuchen JavaScript via C++, Zellenwerte mit bestimmten Daten finden oder durchsuchen
---

{{% alert color="primary" %}}  
Microsoft Excel ermöglicht es Benutzern, Zellen in einem Arbeitsblatt zu finden, die bestimmte Daten enthalten.  
{{% /alert %}}  

## **Suchen von Zellen, die bestimmte Daten enthalten**  

### **Verwendung von Microsoft Excel**  

Microsoft Excel ermöglicht es Benutzern, Zellen in einem Arbeitsblatt zu finden, die bestimmte Daten enthalten. Wenn Sie **Bearbeiten** im **Suchen**-Menü in Microsoft Excel auswählen, sehen Sie einen Dialog, in dem Sie den Suchwert festlegen können.  

Hier suchen wir nach dem Wert "Orangen". Aspose.Cells ermöglicht es Entwicklern auch, in einem Arbeitsblatt Zellen mit bestimmten Werten zu finden.  

### **Mit Aspose.Cells for JavaScript via C++ verwenden**  

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), bereit, die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) enthält eine [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) bietet eine [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert. Die [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung stellt verschiedene Methoden zum Finden von Zellen in einem Arbeitsblatt bereit, die vom Benutzer angegebene Daten enthalten. Einige dieser Methoden werden im Folgenden detaillierter erläutert.  

{{% alert color="primary" %}}  
Alle Find-Methoden geben die Verweise auf die Zellen zurück, die die angegebenen Daten enthalten.  
{{% /alert %}}  

## **Suchen von Zellen, die eine Formel enthalten**  

Entwickler können eine bestimmte Formel im Arbeitsblatt finden, indem sie die [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlungs-Methode [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) aufrufen. Typischerweise akzeptiert die [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-)-Methode drei Parameter:  

- Das Objekt, nach dem gesucht werden soll. Der Typ sollte int, double, DateTime, string, bool sein.  
- Die vorherige Zelle mit demselben Objekt. Dieser Parameter kann auf null gesetzt werden, wenn ab dem Anfang gesucht wird.  
- Optionen zum Finden des benötigten Objekts.  

Die folgenden Beispiele verwenden Arbeitsblattdaten, um die Find-Methoden zu üben:  

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


## **Suchen von Daten oder Formeln mithilfe von FindOptions**  

Es ist möglich, bestimmte Werte mit der [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlungs-[**Cells.find(object, Cell)**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-)-Methode und verschiedenen [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions) zu finden. Typischerweise akzeptiert die [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-)-Methode die folgenden Parameter:  

- **Suchwert**, die Daten oder der Wert, nach dem gesucht werden soll.  
- **Vorherige Zelle**, die letzte Zelle, die den gleichen Wert enthielt. Dieser Parameter kann auf null gesetzt werden, wenn von Anfang an gesucht wird.  
- **Suchoptionen**, die Suchoptionen.  

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


## **Zellen finden, die den angegebenen Zeichenfolgenwert oder die angegebene Zahl enthalten**  

Es ist möglich, bestimmte Zeichenkettenwerte durch Aufrufen derselben [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-)-Methode zu finden, die in der [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-Sammlung mit verschiedenen [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions) vorhanden ist.  

Geben Sie die Eigenschaften [**FindOptions.lookInType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookInType-lookintype-) und [**FindOptions.lookAtType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookAtType-lookattype-) an. Das folgende Beispiel zeigt, wie diese Eigenschaften verwendet werden, um Zellen mit unterschiedlicher Anzahl von Zeichenketten am **Anfang**, in der **Mitte** oder am **Ende** der Zelle zu finden.  

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



## **Erweiterte Themen**  
- [Zellen mit bestimmtem Stil finden](/cells/de/javascript-cpp/find-cells-with-specific-style/)  
- [Finden, ob der Zellenwert mit einem einzelnen Anführungszeichen beginnt](/cells/de/javascript-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Daten mithilfe der Originalwerte suchen](/cells/de/javascript-cpp/search-data-using-original-values/)
