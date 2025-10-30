---
title: Implementación de rangos no secuenciales con JavaScript mediante C++
linktitle: Implementando rangos no secuenciales
type: docs
weight: 700
url: /es/javascript-cpp/implementing-non-sequential-ranges/
description: Aprende cómo crear rangos no secuenciales con nombres usando Aspose.Cells for JavaScript vía C++. Usa rangos de celdas no adyacentes eficazmente.
---

{{% alert color="primary" %}} 

Normalmente, los rangos con nombre son rectangulares con celdas continuas y adyacentes entre sí. Pero a veces, puedes necesitar usar un rango de celdas no secuencial donde las celdas no son adyacentes. Aspose.Cells for JavaScript vía C++ soporta la creación de un rango con nombre con celdas no adyacentes.

{{% /alert %}} 

El ejemplo de código a continuación muestra cómo crear un rango no secuencial con nombre usando Aspose.Cells for JavaScript vía C++.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add NonSequenced Range Name</h1>
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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a Name for non sequenced range
            const index = workbook.worksheets.names.add("NonSequencedRange");

            const name = workbook.worksheets.names.get(index);

            // Creating a non sequence range of cells
            name.refersTo = "=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6";

            // Saving the workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and name added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
