---
title: Trabajando con el formato ThreeDFormat de Shape o Chart con JavaScript a través de C++
linktitle: Trabajar con el Formato ThreeD de la Forma o Gráfico
type: docs
weight: 250
url: /es/javascript-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **Escenarios de uso posibles**
Aspose.Cells for JavaScript a través de C++ proporciona la propiedad [Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--) junto con la clase [ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat) para trabajar con el formato 3D de la forma o gráfico. La clase [ThreeDFormat](https://reference.aspose.com/cells/javascript-cpp/threedformat) contiene diferentes propiedades que se pueden establecer para lograr diferentes resultados según los requisitos de la aplicación.

## **Trabajar con el Formato ThreeD de la Forma o Gráfico**
El siguiente código de ejemplo carga el [archivo de Excel fuente](5115419.xlsx) y accede a la primera forma en la primera hoja de trabajo y establece las subpropiedades de [Shape.threeDFormat](https://reference.aspose.com/cells/javascript-cpp/shape/#threeDFormat--) y luego guarda el libro en el [archivo de Excel de salida](5115410.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Apply 3D Format Example</title>
    </head>
    <body>
        <h1>Apply 3D Format to Shape</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const ws = workbook.worksheets.get(0);

            const sh = ws.shapes.get(0);

            const n3df = sh.threeDFormat;
            n3df.contourWidth = 17;
            n3df.extrusionHeight = 32;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">3D formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
