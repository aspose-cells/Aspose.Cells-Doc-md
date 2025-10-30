---
title: Usar opciones de revisión de errores con JavaScript a través de C++
linktitle: Usar opciones de verificación de errores
type: docs
weight: 140
url: /es/javascript-cpp/use-error-checking-options/
description: Aprende cómo usar programáticamente las opciones de revisión de errores en hojas de cálculo de Excel usando Script Aspose.Cells for Java a través de C++.
keywords: guardar número como texto en Excel usando JavaScript a través de C++, opciones de revisión de errores en JavaScript a través de C++
---

{{% alert color="primary" %}}  
Microsoft Excel permite a los usuarios definir opciones y reglas de verificación de errores. Los usuarios a menudo ven verificaciones de errores al crear fórmulas, un pequeño triángulo en la esquina superior derecha de una celda resalta cuando hay un problema con una celda. Excel proporciona información que ayuda a los usuarios a corregir problemas comunes.  
{{% /alert %}}  

## **Tipos de Errores**  

Los errores que indican que la fórmula no puede devolver un resultado, como dividir un número por cero, requieren atención inmediata y se muestra un valor de error en la celda. Al hacer clic en el triángulo verde, aparece un signo de exclamación; hacer clic en esto abre una lista de opciones.  

El error puede ser resuelto usando las opciones o ser ignorado. Ignorar un error significa que ese error no aparecerá en controles de errores futuros.  

Aspose.Cells proporciona funciones de opción de comprobación de errores. La clase [**ErrorCheckOption**](https://reference.aspose.com/cells/javascript-cpp/errorcheckoption) gestiona diferentes tipos de comprobaciones de errores, por ejemplo, números almacenados como texto, errores de cálculo de fórmulas y errores de validación. Use la enumeración [**ErrorCheckType**](https://reference.aspose.com/cells/javascript-cpp/errorchecktype) para establecer la comprobación de errores deseada.  

## **Números Almacenados como Texto**  

Ocasionalmente, los números pueden formatearse y almacenarse en celdas como texto. Esto puede causar problemas con cálculos o producir órdenes de clasificación confusos. Los números formateados como texto están alineados a la izquierda en lugar de a la derecha en la celda. Si una fórmula que debería realizar una operación matemática en celdas no devuelve un valor, verifica la alineación en las celdas a las que hace referencia la fórmula; algunas o todas esas celdas pueden ser números formateados como texto.  

Puedes usar las opciones de verificación de errores para convertir rápidamente los números almacenados como texto en números reales. En Microsoft Excel 2003:  

1. En el menú **Herramientas**, haz clic en **Opciones**.  
1. Selecciona la pestaña de Verificación de Errores.  
   La opción de **Número almacenado como texto** está marcada por defecto.  
1. Desactívala.  

El siguiente código de muestra muestra cómo deshabilitar la opción de verificación de errores de números almacenados como texto para una hoja de cálculo en el archivo XLS de plantilla utilizando las APIs de Aspose.Cells.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Error Check Options</title>
    </head>
    <body>
        <h1>Error Check Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a Workbook by reading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Instantiate the error checking options
            const opts = sheet.errorCheckOptions;

            const index = opts.add();
            const opt = opts.get(index);
            // Disable the numbers stored as text option
            // Converted from opt.setErrorCheck(type, value) to a property-style assignment
            opt.errorCheck = opt.errorCheck || {};
            opt.errorCheck[AsposeCells.ErrorCheckType.NumberStoredAsText] = false;
            // Set the range
            opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

            // Save the Excel file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_test.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
