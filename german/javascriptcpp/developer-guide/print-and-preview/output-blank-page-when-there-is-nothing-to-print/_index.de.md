---
title: Leere Seite ausgeben, wenn nichts gedruckt werden soll, mit JavaScript via C++
linktitle: Leeres Blatt ausgeben, wenn nichts gedruckt werden muss
type: docs
weight: 90
url: /de/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **Mögliche Verwendungsszenarien**

Wenn das Blatt leer ist, druckt Aspose.Cells beim Exportieren des Arbeitsblatts in ein Bild nichts. Sie können dieses Verhalten ändern, indem Sie die [**ImageOrPrintOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#outputBlankPageWhenNothingToPrint--)-Eigenschaft verwenden. Wenn Sie sie auf **true** setzen, wird die leere Seite gedruckt.

## **Leeres Blatt ausgeben, wenn nichts gedruckt werden muss**

Das folgende Beispiel erstellt ein leeres Arbeitsbuch mit einem leeren Arbeitsblatt und rendert das leere Arbeitsblatt in ein Bild, nachdem die [**ImageOrPrintOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#outputBlankPageWhenNothingToPrint--)-Eigenschaft auf **true** gesetzt wurde. Dadurch wird die leere Seite generiert, da nichts gedruckt werden kann, siehe Bild unten.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Render Blank Sheet to PNG</title>
    </head>
    <body>
        <h1>Render Blank Sheet to PNG</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender, Utils } = AsposeCells;

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

            // Create or load workbook: if a file is provided, open it; otherwise create a new blank workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet - it is empty sheet for a new workbook or first sheet of provided workbook
            const ws = workbook.worksheets.get(0);

            // Specify image or print options
            // Since the sheet may be blank, set outputBlankPageWhenNothingToPrint to true
            const opts = new ImageOrPrintOptions();
            opts.imageType = ImageType.Png;
            opts.outputBlankPageWhenNothingToPrint = true;

            // Render empty sheet to png image
            const sr = new SheetRender(ws, opts);
            const imgData = sr.toImage(0);

            // Create downloadable blob and link
            const blob = new Blob([imgData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputBlankPageWhenNothingToPrint.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PNG Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the PNG file.</p>';
        });
    </script>
</html>
```
