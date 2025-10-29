---
title: Modifier l alignement des cellules et conserver la mise en forme existante
linktitle: Modifier l alignement des cellules et conserver la mise en forme existante
description: Utiliser la bibliothèque Aspose.Cells pour changer l alignement des cellules et préserver la mise en forme existante en JavaScript via C++
keywords: Aspose.Cells, JavaScript via C++, alignement des cellules, préserver la mise en forme existante
type: docs
weight: 340
url: /fr/javascript-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez changer l'alignement de plusieurs cellules tout en conservant la mise en forme existante. Aspose.Cells for JavaScript via C++ vous permet de le faire en utilisant la méthode [**StyleFlag.alignments(boolean)**](https://reference.aspose.com/cells/javascript-cpp/styleflag/#alignments-boolean-). Si vous la définissez sur **true**, les changements d'alignement seront appliqués, sinon non. Veuillez noter que l'objet [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) est passé en paramètre à la méthode [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-) qui applique réellement la mise en forme à une plage de cellules.

## **Modifier l'alignement des cellules et conserver la mise en forme existante**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338585.xlsx), crée la plage et centre l'alignement horizontalement et verticalement tout en conservant le formatage existant intact. La capture d'écran suivante compare le fichier Excel d'exemple et le [fichier Excel en sortie](67338586.xlsx) et montre que tout le formatage existant des cellules est le même, sauf que les cellules sont maintenant alignées au centre horizontalement et verticalement.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Cells Alignment and Keep Existing Formatting</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, TextAlignmentType, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create cells range
            const range = worksheet.cells.createRange("B2:D7");

            // Create style object
            const style = workbook.createStyle();

            // Set the horizontal and vertical alignment to center using property assignments
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            // Create style flag object
            const flag = new StyleFlag();
            flag.alignments = true; // Set style flag alignments true

            // Apply style to range of cells
            range.applyStyle(style, flag);

            // Save the workbook in XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
