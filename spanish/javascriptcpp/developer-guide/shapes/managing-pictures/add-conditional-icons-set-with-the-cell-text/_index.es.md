---
title: Agregar conjunto de iconos condicionales con el texto de la celda usando JavaScript a través de C++
linktitle: Agregar un conjunto de iconos condicionales con el texto de la celda
type: docs
weight: 160
url: /es/javascript-cpp/add-conditional-icons-set-with-the-cell-text/
description: Aprende cómo agregar iconos condicionales junto al texto de la celda usando Aspose.Cells for JavaScript a través de C++. Mejorando el significado de los datos mediante iconos.
---

{{% alert color="primary" %}} 

A veces, quieres agregar iconos condicionales junto al texto en una celda para que los datos sean más significativos para los lectores. Quieres usar algunos de los tipos de iconos de formato condicional pero sin aplicar formato condicional a las celdas. Aspose.Cells for JavaScript a través de C++ admite esta función.

{{% /alert %}} 

La siguiente muestra de código muestra cómo agregar un conjunto de iconos condicionales con el texto de la celda.



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
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();
            // Get the first worksheet (default worksheet) in the workbook
            const worksheet = workbook.worksheets.get(0);
            // Get the cells
            const cells = worksheet.cells;
            // Set the columns widths (A, B and C) by setting column width on each column
            worksheet.cells.columns.get(0).width = 24;
            worksheet.cells.columns.get(1).width = 24;
            worksheet.cells.columns.get(2).width = 24;

            // Input data into the cells
            cells.get("A1").value = "KPIs";
            cells.get("A2").value = 19551794;
            cells.get("A3").value = 11.8070745566204;
            cells.get("A4").value = 11.858589818569;
            cells.get("B1").value = "UA Contract Size Group 4";
            cells.get("B2").value = 19551794;
            cells.get("B3").value = 11.8070745566204;
            cells.get("B4").value = 11.858589818569;
            cells.get("C1").value = "UA Contract Size Group 3";
            cells.get("C2").value = 8150131.66666667;
            cells.get("C3").value = 10.3168384396244;
            cells.get("C4").value = 11.3326931937091;

            // Get the conditional icon's image data and add pictures
            const iconTypes = [
                { type: AsposeCells.IconSetType.TrafficLights31, row: 1, column: 1 },
                { type: AsposeCells.IconSetType.Arrows3, row: 1, column: 2 },
                { type: AsposeCells.IconSetType.Symbols3, row: 2, column: 1 },
                { type: AsposeCells.IconSetType.Stars3, row: 2, column: 2 },
                { type: AsposeCells.IconSetType.Boxes5, row: 3, column: 1 },
                { type: AsposeCells.IconSetType.Flags3, row: 3, column: 2 }
            ];

            iconTypes.forEach(icon => {
                const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(icon.type, icon.type === AsposeCells.IconSetType.Flags3 ? 1 : 0);
                const stream = new Uint8Array(imagedata);
                worksheet.pictures.add(icon.row, icon.column, stream);
            });

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
