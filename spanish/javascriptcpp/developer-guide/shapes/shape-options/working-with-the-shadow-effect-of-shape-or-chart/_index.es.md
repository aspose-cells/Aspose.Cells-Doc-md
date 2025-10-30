---
title: Trabajando con el efecto de sombra de Forma o Gráfico con JavaScript a través de C++
linktitle: Trabajando con el Efecto de Sombra de Forma o Gráfico
type: docs
weight: 220
url: /es/javascript-cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Aprende a trabajar con el efecto de sombra de formas o gráficos usando Aspose.Cells for JavaScript a través de C++.
---

## **Escenarios de uso posibles**  
Aspose.Cells for JavaScript a través de C++ proporciona la propiedad [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) junto con la clase [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) para trabajar con el efecto de sombra de forma o gráfico. La clase [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) contiene las siguientes propiedades que se pueden establecer para lograr diferentes resultados según los requisitos de la aplicación.  

- [ShadowEffect.ángulo](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#angle--)  
- [ShadowEffect.desenfoque](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#blur--)  
- [ShadowEffect.color](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#color--)  
- [ShadowEffect.distancia](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#distance--)  
- [ShadowEffect.tipoPredefinido](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--)  
- [ShadowEffect.tamaño](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#size--)  
- [Transparencia del Efecto de Sombra](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#transparency--)  

## **Trabajar con el Efecto de Sombra de la Forma o Gráfico**  
El siguiente código de ejemplo carga el [archivo de Excel fuente](5115425.xlsx) y accede a la primera forma en la primera hoja de trabajo y establece las subpropiedades de la propiedad [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) y luego guarda el libro en el [archivo de Excel de salida](5115411.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Shape Shadow Effect Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            const shadowEffect = shape.shadowEffect;
            shadowEffect.angle = 150;
            shadowEffect.blur = 4;
            shadowEffect.distance = 45;
            shadowEffect.transparency = 0.3;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shadow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
