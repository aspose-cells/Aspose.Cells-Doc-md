---
title: 通过JavaScript使用C++保护工作表
linktitle: 保护工作表
type: docs
weight: 10
url: /zh/javascript-cpp/protecting-worksheets/
description: 学习如何使用Aspose.Cells for Java脚本通过C++保护Excel中的工作表，包括保护行、列和特定单元格。
---

{{% alert color="primary" %}}

当工作表被保护时，用户可以执行的操作受到限制。例如，不能输入数据、插入或删除行或列等。

{{% /alert %}}

## **保护工作表**

### **介绍**

Microsoft Excel中的常规保护选项包括：

- 内容
- 对象
- 方案

受保护的工作表不会隐藏或保护敏感数据，因此它与文件加密不同。通常，工作表保护适用于展示目的。它防止最终用户修改工作表中的数据、内容和格式。

### **保护工作表**

Aspose.Cells提供一个类[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，代表Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)集合，可以访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示。

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类提供用于在工作表上应用保护的[**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-)方法。[**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-)方法接受以下参数：

- 保护类型，应用于工作表的保护类型。保护类型是使用[**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype)枚举来应用的。
- 新密码，用于保护工作表的新密码。
- 旧密码，如果工作表已经受到密码保护，则传入旧密码。如果工作表尚未受到保护，则传递 null。

[**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype)枚举包含以下预定义的保护类型：

|**保护类型**|**描述**|
| :- | :- |
|All| 用户无法修改工作表中的任何内容
|Contents| 用户无法在工作表中输入数据
|Objects| 用户无法修改绘图对象
|Scenarios| 用户无法修改已保存的情景
|Structure| 用户无法修改结构
|Windows| 保护应用于窗口
|None| 不应用任何保护

下例显示如何使用密码保护工作表。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
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

            // Ensure Aspose.Cells is initialized before proceeding
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Protecting the worksheet with a password
            worksheet.protect(ProtectionType.All, "aspose", null);

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

使用上述代码保护工作表后，打开工作表即可检查工作表的保护。一旦打开文件并尝试向工作表添加一些数据，您将会看到以下对话框：

|**警告对话框，提示用户无法修改工作表**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

要在工作表上操作，请选择 **保护**，然后在 **工具** 菜单项中选择 **取消保护工作表**。

选择取消保护工作表菜单项后，将会打开一个对话框，提示您输入密码，以便您可以在工作表上进行操作，如下所示：

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **使用Microsoft Excel保护工作表的部分单元格**

某些情况下你可能只需要锁定工作表中的部分单元格。如果你想锁定工作表中的特定单元格，你必须解锁工作表中的所有其他单元格。工作表中的所有单元格默认都已初始化为锁定状态；你可以通过在MS Excel中打开任何Excel文件，点击“格式|单元格...”弹出“单元格格式”对话框，再点击“保护”标签，看到被选中的“锁定”复选框（默认已勾选）来确认这一点。

以下内容描述了如何使用MS Excel锁定部分单元格。此方法适用于Microsoft Office Excel 97、2000、2002、2003及更高版本。

1. 点击**全选**按钮（位于行号1上方和列号A左侧的灰色矩形）来选择整个工作表。
2. 在“格式”菜单中点击“单元格”，切换到“保护”标签，然后取消选中“锁定”复选框。
   这样就解锁了工作表上的所有单元格。
   如果**单元格**命令不可用，工作表的部分可能已被锁定。在**工具**菜单上，指向**保护**，然后点击**取消保护工作表**。
3. 仅选择你想锁定的单元格，重复第2步，但这次勾选“锁定”。
4. 在“工具”菜单中，指向“保护”，点击“保护工作表”，然后点击“确定”。
5. 在“保护工作表”对话框中，你可以设置密码，并选择用户可更改的元素。

### **使用Aspose.Cells保护工作表中的部分单元格**

在此方法中，我们仅使用Aspose.Cells API完成任务。

