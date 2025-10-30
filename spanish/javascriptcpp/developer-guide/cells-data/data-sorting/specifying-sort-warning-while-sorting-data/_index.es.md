---
title: Especificar advertencia de ordenación al ordenar los datos
type: docs
weight: 140
url: /es/javascript-cpp/specifying-sort-warning-while-sorting-data/
description: Aprende cómo especificar advertencias de ordenamiento al ordenar datos usando el script Aspose.Cells for Java a través de la API C++.
keywords: Agregar advertencia de ordenación al ordenar datos, establecer advertencia de ordenación al ordenar datos, seleccionar advertencia de ordenación al ordenar datos.
---

## **Escenarios de uso posibles**

Por favor, considera estos datos textuales, es decir, {11, 111, 22}. Estos datos se ordenan porque, en términos de texto, 111 viene antes que 22. Pero, si quieres ordenar estos datos no como texto sino como números, entonces será {11, 22, 111} porque numéricamente 111 viene después de 22. El script Aspose.Cells for Java a través de C++ proporciona la propiedad {0} para tratar este problema. Por favor, establece esta propiedad en **true** y tus datos textuales se ordenarán como datos numéricos. La siguiente captura de pantalla muestra la advertencia de ordenamiento que muestra Microsoft Excel cuando los datos textuales que parecen datos numéricos se ordenan.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Código de muestra**

El siguiente código de ejemplo ilustra el uso de la propiedad [**DataSorter.sortAsNumber**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortAsNumber-boolean-) como se explica anteriormente. Consulte su [archivo de Excel de ejemplo](43352075.xlsx) y [archivo de Excel de salida](43352076.xlsx) para obtener más ayuda.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sort As Number Example</title>
    </head>
    <body>
        <h1>Sort As Number Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper, CellArea, SortOrder } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Create your cell area.
            const ca = AsposeCells.CellArea.createCellArea("A1", "A20");

            // Create your sorter.
            const sorter = workbook.dataSorter;

            // Find the index for column A.
            const idx = CellsHelper.columnNameToIndex("A");

            // Add key in sorter, it will sort in Ascending order.
            sorter.addKey(idx, SortOrder.Ascending);

            // Set sort as number
            sorter.sortAsNumber = true;

            // Perform sort.
            sorter.sort(worksheet.cells, ca);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortAsNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sort completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
