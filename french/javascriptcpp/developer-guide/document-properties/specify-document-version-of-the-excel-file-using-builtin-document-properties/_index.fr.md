---
title: Spécifier la version du document du fichier Excel en utilisant les propriétés document intégrées avec JavaScript via C++
linktitle: Spécifier la version du document du fichier Excel en utilisant les propriétés de document intégrées
type: docs
weight: 20
url: /fr/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Apprenez comment spécifier la version du document d un fichier Excel de manière programmatique en utilisant les propriétés document intégrées avec JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

 Vous pouvez modifier le **Numéro de version** d'un fichier Excel en cliquant avec le bouton droit sur le fichier, puis en sélectionnant Propriétés > Détails et en modifiant le champ **Numéro de version**. Veuillez utiliser la propriété [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--) pour la changer de manière programmatique avec Aspose.Cells APIs.  

## **Spécifier la version du document du fichier Excel à l'aide des propriétés de document intégrées**  

 Le code d'exemple suivant crée un classeur et modifie ses propriétés intégrées du document, notamment le Titre, les Auteurs et le Numéro de version. Veuillez consulter le [fichier Excel de sortie](64716811.xlsx) généré par le code et la capture d'écran qui montre la modification du numéro de version par la propriété [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--).  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Document Version Example</h1>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create workbook object
            const wb = new Workbook();

            // Access built-in document property collection
            const bdpc = wb.builtInDocumentProperties;

            // Set the title
            bdpc.title = "Aspose File Format APIs";

            // Set the author
            bdpc.author = "Aspose APIs Developers";

            // Set the document version
            bdpc.documentVersion = "Aspose.Cells Version - 18.3";

            // Save the workbook in xlsx format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyDocumentVersionOfExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and prepared for download. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
