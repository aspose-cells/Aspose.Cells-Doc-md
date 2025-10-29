---
title: دور النص مع الشكل داخل ورقة العمل باستخدام جافا سكريبت عبر C++
linktitle: تدوير النص مع الشكل داخل ورقة العمل
type: docs
weight: 1300
url: /ar/javascript-cpp/rotate-text-with-shape-inside-the-worksheet/
description: تعلم كيفية تدوير النص مع الشكل داخل ورقة عمل إكسل باستخدام Script Aspose.Cells for Java عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك إضافة نص داخل أي شكل باستخدام Microsoft Excel. إذا أضفت شكل باستخدام إصدار Microsoft Excel القديم جدًا 2003، فلن يدور النص مع الشكل. ولكن إذا أضفت شكل باستخدام إصدارات أحدث من Microsoft Excel مثل 2007، 2010، 2013 أو 2016، فسيتم تدوير النص مع الشكل. يمكنك التحكم فيما إذا كان النص يجب أن يدور مع الشكل أم لا باستخدام الخاصية [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--). القيمة الافتراضية لها هي **true** مما يعني أن النص سيدور مع الشكل، ولكن إذا ضبطتها على **false**، فلن يدور النص مع الشكل.

## **تدوير النص مع الشكل داخل ورقة العمل**

يحمّل الكود النموذجي التالي ملف إكسل عينة الذي يحتوي على شكل مثلث والنص يتغير مع دوران الشكل. عند فتح الملف في إكسل، ودوران الشكل، سيدور النص معه. ثم يتم ضبط خاصية [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--) على **false** ويحفظ الملف باسم ملف إكسل الناتج. عند فتح الملف الناتج في إكسل، ودوران الشكل، لن يدور النص معه. الرجاء الاطلاع على لقطة الشاشة التالية التي تظهر تأثير الكود على ملف الإكسل العينة كمرجع.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Rotate Text With Shape</title>
    </head>
    <body>
        <h1>Rotate Text With Shape Example</h1>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access cell B4 and add message inside it.
            const cellB4 = worksheet.cells.get("B4");
            cellB4.value = "Text is not rotating with shape because RotateTextWithShape is false.";

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Access shape text alignment.
            const shapeTextAlignment = shape.textBody.textAlignment;

            // Do not rotate text with shape by setting RotateTextWithShape as false.
            shapeTextAlignment.rotateTextWithShape = false;

            // Saving the modified Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRotateTextWithShapeInsideWorksheet.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
