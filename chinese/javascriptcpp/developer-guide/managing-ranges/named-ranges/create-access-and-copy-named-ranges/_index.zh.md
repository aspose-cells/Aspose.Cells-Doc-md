---
title: 用JavaScript通过C++创建和复制命名范围
linktitle: 创建访问并复制已命名区域
type: docs
weight: 200
url: /zh/javascript-cpp/create-access-and-copy-named-ranges/
description: 学习如何使用Aspose.Cells for JavaScript通过C++在Excel中创建、访问和复制命名范围。
---

## **介绍**  

通常，列和行标签用于引用单个单元格。可以创建描述性名称以表示单元格、单元格范围、公式或常数值。**名称**一词可能指代表单元格、单元格范围、公式或常数值的字符序列。为范围命名意味着可以通过其名称引用该范围。使用易于理解的名称，例如Products，来指代难以理解的范围，例如Sales!C20:C30。标签可用于引用同一工作表上的数据的公式；如果要表示另一工作表上的范围，可以使用名称。*命名范围是Microsoft Excel最强大的功能之一，特别是在用作列表控件、透视表、图表等的源范围时。*  

## **使用Microsoft Excel处理已命名区域**  

### **创建已命名范围**  

以下步骤描述了如何使用 **MS Excel** 命名单元格或范围。这种方法适用于 **Microsoft Office Excel 2003**、**Excel 97**、**2000** 和 **2002**。  

1. 选择你想命名的单元格或单元格范围。  
2. 点击公式栏左端的**名称框**。  
3. 输入单元格的名称。  
4. 按 ENTER。  

{{% alert color="primary" %}}  
在更改单元格内容时，不能为单元格命名。  
{{% /alert %}}  

## **使用Aspose.Cells处理命名范围**  

