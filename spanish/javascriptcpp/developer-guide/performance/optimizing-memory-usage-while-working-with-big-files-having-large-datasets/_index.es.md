---
title: Optimización del uso de memoria al trabajar con archivos grandes que contienen conjuntos de datos extensos
type: docs
weight: 110
url: /es/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Cuando se construye un libro con grandes conjuntos de datos o se lee un archivo grande de Microsoft Excel, la cantidad total de RAM que utilizará el proceso siempre es una preocupación. Existen medidas que se pueden adaptar para enfrentar el desafío. Aspose.Cells proporciona algunas opciones y llamadas de API relevantes para reducir y optimizar el uso de memoria, lo que puede ayudar al proceso a trabajar de manera más eficiente y rápida.

Utilice la opción [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) para optimizar el uso de memoria para los datos de las celdas y así disminuir el costo total de memoria. Al construir un conjunto de datos grande para las celdas, puede ahorrar una cierta cantidad de memoria en comparación con el uso de la configuración predeterminada [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).

{{% /alert %}}

## **Optimización de memoria**

El siguiente ejemplo muestra cómo optimizar el uso de memoria mientras trabajas con grandes datos en Aspose.Cells for JavaScript a través de C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Optimize Memory Usage Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MemorySetting } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file or leave empty to create a new one.</p>';
                // Allow creating a new workbook even if no file selected; return only if user explicitly requires file.
            }

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // apply the setting to existing "Sheet1"
            workbook.worksheets.get(0).cells.memorySetting = MemorySetting.MemoryPreference;

            // apply the setting globally
            workbook.settings.memorySetting = MemorySetting.MemoryPreference;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Memory settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Precaución**

La opción predeterminada, [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) se aplica a todas las versiones. Para algunas situaciones, como la creación de un libro de trabajo con un gran conjunto de datos para celdas, la opción [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) puede optimizar el uso de memoria y disminuir el costo de memoria para la aplicación. Sin embargo, esta opción puede degradar el rendimiento en algunos casos especiales como sigue.

1. **Acceso a celdas de forma aleatoria y repetida**: La secuencia más eficiente para acceder a la colección de celdas es celda por celda en una fila, y luego fila por fila. Especialmente, si accede a filas/celdas mediante el Enumerador adquirido de [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection) y [**Row**](https://reference.aspose.com/cells/javascript-cpp/row), el rendimiento será maximizado con [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).
1. **Inserción y eliminación de celdas y filas**: Tenga en cuenta que si hay muchas operaciones de inserción/eliminación para Celdas/Filas, la degradación del rendimiento será notable para el modo [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) en comparación con el modo [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) .
1. **Operación en diferentes tipos de celdas**: Si la mayoría de las celdas contienen valores de cadena o fórmulas, el costo de memoria será el mismo que el modo [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) pero si hay muchas celdas vacías, o los valores de las celdas son numéricos, booleanos, etc., la opción [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) dará un mejor rendimiento.
