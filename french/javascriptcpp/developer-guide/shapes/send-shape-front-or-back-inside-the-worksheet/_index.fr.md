---
title: Envoyer la forme en avant ou en arrière dans la feuille de calcul avec JavaScript via C++
linktitle: Envoyer une forme vers l avant ou vers l arrière à l intérieur de la feuille de calcul
type: docs
weight: 3400
url: /fr/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Apprenez comment envoyer une forme au premier plan ou à l’arrière dans une feuille en utilisant Aspose.Cells for JavaScript via C++. 
---

## **Scénarios d'utilisation possibles**

Lorsqu'il y a plusieurs formes au même endroit, leur visibilité est déterminée par leur position z-order. Aspose.Cells offre la méthode [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/javascript-cpp/shape/#toFrontOrBack-number-), qui modifie la position z-order de la forme. Pour envoyer une forme à l'arrière, utilisez un nombre négatif comme -1, -2, -3, etc., et pour amener une forme en avant, utilisez un nombre positif comme 1, 2, 3, etc.

## **Envoyer la forme à l'avant ou à l'arrière dans la feuille de calcul**

Le code exemple suivant explique l'utilisation de la méthode [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/javascript-cpp/shape/#toFrontOrBack-number-). Veuillez consulter le [fichier Excel d'exemple](50528330.xlsx) utilisé dans le code ainsi que le [fichier Excel de sortie](50528331.xlsx) généré. La capture d'écran montre l'effet du code sur le fichier Excel d'exemple lors de l'exécution.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Send Shapes Front or Back</title>
    </head>
    <body>
        <h1>Send Shapes to Front or Back Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Access first and fourth shapes
            const shape1 = worksheet.shapes.get(0);
            const shape4 = worksheet.shapes.get(3);

            // Print the Z-Order position of shape1
            resultDiv.innerHTML = `<p>Z-Order Shape 1: ${shape1.zOrderPosition}</p>`;

            // Send this shape to front
            shape1.toFrontOrBack(2);

            // Print the Z-Order position of shape4
            resultDiv.innerHTML += `<p>Z-Order Shape 4: ${shape4.zOrderPosition}</p>`;

            // Send this shape to back
            shape4.toFrontOrBack(-2);

            // Saving the modified Excel file and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputToFrontOrBack.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
