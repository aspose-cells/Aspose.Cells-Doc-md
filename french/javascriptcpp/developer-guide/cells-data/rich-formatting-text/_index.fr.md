---
title: Accéder et mettre à jour les parties du texte enrichi de la cellule
linktitle: Texte enrichi avec formatage
type: docs
weight: 40
url: /fr/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Apprenez comment accéder et mettre à jour les parties du texte enrichi d une cellule via l API Aspose.Cells for JavaScript via C++.
keywords: Accéder et mettre à jour le texte enrichi de la cellule, obtenir le texte enrichi de la cellule, modifier le texte enrichi de la cellule, accéder au texte enrichi de la cellule, mettre à jour le texte enrichi de la cellule, changer le texte enrichi de la cellule
---

{{% alert color="primary" %}}

 Aspose.Cells for JavaScript via C++ permet d'accéder et de mettre à jour les parties du texte enrichi de la cellule. Pour cela, vous pouvez utiliser les propriétés [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) et [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-). Ces propriétés renverront et accepteront un tableau d'objets [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) que vous pouvez utiliser pour accéder et mettre à jour diverses propriétés de la police comme le nom de la police, la couleur de la police, le gras, etc.

{{% /alert %}}

## **Accéder et mettre à jour les parties du texte enrichi de la cellule**

Le code suivant montre l'utilisation des propriétés [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) et [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) en utilisant le [fichier excel source](5112369.xlsx) que vous pouvez télécharger via le lien fourni. Le fichier Excel source contient un texte enrichi dans la cellule A1. Il a 3 parties dont chaque partie a une police différente. Le code suivant accède à ces parties et met à jour la première avec un nouveau nom de police. Enfin, il enregistre le classeur en tant que [fichier excel de sortie](5112366.xlsx). Lorsque vous l'ouvrirez, vous constaterez que la police de la première partie du texte a été modifiée en **"Arial"**.

### Code JavaScript pour accéder et mettre à jour les parties du texte enrichi d'une cellule

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Cell Character Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            // Ensure Aspose.Cells is initialized
            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("A1");

            console.log("Before updating the font settings....");
            let fnts = cell.characters;
            const count = fnts.length;
            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Modify the first FontSetting Font Name
            fnts[0].font.name = "Arial";

            // And update it using characters property
            cell.characters = fnts;

            console.log("After updating the font settings....");

            fnts = cell.characters;

            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### Sortie de la console générée par le code d'exemple



{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
