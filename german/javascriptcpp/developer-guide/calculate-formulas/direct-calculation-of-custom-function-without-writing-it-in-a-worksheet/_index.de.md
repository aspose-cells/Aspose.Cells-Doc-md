---
title: Direkte Berechnung einer benutzerdefinierten Funktion, ohne sie in einem Arbeitsblatt mit JavaScript via C++ zu schreiben
linktitle: Direkte Berechnung einer benutzerdefinierten Funktion ohne sie in einem Arbeitsblatt zu schreiben
description: Dieser Artikel führt ein, wie man die Aspose.Cells Bibliothek nutzt, um benutzerdefinierte Funktionen direkt in Microsoft Excel zu berechnen, ohne die Funktion in einem Arbeitsblatt mit JavaScript via C++ zu schreiben. Laden Sie eine bestehende Excel Datei oder erstellen Sie eine neue, berechnen Sie die benutzerdefinierte Funktion und speichern Sie die modifizierte Datei.
keywords: Aspose.Cells, Excel, benutzerdefinierte Funktionen, direkte Berechnungen, JavaScript via C++, kein Schreiben notwendig, Arbeitsblätter
type: docs
weight: 90
url: /de/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Direkte Berechnung einer benutzerdefinierten Funktion ohne Eintragung in ein Arbeitsblatt**

Dieses Thema erklärt, wie Sie Ihre benutzerdefinierten Funktionen direkt berechnen können, ohne sie zuerst in einem Arbeitsblatt zu schreiben. Bitte verwenden Sie dafür die [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-CalculationOptions-)-Methode.

Bitte beachten Sie den folgenden Beispielcode, der die Verwendung dieser Methode veranschaulicht. Wir haben eine benutzerdefinierte Funktion namens MyCompany.CustomFunction() verwendet und ihren Wert als "Aspose.Cells." selbst berechnet. Dieser Wert wird dann automatisch mit dem Wert der Zelle A1, der "Willkommen bei " durch den Berechnungsmotor, konkateniert und der endgültig berechnete Wert als "Willkommen bei Aspose.Cells." zurückgegeben. Wie Sie im Code sehen können, haben wir unsere benutzerdefinierte Funktion nirgendwo in einem Arbeitsblatt geschrieben und sie wird direkt durch unsere eigene benutzerdefinierte Logik berechnet.

### **Programmierbeispiel**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Custom Function Example</title>
    </head>
    <body>
        <h1>Implement Direct Calculation Of Custom Function</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AbstractCalculationEngine, CalculationOptions } = AsposeCells;

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

        class CustomEngine extends AbstractCalculationEngine {
            // Override the calculate method with custom logic
            calculate(data) {
                // Check the formula name and calculate it yourself
                if (data.functionName === "MyCompany.CustomFunction") {
                    // This is our calculated value
                    data.calculatedValue = "Aspose.Cells.";
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Add some text in cell A1
            ws.cells.get("A1").putValue("Welcome to ");

            // Create a calculation options with custom engine
            const opts = new CalculationOptions();
            opts.customEngine = new CustomEngine();

            // This line shows how you can call your own custom function without
            // a need to write it in any worksheet cell
            // After the execution of this line, it will return
            // Welcome to Aspose.Cells.
            const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

            // Write the returned value into B1 for demonstration
            ws.cells.get("B1").putValue(ret);

            // Prepare download of the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculated Value: ' + ret + '</p>';
        });
    </script>
</html>
```

### **Konsolenausgabe**

Im Folgenden finden Sie die Konsolenausgabe des obigen Beispielcodes.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Verwandter Artikel**

{{% alert color="primary" %}}

 [Implementieren Sie eine benutzerdefinierte Berechnungseinheit, um die Standard-Berechnungseinheit von Aspose.Cells zu erweitern](/cells/de/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
