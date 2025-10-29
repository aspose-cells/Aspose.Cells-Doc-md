---
title: تعيين تباعد الأسطر للفقرات في شكل أو مربع نص باستخدام جافا سكريبت عبر C++
linktitle: تعيين تباعد السطر للفقرة في شكل أو صندوق النص
type: docs
weight: 290
url: /ar/javascript-cpp/set-line-spacing-of-the-paragraph-in-a-shape-or-textbox/
description: تعلم كيفية تعيين تباعد الأسطر للفقرات في الأشكال أو مربعات النص باستخدام Script Aspose.Cells for Java عبر C++.
---

{{% alert color="primary" %}}

يمكنك ضبط تباعد السطر للفقرة، والمسافة قبلها وبعدها باستخدام خصائص [**TextParagraph.lineSpace**](https://reference.aspose.com/cells/javascript-cpp/textparagraph/#lineSpace--)، [**TextParagraph.spaceBefore**](https://reference.aspose.com/cells/javascript-cpp/textparagraph/#spaceBefore--)، و [**TextParagraph.spaceAfter**](https://reference.aspose.com/cells/javascript-cpp/textparagraph/#spaceAfter--) من فئة [**TextParagraph**](https://reference.aspose.com/cells/javascript-cpp/textparagraph/).

{{% /alert %}}

الكود المصدري التالي يشرح كيفية استخدام الخصائص المذكورة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells TextBox Paragraph Formatting Example</h1>
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
            let wb;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            const ws = wb.worksheets.get(0);

            ws.shapes.addTextBox(2, 0, 2, 0, 100, 200);

            const shape = ws.shapes.get(0);
            shape.text = "Sign up for your free phone number.\nCall and text online for free.";

            const p = shape.textBody.textParagraphs.get(1);

            p.lineSpaceSizeType = AsposeCells.LineSpaceSizeType.Points;
            p.lineSpace = 20;

            p.spaceAfterSizeType = AsposeCells.LineSpaceSizeType.Points;
            p.spaceAfter = 10;

            p.spaceBeforeSizeType = AsposeCells.LineSpaceSizeType.Points;
            p.spaceBefore = 10;

            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
