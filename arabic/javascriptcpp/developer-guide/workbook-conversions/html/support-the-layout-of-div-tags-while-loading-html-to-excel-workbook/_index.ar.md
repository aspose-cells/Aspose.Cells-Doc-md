---
title: دعم تنسيق علامات DIV أثناء تحميل HTML إلى دفتر بيانات Excel باستخدام JavaScript عبر C++
linktitle: دعم تخطيط علامات DIV أثناء تحميل HTML إلى دفتر عمل Excel
type: docs
weight: 50
url: /ar/javascript-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}}
عادةً، يتم تجاهل تخطيط علامات div أثناء تحميل HTML إلى كائن دفتر عمل Excel. ومع ذلك، إذا كنت تريد عدم تجاهل تخطيط علامات div، فقم بضبط الخاصية [HtmlLoadOptions.supportDivTag](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#supportDivTag--) على **true**. القيمة الافتراضية لهذه الخاصية هي **false**.
{{% /alert %}}

يوضح رمز النموذج التالي استخدام خاصية [HtmlLoadOptions.supportDivTag](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/#supportDivTag--)، يرجى تنزيل [شعار Aspose](5115218.png) المستخدم داخل HTML الإدخالی وملف Excel الناتج [ملف الإكسل](5115220.xlsx) الذي تم إنشاؤه بواسطة الكود.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlLoadOptions, LoadFormat, Utils } = AsposeCells;

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
            const exportHtml = `
<html>
<body>
<table>
<tr>
<td>
<div>This is some Text.</div>
<div>
<div>
<span>This is some more Text</span>
</div>
<div>
<span>abc@abc.com</span>
</div>
<div>
<span>1234567890</span>
</div>
<div>
<span>ABC DEF</span>
</div>
</div>
<div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>
</td>
<td>
<img src="ASpose_logo_100x100.png" />
</td>
</tr>
</table>
</body>
</html>`;

            // Encode HTML string to Uint8Array
            const encoder = new TextEncoder();
            const ms = encoder.encode(exportHtml);

            // Specify HTML load options, support div tag layouts
            const loadOptions = new HtmlLoadOptions(LoadFormat.Html);
            loadOptions.supportDivTag = true;

            // Create workbook object from the html using load options
            const wb = new Workbook(ms, loadOptions);

            // Auto fit rows and columns of first worksheet
            const ws = wb.worksheets.get(0);
            ws.autoFitRows();
            ws.autoFitColumns();

            // Save the workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DivTagsLayout_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
