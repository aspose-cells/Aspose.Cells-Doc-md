---
title: Travailler avec ContentTypeProperties en JavaScript via C++
linktitle: Travailler avec ContentTypeProperties
type: docs
weight: 150
url: /fr/javascript-cpp/working-with-contenttypeproperties/
description: Apprenez à travailler avec des ContentTypeProperties personnalisés dans les fichiers Excel en utilisant Aspose.Cells for JavaScript via C++.
---

Aspose.Cells fournit la méthode [**Workbook.contentTypeProperties**](https://reference.aspose.com/cells/javascript-cpp/workbook/#contentTypeProperties--) pour ajouter des ContentTypeProperties personnalisés à un fichier Excel. Vous pouvez également rendre la propriété facultative en définissant la propriété [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/javascript-cpp/contenttypeproperty/#isNillable--) à **true**. Le code suivant montre comment ajouter des ContentTypeProperties personnalisés optionnels à un fichier Excel. L’image suivante montre les deux propriétés ajoutées par le code.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Le fichier de sortie généré par le code d'exemple est joint pour référence.

[Fichier de sortie](95584314.xlsx)

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Working With Content Type Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');

            // Creating a new Workbook with Xlsx format
            const workbook = new Workbook(FileFormatType.Xlsx);

            // Adding content type properties
            let index = workbook.contentTypeProperties.add("MK31", "Simple Data");
            workbook.contentTypeProperties.get(index).isNillable = false;

            index = workbook.contentTypeProperties.add("MK32", new Date().toISOString(), "DateTime");
            workbook.contentTypeProperties.get(index).isNillable = true;

            // Saving the workbook and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkingWithContentTypeProperties_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
