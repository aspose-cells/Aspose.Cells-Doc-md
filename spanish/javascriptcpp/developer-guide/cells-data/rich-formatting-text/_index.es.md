---
title: Acceder y Actualizar las Partes de Texto Enriquecido de la Celda
linktitle: Texto con Formato Enriquecido
type: docs
weight: 40
url: /es/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Aprende cómo acceder y actualizar las porciones de texto enriquecido de la celda mediante la API de Aspose.Cells for JavaScript via C++.
keywords: Acceder y Actualizar Texto Enriquecido de la Celda, Obtener Texto Enriquecido de la Celda, Editar Texto Enriquecido de la Celda, Acceder a Texto Enriquecido de la Celda, Actualizar Texto Enriquecido de la Celda, Cambiar Texto Enriquecido de la Celda
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ te permite acceder y actualizar las porciones del texto enriquecido de la celda. Para esto, puedes usar las propiedades [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) y [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-). Estas propiedades devolverán y aceptarán un array de objetos [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) que puedes usar para acceder y actualizar varias propiedades de la fuente como nombre de la fuente, color, negrita, etc.

{{% /alert %}}

## **Acceder y actualizar partes de texto enriquecido de la celda**

El siguiente código demuestra el uso de las propiedades [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) y [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) usando el [archivo de Excel fuente](5112369.xlsx) que puedes descargar desde el enlace proporcionado. El archivo de Excel fuente tiene un texto enriquecido en la celda A1. Tiene 3 porciones y cada porción tiene una fuente diferente. El código siguiente accede a estas porciones y actualiza la primera con un nuevo nombre de fuente. Finalmente, guarda el libro como [archivo de Excel de salida](5112366.xlsx). Cuando lo abras, encontrarás que la fuente de la primera porción del texto ha cambiado a **"Arial"**.

### Código JavaScript para acceder y actualizar las porciones del texto enriquecido de la celda

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Cell Character Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized
            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("A1");

            console.log("Before updating the font settings....");
            let fnts = cell.characters;
            const count = fnts.length;
            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Modify the first FontSetting Font Name
            fnts[0].font.name = "Arial";

            // And update it using characters property
            cell.characters = fnts;

            console.log("After updating the font settings....");

            fnts = cell.characters;

            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### Salida de consola generada por el código de ejemplo



{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
