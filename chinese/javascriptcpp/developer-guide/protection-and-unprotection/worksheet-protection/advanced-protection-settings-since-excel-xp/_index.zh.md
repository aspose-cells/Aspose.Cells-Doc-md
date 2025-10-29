---
title: 自 Excel XP 起，通过 C++ 和 JavaScript 实现的高级保护设置
linktitle: 自Excel XP以来的高级保护设置
type: docs
weight: 30
url: /zh/javascript-cpp/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

自Excel 2002或XP发布以来，微软已添加了许多高级保护设置。

{{% /alert %}}


## **介绍**

这些保护设置限制或允许用户:

- 删除行或列。
- 编辑内容、对象或场景。
- 格式化单元格、行或列。
- 插入行、列或超链接。
- 选择锁定或解锁的单元格。
- 使用数据透视表等功能。

Aspose.Cells for Java脚本通过C++支持Excel XP或更高版本提供的所有高级保护设置。

### **使用Excel XP和更高版本的高级保护设置**

要查看Excel XP中提供的保护设置：

1. 从**工具**菜单中选择**保护**，然后选择**保护工作表**。将显示一个对话框。

 在Excel 2016中查看可用的保护设置：

1. 从**文件**菜单中选择**保护工作簿**，然后选择**保护当前工作表**。
1. 在**审阅**菜单中选择**保护工作表**。

 按照上述步骤操作，将弹出一个对话框，您可以在其中允许或限制工作表功能，或为工作表设置密码。

### **使用Aspose.Cells for Java脚本通过C++实现的高级保护设置**

Aspose.Cells for Java脚本通过C++支持所有高级保护设置。

Aspose.Cells 提供了一个类，[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，它代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) 集合，允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类表示。

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类提供了 [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) 属性，用于应用这些高级保护设置。[**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) 属性实际上是 [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection) 类的对象，封装了几个布尔属性，用于禁用或启用限制。

下面是一个小例子应用程序。它打开一个 Excel 文件，并使用 Excel XP 及更新版本支持的大部分高级保护设置。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Worksheet Protection Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const protection = worksheet.protection;

            // Restricting users to delete columns of the worksheet
            protection.allowDeletingColumn = false;

            // Restricting users to delete row of the worksheet
            protection.allowDeletingRow = false;

            // Restricting users to edit contents of the worksheet
            protection.allowEditingContent = false;

            // Restricting users to edit objects of the worksheet
            protection.allowEditingObject = false;

            // Restricting users to edit scenarios of the worksheet
            protection.allowEditingScenario = false;

            // Restricting users to filter
            protection.allowFiltering = false;

            // Allowing users to format cells of the worksheet
            protection.allowFormattingCell = true;

            // Allowing users to format rows of the worksheet
            protection.allowFormattingRow = true;

            // Allowing users to insert columns in the worksheet
            protection.allowFormattingColumn = true;

            // Allowing users to insert hyperlinks in the worksheet
            protection.allowInsertingHyperlink = true;

            // Allowing users to insert rows in the worksheet
            protection.allowInsertingRow = true;

            // Allowing users to select locked cells of the worksheet
            protection.allowSelectingLockedCell = true;

            // Allowing users to select unlocked cells of the worksheet
            protection.allowSelectingUnlockedCell = true;

            // Allowing users to sort
            protection.allowSorting = true;

            // Allowing users to use pivot tables in the worksheet
            protection.allowUsingPivotTable = true;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protection settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

 在使用 [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) 属性时，请勿调用 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类的 [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) 方法。此外，应将文件保存为Excel97至2003或Xlsx格式，因为高级保护设置只支持Excel XP及更高版本。

{{% /alert %}}

### **单元格锁定问题**

 如果要限制用户编辑单元格，必须在应用任何保护设置之前将单元格锁定。否则，即使工作表受保护，单元格仍可编辑。在Microsoft Excel XP中，可以通过以下对话框锁定单元格：

|**在Excel XP中锁定单元格的对话框**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

也可以使用 Aspose.Cells API 来锁定单元格。每个单元格可以获得 [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) 格式，其中包含一个布尔属性 [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)。将 [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) 属性设置为 **true** 或 **false**，即可锁定或解锁单元格。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Lock cell A1 by setting the style property
            const cell = worksheet.cells.get("A1");
            cell.style.isLocked = true;

            // Protect the sheet now.
            worksheet.protect(ProtectionType.All);

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
