---
title: Bekräfta att cellvärdet uppfyller datavalideringsreglerna
type: docs
weight: 210
url: /sv/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Lär dig hur man verifierar att ett cellvärde uppfyller datavalideringsregler med API t Aspose.Cells for JavaScript via C++.
keywords: Hämta cellvalideringsvärde JavaScript via C++, Hämta cellvalideringsvärde JavaScript via C++, Verifiera om ett värde uppfyller reglerna för datavalidering som tillämpats på cellen i JavaScript via C++
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att lägga till datavalideringsregler på celler. Till exempel specificerar en decimaltalsvalidering att endast nummer mellan 10 och 20 kan matas in. Om en användare matar in ett annat nummer visar Excel ett felmeddelande och frågar användaren att ange ett nummer inom rätt intervall. Om du kopierar och klistrar in ett nummer, säg 3, i cellen, kör inte Excel någon valideringskontroll eller visar något felmeddelande.

Ibland är det nödvändigt att kontrollera om ett värde uppfyller datavalideringsreglerna som appliceras på cellen programmatiskt. I fallet ovan bör till exempel inmatningen misslyckas.

{{% /alert %}} 
## **Introduktion**
Aspose.Cells for JavaScript via C++ tillhandahåller egenskapen [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) för att validera cellvärden programmatiskt. Om värdet i en cell inte uppfyller datavalideringsregeln som tillämpats på den cellen, returnerar den **false**, annars **true**.

Följande exempel visar hur egenskapen [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) fungerar. Först matar det in värdet 3 i C1. Eftersom detta inte uppfyller datavalideringsregeln returnerar egenskapen [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) **false**. Sedan matar det in värdet 15 i C1. Eftersom detta värde uppfyller datavalideringsregeln returnerar egenskapen [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) **true**. På samma sätt returnerar det **false** för värdet 30.

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


### **Output**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
