---
title: Libérer les ressources non gérées du classeur avec JavaScript via C++
linktitle: Libérer les ressources non gérées du classeur
type: docs
weight: 310
url: /fr/javascript-cpp/release-unmanaged-resources-of-the-workbook/
description: Apprenez à libérer les ressources non gérées de l objet Workbook en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells fournit la méthode [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) pour libérer les ressources non gérées de l'objet [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). Le modèle de disposition est utilisé uniquement pour les objets qui accèdent à des ressources non gérées, telles que les poignées de fichiers et de tuyaux, les poignées de registre, les poignées d'attente, ou les pointeurs vers des blocs de mémoire non gérée. Cela est dû au fait que le ramasse-miettes est très efficace pour récupérer les objets gérés inutilisés, mais incapable de récupérer les objets non gérés.

{{% /alert %}}

L'objet [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) implémente maintenant l'interface *System.IDisposable* qui possède une seule méthode [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--). Vous pouvez soit appeler directement la méthode [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) ou utiliser la déclaration *Using* pour l'appeler automatiquement.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Dispose Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create workbook object
            const wb1 = new Workbook();

            // Call Dispose method
            wb1.dispose();

            // Call Dispose method via a scoped approach
            (async () => {
                const wb2 = new Workbook();
                // Any other code goes here
                wb2.dispose();
            })();

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully!</p>';
        });
    </script>
</html>
```
