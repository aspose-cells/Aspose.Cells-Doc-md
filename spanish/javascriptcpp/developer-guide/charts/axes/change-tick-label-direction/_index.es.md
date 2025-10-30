---
title: Cambiar la dirección de las etiquetas de marcas de graduación con JavaScript vía C++
linktitle: Cambiar la dirección de la etiqueta del eje
description: Aprende cómo cambiar la dirección de las etiquetas de marcas de graduación en Aspose.Cells for JavaScript vía C++. Nuestra guía te ayudará a entender cómo ajustar la orientación de las etiquetas en los ejes, incluyendo orientaciones horizontales, verticales y anguladas.
keywords: Aspose.Cells for JavaScript vía C++, etiquetas de marcas de graduación, dirección, orientación, ejes, horizontal, vertical, angulada.
type: docs
weight: 170
url: /es/javascript-cpp/change-tick-label-direction/
---

## **Cambiar la dirección de la etiqueta del eje**

Aspose.Cells te permite cambiar la dirección de las etiquetas de marcas en el gráfico usando la propiedad [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--). La propiedad [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) acepta el valor de enumeración [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype). La enumeración [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) proporciona los siguientes miembros:

- Horizontal
- Vertical
- Rotar 90
- Rotar 270
- Apilado

La siguiente imagen compara los archivos de origen y de salida

### **Imagen del archivo de origen**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Imagen del archivo de salida**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

El siguiente fragmento de código cambia la dirección de las etiquetas de las marcas de verificación de Rotar90 a Horizontal.

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Tick Label Direction Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartTextDirectionType } = AsposeCells;

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const chart = worksheet.charts.get(0);

            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Horizontal;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataLableDirection.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Tick label direction changed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Los archivos de origen y de salida se pueden descargar desde los siguientes enlaces.

[Archivo de origen](105480221.xlsx)

[Archivo de salida](105480223.xlsx)
