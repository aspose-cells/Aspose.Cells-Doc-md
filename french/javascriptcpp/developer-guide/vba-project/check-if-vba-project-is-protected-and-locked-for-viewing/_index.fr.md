---
title: Vérifiez si le projet VBA est protégé et verrouillé pour la visualisation avec JavaScript via C++
linktitle: Vérifier si le projet VBA est protégé et verrouillé pour consultation
type: docs
weight: 30
url: /fr/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Apprenez comment vérifier si un projet VBA dans un fichier Excel est protégé et verrouillé pour la visualisation en utilisant Aspose.Cells for JavaScript via C++.
---

## Vérifiez si le projet VBA est protégé et verrouillé pour la visualisation en JavaScript via C++

Aspose.Cells vous permet de vérifier si le projet VBA (Visual Basic for Applications) d'un fichier Excel est protégé et verrouillé pour la visualisation. Pour cela, l'API fournit la propriété [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--). S'il est verrouillé pour la visualisation, alors la propriété [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--) retourne **true**.

## **Code d'exemple**

Le code d'exemple suivant charge le [fichier Excel exemple](43352065.xlsm) et vérifie si le projet VBA (Visual Basic for Applications) du fichier Excel est protégé et verrouillé en lecture seule. Veuillez également voir sa sortie Console pour référence.

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

## **Sortie console**

Il s'agit de la sortie de la console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier Excel d'exemple](43352065.xlsm) fourni.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
