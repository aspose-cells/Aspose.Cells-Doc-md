---
title: الحصول على التحقق المطبق على خلية ما
type: docs
weight: 200
url: /ar/javascript-cpp/get-validation-applied-on-a-cell/
description: توضح هذه المقالة كيفية تطبيق التحقق على خلية باستخدام جافا سكريبت عبر C++.
keywords: تطبيق التحقق من الخلية في إكسل باستخدام جافا سكريبت عبر C++، تطبيق التحقق على خلية في إكسل باستخدام جافا سكريبت عبر C++، تطبيق التحقق في إكسل باستخدام جافا سكريبت عبر C++، التحقق من الخلية في إكسل باستخدام جافا سكريبت عبر C++، جافا سكريبت عبر C++ تطبيق التحقق من الخلايا في إكسل، جافا سكريبت عبر C++ تطبيق التحقق على خلية في إكسل، جافا سكريبت عبر C++ التحقق من خلايا إكسل
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells for JavaScript عبر C++ للحصول على التحقق المطبق على خلية. يوفر Aspose.Cells طريقة [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) لهذا الغرض. إذا لم يكن هناك تحقق مطبق على الخلية، فإنه يعيد null.

بالمثل، يمكنك استخدام الأسلوب [**Worksheet.validations.validationInCell(number, number)**](https://reference.aspose.com/cells/javascript-cpp/validationcollection/#validationInCell-number-number-) للحصول على التحقق المطبق على خلية عن طريق توفير مؤشرات الصف والعمود الخاصة بها.

{{% /alert %}}

## كود جافا سكريبت للحصول على التحقق المطبق على خلية

يعرض لك رمز العينة التالي كيفية الحصول على التحقق المطبق على خلية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Validation Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiate the workbook from the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Cell C1 has the Decimal Validation applied on it.
            const cell = worksheet.cells.get("C1");

            // Access the validation applied on this cell
            const validation = cell.validation;

            // Read various properties of the validation
            let output = '';
            output += '<p>Reading Properties of Validation</p>';
            output += '<hr />';
            output += `<p>Type: ${validation.type}</p>`;
            output += `<p>Operator: ${validation.operator}</p>`;
            output += `<p>Formula1: ${validation.formula1}</p>`;
            output += `<p>Formula2: ${validation.formula2}</p>`;
            output += `<p>Ignore blank: ${validation.ignoreBlank}</p>`;

            document.getElementById('result').innerHTML = output;
        });
    </script>
</html>
```


## مقالات ذات صلة

- [التحقق من البيانات](/cells/ar/javascript-cpp/data-validation/)
