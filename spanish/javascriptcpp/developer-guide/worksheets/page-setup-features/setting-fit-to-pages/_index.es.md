---
title: Cómo imprimir Excel a páginas ajustadas en ancho y alto con JavaScript mediante C++
linktitle: Cómo imprimir Excel como páginas ajustadas en ancho y alto
type: docs
weight: 200
url: /es/javascript-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Este artículo muestra código que explica cómo configurar FitToPagesWide y FitToPagesTall usando Aspose.Cells for JavaScript mediante C++.
keywords: JavaScript mediante C++ Cómo establecer FitToPagesWide y FitToPagesTall, Cómo agregar FitToPagesWide y FitToPagesTall en JavaScript, Cómo establecer FitToPagesWide y FitToPagesTall en Excel, Cómo limpiar FitToPagesWide y FitToPagesTall en Excel, Cómo imprimir Excel en páginas ajustadas en ancho y alto, Cómo imprimir hoja en una página, Cómo imprimir todas las columnas de la hoja en una sola página.
---

## **Introducción**

Las configuraciones FitToPagesWide y FitToPagesTall se usan en aplicaciones de hojas de cálculo (como Microsoft Excel) para controlar cómo se escala una hoja de cálculo al imprimir. Estas configuraciones ayudan a garantizar que tu salida impresa quepa dentro de un número específico de páginas, tanto en horizontal como en vertical. Aquí hay una descripción de cada configuración:

1. FitToPagesWide: Esta configuración especifica el número de páginas de ancho en las que la salida impresa debe ajustarse. Por ejemplo, establecer FitToPagesWide en 1 significa que el contenido se escalará para ajustarse dentro de una sola anchura de página, sin importar cuán ancha sea la hoja de cálculo.
2. FitToPagesTall: Esta configuración especifica el número de páginas de alto en las que la salida impresa debe ajustarse. Por ejemplo, configurar FitToPagesTall en 1 significa que el contenido se escalará para caber dentro de una sola página de altura, sin importar el número de filas.

## **Por qué usar FitToPagesWide y FitToPagesTall**
Aquí hay algunas razones para configurar FitToPagesWide y FitToPagesTall:
1. Control sobre el diseño impreso: Al especificar el número de páginas de ancho y alto, puedes asegurarte de que tu documento impreso sea fácil de leer y esté bien organizado, sin que columnas o filas se dividan de manera incómoda en las páginas.
2. Consistencia: Si imprimes varias hojas o informes, usar estas configuraciones ayuda a mantener un formato consistente, facilitando la comparación y análisis de los documentos impresos.
3. Presentación profesional: Escalar y ajustar correctamente el contenido a un número específico de páginas puede dar lugar a una presentación más profesional y pulida de tus datos.

## **Cómo imprimir un archivo como páginas ajustadas en ancho y alto en Excel**

Para configurar FitToPagesWide y FitToPagesTall en Microsoft Excel, sigue estos pasos:

1. Abre tu libro de Excel y ve a la hoja que deseas imprimir.
2. Ve a la pestaña Diseño de página en la Cinta de opciones.
3. En el grupo Configuración de página, haz clic en la pequeña flecha en la esquina inferior derecha para abrir el cuadro de diálogo Configuración de página.
4. En el cuadro de diálogo Configuración de página, ve a la pestaña Página.
5. En Escalado, selecciona la opción "Ajustar a" y luego especifica el número de páginas de ancho y alto que deseas: Ingresa el número de páginas de ancho en la primera casilla (Ajustar a x páginas de ancho). Ingresa el número de páginas de alto en la segunda casilla (Ajustar a y páginas de alto).
<br>
<img src="2.png" width=60% />

6. Haz clic en Aceptar para aplicar la configuración.

## **Cómo imprimir Excel en páginas ajustadas en ancho y alto usando Aspose.Cells for JavaScript mediante C++**

Para establecer FitToPagesWide y FitToPagesTall en una hoja de cálculo especificada: primero, carga el [archivo ejemplo](input.xlsx), y luego necesitas modificar las propiedades [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) y [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--) del objeto [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) para la hoja deseada. Aquí tienes un ejemplo en JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Worksheet Fit To Pages and Save as PDF</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the number of pages to which the length of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesWide = 1;

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_net.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

El resultado de la salida:
<br>
<img src="1.png" width=60% />

## **Cómo imprimir una hoja de cálculo como una página usando Aspose.Cells for JavaScript mediante C++**

Para imprimir la hoja como una página: primero, carga el [archivo ejemplo](sample.xlsx), y luego debes establecer la propiedad [**PdfSaveOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) del objeto [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/). Aquí tienes un ejemplo en JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>One Page Per Sheet to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the workbook to PDF format and provide download link
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

El resultado de la salida:
<br>
<img src="3.png" width=60% />

## **Cómo imprimir todas las columnas de la hoja de cálculo en una sola página usando Aspose.Cells for JavaScript vía C++**

Para imprimir todas las columnas de la hoja de cálculo en una página: Primero, carga el [archivo de ejemplo](sample.xlsx), y luego necesitas establecer la propiedad [**PdfSaveOptions.allColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#allColumnsInOnePagePerSheet--) del objeto [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/). Aquí tienes un ejemplo en JavaScript:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>All Columns In One Page Per Sheet Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and set allColumnsInOnePagePerSheet property
            const options = new AsposeCells.PdfSaveOptions();
            options.allColumnsInOnePagePerSheet = true;

            // Save the workbook to PDF format with the options
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AllColumnsInOnePagePerSheet.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

El resultado de la salida:
<br>
<img src="4.png" width=60% />
