---
title: Sadece Stil Kopyala JavaScript ile C++ üzerinden
linktitle: Sadece Aralık Stilini Kopyala
type: docs
weight: 620
url: /tr/javascript-cpp/copy-range-style-only/
description: Aspose.Cells for JavaScript C++ kullanarak sadece stilin nasıl kopyalanacağını öğrenin. 
---

{{% alert color="primary" %}}

[Sadece Aralık Verisini Kopyala](/cells/tr/javascript-cpp/copy-range-data-only/) ve [Stil ile Aralık Verisini Kopyala](/cells/tr/javascript-cpp/copy-range-data-with-style/) hücre aralığından başka bir aralığa veya tam biçimlendirmeyle nasıl kopyalanacağını açıkladı. Sadece biçimlendirmeyi de kopyalamak mümkündür. Bu makale nasıl yapıldığını gösterir.

{{% /alert %}} 

Bu örnek bir çalışma kitabı oluşturur, veri ile doldurur ve yalnızca bir aralığın stilini kopyalar.

1. Bir aralık oluştur.
1. Belirtilen biçimlendirme özellikleriyle bir `Stil` nesnesi oluşturun.
1. Stil biçimlendirmesini aralığa uygular.
1. Hücrelerin ikinci bir aralığını oluşturur.
1. İlk aralığın biçimlendirmesini ikinci aralığa kopyalar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Copy Range Style</h1>
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

            // Instantiate or load a Workbook.
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first Worksheet Cells.
            const cells = workbook.worksheets.get(0).cells;

            // Fill some sample data into the cells.
            for (let i = 0; i < 50; i++) {
                for (let j = 0; j < 10; j++) {
                    cells.get(i, j).putValue(i.toString() + "," + j.toString());
                }
            }

            // Create a range (A1:D3).
            const range = cells.createRange("A1", "D3");

            // Create a style object.
            const style = workbook.createStyle();
            // Specify the font attribute.
            style.font.name = "Calibri";
            // Specify the shading color.
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            // Specify the border attributes.
            const top = style.borders.get(AsposeCells.BorderType.TopBorder);
            top.lineStyle = AsposeCells.CellBorderType.Thin;
            top.color = AsposeCells.Color.Blue;

            const bottom = style.borders.get(AsposeCells.BorderType.BottomBorder);
            bottom.lineStyle = AsposeCells.CellBorderType.Thin;
            bottom.color = AsposeCells.Color.Blue;

            const left = style.borders.get(AsposeCells.BorderType.LeftBorder);
            left.lineStyle = AsposeCells.CellBorderType.Thin;
            left.color = AsposeCells.Color.Blue;

            const right = style.borders.get(AsposeCells.BorderType.RightBorder);
            right.lineStyle = AsposeCells.CellBorderType.Thin;
            right.color = AsposeCells.Color.Blue;

            // Create the styleflag object.
            const flag1 = new AsposeCells.StyleFlag();
            // Implement font attribute
            flag1.fontName = true;
            // Implement the shading / fill color.
            flag1.cellShading = true;
            // Implement border attributes.
            flag1.borders = true;
            // Set the Range style.
            range.applyStyle(style, flag1);

            // Create a second range (C10:E13).
            const range2 = cells.createRange("C10", "E13");

            // Copy the range style only.
            range2.copyStyle(range);

            // Saving the modified Excel file as XLS (Excel97To2003)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'copyrangestyle.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
