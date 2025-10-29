---
title: 用 JavaScript 通过 C++ 设置页眉和页脚
linktitle: 设置页眉和页脚
type: docs
weight: 30
url: /zh/javascript-cpp/setting-headers-and-footers/
description: 本文介绍如何使用 Aspose.Cells for JavaScript 通过 C++ 编程在 Excel 工作表的页眉和页脚中插入图片。 
keywords: 在 Excel 页眉页脚中插入图片，使用 C++ 通过 JavaScript，设置 Excel 页眉页脚脚本命令
---

{{% alert color="primary" %}}

页眉和页脚是显示在顶部边距下方或底部边距上方的文本行。还可以将页眉和页脚添加到工作表中。页眉和页脚可用于显示有用的信息，如页码、作者姓名、主题名称或日期和时间。通过页面设置设置页眉和页脚。

{{% /alert %}}

## **设置页眉和页脚**

Aspose.Cells for JavaScript 通过 C++ 允许在运行时为工作表添加页眉和页脚，但我们建议在预设计的文件中手动设置页眉和页脚以便打印。你可以使用 Microsoft Excel 作为图形界面工具来设置页眉和页脚，以节省精力和开发时间。Aspose.Cells 可以导入文件并保存设置。

要在运行时添加页眉和页脚，Aspose.Cells提供了特殊的API调用和脚本命令来格式化页眉和页脚。

### **脚本命令**

脚本命令是特殊命令，允许您设置页眉和页脚的格式。

|**脚本命令**|**描述**|
| :- | :- |
当前页号||&P|
图片||&G|
总页数||&N|
|&D|当前日期|
|&T|当前时间|
|&A|工作表名称|
|&F|文件名（不含路径）|
|&&文本|显示 &文本。例如：&&WO 将显示为 &WO|
|&"\<FontName>"|表示字体名称。例如：&"Arial"|
|&"\<FontName>, \<FontStyle>"|表示带有样式的字体名称。例如：&"Arial,Bold"|
|&\<FontSize>|代表字体大小。例如：“&14abc”。但如果此命令后跟一个要在页眉中打印的普通数字，则应与字体大小用空格分隔。例如：“&14 123”。

### **设置页眉和页脚**

[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) 类提供两个方法，[**header(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-string-) 和 [**footer(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-string-)，用于向工作表添加页眉和页脚。这些方法只接受两个参数：

- **Section** – 应放置页眉或页脚的部分。有三个部分：左、中、右，分别由0、1和2表示。
- **Script** – 用于页眉或页脚的脚本。此脚本包含对页眉或页脚进行格式化的脚本命令。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Set Headers and Footers Example</h1>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            // Setting worksheet name at the left section of the header
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[0] = "&A";

            // Setting current date and current time at the central section of the header
            // and changing the font of the header
            pageSetup.header[1] = "&\"Times New Roman,Bold\"&D-&T";

            // Setting current file name at the right section of the header and changing the
            // font of the header
            pageSetup.header[2] = "&\"Times New Roman,Bold\"&12&F";

            // Setting a string at the left section of the footer and changing the font
            // of a part of this string ("123")
            pageSetup.footer = pageSetup.footer || [];
            pageSetup.footer[0] = "Hello World! &\"Courier New\"&14 123";

            // Setting the current page number at the central section of the footer
            pageSetup.footer[1] = "&P";

            // Setting page count at the right section of footer
            pageSetup.footer[2] = "&N";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetHeadersAndFooters_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers and footers set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **将图像插入页眉或页脚**

[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) 类还有两个额外的方法，[**headerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerPicture-number-numberarray-) 和 [**footerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerPicture-number-numberarray-)，用于在页眉和页脚中添加图片。这些方法接受的参数为：

- **Section** – 图片将放置的页眉或页脚部分。有三个部分：左、中、右，分别由值0、1和2表示。
- **字节数组** – 图形数据（二进制数据应写入字节数组的缓冲区）。

执行以下代码并打开文件后，请通过以下方式检查工作表的页眉：

1. 在 **文件** 菜单上，选择 **页面设置**。将显示一个对话框。
1. 选择 **页眉/页脚** 选项卡。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Image in Header/Footer Example</title>
    </head>
    <body>
        <h1>Insert Image in Header/Footer Example</h1>
        <p>Select an existing Excel file to modify (optional). If none is selected, a new workbook will be used.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select an image to insert into the header:</p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Insert Image into Header</button>
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
            const fileInput = document.getElementById('fileInput');
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the header.</p>';
                return;
            }

            // Read image bytes
            const imageFile = imageInput.files[0];
            const imageBuffer = await imageFile.arrayBuffer();
            const binaryData = new Uint8Array(imageBuffer);

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const excelBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(excelBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet's page setup
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Set the header picture and header scripts (converted from setters to properties)
            pageSetup.headerPicture = binaryData;
            pageSetup.header = "&G";
            pageSetup.header = "&A";

            // Save the workbook as Excel97-2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertImageInHeaderFooter_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Image inserted into header successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
