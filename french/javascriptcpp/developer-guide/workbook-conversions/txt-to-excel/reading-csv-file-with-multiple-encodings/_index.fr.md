---
title: Lecture de fichiers CSV avec plusieurs encodages avec JavaScript via C++
linktitle: Lecture du fichier CSV avec plusieurs encodages
type: docs
weight: 200
url: /fr/javascript-cpp/reading-csv-file-with-multiple-encodings/
description: Apprenez comment lire des fichiers CSV avec plusieurs encodages en utilisant le script Aspose.Cells for Java via C++.
---

{{% alert color="primary" %}}

Parfois, votre fichier CSV contient plusieurs encodages (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells vous permet de charger ces fichiers CSV et de les convertir dans d'autres formats, par exemple PDF ou XLSX.

{{% /alert %}}

Aspose.Cells fournit la propriété [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--), que vous devez définir à **true** pour charger correctement votre fichier CSV avec plusieurs encodages.

La capture d'écran suivante montre un exemple de fichier CSV contenant deux lignes. La première ligne est en encodage **ANSI** et la deuxième ligne est en encodage **Unicode**

|**Fichier d'entrée**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

La capture d'écran suivante montre le fichier XLSX converti à partir du CSV ci-dessus sans définir la propriété [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) à **true**. Comme vous pouvez le voir, le texte Unicode n'a pas été converti correctement.

|**Fichier de sortie 1: aucune adaptation pour plusieurs encodages**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

La capture d'écran suivante montre le fichier XLSX converti à partir du CSV ci-dessus après avoir défini la propriété [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) à **true**. Comme vous pouvez le voir, le texte Unicode est maintenant converti correctement.

|**Fichier de sortie 2: IsMultiEncoded est défini sur true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Ci-dessous se trouve le code d'exemple qui convertit le fichier CSV ci-dessus en format XLSX correctement.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Multi-Encoded CSV to XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Convert to XLSX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create TxtLoadOptions and set isMultiEncoded property
            const options = new TxtLoadOptions();
            options.isMultiEncoded = true;

            // Load the CSV into a Workbook using the options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const outName = file.name.replace(/(\.[^/.]+)$/, '$1.out.xlsx');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = outName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to save the XLSX file.</p>';
        });
    </script>
</html>
```

## Articles Connexes

- [Ouverture des fichiers CSV](/cells/fr/javascript-cpp/opening-files-with-different-formats/#opening-csv-files)
