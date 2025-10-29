---
title: Exporter une plage de cellules d une feuille de calcul en image avec JavaScript via C++
linktitle: Exporter la plage de cellules dans une feuille de calcul en tant qu image
type: docs
weight: 60
url: /fr/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/
---

## **Scénarios d'utilisation possibles**  

Vous pouvez réaliser une image d'une feuille de calcul en utilisant Aspose.Cells for JavaScript via C++. Cependant, parfois vous devez exporter uniquement une plage de cellules en image. Cet article explique comment accomplir cela.  

## **Exporter une plage de cellules d'une feuille de calcul vers une image**  

Pour prendre une image d'une plage, définissez la zone d'impression sur la plage souhaitée, puis réglez toutes les marges à 0. Configurez également [**ImageOrPrintOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#onePagePerSheet--) sur **true**. Le code suivant capture une image de la plage D8:G16. Ci-dessous, une capture d'écran du [fichier Excel d'exemple](47153160.xlsx) utilisé dans le code. Vous pouvez essayer le code avec n'importe quel fichier Excel.  

## **Capture d'écran du fichier Excel d'exemple et de son image exportée**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

L'exécution du code crée une image de la plage D8:G16 seulement.  

**![todo:image_alt_text](Output-Image.png)**  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Range To Image</title>
    </head>
    <body>
        <h1>Export Range Of Cells In Worksheet To Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender } = AsposeCells;

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

            // Create workbook from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the print area with your desired range
            worksheet.pageSetup.printArea = "D8:G16";

            // Set all margins as 0
            worksheet.pageSetup.leftMargin = 0;
            worksheet.pageSetup.rightMargin = 0;
            worksheet.pageSetup.topMargin = 0;
            worksheet.pageSetup.bottomMargin = 0;

            // Set OnePagePerSheet option as true and image options
            const options = new ImageOrPrintOptions();
            options.onePagePerSheet = true;
            options.imageType = ImageType.Jpeg;
            options.horizontalResolution = 200;
            options.verticalResolution = 200;

            // Take the image of your worksheet
            const sr = new SheetRender(worksheet, options);
            const outputData = sr.toImage(0);

            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportRangeOfCellsInWorksheetToImage.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image exported successfully! Click the download link to download the image.</p>';
        });
    </script>
</html>
```
