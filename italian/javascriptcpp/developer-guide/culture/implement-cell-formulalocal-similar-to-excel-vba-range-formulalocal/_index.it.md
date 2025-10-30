---
title: Implementa Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal con JavaScript tramite C++
linktitle: Implementa la Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /it/javascript-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Impara come implementare Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal usando Aspose.Cells for JavaScript tramite C++. 
---

## **Possibili Scenari di Utilizzo**

Le formule di Microsoft Excel possono avere nomi diversi in diverse località, regioni o lingue. Ad esempio, la funzione **SUM** è chiamata **SUMME** in tedesco. Aspose.Cells non può funzionare con nomi di funzioni non in inglese. In Microsoft Excel VBA, c'è la proprietà **Range.FormulaLocal** che restituisce il nome della funzione secondo la lingua o regione. Aspose.Cells for JavaScript tramite C++ fornisce anche la proprietà [**Cell.formulaLocal**](https://reference.aspose.com/cells/javascript-cpp/cell/#formulaLocal--) per questo scopo. Tuttavia, questa proprietà funzionerà solo quando si implementa il metodo [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-).

## **Implementa Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal**

Il seguente esempio di codice spiega come implementare il metodo [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-). Il metodo restituisce il nome locale della funzione standard. Se il nome della funzione standard è **SUM**, ritorna **UserFormulaLocal_SUM**. Puoi modificare il codice secondo le tue esigenze e restituire i nomi corretti delle funzioni locali, ad esempio **SUM** è **SUMME** in tedesco e **TEXT** è **ТЕКСТ** in Russo. Vedi anche l'output sulla console del codice di esempio fornito sotto per riferimento.

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Globalization Example</h1>
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

        // Define GS class implementing localization override
        class GS extends AsposeCells.GlobalizationSettings {
            localFunctionName(standardName) {
                // Change the SUM function name as per your needs.
                if (standardName === "SUM") {
                    return "UserFormulaLocal_SUM";
                }

                // Change the AVERAGE function name as per your needs.
                if (standardName === "AVERAGE") {
                    return "UserFormulaLocal_AVERAGE";
                }

                return "";
            }
        }

        document.getElementById('runExample').addEventListener('click', () => {
            const resultDiv = document.getElementById('result');

            // Create workbook
            const wb = new Workbook();

            // Assign GlobalizationSettings implementation class
            wb.settings.globalizationSettings = new GS();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access some cell
            const cell = ws.cells.get("C4");

            // Assign SUM formula and get its FormulaLocal
            cell.formula = "SUM(A1:A2)";
            const formulaLocal1 = cell.formulaLocal;

            // Assign AVERAGE formula and get its FormulaLocal
            cell.formula = "=AVERAGE(B1:B2, B5)";
            const formulaLocal2 = cell.formulaLocal;

            resultDiv.innerHTML = `<p>Formula Local 1: ${formulaLocal1}</p><p>Formula Local 2: ${formulaLocal2}</p>`;

            // Save the workbook and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

## **Output della console**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
