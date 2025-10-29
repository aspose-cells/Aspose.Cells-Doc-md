---
title: Ajout de texte enrichi HTML dans la cellule
linktitle: Valeur de chaîne HTML
type: docs
weight: 50
url: /fr/javascript-cpp/adding-html-rich-text-inside-the-cell/
description: Apprenez comment ajouter du texte enrichi HTML dans la cellule via l API Script Aspose.Cells for Java via C++.
keywords: Ajouter du texte enrichi HTML dans la cellule JavaScript via C++, Définir du texte enrichi HTML dans la cellule JavaScript via C++, Ajouter du texte HTML enrichi dans la cellule JavaScript via C++
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion de HTML orienté Microsoft Excel en format XLS/XLSX. Cela signifie que le HTML généré par Microsoft Excel peut être reconverti en format XLS/XLSX à l'aide d'Aspose.Cells.

De même, s'il y a un HTML simple, Aspose.Cells peut le convertir en texte enrichi HTML. Aspose.Cells fournit la propriété [**Cell.htmlString**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-) qui peut prendre un HTML simple et le convertir en texte de cellule formaté.

{{% /alert %}}

L'exemple de code ci-dessous vous montre comment ajouter du texte enrichi HTML dans la cellule. Veuillez consulter la capture d'écran du fichier Excel de sortie.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells HTML String Example</h1>
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
            let workbook;

            // If a file is provided, open it; otherwise create a new workbook
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set HTML formatted string to the cell (converted setter -> property)
            cell.htmlString = "<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML string written to A1. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## Articles Connexes

- [Afficher des puces en définissant la valeur de la cellule à l'aide de HTML](/cells/fr/javascript-cpp/display-bullets-by-setting-cell-value-using/)
- [Obtenir une chaîne HTML5 à partir de la cellule](/cells/fr/javascript-cpp/get-html5-string-from-cell/)
