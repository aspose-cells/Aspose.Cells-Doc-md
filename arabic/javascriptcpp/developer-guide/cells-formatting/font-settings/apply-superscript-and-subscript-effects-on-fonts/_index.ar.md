---
title: تطبيق تأثيرات فوق السطر وتحت السطر على الخطوط
linktitle: تطبيق تأثيرات فوق السطر وتحت السطر على الخطوط
type: docs
weight: 80
url: /ar/javascript-cpp/apply-superscript-and-subscript-effects-on-fonts/
description: كود جافا سكريبت لتطبيق تأثير الفوقية والنص الفرعي على النص في إكسل باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: جافا سكريبت للرفع فوق النص في إكسل عبر C++، جافا سكريبت للنص الفرعي في إكسل عبر C++، جافا سكريبت للرفع والنص الفرعي معًا في إكسل، إدراج النص الفرعي والرفع في إكسل باستخدام جافا سكريبت عبر C++، إضافة النص الفرعي والرفع في إكسل جافا سكريبت عبر C++، إضافة الرفع والنص الفرعي في إكسل جافا سكريبت عبر C++، إضافة الرفع في إكسل جافا سكريبت عبر C++، إضافة النص الفرعي في إكسل جافا سكريبت عبر C++
---

{{% alert color="primary" %}}

توفر Aspose.Cells الوظيفة لتطبيق تأثيرات فوق السطر (نص فوق الخط الأساسي) وتحت السطر (نص تحت الخط الأساسي) على النص.

{{% /alert %}}

## **العمل مع تأثير فوق السطر وتحت السطر**

تطبيق تأثير الرفع من خلال ضبط خاصية [**isSuperscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSuperscript-boolean-) لكائن [**Font**](https://reference.aspose.com/cells/javascript-cpp/font) إلى **true**. لتطبيق النص الفرعي، اضبط خاصية [**isSubscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSubscript-boolean-) لكائن [**Font**](https://reference.aspose.com/cells/javascript-cpp/font) إلى **true**.

تظهر أمثلة الشيفرة التالية كيفية تطبيق حالة فوقية وتحتية على النص.

### كود جافا سكريبت لتطبيق تأثير الرفع على النص

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Superscript Example</title>
    </head>
    <body>
        <h1>Superscript Example</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello";

            // Setting the font Superscript
            const style = cell.style;
            style.font.isSuperscript = true;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Superscript.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### كود جافا سكريبت لتطبيق تأثير النص الفرعي على النص

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Subscript Example</h1>
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
            // Instantiate a Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Access the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello";

            // Setting the font Subscript
            const style = cell.style;
            style.font.isSubscript = true;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Subscript.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created with subscript formatting. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
