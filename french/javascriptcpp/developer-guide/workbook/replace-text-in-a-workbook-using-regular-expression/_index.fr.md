---
title: Remplacer du texte dans un classeur en utilisant une expression régulière avec JavaScript via C++
linktitle: Remplacer du texte dans un classeur en utilisant une expression régulière
type: docs
weight: 90
url: /fr/javascript-cpp/replace-text-in-a-workbook-using-regular-expression/
description: Remplacer du texte dans un classeur en utilisant une expression régulière en JavaScript via C++.
---

Aspose.Cells propose la fonctionnalité de remplacer du texte dans un classeur en utilisant une expression régulière. Pour cela, l'API fournit la propriété [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) de la classe [**ReplaceOptions**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions). La définition de [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) sur **true** indique que la clé recherchée sera une expression régulière.

Le code ci-dessous démontre l'utilisation de la propriété [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) en utilisant le [fichier Excel d'exemple](101089318.xlsx). Le [fichier de sortie](101089319.xlsx) généré par ce code est joint pour référence.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Regex Replace Example</title>
    </head>
    <body>
        <h1>Regex Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ReplaceOptions } = AsposeCells;

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

            const replaceOptions = new ReplaceOptions();
            replaceOptions.caseSensitive = false;
            replaceOptions.matchEntireCellContents = false;
            replaceOptions.regexKey = true;

            workbook.replace("\\bKIM\\b", "^^^TIM^^^", replaceOptions);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RegexReplace_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Regex replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
