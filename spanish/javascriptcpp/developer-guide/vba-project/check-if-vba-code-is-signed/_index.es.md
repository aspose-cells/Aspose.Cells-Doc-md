---
title: Verificar si el código VBA está firmado con JavaScript a través de C++
linktitle: Verifique si el Código VBA está firmado
type: docs
weight: 100
url: /es/javascript-cpp/check-if-vba-code-is-signed/
description: Aprende cómo verificar si el proyecto de código VBA está firmado usando Aspose.Cells for JavaScript vía C++. 
---

{{% alert color="primary" %}}

Aspose.Cells permite al usuario verificar si el proyecto de código VBA está firmado o no. Por favor utiliza la propiedad [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--) para verificar si el proyecto de código VBA está firmado o no.

{{% /alert %}}

El siguiente código explica cómo verificar si el código VBA está firmado o no usando la propiedad [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--). Puedes usar cualquiera de tus archivos de Excel para probar este código. Para fines de prueba, puedes usar [este archivo de Excel usado en el código](5115032.xlsm).

## **Verifica si el código VBA está firmado en JavaScript**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const vbaProject = workbook.vbaProject;
            const isSigned = vbaProject.isSigned();

            resultDiv.innerHTML = `<p>Is VBA Code Project Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```

## Salida de la consola

A continuación se muestra la salida de consola del código anterior utilizando el [archivo excel de muestra](5115032.xlsm) proporcionado por el enlace.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
