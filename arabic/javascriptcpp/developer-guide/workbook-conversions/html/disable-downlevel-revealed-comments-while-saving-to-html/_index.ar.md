---
title: تعطيل التعليقات المعروضة في مؤخرة الصفحة عند الحفظ إلى HTML باستخدام JavaScript عبر C++
linktitle: تعطيل التعليقات المكشوفة على مستوى أقل أثناء الحفظ إلى HTML
type: docs
weight: 20
url: /ar/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: تعلم كيفية تعطيل التعليقات المعروضة في مؤخرة الصفحة عند حفظ ملف Excel إلى HTML باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel إلى HTML، تكشف Aspose.Cells عن التعليقات الشرطية من المستوى الأدنى. هذه التعليقات الشرطية ذات صلة في الغالب بالإصدارات القديمة من Internet Explorer وغير ذات صلة بالمتصفحات الحديثة. يمكنك الاطلاع على التفاصيل عبر الرابط التالي.

- [تعليق شرطي - تعليق شرطي مكشوف على مستوى أقل](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

 يتيح لك Aspose.Cells for JavaScript عبر C++ القضاء على هذه التعليقات المعروضة في مؤخرة الصفحة عن طريق ضبط خاصية [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--) على **true**.

## **تعطيل كشف التعليقات عند الاستخدام التسلسلي لأسفل عند الحفظ في HTML**

يعرض مثال الكود التالي استخدام الخاصية [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--). تُظهر لقطة الشاشة تأثير هذه الخاصية عندما لا تكون معدلة إلى true. يرجى تحميل ملف Excel النموذجي المستخدم في هذا الكود وملف HTML الناتج عنه للمرجعة.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Disable Downlevel Revealed Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

            // Load sample workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable DisableDownlevelRevealedComments
            const opts = new HtmlSaveOptions();
            opts.disableDownlevelRevealedComments = true;

            // Save the workbook in html
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisableDownlevelRevealedComments_true.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML with DisableDownlevelRevealedComments = true. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
