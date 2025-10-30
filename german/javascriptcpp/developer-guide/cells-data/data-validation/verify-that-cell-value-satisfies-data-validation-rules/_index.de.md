---
title: Überprüfen Sie, ob der Zellenwert den Datenvalidierungsregeln entspricht
type: docs
weight: 210
url: /de/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Lernen Sie, wie Sie mit der Aspose.Cells for JavaScript via C++ verifizieren, ob ein Zellwert die Datenvalidierungsregeln erfüllt.
keywords: Zellvalidierungswert JavaScript via C++, Zellvalidierungswert JavaScript via C++, Überprüfen, ob ein Wert die auf die Zelle angewendeten Datenvalidierungsregeln erfüllt JavaScript via C++
---

{{% alert color="primary" %}} 

Microsoft Excel erlaubt es Benutzern, Datenvalidierungsregeln zu Zellen hinzuzufügen. Zum Beispiel gibt eine Dezimalvalidierung an, dass nur Zahlen zwischen 10 und 20 eingegeben werden können. Wenn ein Benutzer eine andere Zahl eingibt, zeigt Excel eine Fehlermeldung an und fordert ihn auf, eine Zahl im richtigen Bereich einzugeben. Wenn Sie eine Zahl, z.B. 3, in die Zelle kopieren und einfügen, überprüft Excel die Validierung nicht und zeigt keine Fehlermeldung an.

Manchmal ist es erforderlich, programmgesteuert zu überprüfen, ob ein Wert den auf die Zelle angewendeten Datenvalidierungsregeln entspricht. Im obigen Fall sollte der Eintrag beispielsweise fehlschlagen.

{{% /alert %}} 
## **Einführung**
Die Aspose.Cells for JavaScript via C++ bietet die Eigenschaft [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) zur programmgesteuerten Validierung von Zellwerten. Wenn der Wert in einer Zelle die angewendete Datenvalidierungsregel nicht erfüllt, gibt sie **false** zurück, sonst **true**.

Der folgende Beispielcode veranschaulicht, wie die Eigenschaft [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) funktioniert. Zuerst wird der Wert 3 in C1 eingegeben. Da dies die Datenüberprüfungsregel nicht erfüllt, gibt die Eigenschaft [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) **false** zurück. Dann wird der Wert 15 in C1 eingegeben. Da dieser Wert die Datenüberprüfungsregel erfüllt, gibt die Eigenschaft [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) **true** zurück. Ebenso wird **false** für den Wert 30 zurückgegeben.

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


### **Ergebnis**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
