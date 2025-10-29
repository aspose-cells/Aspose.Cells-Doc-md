---
title: Gérer les propriétés du document avec JavaScript via C++
linktitle: Propriétés de document
type: docs
weight: 80
url: /fr/javascript-cpp/managing-document-properties/
description: Découvrez comment gérer les propriétés du document via les API Aspose.Cells for JavaScript via C++.
keywords: Comment gérer les propriétés du document en JavaScript via C++, obtenir ou définir les propriétés du document avec JavaScript via C++, ajouter ou supprimer des propriétés de document via JavaScript via C++, insérer ou supprimer des propriétés de document avec JavaScript via C++, comment accéder aux propriétés du document avec les API Aspose.Cells for JavaScript via C++.
---

## **Introduction**

Microsoft Excel permet d'ajouter des propriétés aux fichiers de feuille de calcul. Ces propriétés de document fournissent des informations utiles et sont divisées en 2 catégories comme détaillé ci-dessous.

- Propriétés système définies (intégrées) : Les propriétés intégrées contiennent des informations générales sur le document telles que le titre du document, le nom de l'auteur, les statistiques du document, etc.
- Propriétés utilisateur définies (personnalisées) : Propriétés personnalisées définies par l'utilisateur final sous forme de paire nom-valeur.

{{% alert color="primary" %}}

Le point le plus important à savoir sur les propriétés intégrées et personnalisées est que les propriétés intégrées peuvent être consultées et modifiées, mais pas créées ou supprimées. Cependant, les propriétés personnalisées peuvent être créées et gérées.

{{% /alert %}}

## **Comment gérer les propriétés de document à l'aide de Microsoft Excel**

Microsoft Excel permet de gérer les propriétés du document des fichiers Excel de manière WYSIWYG. Veuillez suivre les étapes ci-dessous pour ouvrir la boîte de dialogue **Propriétés** dans Excel 2016.

1. Dans le menu **Fichier**, sélectionnez **Infos**.

|**Sélection du menu Infos**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Cliquez sur le titre **Propriétés** et sélectionnez "Propriétés avancées".

|**Cliquez pour sélectionner les propriétés avancées**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Gérez les propriétés de document du fichier.

|**Boîte de dialogue des propriétés**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
Dans la boîte de dialogue des propriétés, il y a différents onglets, comme Général, Résumé, Statistiques, Contenu et Personnalisés. Chaque onglet aide à configurer différents types d'informations liées au fichier. L'onglet Personnalisé est utilisé pour gérer les propriétés personnalisées.

## **Comment travailler avec les propriétés de document à l'aide d'Aspose.Cells**

Les développeurs peuvent gérer dynamiquement les propriétés de document à l'aide des API Aspose.Cells. Cette fonctionnalité aide les développeurs à stocker des informations utiles avec le fichier, telles que la date de réception du fichier, le traitement, l'horodatage, etc.

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ écrit directement les informations sur l'API et le numéro de version dans les documents de sortie. Par exemple, lors de la conversion d’un document en PDF, Aspose.Cells for JavaScript via C++ remplit le champ **Application** avec la valeur 'Aspose.Cells' et le champ **Producteur PDF** avec la valeur, par exemple 'Aspose.Cells v17.9'.

Veuillez noter que vous ne pouvez pas demander à Aspose.Cells for JavaScript via C++ de changer ou de supprimer cette information des documents de sortie.

{{% /alert %}}

### **Comment accéder aux propriétés de document**

Les API Aspose.Cells supportent les deux types de propriétés de document, intégrées et personnalisées. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) de Aspose.Cells représente un fichier Excel et, comme un fichier Excel, la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) peut contenir plusieurs feuilles, chacune représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) tandis que la collection de feuilles est représentée par la classe [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection).

Utiliser [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) pour accéder aux propriétés du document du fichier comme décrit ci-dessous.

- Pour accéder aux propriétés de document intégrées, utilisez [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--).
- Pour accéder aux propriétés de document personnalisées, utilisez [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--).

Les deux, [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--) et [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--), renvoient l'instance de [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/). Cette collection contient [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) objets, chacun représentant une propriété de document intégrée ou personnalisée.

Il appartient à l'application de déterminer comment accéder à une propriété, c'est-à-dire en utilisant l'index ou le nom de la propriété à partir de [**DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/) comme illustré ci-dessous.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Document Properties</title>
    </head>
    <body>
        <h1>Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Load Document Properties</button>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object and opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Accessing a custom document property by using the property name
            const customProperty1 = customProperties.get("ContentTypeId");
            // Accessing the same custom document property by using the property index
            const customProperty2 = customProperties.get(0);

            const outputs = [];
            if (customProperty1) {
                outputs.push(`<p>${customProperty1.name} ${customProperty1.value}</p>`);
            }
            if (customProperty2) {
                outputs.push(`<p>${customProperty2.name} ${customProperty2.value}</p>`);
            }
            if (!outputs.length) {
                resultEl.innerHTML = '<p style="color: orange;">No custom document properties found.</p>';
            } else {
                resultEl.innerHTML = outputs.join('');
            }
        });
    </script>
