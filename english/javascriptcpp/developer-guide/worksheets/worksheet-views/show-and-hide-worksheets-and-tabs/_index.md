---
title: Show and Hide Worksheets and Tabs with JavaScript via C++
linktitle: Show and Hide Worksheets and Tabs
type: docs
weight: 10
url: /javascript-cpp/show-and-hide-worksheets-and-tabs/
description: This article provides sample code for using the JavaScript API or JavaScript Library to programmatically display and hide an Excel worksheet. Additionally, it shows how to show and hide Excel workbook tabs.
---

{{% alert color="primary" %}}
Aspose.Cells allows the user to show and hide elements of a workbook, including worksheets and tabs.
{{% /alert %}}

## **Show and Hide a Worksheet**

An Excel file can have one or more worksheets. Whenever we create an Excel file, we add worksheets to the file in which we work. Each worksheet in an Excel file is independent from the other worksheets, having its own data and formatting settings, etc. Sometimes, developers may require to make a few worksheets hidden and others visible in the Excel file for their own interest. So, **Aspose.Cells** allows developers to control the visibility of the worksheets in their Excel files.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class contains a [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class provides a wide range of properties and methods to manage worksheets. To control a worksheet's visibility, use the [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) property of the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class. [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) is a Boolean property, which means that it can only store either a **true** or **false** value.

### **Making a Worksheet Visible**

Make a worksheet visible by setting the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class' [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) property to **true**.

### **Hiding a Worksheet**

Hide a worksheet by setting the [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) class' [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) property to **false**.

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

## **Show and Hide Tabs**

If you closely look at the bottom of a Microsoft Excel file, you will see a number of controls. These include:

- Sheet tabs.
- Tab scrolling buttons.

Sheet tabs represent the worksheets in the Excel file. Click any tab to switch to that worksheet. The more worksheets in the workbook, the more sheet tabs there are. If the Excel file has a large number of worksheets, you need buttons to navigate through them. Therefore, Microsoft Excel provides tab scrolling buttons for scrolling through the sheet tabs.

Using Aspose.Cells, developers can control the visibility of sheet tabs and tab scrolling buttons in Excel files.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class provides a wide range of properties and methods to manage an Excel file. To control the visibility of tabs in an Excel file, developers can use the [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class' [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) property. [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) is a Boolean property, which means that it can only store either a **true** or **false** value.

### **Making Tabs Visible**

Make tabs visible by setting the [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class' [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) property to **true**.

### **Hiding Tabs**

Hide tabs in an Excel file by setting the [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class' [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) property to **false**.

Below is a complete example that opens an Excel file (`book1.xls`), hides its tabs, and saves the modified file as `output.xls`. After the code execution, you will see that the tabs of the workbook are hidden.

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

### **Controlling the Tab Bar Width**

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
            
            // Showing the tabs of the Excel file
            workbook.settings.showTabs = true;
            
            // Adjusting the sheet tab bar width
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