在这里，我们使用Aspose.Cells API来完成任务。  
Aspose.Cells提供了一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类包含一个[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)类提供[**cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合。  

### **创建已命名范围**  

通过调用 [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 集合的重载 [**createRange(string, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) 方法，可以创建命名范围。 [**createRange(string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-) 方法的典型版本使用以下参数：  

- 左上角单元格的名称，范围中左上角单元格的名称。  
- 右下角单元格的名称，范围中右下角单元格的名称。  

调用 [**createRange(string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-) 方法时，它将返回新创建的范围，作为 [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) 类的实例。使用此 [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) 对象来配置命名范围。例如，使用 [**name**](https://reference.aspose.com/cells/javascript-cpp/range/#name--) 属性设置范围的名称。以下示例展示了如何创建跨越 B4:G14 的单元格命名范围。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Creating a named range
            const range = worksheet.cells.createRange("B4", "G14");

            // Setting the name of the named range
            range.name = "TestRange";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **将数据输入到命名范围内的单元格**  

您可以按照模式将数据插入到范围内单个单元格中  

- **JavaScript**：Range[row,column]  

假设您有一个跨越 A1:C4 的命名范围。该矩阵包含 4 * 3 = 12 个单元格。单个范围单元按顺序排列：Range[0,0]，Range[0,1]，Range[0,2]，Range[1,0]，Range[1,1]，Range[1,2]，Range[2,0]，Range[2,1]，Range[2,2]，Range[3,0]，Range[3,1]，Range[3,2]。  

使用以下属性来识别范围中的单元格:  

- firstRow 返回命名范围中第一行的索引。  
- firstColumn 返回命名范围中第一列的索引。  
- rowCount 返回命名范围中总行数。  
- columnCount 返回命名范围中总列数。  

以下示例显示如何向指定范围的单元格输入一些值。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first worksheet in the workbook.
            const worksheet1 = workbook.worksheets.get(0);

            // Create a range of cells based on H1:J4.
            const range = worksheet1.cells.createRange("H1", "J4");

            // Name the range.
            range.name = "MyRange";

            // Input some data into cells in the range.
            range.get(0, 0).value = "USA";
            range.get(0, 1).value = "SA";
            range.get(0, 2).value = "Israel";
            range.get(1, 0).value = "UK";
            range.get(1, 1).value = "AUS";
            range.get(1, 2).value = "Canada";
            range.get(2, 0).value = "France";
            range.get(2, 1).value = "India";
            range.get(2, 2).value = "Egypt";
            range.get(3, 0).value = "China";
            range.get(3, 1).value = "Philipine";
            range.get(3, 2).value = "Brazil";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'rangecells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and range populated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

### **标识命名范围中的单元格**  

您可以按照以下模式向范围内的单个单元格插入数据：  

- **JavaScript**：Range[row,column]  

如果您有一个跨越 A1:C4 的命名范围。该矩阵包含 4 * 3 = 12 个单元格。单个范围单元按顺序排列：Range[0,0]，Range[0,1]，Range[0,2]，Range[1,0]，Range[1,1]，Range[1,2]，Range[2,0]，Range[2,1]，Range[2,2]，Range[3,0]，Range[3,1]，Range[3,2]。  

使用以下属性来识别范围中的单元格:  

- firstRow 返回命名范围中第一行的索引。  
- firstColumn 返回命名范围中第一列的索引。  
- rowCount 返回命名范围中总行数。  
- columnCount 返回命名范围中总列数。  

以下示例显示如何向指定范围的单元格输入一些值。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Named Range</title>
    </head>
    <body>
        <h1>Get Named Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Getting the specified named range
            const range = workbook.worksheets.rangeByName("TestRange");

            if (!range) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Named range "TestRange" not found.</p>';
                return;
            }

            // Identify range cells and display properties
            const firstRow = range.firstRow;
            const firstColumn = range.firstColumn;
            const rowCount = range.rowCount;
            const columnCount = range.columnCount;

            const html = [
                `<p>First Row : ${firstRow}</p>`,
                `<p>First Column : ${firstColumn}</p>`,
                `<p>Row Count : ${rowCount}</p>`,
                `<p>Column Count : ${columnCount}</p>`
            ].join('');

            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```  

### **访问命名范围**  

#### **访问特定的命名范围**  

调用 [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) 集合的 [**rangeByName(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#rangeByName-string-) 方法，以按指定名称获取范围。典型的 [**rangeByName(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#rangeByName-string-) 方法接受命名范围的名称，并将所指定的命名范围作为 [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) 类的实例返回。以下示例显示如何通过名称访问指定的范围。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Named Range Example</title>
    </head>
    <body>
        <h1>Get Named Range Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Getting the specified named range
            const worksheets = workbook.worksheets;
            const range = worksheets.rangeByName("TestRange");

            if (range !== null) {
                document.getElementById('result').innerHTML = `<p>Named Range : ${range.refersTo}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Named range "TestRange" not found.</p>';
            }
        });
    </script>
</html>
```  

#### **访问电子表格中的所有命名范围**  

调用 [**worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) 集合的 [**namedRanges()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#namedRanges--) 方法以获取电子表格中的所有命名范围。[**namedRanges()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#namedRanges--) 方法返回所有命名范围的数组，属于[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)集合。  

以下示例显示如何访问工作簿中的所有命名范围。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Named Ranges</title>
    </head>
    <body>
        <h1>Get Named Ranges Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Getting all named ranges
            const ranges = workbook.worksheets.namedRanges;

            if (ranges) {
                // Some collections expose 'count', others may expose 'length'
                const total = (typeof ranges.count !== 'undefined') ? ranges.count : ranges.length;
                document.getElementById('result').innerHTML = `<p style="color: green;">Total Number of Named Ranges: ${total}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No named ranges found.</p>';
            }
        });
    </script>
</html>
```  

### **复制命名范围**  

Aspose.Cells提供了[**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/range/#copy-range-pasteoptions-)方法，用于将具有格式的单元格范围复制到另一个范围。  

以下示例显示如何将源单元格范围复制到另一个命名范围。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Ranges</title>
    </head>
    <body>
        <h1>Copy Ranges Example</h1>
        <p>Select an Excel file to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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

            // Instantiate a new Workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Get the first worksheet in the worksheets collection.
            const worksheet = workbook.worksheets.get(0);

            // Create a range of cells.
            const range1 = worksheet.cells.createRange("E12", "I12");

            // Name the range.
            range1.name = "MyRange";

            // Set the outline border to the range.
            range1.outlineBorder = { borderType: BorderType.TopBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.BottomBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.LeftBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.RightBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };

            // Input some data with some formattings into a few cells in the range.
            range1.get(0, 0).putValue("Test");
            range1.get(0, 4).putValue("123");

            // Create another range of cells.
            const range2 = worksheet.cells.createRange("B3", "F3");

            // Name the range.
            range2.name = "testrange";

            // Copy the first range into second range.
            range2.copy(range1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'copyranges.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
