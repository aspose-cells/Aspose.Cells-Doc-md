---
title: Fuente de tema para encabezados y cuerpo
linktitle: Fuente de tema para encabezados y cuerpo
description: Aspose.Cells es una biblioteca de JavaScript a través de C++ para trabajar con archivos de hojas de cálculo. Admite configurar las fuentes de tema de encabezado y cuerpo en documentos Excel, permitiendo a los usuarios personalizar la apariencia y el estilo del documento. Este artículo presentará cómo usar la biblioteca Aspose.Cells para trabajar con las fuentes de tema en encabezados y cuerpos en documentos Excel.
keywords: Aspose.Cells, Documento Excel, Encabezado, Cuerpo, Fuente de tema, Apariencia, Estilo, JavaScript a través de C++
type: docs
weight: 120
url: /es/javascript-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

La fuente predeterminada cambiará automáticamente cuando se modifique la configuración regional.

Si se cambia la fuente predeterminada, también se cambiará la altura de la fila y el ancho de la columna e incluso puede desconfigurar el diseño de la página.

¿Qué causó el cambio de la fuente predeterminada?

Si se establece una fuente de tema de Excel, Excel cambiará automáticamente entre fuentes diferentes según el entorno de idioma actual.

{{% /alert %}}

## **Fuente de tema para encabezados y cuerpo en Excel**

En Excel, selecciona la pestaña Inicio, haz clic en la lista desplegable de fuente, verás "Fuentes del tema" con dos fuentes del tema: Calibri Light (Encabezados) y Calibri (Cuerpo) en la parte superior con la configuración regional en inglés.

**![Fuentes del tema](Theme-Fonts.png)**

Si se selecciona Fuente del tema, el nombre de la fuente se mostrará de manera diferente en distintas regiones. Si no deseas que la fuente cambie automáticamente en diferentes regiones, no selecciones las dos Fuentes del tema.

## **Cambiar fuentes de encabezados y cuerpo de forma programática**
Con Aspose.Cells for JavaScript a través de C++, podemos verificar si la fuente predeterminada es una fuente de tema o establecer la fuente de tema con el método [**Font.schemeType**](https://reference.aspose.com/cells/javascript-cpp/font/#schemeType-fontschemetype-).

El siguiente código de ejemplo muestra cómo manipular la fuente del tema.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Theme Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontSchemeType, Utils } = AsposeCells;

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

            // Accessing and modifying the default style and its font scheme
            let defaultStyle = workbook.defaultStyle;
            let font = defaultStyle.font;
            let schemeType = font.schemeType;

            if (schemeType === FontSchemeType.Major || schemeType === FontSchemeType.Minor) {
                console.log("It's theme font");
            }

            // Change theme font to normal font
            font.schemeType = FontSchemeType.None;

            // Assign the modified default style back to the workbook
            workbook.defaultStyle = defaultStyle;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Theme font changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **Obtiene dinámicamente la fuente del tema local de forma programática**
A veces, nuestros servidores y las máquinas de los usuarios no están en la misma región. ¿Cómo podemos obtener la misma fuente que los usuarios desean para el procesamiento de archivos?

Debemos establecer la configuración regional del sistema antes de cargar el archivo con el método [**LoadOptions.region**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#region-countrycode-).

El siguiente código de muestra muestra cómo obtener la fuente del tema local.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Default Style Local Font Example</h1>
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

            // Instantiate a new LoadOptions.
            const options = new AsposeCells.LoadOptions();
            // Sets the customer's region
            options.region = AsposeCells.CountryCode.Japan;

            // Instantiate a new Workbook using the uploaded file and load options.
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Get the default style
            const defaultStyle = workbook.defaultStyle;

            // Gets customer's local font.
            const localFontName = defaultStyle.font.name;

            resultDiv.innerHTML = `<p style="color: green;">Local font name: ${localFontName}</p>`;
        });
    </script>
</html>
```
