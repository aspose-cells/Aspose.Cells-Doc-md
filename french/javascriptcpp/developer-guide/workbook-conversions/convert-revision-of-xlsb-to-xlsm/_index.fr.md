---
title: Convertir la révision d’un XLSB en XLSM avec JavaScript via C++
linktitle: Convertir la révision des XLSB en XLSM
type: docs
weight: 290
url: /fr/javascript-cpp/convert-revision-of-xlsb-to-xlsm/
description: Apprenez à convertir complètement les révisions de fichiers XLSB en format XLSM en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Aspose.Cells prend désormais en charge la conversion complète des révisions de fichiers XLSB en fichiers XLSM. Les révisions se trouvent dans le chemin \xl\revisions. Vous pouvez les voir en changeant l'extension de votre fichier XLSB en ZIP. Le chemin \xl\revisions contient des fichiers se terminant par l’extension .bin.

Lorsque vous convertissez votre fichier XLSB en fichier XLSM avec Aspose.Cells, ces fichiers .bin se convertissent avec succès en fichiers .xml comme montré dans ces deux captures d'écran.

{{% /alert %}}

L'exemple de code suivant montre comment convertir le fichier XLSB au format XLSM en utilisant Aspose.Cells for JavaScript via C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert XLSB to XLSM Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb, .xls, .xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save Workbook to XLSM format
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted XLSM File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to XLSM successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
