---
title: Afficher des puces en définissant la valeur de la cellule à l aide d HTML
type: docs
weight: 130
url: /fr/javascript-cpp/display-bullets-by-setting-cell-value-using/
description: Ajouter des puces aux cellules Excel en utilisant HTML avec le Script Aspose.Cells for JavaAPI C++ facile à utiliser.
keywords: ajouter des puces dans Excel JavaScript via C++, afficher des puces dans Excel JavaScript via C++, ajouter des puces dans Excel avec HTML JavaScript via C++, afficher des puces dans Excel avec HTML JavaScript via C++, ajouter des puces dans Excel en utilisant HTML JavaScript via C++
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge l'affichage de puces avec du code HTML. Cet article expliquera comment afficher des puces en définissant la valeur de la cellule en utilisant HTML. Nous utiliserons la méthode [**Cell.htmlString(string)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-string-) pour définir la valeur de la cellule avec notre HTML.

{{% /alert %}}

## Code JavaScript pour afficher des puces en définissant la valeur de la cellule avec HTML

Le code suivant utilise le code HTML pour définir la valeur de la cellule. Une fois que vous exécutez ce code, vous obtiendrez la sortie comme illustré dans l'image ci-dessous.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Bullets In Cells</title>
    </head>
    <body>
        <h1>Bullets In Cells Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set the HTML string (converted from setHtmlString -> htmlString property)
            cell.htmlString = "<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font><font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font><font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>";

            // Auto fit the Columns
            worksheet.autoFitColumns();

            // Save the workbook to a Blob and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'BulletsInCells_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File: BulletsInCells_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## Sortie générée par le code d'exemple

La capture d'écran suivante montre la sortie du code d'exemple ci-dessus.

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
