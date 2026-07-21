---
title: Obtener Fuente de Datos de Conexión Externa de la Tabla Dinámica
type: docs
weight: 150
url: /es/javascript-cpp/get-external-connection-data-source-of-pivot-table/
description: Cómo obtener la fuente de datos de conexión externa de una tabla dinámica con Aspose.Cells for JavaScript vía C++.
keywords: Aspose.Cells for JavaScript Excel, biblioteca JavaScript de Excel, obtener la fuente de datos de conexión externa de la tabla dinámica usando Aspose.Cells for JavaScript vía C++ Excel Library.
---

## **Cómo obtener la fuente de datos de conexión externa de la tabla dinámica.**

Aspose.Cells for JavaScript vía C++ ofrece la capacidad de obtener la fuente de datos de conexión externa de la tabla dinámica. Para esto, la API proporciona la propiedad [**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--) de la clase [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable/). La propiedad [**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--) devuelve el objeto [**ExternalConnection**](https://reference.aspose.com/cells/javascript-cpp/externalconnection/). El siguiente fragmento de código demuestra el uso de la propiedad [**externalConnectionDataSource**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#externalConnectionDataSource--) para obtener la fuente de datos de conexión externa de la tabla dinámica.

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Pivot Table External Connection Example</title>
    </head>
    <body>
        <h1>Pivot Table External Connection Example</h1>
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

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get the pivot table
            const pivotTable = worksheet.pivotTables.get(0);

            // Get external connection data source
            const externalConnection = pivotTable.externalConnectionDataSource;

            const name = externalConnection.name;
            const type = externalConnection.type;

            console.log("External Connection Data Source");
            console.log("Name: " + name);
            console.log("Type: " + type);

            resultDiv.innerHTML = `<p style="color: green;">External Connection Data Source</p>
                                   <p>Name: ${name}</p>
                                   <p>Type: ${type}</p>`;
        });
    </script>
</html>
```

El archivo fuente utilizado en el fragmento de código está adjunto para referencia.

[Archivo Fuente](104398862.xlsx)
