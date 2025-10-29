---
title: Créer un classeur partagé avec Aspose.Cells for JavaScript via C++
linktitle: Créer un classeur partagé avec Aspose.Cells
type: docs
weight: 40
url: /fr/javascript-cpp/create-shared-workbook-with-aspose-cells/
description: Découvrez comment créer un classeur partagé en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

Microsoft Excel vous permet de partager le classeur comme montré dans la capture d’écran ci-dessous. Lorsque vous partagez un classeur, plusieurs utilisateurs peuvent l’éditer sur le réseau. Aspose.Cells for JavaScript via C++ vous permet de créer un classeur partagé avec la propriété [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Créer un classeur partagé avec Aspose.Cells**  

Le code d'exemple suivant crée un classeur partagé en définissant la propriété [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--) à **true**. Lorsque vous ouvrez le [fichier Excel de sortie](55541786.xlsx) dans Microsoft Excel, vous verrez **Shared** avec le nom du classeur de sortie comme montré dans cette capture d'écran.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Shared Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="createShared" disabled>Create Shared Workbook</button>
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
            document.getElementById('createShared').disabled = false;
        });

        document.getElementById('createShared').addEventListener('click', async () => {
            const wb = new Workbook();

            // Share the Workbook (converted getter/setter to property)
            wb.settings.shared = true;

            // Save the Shared Workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Shared Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared workbook created successfully! Click the download link to save the file.</p>';
        });
    </script>
</html>
```
