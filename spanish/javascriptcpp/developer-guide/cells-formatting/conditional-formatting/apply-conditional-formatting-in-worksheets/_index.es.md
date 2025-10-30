---
title: Aplicar formato condicional en hojas de cálculo
linktitle: Aplicar formato condicional en hojas de cálculo
description: Cómo usar la biblioteca Aspose.Cells en JavaScript vía C++ para aplicar formato condicional en hojas de cálculo y tener mejor control sobre la apariencia de las celdas.
keywords: Aspose.Cells, Formato condicional, JavaScript vía C++, Hoja de cálculo, Formateo
type: docs
weight: 130
url: /es/javascript-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Este artículo está diseñado para proporcionar una comprensión detallada de cómo agregar formato condicional a un rango de celdas en una hoja de cálculo.

El formato condicional es una función avanzada en Microsoft Excel que le permite aplicar formatos a un rango de celdas, y tener ese formato cambie dependiendo del valor de la celda o el valor de una fórmula. Por ejemplo, el fondo de una celda puede ser rojo para resaltar un valor negativo, o el color del texto podría ser verde para un valor positivo. Cuando el valor de la celda cumple con la condición del formato, se aplica el formato. Si el valor de la celda no cumple con la condición de formato, se utiliza el formato predeterminado de la celda.

Es posible aplicar formato condicional con la Automatización de Office de Microsoft, pero eso tiene sus desventajas. Hay varias razones y problemas involucrados, como la seguridad, la estabilidad, la escalabilidad y la velocidad. La razón principal para encontrar otra solución es que Microsoft en sí mismo recomienda fuertemente en contra de la Automatización de Office para soluciones de software.

Este artículo muestra cómo crear una aplicación web, agregar formato condicional en celdas con unas pocas líneas de código usando la API de Aspose.Cells.

{{% /alert %}}

## **Usar Aspose.Cells para Aplicar Formato Condicional Basado en el Valor de la Celda**

1. **Descargar e Instalar Aspose.Cells**.
   1. Descargar Script Aspose.Cells for Java mediante C++.
1. Instálelo en su equipo de desarrollo.
   Todos los componentes de Aspose, al instalarse, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.
1. **Crear un proyecto**.
   Inicia tu proyecto en JavaScript inicializándolo. Este ejemplo demuestra su uso en una aplicación web basada en navegador.
1. **Agregar referencias**.
   Agrega una referencia a Aspose.Cells en tu proyecto, por ejemplo incluyendo la biblioteca de la siguiente forma:
   ```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Conditional Formatting Example</title>
    </head>
    <body>
        <h1>Apply Conditional Formatting Based on Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FormatConditionType, OperatorType, CellArea, Color } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add conditional formatting collection
            const cfCollection = worksheet.conditionalFormattings;
            const idx = cfCollection.add();
            const formatConditionCollection = cfCollection.get(idx);

            // Define the cell area to apply conditional formatting (A1)
            const area = CellArea.createCellArea(0, 0, 0, 0); // fromRow, fromCol, toRow, toCol
            formatConditionCollection.addArea(area);

            // Add a condition: Cell Value > 100
            const conditionIndex = formatConditionCollection.addCondition(
                FormatConditionType.CellValue,
                OperatorType.Greater,
                "100",
                null
            );

            const formatCondition = formatConditionCollection.get(conditionIndex);

            // Modify the style for the condition: bold and red font
            const style = formatCondition.style;
            if (!style.font) {
                style.font = {};
            }
            style.font.bold = true;
            style.font.color = Color.fromArgb(255, 255, 0, 0); // ARGB red

            // Assign modified style back (property assignment pattern)
            formatCondition.style = style;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'conditional_formatting_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied to cell A1 (value &gt; 100). Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda "A1" en la primera hoja del archivo de salida (output.xls). El formato condicional aplicado a A1 depende del valor de la celda. Si el valor de A1 está entre 50 y 100, el color de fondo será rojo debido al formato condicional aplicado.

## **Usar Aspose.Cells para Aplicar Formato Condicional Basado en Fórmula**

1. Aplicando formato condicional dependiendo de la fórmula (Fragmento de código)
   A continuación se muestra el código para lograr la tarea. Aplica formato condicional en B3.
