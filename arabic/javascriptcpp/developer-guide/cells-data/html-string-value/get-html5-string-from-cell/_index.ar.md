---
title: الحصول على سلسلة HTML5 من الخلية
type: docs
weight: 90
url: /ar/javascript-cpp/get-html5-string-from-cell/
description: تعلم كيفية الحصول على سلسلة HTML5 من الخلية من خلال Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات C++.
keywords: الحصول على سلسلة HTML5 من الخلية JavaScript عبر C++، الحصول على سلسلة HTML5 من الخلية JavaScript، إدارة سلسلة HTML5 للخلية JavaScript عبر C++
---

## **سيناريوهات الاستخدام المحتملة**

يعيد Aspose.Cells السلسلة HTML للخلية باستخدام طريقة [**Cell.htmlString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-boolean-) التي تقبل معيار boolean. إذا مررت **false** كمعامل، فسيعود بـ HTML عادي، وإذا مررت **true**، فسيعود بسلسلة HTML5.

## **الحصول على سلسلة HTML5 من الخلية**

يقوم رمز العينة التالي بإنشاء كائن دفتر عمل ويضيف بعض النص إلى الخلية A1 من ورقة العمل الأولى. ثم يحصل على سلاسل HTML العادية وHTML5 من الخلية A1 باستخدام طريقة [**Cell.htmlString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-boolean-) ويطبعها على وحدة التحكم.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Get HTML String from Cell</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            // This example creates a new workbook, writes text to A1 and retrieves HTML strings.
            const wb = new Workbook();

            const ws = wb.worksheets.get(0);

            const cell = ws.cells.get("A1");
            cell.value = "This is some text.";

            const strNormal = cell.htmlString;
            const strHtml5 = cell.htmlString;

            console.log("Normal:\r\n" + strNormal);
            console.log();
            console.log("Html5:\r\n" + strHtml5);

            document.getElementById('result').innerHTML =
                '<h2>Results</h2>' +
                '<p><strong>Normal:</strong></p><pre>' + escapeHtml(strNormal) + '</pre>' +
                '<p><strong>Html5:</strong></p><pre>' + escapeHtml(strHtml5) + '</pre>' +
                '<p style="color: green;">Operation completed successfully!</p>';
        });

        function escapeHtml(text) {
            if (text === null || text === undefined) return "";
            return String(text)
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
        }
    </script>
</html>
```


## **مخرجات الوحدة**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
