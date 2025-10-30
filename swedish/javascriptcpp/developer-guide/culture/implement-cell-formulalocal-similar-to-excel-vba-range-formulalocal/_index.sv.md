---
title: Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal med JavaScript via C++
linktitle: Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /sv/javascript-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Lär dig hur man implementerar Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal med Aspose.Cells for JavaScript via C++. 
---

## **Möjliga användningsscenario**

Microsoft Excels formelnamn kan ha olika namn i olika platser eller språk. Till exempel heter **SUM**-funktionen **SUMME** på tyska. Aspose.Cells kan inte använda icke-engelska funktionsnamn. I Microsoft Excel VBA finns **Range.FormulaLocal**-attributet som returnerar funktionsnamnets namn på dess språk eller region. Aspose.Cells for JavaScript via C++ erbjuder också [**Cell.formulaLocal**](https://reference.aspose.com/cells/javascript-cpp/cell/#formulaLocal--)-egenskapen för detta ändamål. Denna egenskap fungerar dock endast när du implementerar [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-)-metoden.

## **Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal**

Följande kodexempel förklarar hur man implementerar [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-)-metoden. Metoden returnerar det lokala namnet för en standardfunktion. Om standard funktionsnamnet är **SUM** returneras **UserFormulaLocal_SUM**. Du kan ändra koden efter behov och returnera rätt lokala funktionsnamn, t.ex. är **SUM** **SUMME** på tyska och **TEXT** är **ТЕКСТ** på ryska. Se även exempelutdata från kodexemplet nedan för referens.

## **Exempelkod**

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

## **Konsoloutput**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
