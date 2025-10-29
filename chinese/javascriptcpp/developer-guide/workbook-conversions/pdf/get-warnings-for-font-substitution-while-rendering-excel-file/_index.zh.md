---
title: 在使用JavaScript通过C++渲染Excel文件为PDF时，获取字体替换警告
linktitle: 在呈现Excel文件为PDF时，有时会进行字体替换。Aspose.Cells提供了一个功能，让开发人员知道特定字体已经被替换，从而发出警告。这是一个有用的功能，可以帮助您确定为什么Aspose.Cells呈现的PDF与实际Excel文件不同，并且您可以采取相应的措施。例如，您可以安装缺少的字体，以便呈现结果看起来一致。
type: docs
weight: 230
url: /zh/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: 学习如何在使用Aspose.Cells for Java脚本通过C++将Excel文件渲染为PDF时，获取字体替换的警告。
---

{{% alert color="primary" %}}  

有时，在将Microsoft Excel文件渲染为PDF时，Aspose.Cells会替换字体。Aspose.Cells提供了一个功能，通过触发警告来让开发人员知道特定字体已被替换。这是一个有用的功能，可以帮助您确定为何Aspose.Cells渲染的PDF与原始Microsoft Excel文件看起来不同，因此您可以采取适当的行动。例如，安装缺失的字体，以便渲染结果看起来相同。

{{% /alert %}}  

为了在将Excel文件渲染为PDF时获取字体替换警告，需实现IWarningCallback接口，并将PdfSaveOptions.warningCallback属性设置为您实现的接口。

下面的屏幕截图显示了我们将在以下代码中使用的源Excel文件。在单元格A6和A7中有一些文本，微软Excel无法正确呈现其中的字体。

|**并非所有字体都能正确呈现**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cells将使用合适的字体替换单元格A6和A7中的字体，如下所示。

|**替换字体**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **下载源文件和输出PDF**  
您可以从以下链接下载源Excel文件和输出PDF

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **代码**  
以下代码实现了IWarningCallback接口，并将PdfSaveOptions.warningCallback属性设置为实现的接口。现在，只要任何单元格中有字体被替换，Aspose.Cells就会在WarningCallback.Warning()方法内部触发警告。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - GetWarningsForFontSubstitution</title>
    </head>
    <body>
        <h1>GetWarningsForFontSubstitution Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

        class GetWarningsForFontSubstitution {
            static warning(info) {
                if (info.type === AsposeCells.WarningType.FontSubstitution) {
                    console.log("WARNING INFO: " + info.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare PDF save options and assign warning callback
            const options = new PdfSaveOptions();
            options.warningCallback = GetWarningsForFontSubstitution;

            // Save workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  
## **输出**  
将源Excel文件转换为PDF后，警告将输出到调试控制台，例如：

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用Workbook.calculateFormula方法。这样做将确保重新计算基于公式的值，并且在PDF中呈现正确的值。

{{% /alert %}}
