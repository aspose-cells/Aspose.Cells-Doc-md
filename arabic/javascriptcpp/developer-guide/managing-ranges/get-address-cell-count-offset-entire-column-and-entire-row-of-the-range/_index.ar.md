---
title: الحصول على عنوان الخلية، وعدد، وتعويض الإزاحة، وسطر كامل، وعمود كامل للنطاق باستخدام JavaScript عبر C++
linktitle: الحصول على عنوان خلية، عدد الخلايا، الإزاحة، العمود الكامل والصف الكامل للنطاق
type: docs
weight: 330
url: /ar/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **سيناريوهات الاستخدام المحتملة**
يوفر Aspose.Cells for JavaScript عبر C++ كائن النطاق الذي يحتوي على طرق مساعدة متعددة تسهل على المستخدم العمل مع نطاقات Excel. توضح هذه المقالة استخدام الطرق أو الخصائص التالية لكائن النطاق.

- **العنوان**

الحصول على عنوان النطاق.

- **عدد الخلايا**

الحصول على جميع عدد الخلايا في النطاق.

- **الإزاحة**

الحصول على النطاق بواسطة الإزاحة.

- **العمود الكامل**

الحصول على كائن نطاق يمثل العمود الكامل (أو الأعمدة) الذي يحتوي على النطاق المحدد.

- **الصف الكامل**

الحصول على كائن نطاق يمثل الصف الكامل (أو الصفوف) التي تحتوي على النطاق المحدد.

## **الحصول على العنوان، عدد الخلايا، الإزاحة، العمود الكامل والصف الكامل للنطاق**
يشرح الكود العيني التالي استخدام الطرق والخصائص كما تم مناقشتها أعلاه. يُرجى الرجوع إلى الانتاج على وحدة التحكم للكود الوارد أدناه للرجوع.

## **الكود المثالي**
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
            // This example creates ranges on a new empty workbook and prints info to the page.
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Create range A1:B3.
            console.log("Creating Range A1:B3\n");
            let rng = ws.cells.createRange("A1:B3");

            // Print range address and cell count.
            const lines = [];
            lines.push("Range Address: " + rng.address);
            lines.push("Range row Count: " + rng.rowCount);
            lines.push("Range column Count: " + rng.columnCount);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Create range A1.
            console.log("Creating Range A1\n");
            rng = ws.cells.createRange("A1");

            // Print range offset, entire column and entire row.
            lines.push("Offset: " + rng.offset(2, 2).address);
            lines.push("Entire Column: " + rng.entireColumn.address);
            lines.push("Entire Row: " + rng.entireRow.address);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Display results
            resultEl.innerHTML = '<pre>' + lines.join("\n") + '</pre>';
        });
    </script>
</html>
```

## **مخرجات الوحدة**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
