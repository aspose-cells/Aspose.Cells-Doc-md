---
title: Trabajar con el efecto de reflexión de una forma o gráfico con JavaScript a través de C++
linktitle: Trabajando con el Efecto de Reflexión de Forma o Gráfico
type: docs
weight: 210
url: /es/javascript-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Aprende a trabajar con el efecto de reflexión de formas o gráficos usando Aspose.Cells for JavaScript a través de C++. Establece varias propiedades de reflexión para lograr los resultados deseados.
---

## **Escenarios de uso posibles**
Aspose.Cells for JavaScript a través de C++ proporciona la propiedad [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) junto con la clase [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) para trabajar con el efecto de reflexión de forma o gráfico. La clase [ReflectionEffect](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect) contiene las siguientes propiedades que se pueden establecer para lograr diferentes resultados según los requisitos de la aplicación.

- [Reflexión.Efecto.desenfoque](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#blur--)
- [Reflexión.Efecto.dirección](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#direction--)
- [Reflexión.Efecto.distancia](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#distance--)
- [Reflexión.Efecto.direcciónFade](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#fadeDirection--)
- [Reflexión.Efecto.rotConForma](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#rotWithShape--)
- [Reflexión.Efecto.tamaño](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#size--)
- [Reflexión.Efecto.transparencia](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#transparency--)
- [Reflexión.Efecto.tipo](https://reference.aspose.com/cells/javascript-cpp/reflectioneffect/#type--)

## **Trabajando con el Efecto de Reflexión de Forma o Gráfico**
El siguiente código de ejemplo carga el [archivo fuente de Excel](5115424.xlsx) y accede a la primera forma en la hoja predeterminada. Establece diferentes propiedades de [Shape.reflection](https://reference.aspose.com/cells/javascript-cpp/shape/#reflection--) y luego guarda el libro en el [archivo Excel de salida](5115423.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Shape Reflection Effect Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
            const reflectionEffect = shape.reflection;
            reflectionEffect.blur = 30;
            reflectionEffect.size = 90;
            reflectionEffect.transparency = 0;
            reflectionEffect.distance = 80;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Reflection effect updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
