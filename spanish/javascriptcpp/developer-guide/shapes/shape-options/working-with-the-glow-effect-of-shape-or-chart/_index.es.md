---
title: Trabajando con el efecto de resplandor de forma o gráfico con JavaScript a través de C++
linktitle: Trabajar con el efecto de resplandor de la forma o el gráfico
type: docs
weight: 240
url: /es/javascript-cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Aprende cómo trabajar con el efecto de resplandor en formas o gráficos en JavaScript usando Aspose.Cells for JavaScript a través de C++.
---

## **Escenarios de uso posibles**  
Aspose.Cells proporciona la propiedad [Shape.glow](https://reference.aspose.com/cells/javascript-cpp/shape/#glow--) junto con la clase [GlowEffect](https://reference.aspose.com/cells/javascript-cpp/gloweffect/) para trabajar con el efecto de resplandor de la forma o gráfico. La clase [GlowEffect](https://reference.aspose.com/cells/javascript-cpp/gloweffect/) contiene las siguientes propiedades que pueden establecerse para lograr diferentes resultados según los requisitos de la aplicación.  

- [GlowEffect.size](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#size--)  
- [GlowEffect.transparency](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#transparency--)  
- [GlowEffect.color](https://reference.aspose.com/cells/javascript-cpp/gloweffect/#color--)  

## **Trabajando con el Efecto de Resplandor de Forma o Gráfico**  
El siguiente código de ejemplo carga el [archivo de Excel de origen](5115407.xlsx) y accede a la primera forma en la primera hoja, establece las subpropiedades de la propiedad [Shape.glow](https://reference.aspose.com/cells/javascript-cpp/shape/#glow--) y luego guarda el libro en el [archivo de Excel de salida](5115414.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Glow Effect</title>
    </head>
    <body>
        <h1>Apply Glow Effect to First Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Apply Glow Effect</button>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first shape
            const shape = worksheet.shapes.get(0);

            // Set the glow effect of the shape, Set its Size and Transparency properties
            const glowEffect = shape.glow;
            glowEffect.size = 30;
            glowEffect.transparency = 0.4;

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Glow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
