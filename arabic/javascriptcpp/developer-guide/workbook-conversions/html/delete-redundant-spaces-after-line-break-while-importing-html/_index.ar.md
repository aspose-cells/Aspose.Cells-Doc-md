---
title: حذف المسافات الزائدة بعد فاصل السطر عند استيراد HTML باستخدام JavaScript عبر C++
linktitle: حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML
type: docs
weight: 20
url: /ar/javascript-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: تعلم كيفية حذف المسافات الزائدة بعد فواصل السطر عند استيراد HTML باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

يرجى استخدام الخاصية [**HtmlLoadOptions.deleteRedundantSpaces**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#deleteRedundantSpaces--) وتعيينها **true** لحذف جميع المسافات الزائدة التي تأتي بعد وسم فاصل الأسطر. بشكل افتراضي، تكون هذه الخاصية **false** ويتم الاحتفاظ بالمسافات الزائدة في ملفات Excel الناتجة.

{{% /alert %}}

# تأثير تعيين خاصية HTMLLoadOptions.deleteRedundantSpaces إلى false و true

تُظهر اللقطة الشاشة التالية تأثير تعيين هذه الخاصية إلى **false** و **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML

### مثال برمجي

يعرض رمز النموذج التالي كيفية استخدام الخاصية [**HtmlLoadOptions.deleteRedundantSpaces**](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#deleteRedundantSpaces--). يرجى تعيينها إلى **true** أو **false** للحصول على الناتج كما هو موضح في لقطة الشاشة أعلاه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Delete Redundant Spaces While Importing From HTML</title>
    </head>
    <body>
        <h1>Delete Redundant Spaces While Importing From HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat } = AsposeCells;

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
            // Sample Html containing redundant spaces after <br> tag
            const html = "<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

            // Convert Html to byte array
            const encoder = new TextEncoder();
            const byteArray = encoder.encode(html);

            // Set Html load options and keep precision true
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);
            loadOptions.deleteRedundantSpaces = true;

            // Create workbook from stream with Html load options
            const stream = byteArray;
            const workbook = new Workbook(stream, loadOptions);

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Auto fit the sheet columns
            sheet.autoFitColumns();

            // Saving the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
