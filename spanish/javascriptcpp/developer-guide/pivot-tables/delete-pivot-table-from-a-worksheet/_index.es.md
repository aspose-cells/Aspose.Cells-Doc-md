---
title: Eliminar la tabla dinámica de una hoja de cálculo
type: docs
weight: 60
url: /es/javascript-cpp/delete-pivot-table-from-a-worksheet/
description: Código Script via C++ para eliminar una tabla dinámica de hojas de cálculo de Excel
keywords: Script via C++ para Excel, biblioteca de Excel JavaScript, eliminar tabla dinámica de la hoja de cálculo, eliminar tabla dinámica de Excel, cómo eliminar una tabla dinámica con Script via C++, eliminar tabla dinámica, eliminar tabla dinámica de Excel, eliminar tabla dinámica, Script via C++ para eliminar tabla dinámica, eliminar tabla dinámica, eliminar tabla dinámica, cómo eliminar una tabla dinámica
---

{{% alert color="primary" %}}

Script via C++ para Excel ofrece una función para eliminar o remover una tabla dinámica de una hoja de cálculo. Puedes eliminar la tabla dinámica usando el objeto de tabla dinámica o su posición. Usa el método [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) para eliminar la tabla dinámica usando el objeto y el método [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-) para eliminar la tabla dinámica usando su posición dentro de la colección de tablas dinámicas.

{{% /alert %}}

## **Cómo eliminar una tabla dinámica desde la hoja de cálculo usando Aspose.Cells for JavaScript vía C++**

El siguiente código de muestra elimina dos tablas dinámicas de la hoja de cálculo. Primero elimina la tabla dinámica usando el método [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) y luego elimina la tabla dinámica usando el método [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Table</title>
    </head>
    <body>
        <h1>Remove Pivot Table Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table object
            const pivotTable = worksheet.pivotTables.get(0);

            // Remove pivot table using pivot table object
            worksheet.pivotTables.remove(pivotTable);
            // OR remove by index:
            // worksheet.pivotTables.removeAt(0);

            // Saving the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
