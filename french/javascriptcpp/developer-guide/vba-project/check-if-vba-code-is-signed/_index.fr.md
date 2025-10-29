---
title: Vérifier si le code VBA est signé avec JavaScript via C++
linktitle: Vérifier si le code VBA est signé
type: docs
weight: 100
url: /fr/javascript-cpp/check-if-vba-code-is-signed/
description: Apprenez comment vérifier si le projet de code VBA est signé en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells permet à l'utilisateur de vérifier si le projet de code VBA est signé ou non. Veuillez utiliser la propriété [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--) pour vérifier si le projet de code VBA est signé ou non.

{{% /alert %}}

Le code suivant explique comment vérifier si le code VBA est signé ou non en utilisant la propriété [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--). Vous pouvez utiliser n'importe lequel de vos fichiers Excel pour tester ce code. Pour les tests, vous pouvez utiliser [ce fichier Excel utilisé dans le code](5115032.xlsm).

## **Vérifiez si le code VBA est signé en JavaScript**

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

## Sortie de la console

Ci-dessous se trouve la sortie de la console du code ci-dessus en utilisant le [fichier excel d'exemple](5115032.xlsm) fourni par le lien.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
