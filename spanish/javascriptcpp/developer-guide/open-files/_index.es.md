---
title: Cargando y gestionando archivos de Excel, OpenOffice, Json, Csv y Html
linktitle: Abrir archivos
type: docs
weight: 20
url: /es/javascript-cpp/loading-saving-and-managing/
description: Con Aspose.Cells, es sencillo crear, abrir y administrar archivos de Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, PDF, Jpg, Tiff, Imagen, Mht y XPS usando JavaScript a través de C++.
---

{{% alert color="primary" %}}

Con Aspose.Cells, es simple crear, abrir y gestionar archivos de Excel, por ejemplo, para obtener datos, o usar una plantilla de diseñador para acelerar el proceso de desarrollo.

{{% /alert %}}

## **Creando un libro de trabajo nuevo**
El siguiente ejemplo crea un nuevo libro de trabajo desde cero.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/Aspose.Cells.lic",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a Workbook object (new blank workbook)
            const wb = new Workbook();

            // Access the first worksheet in the workbook
            const sheet = wb.worksheets.get(0);

            // Access the "A1" cell in the sheet
            const cell = sheet.cells.get("A1");

            // Input the "Hello World!" text into the "A1" cell
            cell.value = "Hello World!";

            // Save the Excel file and prepare download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MyBook_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell updated. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Abrir y guardar un archivo**
Con Aspose.Cells, es fácil abrir, guardar y gestionar archivos de Excel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // Creating a Workbook object and opening an Excel file using its file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding new sheet
            const sheetIndex = workbook.worksheets.add("MySheet");
            const sheet = workbook.worksheets.get(sheetIndex);

            // Setting active sheet
            workbook.worksheets.activeSheetIndex = 1;

            // Setting values.
            const cells = sheet.cells;

            // Setting text
            cells.get("A1").putValue("Hello!");

            // Setting number
            cells.get("A2").putValue(1000);

            // Setting Date Time
            const cell = cells.get("A3");
            cell.putValue(new Date());
            const style = cell.style;
            style.number = 14;
            cell.style = style;

            // Setting formula
            cells.get("A4").formula = "=SUM(A1:A3)";

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Diferentes formas de abrir archivos](/cells/es/javascript-cpp/different-ways-to-open-files/)
- [Filtrar nombres definidos al cargar el libro de trabajo](/cells/es/javascript-cpp/filter-defined-names-while-loading-workbook/)
- [Filtrar objetos al cargar el libro de trabajo o de la hoja de cálculo](/cells/es/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtrar el tipo de datos al cargar el libro de trabajo desde un archivo de plantilla](/cells/es/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Obtener advertencias al cargar archivo de Excel](/cells/es/javascript-cpp/get-warnings-while-loading-excel-file/)
- [Cargar archivo de Excel fuente sin gráficos](/cells/es/javascript-cpp/load-source-excel-file-without-charts/)
- [Cargar hojas de cálculo específicas en un libro de trabajo](/cells/es/javascript-cpp/load-specific-worksheets-in-a-workbook/)
- [Cargar libro de trabajo con tamaño de papel de impresora especificado](/cells/es/javascript-cpp/load-workbook-with-specified-printer-paper-size/)
- [Abrir archivos de diferentes versiones de Microsoft Excel](/cells/es/javascript-cpp/opening-different-microsoft-excel-versions-files/)
- [Abriendo Archivos con Diferentes Formatos](/cells/es/javascript-cpp/opening-files-with-different-formats/)
- [Optimización del uso de memoria al trabajar con archivos grandes que contengan conjuntos de datos extensos](/cells/es/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Leer Hojas de cálculo Numbers desarrolladas por Apple Inc. usando Aspose.Cells](/cells/es/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Detener la conversión o carga utilizando InterruptMonitor cuando está tardando demasiado](/cells/es/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Usar la API LightCells](/cells/es/javascript-cpp/using-lightcells-api/)
- [Convertir CSV a JSON](/cells/es/javascript-cpp/convert-csv-to-json/)
- [Convertir Excel a JSON](/cells/es/javascript-cpp/convert-excel-to-json/)
- [Convertir JSON a CSV](/cells/es/javascript-cpp/convert-json-to-csv/)
- [Convertir JSON a Excel](/cells/es/javascript-cpp/convert-json-to-excel/)
- [Convertir Excel a Html](/cells/es/javascript-cpp/convert-excel-to-html/)
