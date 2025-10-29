---
title: Protéger ou déprotéger par mot de passe le classeur partagé avec JavaScript via C++
linktitle: Protéger par mot de passe ou désactiver la protection de la feuille de calcul partagée
type: docs
weight: 10
url: /fr/javascript-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Scénarios d'utilisation possibles**

Vous pouvez protéger ou déprotéger le classeur partagé avec Microsoft Excel comme illustré dans la capture d'écran suivante. Aspose.Cells for JavaScript via C++ supporte également cette fonctionnalité avec les méthodes [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#protectSharedWorkbook-string-) et [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Protéger par mot de passe ou désactiver la protection de la feuille de calcul partagée**

Le code d'exemple suivant crée un classeur et le protège tout en activant le partage, puis le sauvegarde en tant que [fichier Excel de sortie](55541777.xlsx). La capture d'écran montre que lorsque vous essayez de le déprotéger, Microsoft Excel vous invite à entrer le mot de passe pour le déprotéger.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Shared Workbook Example</h1>
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
            // Creating an empty Workbook
            const workbook = new Workbook();

            // Protect the Shared Workbook with Password
            workbook.protectSharedWorkbook("1234");

            // Uncomment this line to Unprotect the Shared Workbook
            // workbook.unprotectSharedWorkbook("1234");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputProtectSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
