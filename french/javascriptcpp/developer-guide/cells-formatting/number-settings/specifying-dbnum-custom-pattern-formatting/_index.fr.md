---
title: Spécification du Format de Motif Personnalisé DBNum
linktitle: Spécification du Format de Motif Personnalisé DBNum
description: Aspose.Cells est une bibliothèque pour JavaScript via C++ qui supporte le formatage des dates et des nombres en utilisant des motifs de formatage personnalisés. Cet article montre comment spécifier le motif de format personnalisé dbnum pour un meilleur contrôle de l’affichage des nombres.
keywords: Aspose.Cells, JavaScript via C++, feuille de calcul électronique, motif de format personnalisé, mise en forme, dbnum , contrôle d affichage
type: docs
weight: 110
url: /fr/javascript-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells for JavaScript via C++ supporte le formatage de motif personnalisé *DBNum*. Par exemple, si la valeur de votre cellule est 123 et que vous spécifiez son format personnalisé comme [DBNum2][$-804]General, elle s'affichera comme 壹佰贰拾叁. Vous pouvez spécifier votre format personnalisé de cellule en utilisant la méthode [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) et la méthode [**Style.custom(string)**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-).

## **Code d'exemple**

Le code d'exemple suivant illustre comment spécifier un motif personnalisé *DBNum*. Veuillez consulter son [PDF de sortie](43352081.pdf) pour plus d’aide.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - DBNum Custom Formatting Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Access cell A1 and put value 123.
            const cell = ws.cells.get("A1");
            cell.value = 123;

            // Access cell style.
            const st = cell.style;

            // Specifying DBNum custom pattern formatting.
            st.custom = "[DBNum2][$-804]General";

            // Set the cell style.
            cell.style = st;

            // Set the first column width.
            ws.cells.columns.get(0).width = 30;

            // Save the workbook in output pdf format.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDBNumCustomFormatting.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
