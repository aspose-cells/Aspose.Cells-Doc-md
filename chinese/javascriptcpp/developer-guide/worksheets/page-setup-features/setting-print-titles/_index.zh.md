---
title: 如何用JavaScript通过C++设置打印标题
linktitle: 如何设置打印标题
type: docs
weight: 200
url: /zh/javascript-cpp/how-to-set-print-titles/
description: 本文向您展示了如何使用C++的JavaScript库设置打印标题。
keywords: 重复打印行和列，JavaScript如何设置打印标题，使用JavaScript设置和清除打印标题，在JavaScript中清除打印标题，使用JavaScript添加打印标题，使用JavaScript移除打印标题，在Excel中设置打印标题，清除Excel中的打印标题。  
---

## **可能的使用场景**  

在Excel中设置打印标题，确保每个打印页面重复特定的行或列，这对于跨多页的大型电子表格尤为有用。以下是设置打印标题的一些原因：  

1. 改善可读性：打印标题帮助读者理解数据，通过在每页保留标题，容易解读每页的信息，而无需回到第一页。  

1. 专业表现：在每一页上持续显示标题或标签，使打印的文档看起来更专业、更有条理。  

1. 改进导航：对于包含大量数据的文档，在每页重复显示标题有助于更快地进行导航和引用，减少来回翻页的次数。  

1. 减少错误：当每页都显示标题时，可以最大限度减少误解或数据录入错误的可能性，因为用户可以轻松查看数据的上下文。  

1. 一致性：确保重要信息（如列标题或行标签）始终可见，保持整个文档的一致性和清晰度。  

## **在 Excel 设置打印标题的方法**  

在 Excel 中设置打印标题，请按照以下步骤操作：  

1. 打开页面布局选项卡：点击 Excel 窗口顶部功能区中的“页面布局”。  
1. 访问打印标题：在“页面设置”组中，点击“打印标题”。  
1. 设置重复行：在“页面设置”对话框中，切换到“工作表”选项卡。在“打印标题”部分，点击“顶端重复的行”旁的框并选择要重复的行。  
1. 设置重复列（如需要）：类似地，你可以点击“左侧重复的列”旁的框，并选择要在每页重复的列。  
<br>  
<img src="3.png" width=60% />  

1. 确认并打印：点击“确定”以应用设置。在打印工作表时，指定的行或列将出现在每一页上。  

## **在 Excel 中清除打印标题的方法**  

要清除 Excel 中的打印标题，需要删除每页都设置为重复的行或列。操作如下：  

1. 打开页面布局选项卡：点击 Excel 窗口顶部功能区中的“页面布局”。  
1. 访问打印标题：在“页面设置”组中，点击“打印标题”。  
1. 清除打印标题：在“页面设置”对话框中，切换到“工作表”选项卡。删除“顶端重复的行”及“左侧重复的列”文本框中的内容。  
<br>  
<img src="4.png" width=60% />  

1. 确认并关闭：点击“确定”以应用更改。  

## **如何用C++的Aspose.Cells for JavaScript设置打印标题**  

要在特定工作表中设置打印标题：首先加载[示例文件](input.xlsx)，然后需要修改目标工作表的 [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) 和 [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) 属性，将这些属性设置为一个范围字符串即可设置打印标题。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Titles</title>
    </head>
    <body>
        <h1>Set Print Titles Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set rows to repeat at the top (e.g., rows 1 and 2)
            worksheet.pageSetup.printTitleRows = "$1:$2";

            // Set columns to repeat at the left (e.g., columns A and B)
            worksheet.pageSetup.printTitleColumns = "$A:$B";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

输出结果：  
<br>  
<img src="1.png" width=60% />  

## **如何用C++的Aspose.Cells for JavaScript清除打印标题**  

要清除特定工作表中的打印标题：首先加载[示例文件](input.xlsx)，然后需要修改目标工作表的 [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) 和 [**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--) 属性，将这些属性设置为空字符串即可清除打印标题。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Clear Print Titles Example</title>
    </head>
    <body>
        <h1>Clear Print Titles Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the rows and columns set to repeat
            worksheet.pageSetup.printTitleRows = "";
            worksheet.pageSetup.printTitleColumns = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

输出结果：  
<br>  
<img src="2.png" width=60% />
