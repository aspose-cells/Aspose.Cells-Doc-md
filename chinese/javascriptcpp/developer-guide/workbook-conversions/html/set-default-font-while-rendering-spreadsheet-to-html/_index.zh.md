---
title: 使用 JavaScript 通过 C++ 为 HTML 渲染的电子表格设置默认字体
linktitle: 在将电子表格渲染为HTML时设置默认字体
type: docs
weight: 370
url: /zh/javascript-cpp/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}
Aspose.Cells允许在将电子表格渲染为HTML时设置默认字体. 请使用[**HtmlSaveOptions.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#defaultFontName--)来实现此目的. 当电子表格中有一些单元格具有无效或不存在的字体时, 特定于[**HtmlSaveOptions.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#defaultFontName--)属性指定的字体将进行渲染.
{{% /alert %}}

## 在将电子表格渲染为HTML时设置默认字体

以下示例代码创建一个工作簿，并在第一个工作表的B4单元格中添加了一些文本，并将其字体设置为某个未知/不存在的字体。然后，它通过设置不同的默认字体名称，如Courier New、Arial、Times New Roman等，将工作簿保存为HTML。

截图显示通过[**HtmlSaveOptions.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#defaultFontName--)属性设置不同默认字体名的效果。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

该代码生成了使用Courier New的[output HTML文件](5115516), 使用Arial的[output HTML文件](5115518), 以及使用Times New Roman的[output HTML文件](5115517).

## 示例代码

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none;">Download Result 1</a><br/>
        <a id="downloadLink2" style="display: none;">Download Result 2</a><br/>
        <a id="downloadLink3" style="display: none;">Download Result 3</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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
            // Creating a new workbook and accessing first worksheet.
            const wb = new Workbook();
            const ws = wb.worksheets.get(0);

            // Access cell B4 and add some text inside it.
            const cell = ws.cells.get("B4");
            cell.value = "This text has some unknown or invalid font which does not exist.";

            // Set the font of cell B4 which is unknown.
            const st = cell.style;
            st.font.name = "UnknownNotExist";
            st.font.size = 20;
            cell.style = st;

            // Prepare HtmlSaveOptions and save three variants with different default fonts.
            const opts = new HtmlSaveOptions();

            // 1) Default font Courier New
            opts.defaultFontName = "Courier New";
            const outputData1 = wb.save(SaveFormat.Html, opts);
            const blob1 = new Blob([outputData1], { type: "text/html" });
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'out_courier_new_out.htm';
            downloadLink1.style.display = 'block';
            downloadLink1.textContent = 'Download out_courier_new_out.htm';

            // 2) Default font Arial
            opts.defaultFontName = "Arial";
            const outputData2 = wb.save(SaveFormat.Html, opts);
            const blob2 = new Blob([outputData2], { type: "text/html" });
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'out_arial_out.htm';
            downloadLink2.style.display = 'block';
            downloadLink2.textContent = 'Download out_arial_out.htm';

            // 3) Default font Times New Roman
            opts.defaultFontName = "Times New Roman";
            const outputData3 = wb.save(SaveFormat.Html, opts);
            const blob3 = new Blob([outputData3], { type: "text/html" });
            const downloadLink3 = document.getElementById('downloadLink3');
            downloadLink3.href = URL.createObjectURL(blob3);
            downloadLink3.download = 'times_new_roman_out.htm';
            downloadLink3.style.display = 'block';
            downloadLink3.textContent = 'Download times_new_roman_out.htm';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated successfully. Click the download links above to save the HTML files.</p>';
        });
    </script>
</html>
```
