---
title: Accéder à la zone de texte par le nom avec JavaScript via C++
linktitle: Accéder à la zone de texte par le nom
type: docs
weight: 230
url: /fr/javascript-cpp/access-the-text-box-by-the-name/
description: Apprenez comment accéder à une zone de texte par son nom dans la collection en Aspose.Cells for JavaScript via C++. 
---

## Accéder à la zone de texte par le nom

Auparavant, les zones de texte étaient accessibles par index dans la collection [**Worksheet.textBoxes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#textBoxes--), mais maintenant, vous pouvez également accéder à la zone de texte par son nom dans cette collection. C'est une méthode pratique et rapide pour accéder à votre zone de texte si vous connaissez déjà son nom.

Le code d'exemple suivant crée d'abord une zone de texte et lui attribue un texte et un nom. Ensuite, dans les lignes suivantes, nous accédons à la même zone de texte par son nom et affichons son texte.

### Code JavaScript pour accéder à la zone de texte par le nom

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox Example</title>
    </head>
    <body>
        <h1>TextBox Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const sheet = workbook.worksheets.get(0);

            const idx = sheet.textBoxes.add(10, 10, 10, 10);

            const tb1 = sheet.textBoxes.get(idx);
            tb1.name = "MyTextBox";
            tb1.text = "This is MyTextBox";

            const tb2 = sheet.textBoxes.get("MyTextBox");

            console.log(tb2.text);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">TextBox added. Text from named TextBox: ${tb2.text}</p>`;
        });
    </script>
</html>
```

### Sortie de la console générée par le code d'exemple



{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
