---
title: Importer XML dans un classeur Excel avec JavaScript via C++
linktitle: Cartes XML
type: docs
weight: 210
url: /fr/javascript-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Importer des données depuis des fichiers XML dans Excel en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'importer la carte XML dans le classeur en utilisant la méthode [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). Vous pouvez importer la carte XML en utilisant Microsoft Excel avec les étapes suivantes :

- Sélectionnez l'onglet **Développeur**
- Cliquez sur **Importer** dans la section XML et suivez les étapes requises.

Vous devrez fournir vos données XML pour compléter l'importation. Voici un [exemple de données XML](5115037.txt) que vous pouvez utiliser pour les tests.

{{% /alert %}}

## **Importer une carte XML en utilisant Microsoft Excel**

La capture d'écran suivante montre comment importer une carte XML en utilisant Microsoft Excel

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importer une cartographie XML en utilisant Aspose.Cells for JavaScript via C++**

Le code exemple suivant montre comment utiliser [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). Il génère le [fichier Excel de sortie](5115036.xlsx) comme indiqué dans cette capture d'écran.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Import XML</title>
    </head>
    <body>
        <h1>Import XML into Workbook Example</h1>
        <input type="file" id="xmlInput" accept=".xml,.txt" />
        <button id="runExample">Import XML and Save</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const fileInput = document.getElementById('xmlInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const xmlText = await file.text();

            // Create a workbook
            const workbook = new Workbook();

            // Import your XML Map data starting from cell A1 on Sheet1
            workbook.importXml(xmlText, "Sheet1", 0, 0);

            // Save workbook to XLSX and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">XML imported and workbook saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Ajouter une carte XML dans le classeur en utilisant la méthode XmlMapCollection.add()](/cells/fr/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Exporter des données XML liées à la carte XML à l'intérieur du classeur](/cells/fr/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Trouver le nom de l'élément racine de la carte XML](/cells/fr/javascript-cpp/find-the-root-element-name-of-xml-map/)
- [Lier des cellules aux éléments de la carte XML](/cells/fr/javascript-cpp/link-cells-to-xml-map-elements/)
