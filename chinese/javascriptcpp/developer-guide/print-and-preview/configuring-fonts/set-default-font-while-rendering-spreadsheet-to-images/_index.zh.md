---
title: 使用C++的JavaScript设置渲染到图片的电子表格的默认字体
linktitle: 在将电子表格呈现为图像时设置默认字体
type: docs
weight: 360
url: /zh/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: 学习如何使用C++中的Aspose.Cells for JavaScript在渲染电子表格为图片时设置默认字体。 
---

{{% alert color="primary" %}}

请使用[**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)属性将默认字体设置为渲染电子表格为图像时的默认字体。仅当工作簿的默认字体无法呈现您的字符时，才会使用[**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)属性指定的默认字体。指定的默认字体将用于所有缺少或不存在的字体的单元格。

{{% /alert %}}

## 渲染电子表格为图像时设置默认字体

以下示例代码创建了一个工作簿，在第一个工作表的单元格 A4 中添加一些文本，并将其字体设置为无效或不存在的字体。然后，分别用 [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) 属性设置为 *Courier New* 和 [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) 属性设置为 *Times New Roman* 来获取两个电子表格图片。

这是将 [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) 属性设置为 *Courier New* 后的输出图片。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

这是将 [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) 属性设置为 *Times New Roman* 后的输出图片。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## 示例代码

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
