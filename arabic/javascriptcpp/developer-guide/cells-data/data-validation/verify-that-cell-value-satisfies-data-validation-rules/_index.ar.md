---
title: التحقق من أن قيمة الخلية تفي بقواعد التحقق من البيانات
type: docs
weight: 210
url: /ar/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: تعرف على كيفية التحقق من أن قيمة الخلية تفي بقواعد التحقق من البيانات من خلال API Aspose.Cells for JavaScript عبر C++.
keywords: الحصول على قيمة التحقق من خلية جافا سكريبت عبر C++، الحصول على قيمة التحقق من خلية جافا سكريبت عبر C++، التحقق مما إذا كانت قيمة تفي بقواعد التحقق من البيانات المطبقة على الخلية جافا سكريبت عبر C++
---

{{% alert color="primary" %}} 

يسمح Microsoft Excel للمستخدمين بإضافة قواعد التحقق من البيانات إلى الخلايا. على سبيل المثال، تحدد التحقق العشري أن يتم إدخال أرقام بين 10 و20 فقط. إذا أدخل المستخدم رقمًا مختلفًا، يظهر Excel رسالة خطأ ويطالب بإدخال رقم في النطاق الصحيح. إذا نسخ ولصق رقم، مثل 3، في الخلية، فإن Excel لا يجري فحص تحقق أو يعرض رسالة خطأ.

في بعض الأحيان، يكون من الضروري التحقق مما إذا كانت القيمة تلبي قواعد التحقق من البيانات المطبقة على الخلية بشكل برمجي. في المثال أعلاه، على سبيل المثال، يجب أن يفشل الإدخال.

{{% /alert %}} 
## **مقدمة**
توفر Aspose.Cells for JavaScript عبر C++ خاصية [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) للتحقق من صحة قيم الخلايا برمجياً. إذا لم تلتزم القيمة في خلية بقواعد التحقق من البيانات المطبقة على تلك الخلية، فإنه يرجع **false**، وإلا **true**.

يُوضح رمز النموذج التالي كيفية عمل خاصية [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--). أولاً، يدخل القيمة 3 في C1. بسبب أنها لا تفي بقواعد التحقق من البيانات، فإن خاصية [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) تُرجع **false**. ثم، يدخل القيمة 15 في C1. لأنها تفي بقواعد التحقق من البيانات، تُرجع الخاصية **true**. وبالمثل، تُرجع **false** للقيمة 30.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Validation Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access Cell C1
            // Cell C1 has the Decimal Validation applied on it.
            // It can take only the values Between 10 and 20
            const cell = worksheet.cells.get("C1");

            // Enter 3 inside this cell (not between 10 and 20)
            cell.value = 3;

            // Check if number 3 satisfies the Data Validation rule applied on this cell
            const valid3 = cell.validationValue;
            console.log("Is 3 a Valid Value for this Cell: " + valid3);
            resultDiv.innerHTML += `<p>Is 3 a Valid Value for this Cell: ${valid3}</p>`;

            // Enter 15 inside this cell (between 10 and 20)
            cell.value = 15;

            // Check if number 15 satisfies the Data Validation rule applied on this cell
            const valid15 = cell.validationValue;
            console.log("Is 15 a Valid Value for this Cell: " + valid15);
            resultDiv.innerHTML += `<p>Is 15 a Valid Value for this Cell: ${valid15}</p>`;

            // Enter 30 inside this cell (not between 10 and 20)
            cell.value = 30;

            // Check if number 30 satisfies the Data Validation rule applied on this cell
            const valid30 = cell.validationValue;
            console.log("Is 30 a Valid Value for this Cell: " + valid30);
            resultDiv.innerHTML += `<p>Is 30 a Valid Value for this Cell: ${valid30}</p>`;
        });
    </script>
</html>
```


### **الناتج**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
