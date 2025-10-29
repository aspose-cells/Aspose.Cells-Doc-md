---
title: استثناء الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML باستخدام JavaScript عبر C++
linktitle: استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML
type: docs
weight: 30
url: /ar/javascript-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: تعلم كيفة استثناء الأنماط غير المستخدمة عند تحويل Excel إلى HTML باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

قد يحتوي ملفات Microsoft Excel على العديد من الأنماط غير المستخدمة. عند تصدير ملف Excel إلى تنسيق HTML، يتم تصدير هذه الأنماط غير المستخدمة أيضًا. يمكن أن يزيد ذلك من حجم الـ HTML. يمكنك استبعاد الأنماط غير المستخدمة أثناء تحويل ملفات Excel إلى HTML باستخدام الخاصية [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--). عند تعيينها على **true**، يتم استبعاد جميع الأنماط غير المستخدمة من الـ HTML الناتج. تعرض لقطة الشاشة التالية مثالًا على نمط غير مستخدم داخل الـ HTML الناتج.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML**  

ينشئ رمز المثال التالي كتاب عمل ويُنشئ نمطًا باسم غير مستخدم. بما أن [**HtmlSaveOptions.excludeUnusedStyles**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#excludeUnusedStyles--) مَعين على **true**، فلن يتم تصدير هذا النمط غير المستخدم إلى [HTML الناتج](61767778.zip). ولكن إذا قمت بضبطها على **false**، فسيكون هذا النمط غير المستخدم موجودًا داخل الـ HTML الناتج ويمكنك رؤيته في تنسيق HTML كما هو موضح في لقطة الشاشة أعلاه.  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Exclude Unused Styles</title>
    </head>
    <body>
        <h1>Exclude Unused Styles from Excel to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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

            if (fileInput.files.length > 0 && fileInput.files[0].size === 0) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a valid Excel file.</p>';
                return;
            }

            // Instantiate workbook from selected file or create a new one
            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Create an unused named style
            const style = wb.createStyle();
            style.name = "UnusedStyle_XXXXXXXXXXXXXX";

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some value in cell C7
            const cell = ws.cells.get("C7");
            cell.value = "This is sample text.";

            // Specify html save options, we want to exclude unused styles
            const opts = new HtmlSaveOptions();
            // Comment this line to include unused styles
            opts.excludeUnusedStyles = true;

            // Save the workbook in html format
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExcludeUnusedStylesInExcelToHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML generated successfully. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
