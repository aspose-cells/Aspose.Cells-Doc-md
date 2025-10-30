---
title: Leer archivo CSV con múltiples codificaciones usando JavaScript vía C++
linktitle: Lectura de archivo CSV con múltiples codificaciones
type: docs
weight: 200
url: /es/javascript-cpp/reading-csv-file-with-multiple-encodings/
description: Aprende cómo leer archivos CSV con múltiples codificaciones usando Aspose.Cells for JavaScript vía C++.
---

{{% alert color="primary" %}}

A veces, tu archivo CSV contiene múltiples codificaciones (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells te permite cargar dichos archivos CSV y convertirlos a otros formatos, por ejemplo, PDF o XLSX.

{{% /alert %}}

Aspose.Cells proporciona la propiedad [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--), que debe configurarse en **true** para cargar correctamente su archivo CSV con múltiples codificaciones.

La siguiente captura de pantalla muestra un archivo CSV de muestra que contiene dos líneas. La primera línea está en codificación **ANSI** y la segunda línea está en codificación **Unicode**.

|**Archivo de entrada**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

 La siguiente captura de pantalla muestra el archivo XLSX convertido desde el CSV anterior sin configurar la propiedad [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) en **true**. Como puede ver, el texto Unicode no se convirtió correctamente.

|**Archivo de salida 1: no se hizo ningún ajuste para la codificación múltiple**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

La siguiente captura de pantalla muestra el archivo XSLX convertido del CSV anterior después de configurar la propiedad [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) en **true**. Como puedes ver, el texto Unicode ahora se convierte correctamente.

|**Archivo de salida 2: IsMultiEncoded se establece en true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

A continuación se muestra el código de ejemplo que convierte el archivo CSV anterior en formato XLSX adecuadamente.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Multi-Encoded CSV to XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Convert to XLSX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create TxtLoadOptions and set isMultiEncoded property
            const options = new TxtLoadOptions();
            options.isMultiEncoded = true;

            // Load the CSV into a Workbook using the options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const outName = file.name.replace(/(\.[^/.]+)$/, '$1.out.xlsx');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = outName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to save the XLSX file.</p>';
        });
    </script>
</html>
```

## Artículos relacionados

- [Abriendo Archivos CSV](/cells/es/javascript-cpp/opening-files-with-different-formats/#opening-csv-files)
