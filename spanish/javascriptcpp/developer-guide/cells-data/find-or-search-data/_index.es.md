---
title: Buscar datos
type: docs
weight: 50
url: /es/javascript-cpp/find-or-search-data/
description: Aprende cómo encontrar o buscar celdas en una hoja de cálculo que contienen datos específicos mediante el Aspose.Cells for JavaScript a través de C++. 
keywords: Buscar datos en JavaScript a través de C++, Buscar datos en JavaScript a través de C++, Buscar celdas que contienen una fórmula en JavaScript a través de C++, Buscar celdas que contienen una fórmula en JavaScript a través de C++, Buscar datos o fórmulas usando FindOptions en JavaScript a través de C++, Buscar datos o fórmulas usando FindOptions en JavaScript a través de C++, Buscar o buscar celdas que contienen una cadena o valor numérico específica en JavaScript a través de C++, Buscar o buscar celdas que contienen datos específicos
---

{{% alert color="primary" %}}  
Microsoft Excel permite a los usuarios encontrar celdas en una hoja de trabajo que contienen datos específicos.  
{{% /alert %}}  

## **Encontrar celdas que contienen datos especificados**  

### **Usar Microsoft Excel**  

Microsoft Excel permite a los usuarios encontrar celdas en una hoja de trabajo que contienen datos específicos. Si seleccionas **Editar** en el menú **Buscar** en Microsoft Excel, verás un cuadro de diálogo donde puedes especificar el valor de búsqueda.  

Aquí, estamos buscando el valor "Naranjas". Aspose.Cells también permite a los desarrolladores encontrar celdas en la hoja de cálculo que contienen valores especificados.  

### **Usando Aspose.Cells for JavaScript a través de C++**  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) contiene una colección [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) que permite acceder a cada hoja de cálculo en el archivo Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) que representa todas las celdas en la hoja de cálculo. La colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) ofrece varios métodos para buscar celdas en una hoja que contienen datos definidos por el usuario. Algunos de estos métodos se discuten a continuación en más detalle.  

{{% alert color="primary" %}}  
Todos los métodos de búsqueda devuelven las referencias de las celdas que contienen los datos especificados.  
{{% /alert %}}  

## **Buscar celdas que contienen una fórmula**  

Los desarrolladores pueden encontrar una fórmula específica en la hoja llamando al método [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) de la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Por lo general, el método [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) acepta tres parámetros:  

-  El objeto a buscar. El tipo debe ser int, double, DateTime, string, bool.  
-  La celda anterior con el mismo objeto. Este parámetro puede establecerse en null si se busca desde el inicio.  
-  Opciones para encontrar el objeto requerido.  

Los ejemplos a continuación utilizan datos de hoja de cálculo para practicar los métodos de búsqueda:  

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


## **Encontrar datos o fórmulas utilizando FindOptions**  

Es posible encontrar valores especificados usando el método [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-) de la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) con varios [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions). Por lo general, el método [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) acepta los siguientes parámetros:  

- **Valor de búsqueda**, los datos o valores a buscar.  
- **Celda anterior**, la última celda que contenía el mismo valor. Este parámetro puede establecerse en nulo al buscar desde el principio.  
- **Opciones de búsqueda**, las opciones de búsqueda.  

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


## **Encontrar celdas que contengan un valor de cadena o número especificado**  

Es posible encontrar valores de cadena especificados llamando al mismo método [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) que se encuentra en la colección [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) con varios [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions).  

Especifica las propiedades [**FindOptions.lookInType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookInType-lookintype-) y [**FindOptions.lookAtType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookAtType-lookattype-). El siguiente ejemplo de código ilustra cómo usar estas propiedades para buscar celdas con varias cadenas al **principio**, en el **centro** o al **final** de la cadena de la celda.  

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



## **Temas avanzados**  
- [Encontrar celdas con estilo específico](/cells/es/javascript-cpp/find-cells-with-specific-style/)  
- [Encontrar si el valor de la celda comienza con una comilla simple](/cells/es/javascript-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Buscar Datos usando Valores Originales](/cells/es/javascript-cpp/search-data-using-original-values/)
