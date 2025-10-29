---
title: الحفاظ على بادئة الاقتباس الفردي لقيمة الخلية أو النطاق
type: docs
weight: 310
url: /ar/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: تعلم كيفية الحفاظ على بادئة اقتباس مفرد لقيمة الخلية أو النطاق من خلال واجهة برمجة التطبيقات Aspose.Cells for JavaScript باستخدام C++.
keywords: الحفاظ على بادئة الاقتباس المفرد لقيمة الخلية أو النطاق JavaScript عبر C++، إخفاء الأ apostrophe أو علامة اقتباس مفردة في البداية JavaScript عبر C++، إظهار الأ apostrophe أو علامة اقتباس مفردة في البداية JavaScript عبر C++
---

## **سيناريوهات الاستخدام المحتملة**

عندما تضع قيمة ما داخل الخلية التي تحتوي على رمز تأشيرة أو علامة اقتباس أحادية في البداية، يخفي Microsoft Excel ذلك، ولكن عند تحديد الخلية، يعرض الرمز التأشيري أو الاقتباس الأحادي في شريط الصيغة كما هو مبين في لقطة الشاشة التالية.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

يخفي برنامج Aspose.Cells for JavaScript باستخدام C++ أيضًا الأ apostrophe أو علامة الاقتباس المفردة في البداية كما في Microsoft Excel ولكنه يحدد [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-) كـ **true** لتلك الخلية. إذا قمت بتعيين نمط فارغ للخلية، يصبح [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) **false** مرة أخرى. لمعالجة هذه المشكلة، يوفر Aspose.Cells for JavaScript باستخدام C++ الخاصية [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-). عندما يتم تعيينها إلى **false**، لا يتم تحديث [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) على الإطلاق ويتم الحفاظ على القيمة القديمة. هذا يعني إذا كانت القيمة القديمة لـ [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) **true**، فستظل **true**، وإذا كانت **false**، فستظل **false**.

## **الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق**

يشرح الكود النموذجي التالي استخدام [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-) كما هو موضح سابقًا. يرجى قراءة التعليقات داخل الكود ورؤية إخراج الكونسول للكود أدناه لمزيد من المساعدة.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells QuotePrefix Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>QuotePrefix Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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
            const resultDiv = document.getElementById('result');
            const outputLines = [];

            // Create workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell A1
            const cell = ws.cells.get("A1");

            // Put some text in cell, it does not have Single Quote at the beginning
            cell.value = "Text";

            // Access style of cell A1
            let st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Put some text in cell, it has Single Quote at the beginning
            cell.value = "'Text";

            // Access style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Print information about StyleFlag.QuotePrefix property
            outputLines.push("");
            outputLines.push("When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.");
            outputLines.push("Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.");
            outputLines.push("");

            // Create an empty style
            st = wb.createStyle();

            // Create style flag - set StyleFlag.QuotePrefix as false
            // It means, we do not want to update the Style.QuotePrefix property of cell A1's style.
            let flag = new AsposeCells.StyleFlag();
            flag.quotePrefix = false;

            // Create a range consisting of single cell A1
            const rng = ws.cells.createRange("A1");

            // Apply the style to the range
            rng.applyStyle(st, flag);

            // Access the style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            // It will print True, because we have not updated the Style.QuotePrefix property of cell A1's style.
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Create an empty style
            st = wb.createStyle();

            // Create style flag - set StyleFlag.QuotePrefix as true
            // It means, we want to update the Style.QuotePrefix property of cell A1's style.
            flag = new AsposeCells.StyleFlag();
            flag.quotePrefix = true;

            // Apply the style to the range
            rng.applyStyle(st, flag);

            // Access the style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            // It will print False, because we have updated the Style.QuotePrefix property of cell A1's style.
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Update result div
            resultDiv.innerHTML = "<pre>" + outputLines.join("\n") + "</pre>";

            // Save the modified workbook and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';
        });
    </script>
</html>
```



## **مخرجات الوحدة**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
