---
title: Cómo agregar/insertar una caja de texto en una hoja de cálculo con JavaScript a través de C++
linktitle: Agregar cuadro de texto a la hoja de cálculo
type: docs
weight: 10
url: /es/javascript-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Cómo agregar/insertar una caja de texto en una hoja de cálculo en Aspose.Cells for JavaScript a través de C++.
keywords: Agregar/insertar texto en una caja de texto en una hoja de cálculo Excel Aspose con JavaScript a través de C++
---

## Agregar cuadro de texto a la hoja de cálculo en Excel

En el programa de Excel (versión 07 y superior), hay dos lugares donde puede insertar cuadros de texto. Uno en "insertar-formas", el otro en la parte derecha del menú superior de la opción "Insertar".

### método uno:

![1](1.png)

### método dos:

![2](2.png)

## Cómo crear

Puedes crear cuadros de texto con texto horizontal o vertical.

- Seleccione la opción correspondiente (horizontal o vertical)
- Haz clic izquierdo en la página
- Mantén presionado el botón izquierdo y arrastra una distancia en la página
- Suelta el botón izquierdo

Ahora tienes un cuadro de texto.

## Agregar una caja de texto a la hoja de cálculo en Aspose.Cells for JavaScript a través de C++

Cuando necesite insertar en bloque TextBox en la hoja de cálculo, el método manual de inserción es claramente un desastre. Si esto le molesta, creo que este documento le ayudará. [Aspose.Cells](https://products.aspose.com/cells/) le proporciona una API para realizar inserciones masivas fácilmente en su código.

El siguiente código de ejemplo crea un cuadro de texto.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add TextBox</title>
    </head>
    <body>
        <h1>Add TextBox to Workbook</h1>
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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the TextBox to the worksheet
            sheet.textBoxes.add(6, 10, 100, 200);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">TextBox added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Obtendrás un archivo similar a [archivo resultante](result.xlsx). En el archivo, verás lo siguiente:

![](52449.png)
