---
title: Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal mit JavaScript in C++
linktitle: Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /de/javascript-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Lernen Sie, wie man Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal mit Aspose.Cells for JavaScript in C++ implementiert. 
---

## **Mögliche Verwendungsszenarien**

 Microsoft Excel-Formeln können in verschiedenen Regionen oder Sprachen unterschiedliche Namen haben. Zum Beispiel heißt die **SUM**-Funktion in Deutsch **SUMME**. Aspose.Cells kann nicht mit nicht-englischen Funktionsnamen arbeiten. In Microsoft Excel VBA gibt es die Eigenschaft **Range.FormulaLocal**, die den Funktionsnamen entsprechend der Sprache oder Region zurückgibt. Aspose.Cells for JavaScript in C++ bietet hierfür auch die [**Cell.formulaLocal**](https://reference.aspose.com/cells/javascript-cpp/cell/#formulaLocal--)-Eigenschaft. Diese Funktioniert jedoch nur, wenn Sie die [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-)-Methode implementieren.

## **Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal**

Das folgende Beispiel erklärt, wie die [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-)-Methode implementiert wird. Die Methode gibt den lokalen Namen der Standardfunktion zurück. Wenn der Standardfunktionsname **SUM** ist, gibt sie **UserFormulaLocal_SUM** zurück. Sie können den Code nach Ihren Bedürfnissen anpassen und die richtigen lokalen Funktionsnamen zurückgeben, z.B. ist **SUM** in Deutsch **SUMME** und **TEXT** in Russisch **ТЕКСТ**. Die Konsolenausgabe des unten stehenden Beispiels liefert ebenfalls Referenzinformationen.

## **Beispielcode**

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

## **Konsolenausgabe**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
