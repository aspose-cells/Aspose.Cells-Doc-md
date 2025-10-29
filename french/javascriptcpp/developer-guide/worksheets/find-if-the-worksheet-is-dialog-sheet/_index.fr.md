---
title: Trouver si la feuille est une feuille de dialogue avec JavaScript via C++
linktitle: Vérifier si la feuille de calcul est une feuille de dialogue
type: docs
weight: 90
url: /fr/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Cet article fournit des instructions et un code d exemple pour déterminer de manière programmatique si une feuille Excel est une feuille de dialogue en utilisant Aspose.Cells for JavaScript via C++.
keywords: trouver le type de dialogue d une feuille Excel JavaScript via C++, script de dialogue de feuille JavaScript via C++
---

## **Scénarios d'utilisation possibles**

 La feuille de dialogue est un ancien format de feuille qui contient une boîte de dialogue. Une telle feuille peut être insérée par une version plus ancienne de Microsoft Excel, par exemple 2003, comme montré dans cette capture d'écran. Elle peut également être insérée avec VBA dans les versions plus récentes, par exemple Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

 Vous pouvez déterminer si la feuille est une feuille de dialogue ou un autre type de feuille avec la propriété [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--) fournie par Aspose.Cells for JavaScript via C++. Si elle retourne la valeur d'énumération [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype), cela signifie que vous avez affaire à une feuille de dialogue.

## **Trouver si la Feuille de calcul est une Feuille de dialogue**

 Le code d'exemple suivant charge le [fichier Excel d'exemple](64716820.xlsx) contenant une feuille de dialogue. Il vérifie la propriété [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--), la compare avec [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype), puis affiche le message. Veuillez consulter la sortie console du code d'exemple ci-dessous pour plus d'aide.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Detect Dialog Sheet</title>
    </head>
    <body>
        <h1>Detect if Worksheet Is a Dialog Sheet</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Find if the sheet type is dialog and print the message
            if (ws.type === AsposeCells.SheetType.Dialog) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet is a Dialog Sheet.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is NOT a Dialog Sheet.</p>';
            }
        });
    </script>
</html>
```

## **Sortie console**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
