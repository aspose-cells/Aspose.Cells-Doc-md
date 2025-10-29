---
title: كيف تغير لون خط التعليق باستخدام JavaScript عبر C++
linktitle: كيفية تغيير لون الخط في التعليق
type: docs
weight: 180
url: /ar/javascript-cpp/how-to-change-the-comment-font-color/
---

{{% alert color="primary" %}}  
 يسمح إكسل Microsoft للمستخدمين بإضافة تعليقات إلى الخلايا لإضافة معلومات إضافية وتسليط الضوء على البيانات. قد يحتاج المطورون إلى تخصيص التعليق لتعيين إعدادات المحاذاة، واتجاه النص، ولون الخط، وما إلى ذلك. يوفر Aspose.Cells for Javaنص البرنامج النصي عبر C++ واجهات برمجة التطبيقات لإنجاز المهمة.  
{{% /alert %}}  

 يوفر Aspose.Cells for Javaنص البرنامج النصي عبر C++ خاصية [**Shape.textBody**](https://reference.aspose.com/cells/javascript-cpp/shape/#textBody--) لضبط لون خط التعليق. يوضح المثال التالي كيفية استخدام خاصية [**Shape.textBody**](https://reference.aspose.com/cells/javascript-cpp/shape/#textBody--) لضبط اتجاه النص لتعليق.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Comment Font Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, StyleFlag } = AsposeCells;

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

            // Instantiate a new Workbook (if a file is provided, open it; otherwise create a new workbook)
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add some text in cell A1
            worksheet.cells.get("A1").putValue("Here");

            // Add a comment to A1 cell
            const commentIndex = worksheet.comments.add("A1");
            const comment = worksheet.comments.get(commentIndex);

            // Set its vertical alignment setting            
            comment.commentShape.textVerticalAlignment = TextAlignmentType.Center;

            // Set the Comment note
            comment.note = "This is my Comment Text. This is Test.";

            const shape = worksheet.comments.get("A1").commentShape;

            shape.fill.solidFill.color = Color.Black;
            const font = shape.font;
            font.color = Color.White;
            const styleFlag = new StyleFlag();
            styleFlag.fontColor = true;
            shape.textBody.format(0, shape.text.length, font, styleFlag);

            // Save the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeCommentFontColor.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

الملف الناتج (102662195.xlsx) الذي تم إنشاؤه بواسطة الكود أعلاه مرفق للرجوع إليه.
