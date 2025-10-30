---
title: Leer subtítulo del gráfico desde archivo ODS usando JavaScript vía C++
linktitle: Leer subtítulo de gráfico de archivo ODS
description: Aprende a usar Aspose.Cells for JavaScript vía C++ para leer el subtítulo del gráfico desde un archivo de hoja de cálculo OpenDocument (ODS). Nuestra guía demostrará cómo extraer y acceder al subtítulo de un gráfico para su análisis o visualización adicional.
keywords: Aspose.Cells for JavaScript vía C++, Leer subtítulo del gráfico, Archivo de hoja de cálculo OpenDocument, Archivo ODS, Extracción de gráficos, Análisis de datos.
type: docs
weight: 160
url: /es/javascript-cpp/read-chart-subtitle-from-ods-file/
---

## **Leer subtítulo del gráfico desde un archivo ODS**

Aspose.Cells te proporciona la capacidad de leer subtítulos de gráficos en archivos ODS usando la propiedad [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--). El siguiente código de ejemplo carga el archivo [ejemplo ODS](89620481.ods) y lee el subtítulo del gráfico usando la propiedad [**Chart.subTitle**](https://reference.aspose.com/cells/javascript-cpp/chart/#subTitle--) y lo imprime en la ventana de la consola. Por favor, consulta la salida de la consola del código a continuación como referencia.

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Chart Subtitle</title>
    </head>
    <body>
        <h1>Get Chart Subtitle Example</h1>
        <input type="file" id="fileInput" accept=".ods,.xls,.xlsx,.csv" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel or ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first chart inside the worksheet
            const chart = worksheet.charts.get(0);

            // Accessing chart subtitle text (converted from getSubTitle().getText())
            const subtitleText = chart.subTitle.text;

            console.log("Chart Subtitle: " + subtitleText);
            document.getElementById('result').innerHTML = '<p>Chart Subtitle: ' + (subtitleText ?? '') + '</p>';
        });
    </script>
</html>
```

## **Salida de la consola**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
