---
title: Exportar el certificado VBA a un archivo o flujo con JavaScript vía C++
linktitle: Exportar Certificado VBA a Archivo o Secuencia
type: docs
weight: 90
url: /es/javascript-cpp/export-vba-certificate-to-file-or-stream/
description: Aprende cómo exportar un certificado digital VBA a un archivo o flujo usando Aspose.Cells for JavaScript vía C++. Accede a los datos en bruto de los certificados digitales VBA.
---

{{% alert color="primary" %}}

Aspose.Cells le permite exportar Certificado Digital VBA a una secuencia como un archivo o memoria. Puede acceder a los datos en bruto del certificado digital VBA utilizando la propiedad [**VbaProject.certRawData**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#certRawData--).

{{% /alert %}}

## **Exportar el certificado VBA a un archivo o flujo en JavaScript**

Consulte el siguiente código de muestra que guarda los datos en bruto del Certificado VBA en un archivo. Puede descargar el [archivo de Excel de muestra utilizado en este código](5115031.xlsm) desde el enlace proporcionado.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract VBA Project Certificate</h1>
        <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel macro-enabled (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve bytes data of Digital Certificate of VBA Project
            const certBytes = workbook.vbaProject.certRawData;

            // Convert to Uint8Array and create a Blob for download
            const certUint8 = Uint8Array.from(certBytes);
            const blob = new Blob([certUint8]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Cert_out_';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Certificate';

            document.getElementById('result').innerHTML = '<p style="color: green;">Certificate extracted successfully! Click the download link to save the certificate.</p>';
        });
    </script>
</html>
```
