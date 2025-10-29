---
title: تغيير اتجاه نص التعليق باستخدام JavaScript عبر C++
linktitle: تم إرفاق [ملف الإخراج](102662195.xlsx) الذي تم إنشاؤه بواسطة الرمز العينة أعلاه للإشارة الخاصة بك.
type: docs
weight: 10
url: /ar/javascript-cpp/change-text-direction-of-the-comment/
description: تعلم كيفية تغيير اتجاه نص التعليقات باستخدام Aspose.Cells for Javaنص البرنامج النصي عبر C++. قم بتخصيص إعدادات محاذاة التعليق بشكل فعال.
---

{{% alert color="primary" %}}

 يسمح إكسل Microsoft للمستخدمين بإضافة تعليقات إلى الخلايا لإضافة معلومات إضافية وتسليط الضوء على البيانات. قد يحتاج المطورون إلى تخصيص التعليق لتحديد إعدادات المحاذاة واتجاه النص. يوفر Aspose.Cells for Javaنص البرنامج النصي عبر C++ واجهات برمجة التطبيقات لإنجاز هذه المهمة.

{{% /alert %}}

 يوفر Aspose.Cells for Javaنص البرنامج النصي عبر C++ خاصية [**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--) لضبط اتجاه النص للتعليق. يوضح المثال التالي كيفية استخدام خاصية [**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--) لضبط اتجاه النص لتعليق.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment Shape</title>
    </head>
    <body>
        <h1>Add Comment Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, TextDirectionType } = AsposeCells;

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
            // Instantiate a new Workbook
            const wb = new Workbook();

            // Get the first worksheet
            const sheet = wb.worksheets.get(0);

            // Add a comment to A1 cell
            const commentIndex = sheet.comments.add("A1");
            const comment = sheet.comments.get(commentIndex);

            // Set its vertical alignment setting            
            comment.commentShape.textVerticalAlignment = TextAlignmentType.Center;

            // Set its horizontal alignment setting
            comment.commentShape.textHorizontalAlignment = TextAlignmentType.Right;

            // Set the Text Direction - Right-to-Left
            comment.commentShape.textOrientationType = TextDirectionType.RightToLeft;

            // Set the Comment note
            comment.note = "This is my Comment Text. This is test";

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutCommentShape.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
