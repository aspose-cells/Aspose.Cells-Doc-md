---
title: 生成条件格式数据条形图像
linktitle: 生成条件格式数据条形图像
description: Aspose.Cells 是一个用于操作电子表格文件的 JavaScript 库。它支持生成有条件格式的数据条和图片，让用户可以根据单元格的值自定义电子表格的显示。本文将介绍如何使用 Aspose.Cells 库生成有条件格式的数据条和图片。
keywords: Aspose.Cells、条件格式、数据条、图片、电子表格、通过 C++ 的 JavaScript
type: docs
weight: 40
url: /zh/javascript-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

有时，您需要生成条件格式数据条的图像。您可以使用Aspose.Cells的[**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/javascript-cpp/databar/#toImage-cell-imageorprintoptions-)方法生成这些图像。本文展示了如何使用Aspose.Cells生成DataBar图像。

{{% /alert %}}

 以下示例代码生成单元格C1的DataBar图片。首先，它访问单元格的格式条件对象，然后从该对象访问 [**DataBar**](https://reference.aspose.com/cells/javascript-cpp/databar) ，并使用其 [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/javascript-cpp/databar/#toImage-cell-imageorprintoptions-) 方法生成单元格的图片。最后，它将图片保存到磁盘上。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Generate DataBar Image</title>
    </head>
    <body>
        <h1>Generate DataBar Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Creating a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell which contains conditional formatting databar
            const cell = worksheet.cells.get("C1");

            // Create and get the conditional formatting of the worksheet
            const idx = worksheet.conditionalFormattings.add();
            const fcc = worksheet.conditionalFormattings.get(idx);
            fcc.addCondition(AsposeCells.FormatConditionType.DataBar);
            fcc.addArea(AsposeCells.CellArea.createCellArea("C1", "C4"));

            // Access the conditional formatting databar
            const dbar = fcc.get(0).dataBar;

            // Create image or print options
            const opts = new AsposeCells.ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Png;

            // Get the image bytes of the databar
            const imgBytes = dbar.toImage(cell, opts);

            // Create a blob and provide download link
            const blob = new Blob([imgBytes], { type: "image/png" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGenerateDatabarImage.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Generated DataBar Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image generated successfully! Click the download link to save the PNG file.</p>';
        });
    </script>
</html>
```
