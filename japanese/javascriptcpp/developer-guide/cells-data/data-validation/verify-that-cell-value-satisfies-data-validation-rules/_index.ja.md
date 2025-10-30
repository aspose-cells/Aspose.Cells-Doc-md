---
title: セルの値がデータ検証ルールを満たしているかを確認
type: docs
weight: 210
url: /ja/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: C++のAspose.Cells for JavaScript APIを通じて、セルの値がデータ検証ルールを満たしているかどうかを検証する方法を学びます。
keywords: C++経由のJavaScriptを使用してセル検証値を取得、C++経由のJavaScriptでセル検証値を取得、セルが適用されたデータ検証ルールを満たしているかどうかを検証する
---

{{% alert color="primary" %}} 

Microsoft Excelは、セルにデータ検証ルールを追加できるようにしています。例えば、少数点の検証は10から20の間の数値のみを入力可能にします。異なる数字を入力した場合、Excelはエラーメッセージを表示し、正しい範囲の数字を入力するよう促します。数字をコピー＆ペーストした場合、検証は行われずエラーメッセージも表示されません。

時には、プログラムでセルに適用されたデータ検証ルールが値を満たしているかどうかを検証する必要があります。たとえば、上記の場合、エントリが失敗する必要があります。

{{% /alert %}} 
## **紹介**
C++経由のAspose.Cells for JavaScriptは、[Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--)プロパティを提供し、セル値のプログラムによる検証を可能にします。セルの値がそのセルに適用されたデータ検証ルールを満たさない場合は**false**を返し、満たす場合は**true**を返します。

次のサンプルコードは、[Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--)プロパティの動作例を示しています。まず、C1に値3を入力します。これはデータ検証ルールを満たさないため、[Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--)プロパティは**false**を返します。次に、値15を入力すると、検証ルールを満たすため、**true**を返します。同様に、値30に対しては**false**を返します。

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


### **出力**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
