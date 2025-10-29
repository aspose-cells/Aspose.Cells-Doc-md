---
title: Spécifiez le nom de l’Extrême Orient et le nom latin de la police dans les options de texte de la forme avec JavaScript via C++
linktitle: Spécifier le nom Extrême Orient et Latin de la police dans les options de texte de la Forme
type: docs
weight: 1600
url: /fr/javascript-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Apprenez comment spécifier les noms des polices de l’Extrême Orient etLatin dans les options de texte des formes en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

 Parfois, vous souhaitez afficher du texte dans une police de langue de l’Extrême-Orient, par exemple japonais, chinois, thaï, etc. Aspose.Cells for JavaScript via C++ offre la propriété [**TextOptions.farEastName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#farEastName--) qui peut être utilisée pour spécifier le nom de la police de la langue de l’Extrême-Orient. De plus, vous pouvez également spécifier le nom de la police latine en utilisant la propriété [**TextOptions.latinName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#latinName--).  

## **Spécifier le nom Extrême-Orient et Latin de la police dans les options de texte de la Forme**  

Le code d'exemple suivant crée une zone de texte et y ajoute du texte japonais. Il spécifie ensuite les noms de polices Latin et Far East du texte, puis enregistre le classeur en tant que [fichier Excel de sortie](67338274.xlsx). La capture d'écran suivante montre les noms de police Latin et Far East de la zone de texte en sortie dans Microsoft Excel.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Code d'exemple**  

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
