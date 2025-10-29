---
title: 用 JavaScript 和 C++ 显示或隐藏工作表及标签
linktitle: 显示和隐藏工作表和选项卡
type: docs
weight: 10
url: /zh/javascript-cpp/show-and-hide-worksheets-and-tabs/
description: 本文提供了使用 JavaScript API 或 JavaScript 库以编程方式显示和隐藏 Excel 工作表的示例代码。此外，还介绍了如何显示和隐藏 Excel 工作簿标签。
---

{{% alert color="primary" %}}
Aspose.Cells 允许用户显示和隐藏工作簿的元素，包括工作表和标签。
{{% /alert %}}

## **显示和隐藏工作表**

Excel文件可以包含一个或多个工作表。每当我们创建一个Excel文件时，都会向其中添加工作表。Excel文件中的每个工作表都是独立的，具有自己的数据和格式设置等。有时，开发人员可能需要将一些工作表隐藏，并使其他工作表对他们的兴趣可见。因此，**Aspose.Cells**允许开发人员控制其Excel文件中工作表的可见性。

Aspose.Cells 提供了一个类[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，代表一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类包含一个[**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)集合，可访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类提供了丰富的属性和方法来管理工作表。要控制工作表的可见性，使用[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类的[**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--)属性。[**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--)是布尔值属性，只能存储**true**或**false**。

### **使工作表可见**

将工作表设为可见，设置{3}类的{2}属性为**true**。

### **隐藏工作表**

将工作表隐藏，设置{3}类的{2}属性为**false**。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Worksheet Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the first worksheet of the Excel file
            worksheet.isVisible = false;

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **显示和隐藏标签**

如果您仔细查看Microsoft Excel文件的底部，您会看到许多控件。其中包括:

- 工作表标签。
- 选项卡滚动按钮。

工作表标签代表Excel文件中的工作表。单击任何选项卡以切换到该工作表。工作簿中有更多的工作表，也会有更多的工作表标签。如果Excel文件有大量工作表，您需要按钮来进行导航。因此，Microsoft Excel提供了选项卡滚动按钮来滚动工作表标签。

使用Aspose.Cells，开发人员可以控制Excel文件中工作表标签和选项卡滚动按钮的可见性。

Aspose.Cells 提供了一个类[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，代表一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)类提供了丰富的属性和方法来管理Excel文件。开发者可以使用[**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--)类的[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)属性来控制Excel文件中标签的显示。[**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--)是布尔值属性，只能存储**true**或**false**。

### **使选项卡可见**

使用{0}类的{2}属性，将标签设为可见（**true**）。

### **隐藏选项卡**

将Excel文件中的标签隐藏，通过设置{0}类的{2}属性为**false**。

下面是一个完整的示例，打开一个Excel文件（book1.xls），隐藏其标签并将修改后的文件保存为output.xls。代码执行后，您将看到工作簿的标签被隐藏了。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Tabs Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file
            workbook.settings.showTabs = false;

            // To show the tabs instead, you could set:
            // workbook.settings.showTabs = true;

            // Saving the modified Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Tabs hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **控制选项卡栏宽度**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Tabs</title>
    </head>
    <body>
        <h1>Hide Tabs Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file (converted setter to property)
            workbook.settings.showTabs = true;

            // Adjusting the sheet tab bar width (converted setter to property)
            workbook.settings.sheetTabBarWidth = 800;

            // Saving the modified Excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
