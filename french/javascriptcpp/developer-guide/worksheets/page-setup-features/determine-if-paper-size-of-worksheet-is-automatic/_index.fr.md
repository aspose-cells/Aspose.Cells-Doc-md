---
title: Déterminer si la taille du papier de la feuille est automatique avec JavaScript via C++
linktitle: Déterminer si la taille du papier de la feuille de calcul est automatique
type: docs
weight: 90
url: /fr/javascript-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Cet article explique comment utiliser l API JavaScript avec des addons C++ pour déterminer si la taille du papier d une feuille est réglée sur automatique de manière programmée.
keywords: déterminer si la taille du papier de la feuille est automatique JavaScript via C++
---

## **Scénarios d'utilisation possibles**

La plupart du temps, la taille du papier de la feuille est automatique. Lorsqu’elle est automatique, elle est souvent réglée sur *Letter*. Parfois, l’utilisateur configure la taille du papier selon ses besoins. Dans ce cas, la taille n’est pas automatique. Vous pouvez vérifier si la taille du papier de la feuille est automatique ou non en utilisant la propriété [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isAutomaticPaperSize--).

## **Déterminer si la taille du papier de la feuille de calcul est automatique**

Le code d'exemple ci-dessous charge les deux fichiers Excel suivants

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

et détermine si la taille du papier de leur première feuille de calcul est automatique ou non. Dans Microsoft Excel, vous pouvez vérifier si la taille du papier est automatique ou non via la fenêtre de configuration de la page comme indiqué dans cette capture d'écran.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup IsAutomaticPaperSize</title>
    </head>
    <body>
        <h1>PageSetup IsAutomaticPaperSize Example</h1>
        <p>Select two Excel files to compare the PageSetup.isAutomaticPaperSize property:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx,.csv" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx,.csv" />
        <br/><br/>
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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');
            const resultDiv = document.getElementById('result');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select both Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Instantiating Workbook objects from uploaded files
            const wb1 = new Workbook(new Uint8Array(arrayBuffer1));
            const wb2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Access first worksheet of both workbooks
            const ws11 = wb1.worksheets.get(0);
            const ws12 = wb2.worksheets.get(0);

            // Read the PageSetup.isAutomaticPaperSize property of both worksheets
            const isAuto1 = ws11.pageSetup.isAutomaticPaperSize;
            const isAuto2 = ws12.pageSetup.isAutomaticPaperSize;

            // Display results
            resultDiv.innerHTML = `
                <p>First Worksheet of First Workbook - IsAutomaticPaperSize: ${isAuto1}</p>
                <p>First Worksheet of Second Workbook - IsAutomaticPaperSize: ${isAuto2}</p>
            `;
        });
    </script>
</html>
```

## **Sortie console**



{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
