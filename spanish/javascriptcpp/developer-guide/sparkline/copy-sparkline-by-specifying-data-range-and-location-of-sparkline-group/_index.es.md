---
title: Copiar Sparkline especificando el rango de datos y la ubicación del grupo de Sparkline con JavaScript a través de C++
linktitle: Copiar Sparkline especificando el rango de datos y la ubicación del grupo de sparkline
type: docs
weight: 300
url: /es/javascript-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Aprende cómo copiar un sparkline en Excel especificando el rango de datos y la ubicación del grupo de sparkline usando Aspose.Cells for JavaScript a través de C++.
---

{{% alert color="primary" %}}
Microsoft Excel le permite copiar una sparkline especificando el rango de datos y la ubicación de un grupo de sparkline. Aspose.Cells soporta esta funcionalidad.
{{% /alert %}}

Para copiar una minigráfica en otras celdas en Microsoft Excel:

1. Seleccione la celda que contiene la miniatura.  
1. Seleccione **Editar datos** en la sección de **Miniatura** de la pestaña **Diseño**.  
1. Seleccione **Editar ubicación y datos de grupo**.  
1. Especifique el rango de datos y la ubicación.  
1. Haz clic en **Aceptar**.

Aspose.Cells proporciona el método `SparklineCollection.add(dataRange, row, column)` para especificar el rango de datos y la ubicación de un grupo de líneas. El siguiente código de ejemplo carga el archivo Excel de origen como se muestra en la captura de pantalla arriba, luego accede al primer grupo de líneas y agrega rangos de datos y ubicaciones en el grupo de líneas. Finalmente, escribe el archivo Excel de salida en disco, también mostrado en la captura de pantalla arriba.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first sparkline group
            const group = worksheet.sparklineGroups.get(0);

            // Add Data Ranges and Locations inside this sparkline group
            group.sparklines.add("Sheet1!D5:O5", 4, 15);
            group.sparklines.add("Sheet1!D6:O6", 5, 15);
            group.sparklines.add("Sheet1!D7:O7", 6, 15);
            group.sparklines.add("Sheet1!D8:O8", 7, 15);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sparklines added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
