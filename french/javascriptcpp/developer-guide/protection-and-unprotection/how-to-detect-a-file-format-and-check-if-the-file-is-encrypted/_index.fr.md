---
title: Comment détecter un format de fichier et vérifier si le fichier est crypté avec JavaScript via C++
linktitle: Comment détecter un format de fichier et vérifier si le fichier est chiffré
type: docs
weight: 2700
url: /fr/javascript-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
description: Apprenez comment détecter un format de fichier et vérifier si un fichier est crypté en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
Parfois, vous devez détecter le format d'un fichier avant de l'ouvrir car l'extension ne garantit pas que le contenu du fichier est approprié. Le fichier pourrait être crypté (protégé par mot de passe), donc il ne peut pas être lu directement, ou nous ne devons pas le lire. Aspose.Cells for JavaScript via C++ fournit la méthode statique [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#detectFileFormat-uint8array-) et quelques API pertinentes que vous pouvez utiliser pour traiter les documents.  
{{% /alert %}}  

L'exemple de code suivant illustre comment détecter un format de fichier (en utilisant le chemin du fichier) et vérifier son extension. Vous pouvez également déterminer si le fichier est chiffré.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells File Format Detection Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Detect file format
            const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(arrayBuffer));

            // Gets the detected load format (converted getter -> property)
            const extension = AsposeCells.FileFormatUtil.loadFormatToExtension(info.loadFormat);
            const encrypted = info.isEncrypted;

            console.log("The spreadsheet format is: " + extension);
            console.log("The file is encrypted: " + encrypted);

            resultDiv.innerHTML = `<p>The spreadsheet format is: <strong>${extension}</strong></p>
                                   <p>The file is encrypted: <strong>${encrypted}</strong></p>`;
        });
    </script>
</html>
```
