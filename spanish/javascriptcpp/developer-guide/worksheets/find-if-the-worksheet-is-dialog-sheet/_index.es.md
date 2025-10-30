---
title: Encontrar si la hoja de cálculo es una Hoja de Diálogo con JavaScript mediante C++
linktitle: Encontrar si la hoja de cálculo es una hoja de diálogo
type: docs
weight: 90
url: /es/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Este artículo proporciona instrucciones y código de ejemplo para determinar programáticamente si una hoja de cálculo de Excel es una Hoja de Diálogo usando Aspose.Cells for JavaScript mediante C++.
keywords: Encontrar el tipo de diálogo de la hoja de cálculo de Excel con JavaScript mediante C++, diálogo de hoja de cálculo con JavaScript mediante C++
---

## **Escenarios de uso posibles**

La hoja de diálogo es un formato antiguo de hoja que contiene un cuadro de diálogo. Esa hoja podría haber sido insertada por una versión antigua de Microsoft Excel, por ejemplo, 2003, como se muestra en esta captura de pantalla. También puede ser insertada con VBA en versiones más recientes, por ejemplo, Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Puedes determinar si la hoja es una hoja de diálogo u otro tipo de hoja con la propiedad [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--) proporcionada por Aspose.Cells for JavaScript a través de C++. Si devuelve un valor de enumeración [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype), entonces significa que estás tratando con una hoja de diálogo.

## **Buscar si la hoja de trabajo es una hoja de diálogo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716820.xlsx) que contiene una hoja de diálogo. Verifica la propiedad [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--), la compara con [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype), y luego imprime el mensaje. Consulta la salida en consola del código de ejemplo a continuación para más ayuda.

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Detect Dialog Sheet</title>
    </head>
    <body>
        <h1>Detect if Worksheet Is a Dialog Sheet</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Find if the sheet type is dialog and print the message
            if (ws.type === AsposeCells.SheetType.Dialog) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet is a Dialog Sheet.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is NOT a Dialog Sheet.</p>';
            }
        });
    </script>
</html>
```

## **Salida de la consola**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
