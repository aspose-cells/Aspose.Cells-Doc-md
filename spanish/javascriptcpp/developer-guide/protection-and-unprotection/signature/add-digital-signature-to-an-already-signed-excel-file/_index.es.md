---
title: Agregar firma digital a un archivo Excel ya firmado con JavaScript a través de C++
linktitle: Agregar Firma Digital a un archivo de Excel que ya está firmado
type: docs
weight: 20
url: /es/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Este artículo describe cómo agregar una firma digital a un archivo Excel ya firmado usando JavaScript con Aspose.Cells for JavaScript mediante C++.
keywords: Agregar firma digital a un archivo Excel ya firmado, Cómo agregar una firma digital a un documento Excel ya firmado usando JavaScript mediante C++.
---

## **Escenarios de uso posibles**

Aspose.Cells for JavaScript mediante C++ proporciona el método [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) que puedes usar para agregar una firma digital a un archivo Excel ya firmado.

{{% alert color="primary" %}}

Tenga en cuenta que al agregar una firma digital a un documento de Excel ya firmado, si el documento original es un documento generado por Aspose.Cells, funciona bien. Pero si el documento original es generado por otros motores (por ejemplo, Microsoft Excel, etc.), Aspose.Cells no puede mantener el archivo igual después de cargarlo y volver a guardarlo, lo que invalidará la firma original.

{{% /alert %}}

## **Cómo agregar una firma digital a un archivo de Excel ya firmado**

El código de ejemplo siguiente demuestra cómo usar el método [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) para agregar una firma digital a un archivo de Excel ya firmado. Por favor, revise el [archivo de Excel de ejemplo](50528280.xlsx) utilizado en este código. Este archivo ya está firmado digitalmente. Por favor, revise el [archivo de Excel de salida](50528281.xlsx) generado por el código. Hemos utilizado el certificado de demostración llamado [AsposeDemo.pfx](50528279.pfx), que tiene una contraseña **aspose**. La captura de pantalla muestra el efecto del código de ejemplo en el archivo de Excel de ejemplo después de la ejecución.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Digital Signature Example</title>
    </head>
    <body>
        <h1>Add Digital Signature to Workbook</h1>
        <p>Select an Excel file and a PFX certificate, enter the certificate password, then click "Add Digital Signature".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <br/><br/>
        <input type="file" id="certInput" accept=".pfx" />
        <br/><br/>
        <label for="certPassword">Certificate Password:</label>
        <input type="password" id="certPassword" value="aspose" />
        <br/><br/>
        <button id="runExample">Add Digital Signature</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, DigitalSignature, DigitalSignatureCollection, SaveFormat, Utils } = AsposeCells;

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
            const certInput = document.getElementById('certInput');
            const passwordInput = document.getElementById('certPassword');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!certInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a .pfx certificate file.</p>';
                return;
            }

            // Read files as ArrayBuffer
            const excelFile = fileInput.files[0];
            const certFile = certInput.files[0];
            const certPassword = passwordInput.value;

            const excelArrayBuffer = await excelFile.arrayBuffer();
            const certArrayBuffer = await certFile.arrayBuffer();

            // Instantiate Workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(excelArrayBuffer));

            // Create the digital signature collection
            const dsCollection = new DigitalSignatureCollection();

            // Create new digital signature and add it in digital signature collection
            // Using certificate bytes (Uint8Array), password, comment and signing date
            const signature = new DigitalSignature(new Uint8Array(certArrayBuffer), certPassword, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
            dsCollection.add(signature);

            // Add digital signature collection inside the workbook
            workbook.addDigitalSignature(dsCollection);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDigitallySignedByCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Digitally Signed Excel File';

            // Dispose the workbook
            workbook.dispose();

            resultDiv.innerHTML = '<p style="color: green;">Digital signature added successfully! Click the download link to get the signed file.</p>';
        });
    </script>
</html>
```
