---
title: Spécifier la langue du fichier Excel en utilisant les propriétés document intégrées avec JavaScript via C++
linktitle: Spécifier la langue du fichier Excel en utilisant les propriétés de document intégrées
type: docs
weight: 30
url: /fr/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Scénarios d'utilisation possibles**

Vous pouvez changer la langue d'un fichier Excel en cliquant droit sur le fichier, puis en sélectionnant Propriétés > Détails, et en éditant le champ Langue. Veuillez utiliser la propriété [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--) pour la modifier de manière programmée via l'API Aspose.Cells for JavaScript en C++.

## **Spécifier la langue du fichier Excel en utilisant les propriétés de document intégrées**

 Le code d'exemple suivant crée un classeur et modifie sa propriété du document intégrée nommée langue. Veuillez consulter le [fichier Excel de sortie](64716891.xlsx) généré par le code et la capture d'écran montrant le champ Langue modifié par la propriété [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Language Using BuiltInDocumentProperties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Create workbook object.
            const wb = new Workbook();

            // Access built-in document property collection.
            const bdpc = wb.builtInDocumentProperties;

            // Set the language of the Excel file.
            bdpc.language = "German, French";

            // Save the workbook in xlsx format.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Language set successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
