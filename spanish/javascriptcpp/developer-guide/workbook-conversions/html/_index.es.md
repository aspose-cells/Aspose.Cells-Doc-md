---
title: HTML con JavaScript a través de C++
linktitle: HTML
type: docs
weight: 230
url: /es/javascript-cpp/convert-excel-to-html/
---

## **Convirtiendo Libro de Excel a HTML**
La API de Aspose.Cells ofrece soporte para exportar hojas de cálculo a formato HTML. Para esto, Aspose.Cells usa la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions) para ofrecer flexibilidad en el control de varios aspectos del HTML de salida.

 El ejemplo de código a continuación muestra cómo guardar un libro de trabajo como un archivo HTML usando JavaScript a través de C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```


## **Convirtiendo Libro de Excel a Archivos MHTML**
MHTML combina HTML normal con recursos externos (es decir, contenido que normalmente está enlazado, como imágenes, animaciones, audio, etc.) en un solo archivo. Se usan para correos electrónicos con extensión de archivo .mht. Aspose.Cells soporta la lectura y escritura de archivos MHTML.

 El ejemplo de código a continuación muestra cómo guardar un libro de trabajo como un archivo MHTML usando JavaScript a través de C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Save as MHT</title>
    </head>
    <body>
        <h1>Save Excel as MHT Example</h1>
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

            // Load your source workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save file to MHT format
            const outputData = workbook.save(SaveFormat.MHtml);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.mht';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download MHT File';

            resultDiv.innerHTML = '<p style="color: green;">File converted to MHT successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Ajustar automáticamente columnas y filas al cargar HTML en el libro de trabajo](/cells/es/javascript-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Evita la notación exponencial de números grandes al importar desde HTML](/cells/es/javascript-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Cambiar el tipo de destino del enlace HTML](/cells/es/javascript-cpp/change-the-html-link-target-type/)
- [Convertir Excel a HTML con tooltip](/cells/es/javascript-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/es/javascript-cpp/create-transparent-image-of-excel-worksheet/)
- [Eliminar espacios redundantes después de salto de línea al importar HTML](/cells/es/javascript-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Desactivar Comentarios Revelados de Niveles Inferiores al guardar en HTML](/cells/es/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Deshabilitar la exportación de scripts de marco y propiedades del documento](/cells/es/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel a HTML - Utilice la opción PresentationPreference para un mejor diseño](/cells/es/javascript-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Excluir estilos no utilizados durante la conversión de Excel a HTML](/cells/es/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Expandir texto de derecha a izquierda al exportar archivo Excel a HTML](/cells/es/javascript-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Exportar Formato Condicional DataBar, ColorScale e IconSet al convertir Excel a HTML](/cells/es/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Exportar comentarios al guardar archivo de Excel como HTML](/cells/es/javascript-cpp/export-comments-while-saving-excel-file-to/)
- [Exportar propiedades del libro y la hoja de cálculo del documento en la conversión de Excel a HTML](/cells/es/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Exportar Excel a HTML con Líneas de Cuadrícula](/cells/es/javascript-cpp/export-excel-to-html-with-gridlines/)
- [Exportar rango del área de impresión a HTML](/cells/es/javascript-cpp/export-print-area-range-to/)
- [Exportar un estilo de borde similar cuando el estilo de borde no es soportado por los navegadores web](/cells/es/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Exportar la hoja de estilos CSS por separado en el HTML de salida](/cells/es/javascript-cpp/export-worksheet-css-separately-in-output/)
- [Ocultar Contenido Superpuesto con CrossHideRight al guardar en HTML](/cells/es/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Prefijo de estilos de elementos de tabla con la propiedad HtmlSaveOptions.TableCssId](/cells/es/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Evitar la exportación del contenido oculto de la hoja de cálculo al guardar en HTML](/cells/es/javascript-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Proporcionar la ruta del archivo HTML de la hoja de cálculo exportada a través de la interfaz IFilePathProvider](/cells/es/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Reconocer etiquetas auto-cierre](/cells/es/javascript-cpp/recognise-self-closing-tags/)
- [Renderizar relleno de degradado para WordArt al convertir hojas de cálculo a HTML](/cells/es/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Establecer el ancho de la columna a una unidad escalable como em o porcentaje](/cells/es/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Establecer fuente predeterminada al renderizar la hoja de cálculo a HTML](/cells/es/javascript-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Especifica cómo cruzar la cadena en HTML de salida utilizando HtmlCrossType](/cells/es/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Soportar el diseño de etiquetas DIV al cargar HTML en un libro de Excel](/cells/es/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Habilitar Propiedades Personalizadas de CSS al guardar en HTML](/cells/es/javascript-cpp/enable-css-custom-properties-while-saving-to-html/)
