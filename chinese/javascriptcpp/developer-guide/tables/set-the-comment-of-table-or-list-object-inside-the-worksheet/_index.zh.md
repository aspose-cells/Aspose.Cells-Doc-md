---
title: 使用JavaScript通过C++设置工作表中表格或列表对象的注释
linktitle: 在工作表内设置表格或列表对象的备注
type: docs
weight: 40
url: /zh/javascript-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: 学习如何使用Aspose.Cells for JavaScript通过C++设置工作表内表格或列表对象的注释。 
---

{{% alert color="primary" %}}

你可以使用[**ListObject.comment**](https://reference.aspose.com/cells/javascript-cpp/listobject/#comment--)属性设置工作表中表或列表对象的注释，注释将显示在xl/tables/tableName.xml文件中。

{{% /alert %}}

## **设置工作表内表格或列表对象的批注**

以下示例代码加载[源Excel文件](5115514.xlsx)，设置工作表中第一个表格或列表对象的注释。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Comment of Table/ListObject</title>
    </head>
    <body>
        <h1>Set Comment of Table/ListObject</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first list object or table.
            const lstObj = worksheet.listObjects.get(0);

            // Set the comment of the list object
            lstObj.comment = "This is Aspose.Cells comment.";

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetCommentOfTableOrListObject_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
