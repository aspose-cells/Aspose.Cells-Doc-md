---
title: 通过C++用JavaScript预览工作簿
linktitle: 预览工作簿 
type: docs
weight: 70
url: /zh/javascript-cpp/workbook-and-worksheet-preview/
description: Aspose.Cells支持使用JavaScript通过C++打印和预览Excel文件，无需安装Microsoft Excel。
---

## **打印预览**  

对于包含数百万页的Excel文件，转换为PDF或图片可能需要很长时间和大量资源。在这种情况下，工作簿和工作表的打印预览功能可能会很有帮助。在转换之前，用户可以检查总页数，然后决定是否转换该文件。本文重点介绍如何使用[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)类来统计总页数。  

Aspose.Cells提供了打印预览功能。API提供[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)类。要生成整个工作簿的打印预览，需要传入[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/)和[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/)对象实例化[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)类，创建它的实例。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)类提供一个[**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--)方法，返回预览中的总页数。与[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)类类似，[**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)类用来为特定工作表生成打印预览，创建实例时传入[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/)和[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/)对象，调用其构造函数。[**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)类还提供一个[**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--)方法，用于返回预览中的总页数。  

以下代码片段演示了如何使用[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/)类，配合[示例Excel文件](94896177.xlsx)。  

### **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Printing Preview</title>
    </head>
    <body>
        <h1>Printing Preview Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, WorkbookPrintingPreview, SheetPrintingPreview } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Creating image/print options
            const imgOptions = new ImageOrPrintOptions();

            // Workbook printing preview
            const preview = new WorkbookPrintingPreview(workbook, imgOptions);
            const workbookPageCount = preview.evaluatedPageCount;
            console.log("Workbook page count: " + workbookPageCount);

            // Worksheet printing preview for first worksheet
            const preview2 = new SheetPrintingPreview(workbook.worksheets.get(0), imgOptions);
            const worksheetPageCount = preview2.evaluatedPageCount;
            console.log("Worksheet page count: " + worksheetPageCount);

            document.getElementById('result').innerHTML = `<p>Workbook page count: ${workbookPageCount}</p><p>Worksheet page count: ${worksheetPageCount}</p>`;
        });
    </script>
</html>
```  

执行上述示例代码生成的输出如下。  

### **控制台输出**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **高级主题**  
- [为呈现电子表的字体进行配置](/cells/zh/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [将工作表转换为图像-去除数据周围的空白](/cells/zh/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [将工作表转为图像以及按页面转为图像](/cells/zh/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [使用ImageOrPrint Options将工作表转换为图像](/cells/zh/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [导出工作表中的单元格范围为图像](/cells/zh/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [使用所需的宽度和高度将工作表或图表导出为图像](/cells/zh/javascript-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [使用ImageOrPrintOptions从工作表中提取图像](/cells/zh/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [生成工作表的缩略图](/cells/zh/javascript-cpp/generate-thumbnail-of-the-worksheet/)  
- [当没有要打印的内容时输出空白页](/cells/zh/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [页面设置和打印选项](/cells/zh/javascript-cpp/page-setup-and-printing-options/)  
- [使用ImageOrPrintOptions的PageIndex和PageCount属性呈现页面序列](/cells/zh/javascript-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [将工作表渲染到图形上下文](/cells/zh/javascript-cpp/render-worksheet-to-graphic-context/)  
- [指定工作簿渲染的个体或私有字体集](/cells/zh/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