</html>
```

La classe [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) permet de récupérer le nom, la valeur et le type de la propriété du document :

- Pour obtenir le nom de la propriété, utilisez [**DocumentProperty.name()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#name--).
- Pour obtenir la valeur de la propriété, utilisez [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--) retourne la valeur sous forme d'un Objet.
- Pour obtenir le type de la propriété, utilisez [**DocumentProperty.type()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#type--). Cela retourne une des valeurs d'énumération de [**PropertyType**](https://reference.aspose.com/cells/javascript-cpp/propertytype/). Après avoir obtenu le type de propriété, utilisez l'une des méthodes **DocumentProperty.ToXXX** pour obtenir la valeur du type approprié au lieu d'utiliser [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). Les méthodes **DocumentProperty.ToXXX** sont décrites dans le tableau ci-dessous.

{{% alert color="primary" %}}

La classe [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) fournit également un ensemble de méthodes qui retournent les valeurs d'autres types de données.

{{% /alert %}}

|**Nom du membre**|**Description**|**Méthode ToXXX**|
| :- | :- | :- |
|Boolean|Le type de données de la propriété est Boolean|ToBool|
|Date|Le type de données de la propriété est DateTime. Notez que Microsoft Excel ne stocke que la partie date, aucune heure ne peut être stockée dans une propriété personnalisée de ce type|ToDateTime|
|Float|Le type de données de la propriété est Double|ToDouble|
|Number|Le type de données de la propriété est Int32|ToInt|
|String| Le type de donnée de la propriété est string|ToString|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Retrieve Custom Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            let outputHtml = '<h2>Custom Document Properties</h2>';

            // Accessing a custom document property (first)
            const customProperty1 = customProperties.get(0);
            if (customProperty1) {
                // Storing the value of the document property as an object
                const objectValue = customProperty1.value;
                outputHtml += `<p><strong>${customProperty1.name}</strong> (type: ${customProperty1.type}) : ${objectValue}</p>`;
            } else {
                outputHtml += '<p>No first custom property found.</p>';
            }

            // Accessing a custom document property (second)
            const customProperty2 = customProperties.get(1);
            if (customProperty2) {
                // Checking the type of the document property and then storing the value according to that type
                if (customProperty2.type === AsposeCells.PropertyType.String) {
                    const value = customProperty2.value.toString();
                    outputHtml += `<p>${customProperty2.name} : ${value}</p>`;
                } else {
                    outputHtml += `<p>${customProperty2.name} (type: ${customProperty2.type}) : ${customProperty2.value}</p>`;
                }
            } else {
                outputHtml += '<p>No second custom property found.</p>';
            }

            resultDiv.innerHTML = outputHtml;
        });
    </script>
</html>
```

### **Comment ajouter ou supprimer des propriétés de document personnalisées**

Comme nous l'avons décrit précédemment au début de ce sujet, les développeurs ne peuvent pas ajouter ou supprimer des propriétés intégrées car ces propriétés sont système-définies, mais il est possible d'ajouter ou de supprimer des propriétés personnalisées car celles-ci sont définies par l'utilisateur.

### **Comment ajouter des propriétés personnalisées**

Les API Aspose.Cells ont exposé la méthode [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) pour la classe [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/) afin d'ajouter des propriétés personnalisées à la collection. La méthode [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) ajoute la propriété au fichier Excel et retourne une référence à la nouvelle propriété de document sous forme d'objet [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Custom Document Property</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object and opening the Excel file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Retrieve a list of all custom document properties of the Excel file
                const customProperties = workbook.customDocumentProperties;

                // Adding a custom document property to the Excel file
                customProperties.add("Publisher", "Aspose");

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'out_sample-document-properties.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Custom property added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```

### **Comment configurer la propriété de document personnalisée “Lien vers le contenu”**

Pour créer une propriété personnalisée liée au contenu d'une plage donnée, appelez la méthode [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) en passant le nom de la propriété et la source. Vous pouvez vérifier si une propriété est configurée comme liée au contenu en utilisant la propriété [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#isLinkedToContent--). De plus, il est également possible d'obtenir la plage source en utilisant la propriété [**source()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#source--) de la classe [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/).

Nous utilisons un fichier modèle Microsoft Excel simple dans l'exemple. Le classeur a une plage nommée définie étiquetée **MyRange** qui fait référence à une valeur de cellule.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Custom Document Properties</h1>
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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.worksheets.customDocumentProperties;

            // Add link to content.
            customProperties.addLinkToContent("Owner", "MyRange");

            // Accessing the custom document property by using the property name
            const customProperty1 = customProperties.get("Owner");

            // Check whether the property is linked to content
            const isLinkedToContent = customProperty1.isLinkedToContent;

            // Get the source for the property
            const source = customProperty1.source;

            // Save the file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = `<p style="color: green;">Operation completed successfully! Property linked: ${isLinkedToContent}. Source: ${source}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

### **Comment supprimer des propriétés personnalisées**

Pour supprimer des propriétés personnalisées avec Aspose.Cells, appelez la méthode [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/#remove-string-) et transmettez le nom de la propriété du document à supprimer.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Remove Custom Document Property Example</title>
    </head>
    <body>
        <h1>Remove Custom Document Property Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Removing a custom document property named "Publisher"
            customProperties.remove("Publisher");

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom property removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Sujets avancés**
- [Ajout de propriétés personnalisées visibles dans le volet Informations sur le document](/cells/fr/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.](/cells/fr/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Spécifier la version du document du fichier Excel à l'aide des propriétés de document intégrées](/cells/fr/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Spécifier la langue du fichier Excel en utilisant les propriétés de document intégrées](/cells/fr/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
