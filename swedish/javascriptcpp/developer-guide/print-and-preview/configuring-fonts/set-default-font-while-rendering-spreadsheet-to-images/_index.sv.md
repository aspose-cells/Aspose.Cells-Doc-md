---
title: Använd standardteckensnitt medan rendering av kalkylblad till bilder med JavaScript via C++
linktitle: Ange standardfont medan du renderar kalkylblad till bilder
type: docs
weight: 360
url: /sv/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Lär dig hur du sätter standardteckensnittet vid rendering av kalkylblad till bilder med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Använd egenskapen [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) för att ange standardfont medan du renderar kalkylblad till bilder. Denna egenskap kommer bara att vara effektiv när arbetsbokens standardfont inte kan rendera dina tecken. Den standardfont som anges med egenskapen [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) används för alla de celler som har ogiltiga eller obefintliga teckensnitt.

{{% /alert %}}

## Ange standardfont medan du renderar kalkylblad till bilder

 Följande exempel skapar en arbetsbok, lägger till lite text i cell A4 i det första kalkylbladet och ställer in dess font till en ogiltig eller icke-existerande font. Sedan tar den två bilder av kalkylbladet. Den första bilden tas genom att ställa in [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)-egenskapen till *Courier New* och den andra genom att ställa in [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)-egenskapen till *Times New Roman*.

Detta är utdatabilden efter att ha ställt in [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)-egenskapen till *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Detta är utdatabilden efter att ha ställt in [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)-egenskapen till *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Exempelkod

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Render Worksheet to Images with Default Fonts</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Courier New Image</a>
            <a id="downloadLink2" style="display: none;">Download Times New Roman Image</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, SheetRender } = AsposeCells;

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
            const result = document.getElementById('result');
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Read the selected file
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Set default font of the workbook to none
            let s = wb.defaultStyle;
            s.font.name = "";
            wb.defaultStyle = s;

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Access cell A4 and add some text inside it.
            const cell = ws.cells.get("A4");
            cell.value = "This text has some unknown or invalid font which does not exist.";

            // Set the font of cell A4 which is unknown.
            let st = cell.style;
            st.font.name = "UnknownNotExist";
            st.font.size = 20;
            st.isTextWrapped = true;
            cell.style = st;

            // Set first column width and fourth row height
            ws.cells.setColumnWidth(0, 80);
            ws.cells.setRowHeight(3, 60);

            // Create image or print options.
            const opts = new ImageOrPrintOptions();
            opts.onePagePerSheet = true;
            opts.imageType = ImageType.Png;

            // Render worksheet image with Courier New as default font.
            opts.defaultFont = "Courier New";
            let sr = new SheetRender(ws, opts);
            const imgData1 = sr.toImage(0);
            const blob1 = new Blob([imgData1], { type: 'image/png' });
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'out_courier_new_out.png';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Courier New Image';

            // Render worksheet image again with Times New Roman as default font.
            opts.defaultFont = "Times New Roman";
            sr = new SheetRender(ws, opts);
            const imgData2 = sr.toImage(0);
            const blob2 = new Blob([imgData2], { type: 'image/png' });
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'times_new_roman_out.png';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Times New Roman Image';

            result.innerHTML = '<p style="color: green;">Images rendered successfully! Use the download links to save the PNG files.</p>';
        });
    </script>
</html>
```
