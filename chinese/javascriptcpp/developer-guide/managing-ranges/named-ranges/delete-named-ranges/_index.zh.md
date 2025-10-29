---
title: 用JavaScript通过C++删除命名范围
linktitle: 删除命名范围
type: docs
weight: 90
url: /zh/javascript-cpp/Delete-named-ranges/
description: 你可以学习如何使用Aspose.Cells for JavaScript通过C++从Excel或OpenOffice文件中删除定义的名称或命名范围。
---

## **介绍**
如果 Excel 文件中有太多的定义名称或命名范围，我们必须清除一些，因为它们再也不会被引用。

## **在MS Excel中删除命名区域**

要从Excel中删除命名区域，可以按照以下步骤进行：
1. 打开Microsoft Excel并打开包含命名区域的工作簿。
2. 转到Excel功能区中的“公式”选项卡。
3. 单击“已定义名称”组中的“名称管理器”按钮。这将打开名称管理器对话框。
4. 在名称管理器对话框中，选择要删除的命名区域。
5. 单击“删除”按钮。在提示时确认删除。
6. 单击“关闭”按钮关闭名称管理器对话框。
7. 保存工作簿以保留更改。

## **使用Aspose.Cells for JavaScript通过C++删除命名范围**
使用Aspose.Cells for JavaScript通过C++可以通过文本[https://reference.aspose.com/cells/javascript-cpp/namecollection/#remove-string-](https://reference.aspose.com/cells/javascript-cpp/namecollection/#remove-string-)或索引[https://reference.aspose.com/cells/javascript-cpp/namecollection/#removeAt-number-](https://reference.aspose.com/cells/javascript-cpp/namecollection/#removeAt-number-)在列表中移除命名范围或定义的名称。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Remove Named Ranges Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Deleted a named range by text.
            worksheets.names.remove("NamedRange");

            // Deleted a defined name by index. Ensure to check the count before removal.
            if (worksheets.names.count > 0) {
                worksheets.names.removeAt(0);
            }

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named ranges removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

注意：如果定义的名称被公式引用，则无法删除。我们只能删除定义名称的公式。

## **删除一些已命名范围**
当我们删除已定义名称时，必须检查它是否被文件中的所有公式引用。
为了提高删除命名范围的性能，我们可以将一些范围同时删除。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Remove Named Ranges Example</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Delete some defined names.
            worksheets.names.remove(["NamedRange1", "NamedRange2"]);

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named ranges removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **删除重复的已定义名称**
有些 Excel 文件损坏是因为有些定义的名称重复。因此我们可以删除这些重复的名称以修复文件。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Remove Duplicate Defined Names</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Deleted some defined names.
            worksheets.names.removeDuplicateNames();

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Duplicate defined names removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
