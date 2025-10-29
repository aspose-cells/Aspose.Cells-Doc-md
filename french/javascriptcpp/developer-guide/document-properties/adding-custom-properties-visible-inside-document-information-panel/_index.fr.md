---
title: Ajout de propriétés personnalisées visibles dans le panneau d informations sur le document avec JavaScript via C++
linktitle: Ajout de propriétés personnalisées visibles dans le volet Informations sur le document
type: docs
weight: 300
url: /fr/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Apprenez comment ajouter des propriétés personnalisées à un objet classeur en utilisant Aspose.Cells for JavaScript via C++. Ces propriétés peuvent être consultées dans le panneau d informations sur le document.
---

## **Ajout de propriétés personnalisées visibles dans le volet Informations sur le document**

Aspose.Cells for JavaScript via C++ peut être utilisé pour ajouter des propriétés personnalisées à l'intérieur de l'objet classeur qui sont visibles dans le panneau d'informations sur le document. Vous pouvez ouvrir le panneau d'informations sur le document dans Microsoft Excel en utilisant les commandes File > Info > Properties > Show Document Panel.

Veuillez utiliser la méthode [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/#add-string-string-) pour ajouter une propriété personnalisée qui sera visible dans le Panneau d'informations sur le document.

Le code d'exemple suivant ajoute deux propriétés personnalisées. La première propriété n'a pas de type, et la seconde a un type DateTime. Une fois que vous ouvrez le fichier Excel généré par ce code, vous verrez ces deux propriétés dans le Panneau d'informations sur le document.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook with Custom Properties</button>
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
            const workbook = new Workbook();

            // Add simple property without any type
            workbook.contentTypeProperties.add("MK31", "Simple Data");

            // Add date time property with type
            workbook.contentTypeProperties.add("MK32", "04-Mar-2015", "DateTime");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingCustomPropertiesVisible_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Article connexe**

{{% alert color="primary" %}}

- [Utiliser des parties XML personnalisées dans Aspose.Cells](/cells/fr/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
