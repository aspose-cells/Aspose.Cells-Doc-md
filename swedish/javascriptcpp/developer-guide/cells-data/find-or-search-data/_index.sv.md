---
title: Hitta eller söka data
type: docs
weight: 50
url: /sv/javascript-cpp/find-or-search-data/
description: Lär dig att hitta eller söka celler i ett kalkylblad som innehåller angivna data med hjälp av Aspose.Cells for JavaScript via C++ API.
keywords: Hitta data Javascript via C++, Sök data Javascript via C++, Hitta celler som innehåller en formel Javascript via C++, Sök celler som innehåller en formel Javascript via C++, Hitta data eller formler med hjälp av FindOptions Javascript via C++, Sök data eller formler med hjälp av FindOptions Javascript via C++, Hitta eller sök celler som innehåller angivet textvärde eller nummer Javascript via C++, Hitta eller sök celler som innehåller angivna data
---

{{% alert color="primary" %}}  
Microsoft Excel tillåter användare att hitta celler i ett kalkblad som innehåller specificerad data.  
{{% /alert %}}  

## **Att hitta celler som innehåller specificerad data**  

### **Använda Microsoft Excel**  

Microsoft Excel tillåter användare att hitta celler i ett kalkblad som innehåller specificerad data. Om du väljer **Redigera** från **Sök**-menyn i Microsoft Excel, ser du en dialogruta där du kan ange sökvärdet.  

Här letar vi efter värdet "Apelsiner". Aspose.Cells tillåter också utvecklare att hitta celler i kalkylarket som innehåller specificerade värden.  

### **Använder Aspose.Cells for JavaScript via C++**  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) innehåller en [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-samling som ger åtkomst till varje kalkblad i Excel-filen. Ett kalkblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)-samling som representerar alla celler i kalkbladet. Samlingen [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) ger flera metoder för att hitta celler som innehåller användarspecifik data. Några av dessa metoder diskuteras nedan i mer detalj.  

{{% alert color="primary" %}}  
Alla Find-metoder returnerar referenser till celler som innehåller den specificerade datan att söka.  
{{% /alert %}}  

## **Att hitta celler som innehåller en formel**  

Utvecklare kan hitta en angiven formel i kalkbladet genom att anropa metoden [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) i [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-)-samlingen. Vanligtvis tar metoden [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) tre parametrar:  

- Objektet att söka efter. Typen bör vara int, double, DateTime, string, bool.  
- Föregående cell med samma objekt. Denna parameter kan anges till null om sökning sker från början.  
- Alternativ för att hitta det kräva objektet.  

Nedan används exempel på kalkylarksdata för att öva på hittametoder.  

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


## **Hitta data eller formler med FindOptions**  

Det är möjligt att hitta specificerade värden med hjälp av [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen och [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-)-metoden med olika [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions). Vanligtvis accepterar [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-)-metoden följande parametrar:  

- **Sökvärde**, data eller värde som ska sökas efter.  
- **Föregående cell**, den sista cellen som innehöll samma värde. Denna parameter kan ställas in till null när du söker från början.  
- **Hitta alternativ**, hitta alternativ.  

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


## **Hitta celler som innehåller specifierade strängvärden eller nummer**  

Det är möjligt att hitta angivna strängvärden genom att anropa samma [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-)-metod som finns i [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen med olika [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions).  

Ange egenskaperna [**FindOptions.lookInType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookInType-lookintype-) och [**FindOptions.lookAtType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookAtType-lookattype-). Följande kodexempel visar hur man använder dessa egenskaper för att hitta celler med olika antal strängar i början, mitten eller slutet av cellens text.  

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



## **Fortsatta ämnen**  
- [Hitta celler med specifik stil](/cells/sv/javascript-cpp/find-cells-with-specific-style/)  
- [Ta reda på om cellvärdet börjar med citattecken](/cells/sv/javascript-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Sök data med originalvärden](/cells/sv/javascript-cpp/search-data-using-original-values/)
