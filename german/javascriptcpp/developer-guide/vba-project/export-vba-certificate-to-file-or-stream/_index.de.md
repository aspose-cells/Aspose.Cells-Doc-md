---
title: Exportieren Sie das VBA Zertifikat in eine Datei oder einen Stream mit JavaScript über C++
linktitle: Exportieren Sie VBA Zertifikat in eine Datei oder einen Stream
type: docs
weight: 90
url: /de/javascript-cpp/export-vba-certificate-to-file-or-stream/
description: Erfahren Sie, wie Sie VBA Digitalzertifikate in eine Datei oder einen Stream exportieren, mit Aspose.Cells for JavaScript über C++. Zugriff auf Rohdaten von VBA Digitalzertifikaten.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, das VBA-Digitalzertifikat in einen Stream wie Datei oder Memory Stream zu exportieren. Sie können auf die Rohdaten des VBA-Digitalzertifikats über die [**VbaProject.certRawData**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#certRawData--)-Eigenschaft zugreifen.

{{% /alert %}}

## ** VBA-Zertifikat in Datei oder Stream exportieren in JavaScript**

Bitte sehen Sie sich den folgenden Beispielscode an, der die Rohdaten des VBA-Zertifikats in einer Datei speichert. Sie können die [Beispiel-Excel-Datei, die in diesem Code verwendet wird](5115031.xlsm) von dem bereitgestellten Link herunterladen.

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
