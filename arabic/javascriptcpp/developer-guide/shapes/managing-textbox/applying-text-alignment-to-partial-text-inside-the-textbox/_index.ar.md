---
title: كيفية تطبيق/ضبط محاذاة النص في مربع النص باستخدام جافا سكريبت عبر C++
linktitle: تطبيق / تعيين محاذاة النص لمربع النص
type: docs
weight: 20
url: /ar/javascript-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: كيفية تطبيق/ضبط محاذاة النص في مربع النص في Aspose.Cells for JavaScript عبر C++.
keywords: تطبيق/ضبط المحاذاة مربع النص في ورقة عمل Excel Aspose JavaScript عبر C++
---

يمكن لصناديق النص أن تعزز تعبيرية مستنداتنا ومخططاتنا، وتطبيق محاذاة مختلفة على أجزاء مختلفة من صندوق النص يمكن أن يساعد في تسليط الضوء على نقاط الاهتمام للقراء. لكن المحاذاة الافتراضية لصندوق النص لا تلبي جميع احتياجاتنا. لذلك، قد تحتاج إلى تعديل كل صندوق نص لتحقيق متطلباتك. إذا لم تمتلك الكثير من أدوات صناديق النص للتعديل، أنت محظوظ. وإذا كانت هناك العديد من صناديق النص للتعديل، أعتقد أنك ستواجه مشكلة. لا تقلق الآن، فإن [Aspose.Cells](https://products.aspose.com/cells/) يوفر واجهة برمجة تطبيقات لمساعدتك على القيام بذلك.

يطبق الكود النموذجي التالي تحديد محاذاة النص على مربع نص.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add TextBox Example</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);
            const shapes = worksheet.shapes;

            // add a TextBox
            const shape = shapes.addTextBox(2, 0, 2, 0, 50, 120);
            shape.text = "This is a test.";

            // set alignment
            shape.textHorizontalAlignment = AsposeCells.TextAlignmentType.Center;
            shape.textVerticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

يمكنك أيضًا تغيير محاذاة النص داخل بعض النصوص بداخل شكل صندوق النص باستخدام نص HTML المناسب. يطبق الرمز المساعد التالي محاذاة النص على جزء من النص داخل صندوق النص.

[ملف المصدر](SampleTextboxExcel2016.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox HTML Transfer Example</title>
    </head>
    <body>
        <h1>TextBox HTML Transfer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, MsoDrawingType, Utils } = AsposeCells;

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

            // Load source workbook from the selected file
            const sourceWb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the target textbox whose text is to be aligned
            const sourceTextBox = sourceWb.worksheets.get(0).shapes.get(0);

            // Create an object of the target workbook
            const destWb = new Workbook();

            // Access the first worksheet from the collection
            const _sheet = destWb.worksheets.get(0);

            // Create new textbox
            const _textBox = _sheet.shapes.addShape(MsoDrawingType.TextBox, 1, 0, 1, 0, 200, 200);

            // Use Html string from a template file textbox
            _textBox.htmlText = sourceTextBox.htmlText;

            // Save the workbook and provide download link
            const outputData = destWb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Text box HTML copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
