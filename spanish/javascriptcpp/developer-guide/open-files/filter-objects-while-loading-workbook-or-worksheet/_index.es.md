---
title: Filtrar objetos al cargar libro de trabajo o hoja de cálculo con JavaScript a través de C++
linktitle: Filtrar objetos al cargar el libro o la hoja de trabajo
type: docs
weight: 330
url: /es/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Aprende cómo filtrar datos al cargar libros de trabajo o hojas de cálculo usando Aspose.Cells for JavaScript a través de C++.
---

## **Escenarios de uso posibles**
Utilice la propiedad [LoadOptions.loadFilter](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) para filtrar datos del libro de trabajo. Pero si desea filtrar datos de hojas de cálculo individuales, deberá anular el método [LoadFilter.startSheet(Worksheet)](https://reference.aspose.com/cells/javascript-cpp/loadfilter/#startSheet-worksheet-). Proporcione un valor apropiado del enumerador [LoadDataFilterOptions](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions) al crear o trabajar con [LoadFilter](https://reference.aspose.com/cells/javascript-cpp/loadfilter).

El enumerador [LoadDataFilterOptions](https://reference.aspose.com/cells/javascript-cpp/loaddatafilteroptions) tiene los siguientes valores posibles.

- Todo
- Configuraciones del libro
- Celda en blanco
- Celda booleana
- Datos de celda
- Error de celda
- Numérico de celda
- Cadena de celda
- Valor de celda
- Chart
- Formato condicional
- Validación de datos
- Nombres definidos
- Propiedades del documento
- Fórmula
- Hipervínculos
- Área fusionada
- Tabla Dinámica
- Configuración
- Forma
- Datos de Hoja
- Configuraciones de Hoja
- Estructura
- Estilo
- Tabla
- VBA
- MapaXml

## **Objetos de Filtro al cargar el Libro**
El siguiente código de ejemplo ilustra cómo filtrar gráficos del libro. Por favor, revise el [archivo de Excel de ejemplo](5115258.xlsx) utilizado en este código y el [PDF de salida](5115257.pdf) generado por él. Como se puede ver en el PDF de salida, todos los gráficos han sido filtrados fuera del libro.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter Charts and Save to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFilter, LoadDataFilterOptions, PdfSaveOptions } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options and filter out charts
            const lOptions = new LoadOptions();
            lOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.Chart);

            // Load the workbook with the above filter
            const workbook = new Workbook(new Uint8Array(arrayBuffer), lOptions);

            // Create PDF save options and set one page per sheet
            const pOptions = new PdfSaveOptions();
            pOptions.onePagePerSheet = true;

            // Save the workbook in PDF format
            const outputData = workbook.save(SaveFormat.Pdf, pOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });

            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sampleFilterCharts.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook saved to PDF (charts filtered out). Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

## **Objetos de Filtro al cargar la Hoja de Trabajo**
El siguiente código de ejemplo carga el [archivo de Excel fuente](5115255.xlsx) y filtra los siguientes datos de sus hojas de trabajo usando un filtro personalizado.

- Filtra los gráficos de la hoja de trabajo llamada SinGráficos.
- Filtra las formas de la hoja de trabajo llamada SinFormas.
- Filtra el formato condicional de la hoja de trabajo llamada SinFormatoCondicional.

Una vez que carga el [archivo de Excel fuente](5115255.xlsx) con un filtro personalizado, toma las imágenes de todas las hojas una por una. Aquí están las imágenes de salida para su referencia. Como se puede ver, la primera imagen no tiene gráficos, la segunda imagen no tiene formas y la tercera imagen no tiene formato condicional.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Custom Load Filter Example</title>
    </head>
    <body>
        <h1>Custom Load Filter Example</h1>
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

        // Converted CustomLoadFilter class
        class CustomLoadFilter extends AsposeCells.LoadFilter {
            startSheet(sheet) {
                if (sheet.name === "NoCharts") {
                    // Load everything and filter charts
                    this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart;
                }

                if (sheet.name === "NoShapes") {
                    // Load everything and filter shapes
                    this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Drawing;
                }

                if (sheet.name === "NoConditionalFormatting") {
                    // Load everything and filter conditional formatting
                    this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.ConditionalFormatting;
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate and (optionally) attach the custom load filter
            const customFilter = new CustomLoadFilter();
            // If the environment supports assigning a load filter to workbook, set it as a property
            workbook.loadFilter = customFilter;

            // Inform user that the filter class was created and assigned
            document.getElementById('result').innerHTML = '<p style="color: green;">CustomLoadFilter created and assigned to workbook. You can download the (possibly unchanged) workbook below.</p>';

            // Save the workbook back to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

Así es como se usa la clase CustomLoadFilter según los nombres de las hojas de cálculo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadList a { display: block; margin: 6px 0; }
            #result p { margin: 8px 0; }
        </style>
    </head>
    <body>
        <h1>Render Worksheets to PNG with Custom Load Filter</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div id="result"></div>
        <div id="downloadList"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, ImageOrPrintOptions, SheetRender, ImageType } = AsposeCells;

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

        // Define CustomLoadFilter class (placeholder - adapt as needed)
        // The original JavaScript code referenced a CustomLoadFilter implementation.
        // This minimal implementation can be replaced with actual filtering logic.
        class CustomLoadFilter {
            constructor() {
            }
            // If the AsposeCells runtime expects specific methods on the filter,
            // implement them here. This is a generic placeholder.
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            const downloadList = document.getElementById('downloadList');
            downloadList.innerHTML = '';
            resultDiv.innerHTML = '';

            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Prepare load options and assign custom load filter
            const loadOpts = new LoadOptions();
            loadOpts.loadFilter = new CustomLoadFilter();

            // Instantiate workbook from uploaded file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOpts);

            // Iterate through worksheets and render each to PNG
            const sheetCount = workbook.worksheets.count;
            for (let i = 0; i < sheetCount; i++) {
                const worksheet = workbook.worksheets.get(i);

                // Create image options
                const imageOpts = new ImageOrPrintOptions();
                imageOpts.onePagePerSheet = true;
                imageOpts.imageType = ImageType.Png;

                // Render worksheet to image bytes
                const render = new SheetRender(worksheet, imageOpts);
                const imgBytes = render.toImage(0);

                // Create blob and download link for each rendered image
                const blob = new Blob([imgBytes], { type: 'image/png' });
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                const sheetNameSafe = worksheet.name ? worksheet.name.replace(/[\/\\:?*"<>|]/g, '_') : `sheet${i+1}`;
                link.href = url;
                link.download = `outputCustomFilteringPerWorksheet_${sheetNameSafe}.png`;
                link.textContent = `Download ${link.download}`;
                downloadList.appendChild(link);
            }

            resultDiv.innerHTML = `<p style="color: green;">Rendered ${sheetCount} worksheet(s). Download links are available below.</p>`;
        });
    </script>
</html>
```
