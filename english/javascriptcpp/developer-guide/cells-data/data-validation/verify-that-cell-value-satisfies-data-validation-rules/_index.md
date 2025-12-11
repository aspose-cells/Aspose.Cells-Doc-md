---
title: Verify that Cell Value Satisfies Data Validation Rules
type: docs
weight: 210
url: /javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Learn how to verify cell value satisfies data validation rules through the Aspose.Cells for JavaScript via C++ API.
keywords: Get Cell Validation Value JavaScript via C++, Obtain Cell Validation Value JavaScript via C++, Verify whether a value satisfies the data validation rules applied to the cell JavaScript via C++
---

{{% alert color="primary" %}} 

Microsoft Excel allows users to add data validation rules to cells. For example, a decimal validation specifies that only numbers between 10 and 20 can be entered. If a user enters a different number, Microsoft Excel shows an error message and prompts them to enter a number in the correct range. If you copy and paste a number, say 3, into the cell, Excel does not run a validation check or show an error message.

Sometimes, it is necessary to verify whether a value satisfies the data validation rules applied to the cell programmatically. In the case above, for example, the entry should fail.

{{% /alert %}} 

## **Introduction**
Aspose.Cells for JavaScript via C++ provides the [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) property to validate cell values programmatically. If the value in a cell does not satisfy the data validation rule applied to that cell, it returns **false**, otherwise **true**.

The following sample code illustrates how the [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) property works. First, it enters the value 3 into C1. Because this does not satisfy the data validation rule, the [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) property returns **false**. Then, it enters the value 15 into C1. Because this value satisfies the data validation rule, the property returns **true**. Similarly, it returns **false** for the value 30.

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
            // Cell C1 has the Decimal Validation applied to it.
            // It can take only the values between 10 and 20
            const cell = worksheet.cells.get("C1");

            // Enter 3 inside this cell (not between 10 and 20)
            cell.value = 3;

            // Check if number 3 satisfies the data validation rule applied to this cell
            const valid3 = cell.validationValue;
            console.log("Is 3 a Valid Value for this Cell: " + valid3);
            resultDiv.innerHTML += `<p>Is 3 a Valid Value for this Cell: ${valid3}</p>`;

            // Enter 15 inside this cell (between 10 and 20)
            cell.value = 15;

            // Check if number 15 satisfies the data validation rule applied to this cell
            const valid15 = cell.validationValue;
            console.log("Is 15 a Valid Value for this Cell: " + valid15);
            resultDiv.innerHTML += `<p>Is 15 a Valid Value for this Cell: ${valid15}</p>`;

            // Enter 30 inside this cell (not between 10 and 20)
            cell.value = 30;

            // Check if number 30 satisfies the data validation rule applied to this cell
            const valid30 = cell.validationValue;
            console.log("Is 30 a Valid Value for this Cell: " + valid30);
            resultDiv.innerHTML += `<p>Is 30 a Valid Value for this Cell: ${valid30}</p>`;
        });
    </script>
</html>
```


### **Output**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}