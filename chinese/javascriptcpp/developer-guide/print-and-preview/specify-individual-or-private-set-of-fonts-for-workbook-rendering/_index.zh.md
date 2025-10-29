---
title: 使用JavaScript通过C++为工作簿渲染指定单独或私有的字体集
linktitle: 指定工作簿渲染的个体或私有字体集
type: docs
weight: 40
url: /zh/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: 学习如何使用C++的Aspose.Cells for JavaScript为工作簿渲染指定单独或私有的字体集。
---

## **可能的使用场景**  

通常情况下，你会为所有工作簿指定字体目录或字体列表，但有时你需要为你的工作簿指定单独或私有的字体集。C++的Aspose.Cells for JavaScript提供了[**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs)类，可用于为你的工作簿指定单独或私有的字体集。  

## **指定工作簿渲染的个体或私有字体集**  

以下示例加载了带有单独或私有字体集的 [示例Excel文件](67338268.xlsx)，使用 [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs) 类指定。请查看示例中的字体文件（67338271.zip）以及由其生成的 PDF（67338269.pdf）。截图显示如果字体成功找到，输出 PDF 的效果。  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Individual Or Private Fonts Example</title>
    </head>
    <body>
        <h1>Specify Individual Or Private Fonts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, IndividualFontConfigs } = AsposeCells;

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

            // Path of your custom font directory.
            const customFontsDir = "C:\\TempDir\\CustomFonts";

            // Specify individual font configs custom font directory.
            const fontConfigs = new IndividualFontConfigs();

            // If you comment this line or if custom font directory is wrong or 
            // if it does not contain required font then output pdf will not be rendered correctly.
            // Converted setFontFolder -> property assignment (first argument used)
            fontConfigs.fontFolder = customFontsDir;

            // Specify load options with font configs.
            const opts = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
            // Converted setFontConfigs -> property assignment
            opts.fontConfigs = fontConfigs;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file with individual font configs.
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save to PDF format.
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
