---
title: Obtener Encabezados o Pies de Página con JavaScript a través de C++
linktitle: Obteniendo Encabezados o Pies de Página
type: docs
weight: 30
url: /es/javascript-cpp/get-headers-or-footers/
description: Este artículo explica cómo obtener programáticamente encabezados y pies de página de archivos Excel o OpenOffice usando la API JavaScript a través de C++.
---

{{% alert color="primary" %}}

Los encabezados y pies de página se muestran solo en la vista Diseño de página, en la vista previa de impresión y en las páginas impresas. 

También puedes usar el cuadro de diálogo Configurar página si deseas ver encabezados o pies de página para más de una hoja de cálculo a la vez. 

Para otros tipos de hojas, como hojas de gráficos o gráficos, solo puedes insertar encabezados y pies de página mediante el cuadro de diálogo Configurar página.

{{% /alert %}}

## **Obteniendo Encabezados y Pies de Página en MS Excel**
1. Haz clic en la hoja de cálculo donde deseas ver o cambiar los encabezados o pies de página.
2. En la pestaña Vista, en el grupo Vistas del libro, haga clic en Diseño de página.
   Excel muestra la hoja de cálculo en la vista Diseño de página.
3. Para ver o editar un encabezado o pie de página, haz clic en el cuadro de texto de encabezado o pie de página izquierdo, central o derecho en la parte superior o inferior de la página de la hoja de cálculo (debajo de Encabezado, o encima de Pie de página).


## **Obteniendo Encabezados y Pies de Página usando Aspose.Cells for JavaScript a través de C++**
Con los métodos [**PageSetup.header(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-) y [**PageSetup.footer(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-), los desarrolladores de JavaScript pueden simplemente obtener encabezados o pies de página del archivo.

1. Construya un libro de trabajo para abrir el archivo.
2. Obtenga la hoja de cálculo donde desea obtener encabezados o pies de página.
3. Obtenga el encabezado o pie de página con un ID de sección específico.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Header/Footer Reader Example</h1>
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

        function escapeHtml(str) {
            if (str === null || str === undefined) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerLeft = sheet.pageSetup.header(0);
            // Gets center section of header
            const headerCenter = sheet.pageSetup.header(1);
            // Gets right section of header
            const headerRight = sheet.pageSetup.header(2);
            // Gets center section of footer
            const footerCenter = sheet.pageSetup.footer(1);

            const resultHtml = [
                `<p><strong>Left Header:</strong> ${escapeHtml(headerLeft)}</p>`,
                `<p><strong>Center Header:</strong> ${escapeHtml(headerCenter)}</p>`,
                `<p><strong>Right Header:</strong> ${escapeHtml(headerRight)}</p>`,
                `<p><strong>Center Footer:</strong> ${escapeHtml(footerCenter)}</p>`
            ].join('');

            document.getElementById('result').innerHTML = resultHtml;
        });
    </script>
</html>
```

## **Analizar Encabezados y Pies de Página para Lista de Comandos**
El texto del encabezado o pie de página puede contener comandos especiales, por ejemplo, un marcador de posición para el número de página, fecha actual o atributos de formato de texto.

Los comandos especiales están representados por una sola letra con un símbolo ampersand inicial ("&").

Las cadenas de encabezado y pie de página se construyen usando la gramática ABNF. No es fácil de entender sin un visor.

Aspose.Cells for JavaScript a través de C++ proporciona el método [**PageSetup.commands(string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#commands-string-) para analizar encabezados y pies de página como una lista de comandos.

El siguiente código muestra cómo analizar el encabezado o pie de página como una lista de comandos y procesar los comandos:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Header/Footer Commands Example</title>
    </head>
    <body>
        <h1>Header/Footer Commands Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerSection = sheet.pageSetup.header(0);
            const commands = sheet.pageSetup.commands(headerSection) || [];

            const items = [];
            commands.forEach(c => {
                const type = c.type;
                switch (type) {
                    case AsposeCells.HeaderFooterCommandType.SheetName:
                        // embedded the name of the sheet to header or footer
                        items.push('<li>SheetName command found (embeds sheet name)</li>');
                        break;
                    default:
                        items.push(`<li>Command type: ${type}</li>`);
                        break;
                }
            });

            if (!items.length) {
                items.push('<li>No header/footer commands found.</li>');
            }

            resultDiv.innerHTML = `<ul>${items.join('')}</ul>`;

            // Save the (possibly unchanged) workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HeaderFooter_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Workbook';
        });
    </script>
</html>
```
