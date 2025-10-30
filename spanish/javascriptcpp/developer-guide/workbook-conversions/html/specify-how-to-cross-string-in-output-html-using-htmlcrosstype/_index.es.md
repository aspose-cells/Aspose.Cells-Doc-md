---
title: Especifica cómo cruzar cadenas en HTML de salida usando HtmlCrossType con JavaScript vía C++
linktitle: Especifique cómo cruzar cadenas en HTML de salida utilizando HtmlCrossType
type: docs
weight: 140
url: /es/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Aprende cómo controlar el desbordamiento de cadenas en la salida HTML especificando HtmlCrossType en Aspose.Cells for JavaScript vía C++.
---

## **Escenarios de uso posibles**

Cuando una celda contiene texto o cadena pero es mayor que el ancho de la celda, la cadena desborda si la siguiente celda en la siguiente columna es null o está vacía. Cuando guardas tu archivo de Excel en HTML, puedes controlar este desbordamiento especificando el tipo de cruce usando la enumeración [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). Tiene los siguientes valores:

- **HtmlCrossType.Default**: Muestra como MS Excel; depende de la siguiente celda. Si la siguiente celda es null, la cadena cruzará o será truncada.

- **HtmlCrossType.MSExport**: Muestra la cadena como exportación HTML de MS Excel.

- **HtmlCrossType.Cross**: Muestra la cadena cruzada en HTML; el rendimiento para crear archivos HTML grandes será más de diez veces más rápido que establecer el valor en Default o FitToCell.

- **HtmlCrossType.FitToCell**: Solo mostrar la cadena dentro del ancho de la celda.

## **Especifica cómo cruzar la cadena en HTML de salida utilizando HtmlCrossType**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](51740732.xlsx) y lo guarda en formato HTML especificando diferentes [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). Descargue los [HTMLs de salida](51740734.zip) generados con este código. El archivo de Excel de muestra contiene la imagen con borde de color rojo como se muestra en esta captura de pantalla que demuestra el efecto de los valores [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) en el HTML de salida.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export HTML Cross String Type Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlCrossType, Utils } = AsposeCells;

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

            // Specify HTML Cross Type via HtmlSaveOptions
            const opts = new HtmlSaveOptions();
            // Applying the sequence of assignments as in the original JavaScript code
            opts.htmlCrossStringType = HtmlCrossType.Default;
            opts.htmlCrossStringType = HtmlCrossType.MSExport;
            opts.htmlCrossStringType = HtmlCrossType.Cross;
            opts.htmlCrossStringType = HtmlCrossType.FitToCell;

            // Save workbook to HTML using the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            const fileName = 'out' + opts.htmlCrossStringType + '.htm';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = fileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
