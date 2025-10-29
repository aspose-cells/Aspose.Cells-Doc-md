---
title: الحصول على رؤوس وتذييلات مع جافا سكريبت عبر C++
linktitle: الحصول على رؤوس أو تذييلات
type: docs
weight: 30
url: /ar/javascript-cpp/get-headers-or-footers/
description: تشرح هذه المقالة كيفية الحصول برمجيًا على رؤوس وتذييلات من ملفات إكسل أو أوبن أوفيس باستخدام واجهة برمجة التطبيقات جافا سكريبت عبر C++.
---

{{% alert color="primary" %}}

يتم عرض الرؤوس والتذييلات فقط في عرض تخطيط الصفحة ومعاينة الطباعة وعلى الصفحات المطبوعة. 

يمكنك أيضًا استخدام مربع حوار إعداد الصفحة إذا كنت ترغب في عرض الرؤوس أو التذييلات لأكثر من ورقة عمل في نفس الوقت. 

بالنسبة لأنواع الورق الأخرى، مثل ورقات الرسومات أو الرسوم البيانية، يمكنك إدراج رؤوس وتذييلات فقط عن طريق مربع حوار إعداد الصفحة.

{{% /alert %}}

## **الحصول على رؤوس وتذييلات في برنامج إكسل**
1. انقر على ورقة العمل حيث ترغب في عرض أو تغيير الرؤوس أو التذييلات.
2. على علامة التبويب عرض، في مجموعة عروض دفتر العمل، انقر فوق تخطيط الصفحة.
   يعرض إكسل ورقة العمل في وضع تخطيط الصفحة.
3. لعرض أو تحرير رأس أو تذييل، انقر على مربع النص للرأس أو التذييل في اليسار، وسط، أو اليمين في الجزء العلوي أو السفلي من صفحة الورقة (تحت رأس، أو فوق تذييل).


## **الحصول على رؤوس وتذييلات باستخدام Aspose.Cells for Javaسكريبت عبر C++**
مع طريقتي [**PageSetup.header(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-) و [**PageSetup.footer(number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-)، يمكن لمطوري جافا سكريبت ببساطة الحصول على رؤوس أو تذييلات من الملف.

1. إنشاء دفتر عمل لفتح الملف.
2. الحصول على ورقة العمل التي تريد الحصول على رؤوس أو تذييلات منها.
3. الحصول على الرأس أو التذييل مع معرف قسم محدد.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Header/Footer Reader Example</h1>
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

        function escapeHtml(str) {
            if (str === null || str === undefined) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerLeft = sheet.pageSetup.header(0);
            // Gets center section of header
            const headerCenter = sheet.pageSetup.header(1);
            // Gets right section of header
            const headerRight = sheet.pageSetup.header(2);
            // Gets center section of footer
            const footerCenter = sheet.pageSetup.footer(1);

            const resultHtml = [
                `<p><strong>Left Header:</strong> ${escapeHtml(headerLeft)}</p>`,
                `<p><strong>Center Header:</strong> ${escapeHtml(headerCenter)}</p>`,
                `<p><strong>Right Header:</strong> ${escapeHtml(headerRight)}</p>`,
                `<p><strong>Center Footer:</strong> ${escapeHtml(footerCenter)}</p>`
            ].join('');

            document.getElementById('result').innerHTML = resultHtml;
        });
    </script>
</html>
```

## **تحليل رؤوس وتذييلات إلى قائمة الأوامر**
يمكن أن تحتوي نصوص الرأس أو التذييل على أوامر خاصة، على سبيل المثال، عنصر نائب لرقم الصفحة، التاريخ الحالي، أو سمات تنسيق النص.

تمثل الأوامر الخاصة بواسطة حرف واحد مع علامة واصلة في المقدمة ("&")

يتم بناء سلاسل الرأس والتذييل باستخدام قواعد ABNF. وليس من السهل فهمها بدون عارض.

يوفر Aspose.Cells for Javaسكريبت عبر C++ طريقة [**PageSetup.commands(string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#commands-string-) لتحليل الرؤوس والتذييلات كقائمة أوامر.

الرموز التالية توضح كيفية تحليل الرأس أو التذييل كقائمة أوامر ومعالجة الأوامر:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Header/Footer Commands Example</title>
    </head>
    <body>
        <h1>Header/Footer Commands Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Gets left section of header
            const headerSection = sheet.pageSetup.header(0);
            const commands = sheet.pageSetup.commands(headerSection) || [];

            const items = [];
            commands.forEach(c => {
                const type = c.type;
                switch (type) {
                    case AsposeCells.HeaderFooterCommandType.SheetName:
                        // embedded the name of the sheet to header or footer
                        items.push('<li>SheetName command found (embeds sheet name)</li>');
                        break;
                    default:
                        items.push(`<li>Command type: ${type}</li>`);
                        break;
                }
            });

            if (!items.length) {
                items.push('<li>No header/footer commands found.</li>');
            }

            resultDiv.innerHTML = `<ul>${items.join('')}</ul>`;

            // Save the (possibly unchanged) workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HeaderFooter_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Workbook';
        });
    </script>
</html>
```
