---
title: 使用JavaScript通过C++将工作簿保存为严格的Open XML电子表格格式
linktitle: 将工作簿保存为严格的 Open XML 电子表格格式
type: docs
weight: 150
url: /zh/javascript-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: 学习如何使用Aspose.Cells for JavaScript通过C++将工作簿保存为严格的Open XML电子表格格式。
---

## **可能的使用场景**

Aspose.Cells for JavaScript通过C++允许你将工作簿保存为*严格的Open XML电子表格*格式。为此，它提供了[**WorkbookSettings.compliance**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#compliance--)属性。如果你将其值设置为[**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompliance)，则输出的Excel文件将以严格的Open XML电子表格格式保存。

## **将工作簿保存为严格的 Open XML 电子表格格式**

以下示例代码创建一个工作簿，并将 [**WorkbookSettings.compliance**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#compliance--) 属性值设为 [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompliance)，然后保存为 [输出Excel文件](67338272.xlsx)。如果你在Microsoft Excel中打开输出的Excel文件，选择另存为...，你将看到其格式为*严格Open XML电子表格*，如下截图所示。

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Save Workbook to Strict Open XML Spreadsheet Format</title>
    </head>
    <body>
        <h1>Save Workbook to Strict Open XML Spreadsheet Format</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OoxmlCompliance, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();

            // Specify - Strict Open XML Spreadsheet - Format.
            workbook.settings.compliance = OoxmlCompliance.Iso29500_2008_Strict;

            // Access first worksheet and set value in B4
            const worksheet = workbook.worksheets.get(0);
            const b4 = worksheet.cells.get("B4");
            b4.value = "This Excel file has Strict Open XML Spreadsheet format.";

            // Save to output Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved to Strict Open XML Spreadsheet format. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
