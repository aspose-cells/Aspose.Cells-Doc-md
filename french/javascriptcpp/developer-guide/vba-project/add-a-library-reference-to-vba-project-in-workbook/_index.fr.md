---
title: Ajouter une référence de bibliothèque au projet VBA dans le classeur avec JavaScript via C++
linktitle: Ajoutez une référence de bibliothèque au projet VBA dans le classeur
type: docs
weight: 80
url: /fr/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/
---

{{% alert color="primary" %}}

Parfois, vous devez ajouter ou enregistrer la référence de la bibliothèque dans le projet VBA par le biais du code. Vous pouvez le faire en utilisant la méthode Aspose.Cells [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/javascript-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-).

{{% /alert %}}

## **Ajouter une référence de bibliothèque au projet VBA dans Microsoft Excel**

Dans Microsoft Excel, vous pouvez ajouter une référence de bibliothèque au projet VBA en cliquant sur **Outils > Références...** manuellement.

## **Ajouter une référence de bibliothèque au projet VBA dans un classeur en utilisant Aspose.Cells for JavaScript via C++**

Le code d'exemple suivant ajoute ou enregistre deux références de bibliothèque au projet VBA du classeur en utilisant la méthode [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/javascript-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add VBA References Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            // Creating a new Workbook
            const workbook = new Workbook();

            // Accessing the VBA project (converted from getVbaProject())
            const vbaProj = workbook.vbaProject;

            // Accessing References collection (converted from getReferences())
            vbaProj.references.addRegisteredReference("stdole", "*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation");
            vbaProj.references.addRegisteredReference("Office", "*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library");

            // Saving the workbook as XLSM and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Generated XLSM File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA references added and file generated. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
