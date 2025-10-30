---
title: Verifica si el proyecto VBA está protegido y bloqueado para visualización con JavaScript vía C++
linktitle: Verifique si el Proyecto VBA está Protegido y Bloqueado para Visualización
type: docs
weight: 30
url: /es/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Aprende cómo verificar si un proyecto VBA en un archivo de Excel está protegido y bloqueado para visualización usando Aspose.Cells for JavaScript vía C++.
---

## Verifica si el proyecto VBA está protegido y bloqueado para visualización en JavaScript vía C++

Aspose.Cells permite verificar si el proyecto VBA (Visual Basic for Applications) de un archivo de Excel está protegido y bloqueado para visualización. Para ello, la API proporciona la propiedad [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--). Si está bloqueado para visualización, entonces la propiedad [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--) devuelve **true**.

## **Código de muestra**

El siguiente ejemplo de código carga el [archivo de Excel de ejemplo](43352065.xlsm) y verifica si el proyecto VBA del archivo de Excel está protegido y bloqueado para visualización. También consulta su Salida en Consola para referencia.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check VBA Project Protection Example</title>
    </head>
    <body>
        <h1>Check if VBA Project is Protected</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.xlsb,.csv" />
        <button id="runExample">Check VBA Protection</button>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm) to check.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the VBA project of the workbook.
            const vbaProject = workbook.vbaProject;

            // Whether "Lock project for viewing" is true or not.
            const isLocked = vbaProject ? vbaProject.islockedForViewing : null;

            if (isLocked === null) {
                resultDiv.innerHTML = '<p style="color: orange;">The workbook does not contain a VBA project.</p>';
            } else {
                resultDiv.innerHTML = `<p>Is VBA Project Locked for Viewing: <strong>${isLocked}</strong></p>`;
                console.log("Is VBA Project Locked for Viewing: " + isLocked);
            }
        });
    </script>
</html>
```

## **Salida de la consola**

Esta es la salida de consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de muestra](43352065.xlsm) proporcionado.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
