---
title: Vérifiez si le projet VBA dans un classeur est signé avec JavaScript via C++
linktitle: Vérifier si le projet VBA dans un classeur est signé
type: docs
weight: 70
url: /fr/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Apprenez comment vérifier si un projet VBA dans un classeur est signé en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Vous pouvez vérifier si votre projet VBA est signé ou non en utilisant Microsoft Excel via la commande de menu **Outils > Signatures numériques...** De même, vous pouvez le vérifier de manière programmatique en utilisant la propriété Aspose.Cells [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--).

{{% /alert %}}

## **Vérifiez si le projet VBA dans un classeur est signé en JavaScript**

Le code suivant charge le classeur et vérifie si son projet VBA est signé en utilisant la propriété [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--). La propriété retournera **true** si le projet est signé, sinon elle retournera **false**.

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
