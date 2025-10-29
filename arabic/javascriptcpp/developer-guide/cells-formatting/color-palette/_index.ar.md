---
title: كيفية استخدام لوحة الألوان
linktitle: كيفية استخدام لوحة الألوان
type: docs
weight: 80
url: /ar/javascript-cpp/excel-color-palette/
description: كود جافاسكريبت لإضافة ألوان مخصصة إلى لوحة الألوان واستخدام لوحة ألوان إكسل مع Aspose.Cells for JavaScript عبر C++.
keywords: جافاسكريبت لإضافة ألوان مخصصة إلى لوحة الألوان، لوحة ألوان إكسل برمجيًا، كيف تستخدم لوحة اللون في دفتر العمل برمجيًا، كيف تستخدم لوحة الألوان في إكسل باستخدام جافاسكريبت
---

## **الألوان واللوحة**

اللوحة هي عدد الألوان المتاحة للاستخدام في إنشاء صورة. يتيح استخدام لوحة معيارية في العرض للمستخدم إنشاء مظهر متسق. كل ملف من ملفات Microsoft Excel (97-2003) لديه لوحة تتكون من 56 لون يمكن تطبيقها على الخلايا، الخطوط، الخطوط الشبكية، الكائنات الرسومية، التعبئات والخطوط في الرسم البياني.

مع Aspose.Cells for JavaScript عبر C++، يمكنك ليس فقط استخدام ألوان اللوحة الحالية ولكن أيضًا الألوان المخصصة. قبل استخدام لون مخصص، أضفه إلى اللوحة أولاً.

يناقش هذا الموضوع كيفية إضافة ألوان مخصصة إلى اللوحة.

## **إضافة ألوان مخصصة إلى اللوحة**

تدعم Aspose.Cells لوحة الألوان من Microsoft Excel التي تتكون من 56 لون. لاستخدام لون مخصص غير معرف في اللوحة، أضف اللون إلى اللوحة.

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/)، التي تمثل ملف إكسل من مايكروسوفت. توفر فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) طريقة [**changePalette(Color, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-) التي تأخذ المعلمات التالية لإضافة لون مخصص لتعديل لوحة الألوان:

- لون مخصص، اللون المخصص الذي سيتم إضافته.
- الفهرس، فهرس اللون في اللوحة الذي سيحل محل اللون المخصص. يجب أن يكون بين 0-55.

المثال أدناه يضيف لون مخصص (Orchid) إلى اللوحة قبل تطبيقه على خط النص.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            const isInPaletteBefore = workbook.isColorInPalette(Color.Orchid);
            console.log(isInPaletteBefore);
            resultDiv.innerHTML = `<p>Is Orchid in palette before change: ${isInPaletteBefore}</p>`;

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(Color.Orchid, 55);

            const isInPaletteAfter = workbook.isColorInPalette(Color.Orchid);
            console.log(isInPaletteAfter);
            resultDiv.innerHTML += `<p>Is Orchid in palette after change: ${isInPaletteAfter}</p>`;

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

تحتوي اللوحة فقط على 56 لونًا. عندما تقوم بإضافة لون مخصص إلى اللوحة، يتم تغيير اللوحة ويتم تغيير أي عنصر في الملف المنسق باللون السابق. لذا، عند تغيير اللوحة، يرجى أن تكون حذرًا جدًا. علاوة على ذلك، هذه هي القيود في تنسيق ملف XLS (Excel 97 - 2003) فقط حيث لا يوجد مثل هذا القيد لتنسيق ملف XLSX أو لأنساق ملفات Microsoft Excel (2007/2010 أو 2013) المتقدمة.

{{% /alert %}}
