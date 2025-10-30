---
title: Stil ile birlikte Aralık Verisini Kopyala JavaScript ile C++ üzerinden
linktitle: Stil ile Aralık Verileri Kopyalama
type: docs
weight: 610
url: /tr/javascript-cpp/copy-range-data-with-style/
description: Aspose.Cells for JavaScript C++ kullanarak biçimlendirmeyle birlikte hücre aralığını nasıl kopyalayacağınızı öğrenin.
---

{{% alert color="primary" %}}

[Sadece Aralık Verisini Kopyala](/cells/tr/javascript-cpp/copy-range-data-only/) hücre aralığından başka bir aralığa veri kopyalamayı nasıl yapılacağını açıkladı. Özellikle, kopyalanan hücrelere yeni bir stil seti uygular. Aspose.Cells ayrıca biçimlendirmeyle birlikte bütün bir aralığı kopyalayabilir. Bu makale nasıl yapıldığını açıklar.

{{% /alert %}}

Aspose.Cells, örneğin [**createRange(string, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-), [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag/) ve [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/cells/#applyStyle-style-styleflag-) gibi aralıklarla çalışmak için bir dizi sınıf ve yöntem sağlar.

Bu örnek:

1. Bir çalışma kitabı oluşturur.  
2. Birinci sayfadaki bir dizi hücreyi veriyle doldurur.  
3. Bir [**Range**](https://reference.aspose.com/cells/javascript-cpp/range/) oluşturur.  
4. Belirtilen biçimlendirme özellikleriyle bir [**Style**](https://reference.aspose.com/cells/javascript-cpp/style/) nesnesi oluşturur.  
5. Bu stili veri aralığına uygular.  
6. İkinci bir hücre aralığı oluşturur.  
7. Birinci aralıktaki veriyi ve biçimlendirmeyi ikinci aralığa kopyalar.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy Range Example</h1>
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
            if (fileInput.files.length && fileInput.files[0]) {
                // If a file is provided, open it and modify
            } else {
                // No file provided, will create a new workbook
            }

            // Instantiate or load workbook
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
                    cells.get(i, j).value = `${i},${j}`;
                }
            }

            // Create a range (A1:D3).
            const range = cells.createRange("A1", "D3");

            // Create a style object.
            let style = workbook.createStyle();
            // Specify the font attribute.
            style.font.name = "Calibri";
            // Specify the shading color.
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            // Specify the border attributes.
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Blue;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Blue;

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

            // Create a second range (C10:F12).
            const range2 = cells.createRange("C10", "F12");

            // Copy the range data with formatting.
            range2.copy(range);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyRange.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
