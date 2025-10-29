---
title: 应用Microsoft Excel的高级筛选以显示符合复杂条件的记录
type: docs
weight: 280
url: /zh/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: 学习如何通过C++ API使用Aspose.Cells for JavaScript应用Microsoft Excel的高级筛选以显示满足复杂标准的记录。
keywords: 通过C++应用高级筛选JavaScript，设置高级筛选JavaScript，添加高级筛选JavaScript，创建高级筛选JavaScript，如何将高级筛选添加到范围JavaScript
---

## **可能的使用场景**  

Microsoft Excel允许在工作表数据上应用*高级筛选*以显示满足复杂条件的记录。你可以通过*数据 > 高级*命令应用高级筛选，如此截屏所示。  

![todo:image_alt_text](1.png)  

Aspose.Cells for JavaScript通过C++还允许你使用[**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-)方法应用高级筛选。就像Microsoft Excel一样，它接受以下参数。  

**isFilter**  

-**listRange**- 列表范围。  

-**criteriaRange**- 条件范围。  

列表范围。  

**criteriaRange**  

条件范围。  

**copyTo**  

拷贝数据的范围。  

**uniqueRecordOnly**  

仅显示或拷贝唯一行。  

## **将 Microsoft Excel 的高级筛选应用于显示符合复杂条件的记录**  

以下示例代码在[示例Excel文件](48496692.xlsx)上应用高级筛选，并生成[输出Excel文件](48496691.xlsx)。截图显示两个文件以供比较。如截图所示，数据已根据复杂条件在输出Excel文件中被筛选。  

![todo:image_alt_text](2.png)  

## **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Advanced Filter Example</title>
    </head>
    <body>
        <h1>Advanced Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Advanced Filter</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (sampleAdvancedFilter.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const wb = new Workbook(new Uint8Array(arrayBuffer));

            const ws = wb.worksheets.get(0);

            // Apply advanced filter on range A5:D19 with criteria A1:D2, filter in place, include all records (not unique)
            ws.advanced_Filter(true, "A5:D19", "A1:D2", "", false);

            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAdvancedFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Advanced filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
