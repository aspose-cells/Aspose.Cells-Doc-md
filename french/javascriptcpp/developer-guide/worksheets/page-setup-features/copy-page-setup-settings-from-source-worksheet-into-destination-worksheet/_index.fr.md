---
title: Copier les paramètres de mise en page d une feuille source vers une feuille de destination avec JavaScript via C++
linktitle: Copier les paramètres de mise en page de la feuille de calcul source dans la feuille de calcul de destination
type: docs
weight: 80
url: /fr/javascript-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Cet article explique comment utiliser l API JavaScript ou le code d exemple C++ pour copier les paramètres de mise en page d une feuille source vers une feuille de destination de manière programmatique.
keywords: Copier les paramètres de mise en page JavaScript via C++, copier les paramètres de mise en page vers la feuille cible JavaScript via C++
---

## **Scénarios d'utilisation possibles**

Lorsque vous ajoutez une nouvelle feuille à un classeur, elle contient les paramètres *Mise en page*. Il peut arriver que vous deviez transférer ces paramètres ([**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)) d'une feuille à une autre. Ce document explique comment copier les paramètres de mise en page d'une feuille à une autre en utilisant l'API Aspose.Cells for JavaScript via C++.

## **Copier les paramètres de configuration de la page de la feuille source dans la feuille de destination**

Le code d'exemple suivant illustre comment copier les *paramètres de configuration de la page* d'une feuille à une autre en utilisant la méthode [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#copy-pagesetup-copyoptions-). Veuillez consulter le code d'exemple suivant et sa sortie console pour référence.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Copy</title>
    </head>
    <body>
        <h1>PageSetup Copy Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CopyOptions, PaperSizeType, Utils } = AsposeCells;

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
            // Create workbook
            const wb = new Workbook();

            // Add two test worksheets
            wb.worksheets.add("TestSheet1");
            wb.worksheets.add("TestSheet2");

            // Access both worksheets as TestSheet1 and TestSheet2
            const TestSheet1 = wb.worksheets.get("TestSheet1");
            const TestSheet2 = wb.worksheets.get("TestSheet2");

            // Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
            TestSheet1.pageSetup.paperSize = PaperSizeType.PaperA3ExtraTransverse;

            // Print the Paper Size of both worksheets (before copy)
            const before1 = TestSheet1.pageSetup.paperSize;
            const before2 = TestSheet2.pageSetup.paperSize;

            // Copy the PageSetup from TestSheet1 to TestSheet2
            TestSheet2.pageSetup.copy(TestSheet1.pageSetup, new CopyOptions());

            // Print the Paper Size of both worksheets (after copy)
            const after1 = TestSheet1.pageSetup.paperSize;
            const after2 = TestSheet2.pageSetup.paperSize;

            // Display results
            document.getElementById('result').innerHTML =
                '<pre>' +
                'Before Paper Size (TestSheet1): ' + before1 + '\n' +
                'Before Paper Size (TestSheet2): ' + before2 + '\n\n' +
                'After Paper Size (TestSheet1): ' + after1 + '\n' +
                'After Paper Size (TestSheet2): ' + after2 +
                '</pre>';

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

## **Sortie console**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