示例：以下示例演示如何保护工作表中的部分单元格。它先解锁所有单元格，然后锁定3个单元格（A1、B1、C1），最后保护工作表。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)对象包含一个布尔属性[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)，你可以将[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)属性设置为true或false，并使用*Column/Row.applyStyle()*方法锁定或解锁行/列，使用你希望的属性。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unlock Columns and Protect Specific Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            await readyPromise;

            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object
            const styleflag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                styleflag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, styleflag);
            }

            // Lock the three cells...i.e. A1, B1, C1.
            style = sheet.cells.get("A1").style;
            style.isLocked = true;
            sheet.cells.get("A1").style = style;

            style = sheet.cells.get("B1").style;
            style.isLocked = true;
            sheet.cells.get("B1").style = style;

            style = sheet.cells.get("C1").style;
            style.isLocked = true;
            sheet.cells.get("C1").style = style;

            // Finally, Protect the sheet now.
            sheet.protect(ProtectionType.All);

            // Save the excel file and provide download link
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **在工作表中保护一行**

Aspose.Cells允许你轻松锁定工作表中的任一行。在这里，我们可以使用[**Aspose.Cells.Row**](https://reference.aspose.com/cells/javascript-cpp/row)类的[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-)方法，将[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)应用于工作表中的特定行。此方法接受两个参数：一个[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)对象和一个[**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)对象，后者包含所有与应用格式相关的成员。

以下示例演示如何保护工作表中的某一行。它先解锁所有单元格，然后锁定第一行，最后保护工作表。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)对象包含一个布尔属性[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)，你可以将[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)设为true或false，以锁定或解锁该行/列，使用 [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)对象。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType, Utils } = AsposeCells;

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
            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first row style.
            style = sheet.cells.rows.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Set the lock setting.
            flag.locked = true;

            // Apply the style to the first row.
            sheet.cells.applyRowStyle(0, style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **在工作表中保护一列**

Aspose.Cells允许你轻松锁定工作表中的某一列。这里，我们可以使用[**Aspose.Cells.Column**](https://reference.aspose.com/cells/javascript-cpp/column)类的[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/column/#applyStyle-style-styleflag-)方法，将[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)应用于工作表中的特定列。此方法接受两个参数：一个[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)对象和一个[**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)对象，后者包含所有相关格式成员。

以下示例显示如何保护工作表中的某一列。它先解锁所有单元格，然后锁定第一列，最后保护工作表。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)对象包含一个布尔属性[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)，你可以将[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)设为true或false，以锁定或解锁该列，使用[**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)对象。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Unlock Columns and Protect Sheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
                // If no file provided, a new workbook will be created
                document.getElementById('result').innerHTML = '<p style="color: orange;">No file selected. A new workbook will be created and processed.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Processing selected file...</p>';
            }

            await readyPromise;

            // Load workbook from file if provided, otherwise create new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a worksheet object and obtain the first sheet.
            const sheet = workbook.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first column style.
            style = sheet.cells.columns.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Apply the style to the first column.
            sheet.cells.columns.get(0).applyStyle(style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **允许用户编辑范围**

下面的示例展示了如何允许用户在受保护的工作表中编辑范围。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect Range</title>
    </head>
    <body>
        <h1>Protect Range Example</h1>
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

            // Instantiate a new or loaded Workbook
            let book;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                book = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                book = new Workbook();
            }

            // Get the first (default) worksheet
            const sheet = book.worksheets.get(0);

            // Get the Allow Edit Ranges
            const allowRanges = sheet.allowEditRanges;

            // Define ProtectedRange
            let protected_range;

            // Create the range
            const idx = allowRanges.add("r2", 1, 1, 3, 3);
            protected_range = allowRanges.get(idx);

            // Specify the password
            protected_range.password = "123";

            // Protect the sheet
            sheet.protect(ProtectionType.All);

            // Save the Excel file
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'protectedrange.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Range Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Protected range added and sheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
