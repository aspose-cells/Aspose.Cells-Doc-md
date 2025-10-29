---
title: Fournir le chemin du fichier HTML de la feuille exportée via l interface IFilePathProvider avec JavaScript via C++
linktitle: Fournir le chemin du fichier HTML de la feuille de calcul exportée via l interface IFilePathProvider
type: docs
weight: 70
url: /fr/javascript-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Scénarios d'utilisation possibles**
Supposez que vous avez un fichier Excel avec plusieurs feuilles et que vous souhaitez exporter chaque feuille en un fichier HTML individuel. Si l'une de vos feuilles contient des liens vers d'autres feuilles, ces liens seront brisés dans le HTML exporté. Pour résoudre ce problème, Aspose.Cells for JavaScript via C++ fournit l'interface [IFilePathProvider](https://reference.aspose.com/cells/javascript-cpp/ifilepathprovider), que vous pouvez implémenter pour corriger les liens cassés.

## **Fournir le chemin du fichier HTML de la feuille de calcul exportée via l'interface IFilePathProvider**
Veuillez télécharger le [fichier Excel d'exemple](5115213.zip) utilisé dans le code ci-dessous et ses fichiers HTML exportés. Tous ces fichiers se trouvent dans le répertoire Temp. Vous devriez l'extraire sur le lecteur C:. Ensuite, il deviendra le répertoire C:\Temp. Ensuite, vous ouvrirez le fichier Sheet1.html dans le navigateur et cliquerez sur les deux liens à l’intérieur. Ces liens font référence à ces deux feuilles HTML exportées qui se trouvent dans le répertoire C:\Temp\OtherSheets.

{{< highlight javascript >}}
 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1
{{< /highlight >}}

La capture d'écran suivante montre à quoi ressemblent le C:\Temp\Sheet1.html et ses liens

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

La capture d'écran suivante montre la source HTML. Comme vous pouvez le constater, les liens font maintenant référence au répertoire C:\Temp\OtherSheets. Cela a été réalisé en utilisant l'interface [IFilePathProvider](https://reference.aspose.com/cells/javascript-cpp/ifilepathprovider).

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)

## **Code d'exemple**
Veuillez noter que le répertoire C:\Temp est uniquement à titre d'illustration. Vous pouvez utiliser n'importe quel répertoire de votre choix et y placer le [fichier Excel d'exemple](5115211.xlsx) puis exécuter le code fourni. Cela créera alors un sous-répertoire OtherSheets dans votre répertoire et exportera le HTML des deuxième et troisième feuilles de calcul à l’intérieur. Veuillez modifier la variable dirPath dans le code fourni pour la faire pointer vers le répertoire de votre choix avant l'exécution.

{{% alert color="primary" %}} 

Le code d'exemple ne fonctionnera que lorsque vous aurez défini la licence Aspose.Cells. Si vous essayez d'exécuter le code sans définir la licence, il entrera dans une boucle infinie. C'est pourquoi nous avons ajouté une vérification pour afficher un message et arrêter l'exécution si la licence n’est pas définie. Vous pouvez soit acheter une licence, soit demander une licence temporaire de 30 jours à l'équipe Aspose.Purchase.

{{% /alert %}} 

Notez que commenter ces lignes dans le code annulera les liens dans Sheet1.html, et Sheet2.html ou Sheet3.html ne s'ouvriront pas lorsque leurs liens seront cliqués dans Sheet1.html.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Worksheet to HTML with FilePathProvider Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

        // Implementation of IFilePathProvider for browser
        class FilePathProvider extends AsposeCells.IFilePathProvider {
            constructor() {
                super();
            }

            // Converted method name from getFullName -> fullName per universal getter/setter conversion rule
            fullName(sheetName) {
                if (sheetName === "Sheet2") {
                    return "file:///OtherSheets/Sheet2.html";
                } else if (sheetName === "Sheet3") {
                    return "file:///OtherSheets/Sheet3.html";
                }
                return "";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and assign FilePathProvider (converted setter to property assignment)
            const options = new HtmlSaveOptions();
            options.filePathProvider = new FilePathProvider();

            // Save workbook to HTML using options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - IFilePathProvider</title>
    </head>
    <body>
        <h1>Aspose.Cells IFilePathProvider Example (Browser)</h1>
        <p>Select the Sample_filepath.xlsx file to export worksheets to separate HTML files.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <div id="links"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

        // Implementation of IFilePathProvider interface for browser
        class FilePathProvider extends AsposeCells.IFilePathProvider {
            constructor() {
                super();
            }

            // Gets the full path of the file by worksheet name when exporting worksheet to html separately.
            // So the references among the worksheets could be exported correctly.
            getFullName(sheetName) {
                if (sheetName === "Sheet2") {
                    return "file:///OtherSheets/Sheet2.html";
                } else if (sheetName === "Sheet3") {
                    return "file:///OtherSheets/Sheet3.html";
                }
                return "";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const linksDiv = document.getElementById('links');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select the Sample_filepath.xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Check license
            if (!workbook.isLicensed()) {
                resultDiv.innerHTML = '<p style="color: red;">You must set the license to execute this code successfully.</p>';
                return;
            }

            // Export each worksheet to separate HTML using HtmlSaveOptions and FilePathProvider
            const sheetCount = workbook.worksheets.count;

            for (let i = 0; i < sheetCount; i++) {
                // Set the active worksheet to current index
                workbook.worksheets.activeSheetIndex = i;

                // Create html save option
                const options = new HtmlSaveOptions();
                options.exportActiveWorksheetOnly = true;
                // Provide file path provider so hyperlinks among sheets are preserved correctly
                options.filePathProvider = new FilePathProvider();

                // Save the active worksheet to HTML (returns Uint8Array)
                const outputData = workbook.save(SaveFormat.Html, options);

                // Create downloadable blob for the HTML
                const blob = new Blob([outputData], { type: 'text/html' });

                // Determine filename similar to original logic
                const sheetIndex = i + 1;
                let filename = '';
                if (i === 0) {
                    filename = 'Sheet1.html';
                } else {
                    filename = `OtherSheets_Sheet${sheetIndex}_out.html`;
                }

                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = filename;
                link.textContent = 'Download ' + filename;
                link.style.display = 'block';
                linksDiv.appendChild(link);
            }

            resultDiv.innerHTML = '<p style="color: green;">Worksheets exported successfully! Use the links below to download each HTML file.</p>';
        });
    </script>
</html>
```
