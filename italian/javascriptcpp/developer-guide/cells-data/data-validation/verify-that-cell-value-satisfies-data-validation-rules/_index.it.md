---
title: Verificare che il valore della cella soddisfi le regole di convalida dei dati
type: docs
weight: 210
url: /it/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Scopri come verificare se il valore di una cella soddisfa le regole di validazione dei dati tramite l API Aspose.Cells for JavaScript via C++.
keywords: Ottieni il valore di validazione della cella JavaScript tramite C++, ottieni il valore di validazione della cella JavaScript tramite C++, verifica se un valore soddisfa le regole di validazione dei dati applicate alla cella JavaScript tramite C++
---

{{% alert color="primary" %}} 

Microsoft Excel consente agli utenti di aggiungere regole di validazione dei dati alle celle. Ad esempio, una validazione decimale specifica che possono essere inseriti solo numeri tra 10 e 20. Se l'utente inserisce un numero diverso, Excel mostra un messaggio di errore e invita a inserire un numero nel range corretto. Se si copia e incolla un numero, per esempio 3, nella cella, Excel non esegue un controllo di validazione né mostra un messaggio di errore.

A volte è necessario verificare se un valore soddisfa le regole di convalida dei dati applicate alla cella in modo programmatico. Nel caso sopra, ad esempio, l'ingresso dovrebbe fallire.

{{% /alert %}} 
## **Introduzione**
Aspose.Cells for JavaScript tramite C++ fornisce la proprietà [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) per convalidare i valori delle celle programmaticamente. Se il valore in una cella non soddisfa la regola di validazione dei dati applicata a quella cella, restituisce **false**, altrimenti **true**.

Il seguente esempio di codice illustra come funziona la proprietà [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--). Innanzitutto, inserisce il valore 3 in C1. Poiché questo non soddisfa la regola di validazione dei dati, la proprietà [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) restituisce **false**. Poi, inserisce il valore 15 in C1. Poiché questo valore soddisfa la regola di validazione dei dati, la proprietà [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) restituisce **true**. Allo stesso modo, restituisce **false** per il valore 30.

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
