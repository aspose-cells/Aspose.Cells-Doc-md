---
title: Utiliser des parties XML personnalisées dans Aspose.Cells avec JavaScript via C++
linktitle: Utilisez des parties XML personnalisées dans Aspose.Cells
type: docs
weight: 390
url: /fr/javascript-cpp/use-custom-xml-parts-in-aspose-cells/
description: Apprenez à utiliser des parties XML personnalisées en Aspose.Cells for JavaScript via C++. Intégrez des données XML externes dans les fichiers Excel de façon transparente.
---

## Utilisation de parties XML personnalisées dans Aspose.Cells

Les parties XML personnalisées sont les données XML stockées par différentes applications comme SharePoint, etc. à l'intérieur du fichier Excel. Ces données sont utilisées par différentes applications qui en ont besoin. Microsoft Excel n'utilise pas ces données, il n'y a donc pas d'interface graphique pour les ajouter. Vous pouvez visualiser ces données en changeant l’extension de **.xlsx** à **.zip** puis en l’ouvrant avec **WinZip**. Vous pouvez également ouvrir le fichier ZIP avec n'importe quel utilitaire de compression Windows tiers tel que WinRAR ou WinZip. Les données se trouvent dans le dossier **customXml**.

Vous pouvez ajouter des parties XML personnalisées en utilisant Aspose.Cells for JavaScript via C++ grâce à la méthode [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/).

Le code d'exemple ci-dessous utilise la méthode [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) et ajoute le **Book Catalog XML** dont le nom est **BookStore**. L'image suivante montre le résultat de ce code. Comme vous pouvez le voir, le Book Catalog XML est ajouté dans le nœud BookStore, qui est le nom de cette propriété.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Code JavaScript pour utiliser des parties XML personnalisées

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Custom XML to Workbook Example</h1>
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

        const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create an instance of Workbook class
            const workbook = new Workbook();

            // Add Custom XML Part to ContentTypePropertyCollection
            workbook.contentTypeProperties.add("BookStore", booksXML);

            // Save the resultant spreadsheet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom XML added and file prepared. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## Article connexe

- [Ajout de propriétés personnalisées visibles dans le volet Informations sur le document](/cells/fr/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
