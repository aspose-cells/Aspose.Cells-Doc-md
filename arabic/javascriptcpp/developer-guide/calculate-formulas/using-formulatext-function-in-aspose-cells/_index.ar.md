---
title: استخدام وظيفة FormulaText في Aspose.Cells for JavaScript عبر C++
linktitle: استخدام وظيفة FormulaText في Aspose.Cells
description: تقدم هذه المقالة شرحًا لكيفية استخدام وظيفة FormulaText في مكتبة Aspose.Cells لمعالجة الصيغ في Microsoft Excel. تعلم كيفية الحصول على نص الصيغة وتعيينه للخلية وحفظ ملفات Excel المعدلة باستخدام جافا سكريبت عبر C++.
keywords: وظائف FormulaText من Aspose.Cells، Excel، JavaScript عبر C++
type: docs
weight: 60
url: /ar/javascript-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText هي دالة من إكسل 2013 وما بعده. غير مدعومة من قبل الإصدارات السابقة مثل Excel 2010 أو 2007، وما إلى ذلك. كما يوحي الاسم، فهي تطبع نص الصيغة الموجودة في خلية معينة. ستوضح لك هذه المقالة كيفية استخدام هذه الوظيفة باستخدام Aspose.Cells for JavaScript عبر C++.

{{% /alert %}} 

الرمز النموذجي التالي يوضح استخدام وظيفة FormulaText مع Aspose.Cells for JavaScript عبر C++. يكتب الرمز أولاً صيغة في الخلية A1 ثم يطبع نص الصيغة باستخدام FormulaText في الخلية A2.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - FormulaText</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some formula in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.formula = "=Sum(B1:B10)";

            // Get the text of the formula in cell A2 using FORMULATEXT function
            const cellA2 = worksheet.cells.get("A2");
            cellA2.formula = "=FormulaText(A1)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Print the results of A2, It will now print the text of the formula inside cell A1
            console.log(cellA2.stringValue);

            resultDiv.innerHTML = `<p style="color: green;">Operation completed successfully! Formula text: ${cellA2.stringValue}</p>`;
        });
    </script>
</html>
```
## **مخرجات الوحدة**


{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
