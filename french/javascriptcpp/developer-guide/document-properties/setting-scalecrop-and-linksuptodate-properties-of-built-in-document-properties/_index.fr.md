---
title: Définir les propriétés ScaleCrop et LinksUpToDate des propriétés intégrées du document avec JavaScript via C++
linktitle: Définir les propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.
type: docs
weight: 320
url: /fr/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Apprenez comment définir les propriétés ScaleCrop et LinksUpToDate des propriétés intégrées du document en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**
[BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) et [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) sont deux propriétés document étendues intégrées définies dans le format OpenXml. L'objectif de ces propriétés est le suivant.

## **1) ScaleCrop**
Cet élément indique le mode d'affichage de la vignette du document. Définissez cet élément sur **TRUE** pour activer le redimensionnement de la vignette du document à l'affichage. Définissez cet élément sur **FALSE** pour activer le rognage de la vignette du document afin de montrer uniquement les sections qui s'adaptent à l'affichage.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.

## **2) LinksUpToDate**
Cet élément indique si les hyperliens dans un document sont à jour. Définissez cet élément sur **TRUE** pour indiquer que les hyperliens sont mis à jour. Définissez cet élément sur **FALSE** pour indiquer que les hyperliens sont obsolètes.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.

## **Capture d'écran montrant ces propriétés dans le fichier app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.**
Le code d'exemple suivant définit les propriétés document étendues intégrées [BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) et [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) du classeur. Veuillez vérifier le [fichier excel généré](5115500.xlsx) avec ce code, changer son extension en .zip, extraire son contenu et voir le app.xml comme montré dans la capture d'écran ci-dessus.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set BuiltIn Document Properties</h1>
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
            const fileInput = document.getElementById('fileInput');

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Accessing BuiltIn Document Properties and setting properties
            const builtInDocumentProperties = workbook.builtInDocumentProperties;
            // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
            builtInDocumentProperties.scaleCrop = true;
            builtInDocumentProperties.linksUpToDate = true;

            // Saving the Excel file.
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
