---
title: Verifica si el proyecto VBA en un libro de trabajo está firmado con JavaScript vía C++
linktitle: Verifique si el proyecto VBA en un Libro de Trabajo está firmado
type: docs
weight: 70
url: /es/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Aprende cómo verificar si un proyecto VBA en un libro de trabajo está firmado usando Aspose.Cells for JavaScript vía C++.
---

{{% alert color="primary" %}}

Puedes verificar si tu proyecto VBA está firmado o no utilizando Microsoft Excel a través del menú **Herramientas > Firmas Digitales...**. Del mismo modo, puedes verificarlo programáticamente utilizando la propiedad [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--) de Aspose.Cells.

{{% /alert %}}

## **Verifica si el proyecto VBA en un libro de trabajo está firmado en JavaScript**

El siguiente código carga el libro de trabajo y verifica si su proyecto VBA está firmado usando la propiedad [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--). La propiedad devolverá **true** si el proyecto está firmado, de lo contrario devolverá **false**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const isSigned = workbook.vbaProject.isSigned;

            console.log("VBA Project is Signed: " + isSigned);
            document.getElementById('result').innerHTML = `<p>VBA Project is Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```
