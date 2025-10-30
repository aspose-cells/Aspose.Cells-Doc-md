---
title: Der fernöstliche und lateinische Name der Schriftart in den Texteinstellungen des Shapes mit JavaScript über C++ angeben
linktitle: Den Fernost und Lateinischen Namen der Schriftart in den Textoptionen der Form festlegen
type: docs
weight: 1600
url: /de/javascript-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Erfahren Sie, wie Sie fernöstliche und lateinische Schriftartnamen in den Texteinstellungen von Shapes mit Aspose.Cells for JavaScript über C++ angeben.
---

## **Mögliche Verwendungsszenarien**  

Manchmal möchten Sie Text in einer fernöstlichen Sprache, z.B. Japanisch, Chinesisch, Thailändisch, anzeigen. Aspose.Cells for JavaScript über C++ bietet die Eigenschaft [**TextOptions.farEastName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#farEastName--), mit der der Name der fernöstlichen Schriftart festgelegt werden kann. Außerdem können Sie den lateinischen Schriftartnamen mit der Eigenschaft [**TextOptions.latinName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#latinName--) angeben.  

## **Den Fernost- und Lateinischen Namen der Schriftart in den Textoptionen der Form festlegen**  

Das folgende Beispiel erstellt eine Textbox und fügt some Japanischen Text darin ein. Es gibt dann die lateinischen und Fernost-Schriftartnamen des Textes an und speichert die Arbeitsmappe als [Ausgabe-Excel](67338274.xlsx). Der folgende Screenshot zeigt die lateinischen und Fernost-Schriftartnamen der Ausgabetextbox in Microsoft Excel.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Far East and Latin Name of Font in TextOptions of Shape</h1>
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
            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Add textbox inside the worksheet.
            const idx = ws.textBoxes.add(5, 5, 50, 200);
            const tb = ws.textBoxes.get(idx);

            // Set the text of the textbox.
            tb.text = "こんにちは世界";

            // Specify the Far East and Latin name of the font.
            tb.textOptions.latinName = "Comic Sans MS";
            tb.textOptions.farEastName = "KaiTi";

            // Save the output Excel file.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
