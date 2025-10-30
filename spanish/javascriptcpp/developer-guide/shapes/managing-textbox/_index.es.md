---
title: Gestión de TextBox con JavaScript a través de C++
linktitle: Gestionar cuadro de texto
type: docs
weight: 50
url: /es/javascript-cpp/managing-textbox-of-excel/
description: Aprende cómo gestionar TextBox en Excel usando Aspose.Cells for JavaScript a través de C++. 
keywords: Gestionar TextBox en Excel con JavaScript a través de C++
---

## **Escenarios de uso posibles**
Existen escenarios en los que puede ser necesario agregar, actualizar o manipular objetos TextBox dentro de una hoja de cálculo de Excel. Esto puede ser útil para agregar anotaciones, textos de orientación o cualquier información adicional que ayude en la presentación de datos. Aspose.Cells for JavaScript a través de C++ ofrece funciones robustas para gestionar TextBox en documentos de Excel. 

## **Gestionar TextBox usando Aspose.Cells for JavaScript a través de C++**
Este ejemplo muestra cómo:

1. Cree un nuevo libro de trabajo.
2. Agregar una forma de TextBox.
3. Modificar las propiedades del TextBox según sea necesario.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox Example</title>
    </head>
    <body>
        <h1>TextBox Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            let workbook;

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding a TextBox shape
            const textBox = worksheet.shapes.addTextBox(2, 2, 100, 100);

            // Set TextBox properties (converted getters/setters to properties)
            textBox.text = "This is a TextBox.";
            textBox.fontSize = 12;
            textBox.fillColor = Color.fromArgb(255, 255, 255); // White background

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'TextBoxExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Este código demuestra cómo crear y configurar un TextBox dentro de una hoja de cálculo de Excel, mostrando cómo ajustar su tamaño, posición y formato según tus requerimientos.

Tenga en cuenta que las interacciones con los cuadros de texto pueden variar según los casos de uso específicos, así que consulte la documentación de Aspose.Cells for JavaScript a través de C++ para métodos y propiedades adicionales.
