---
title: Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal con JavaScript a través de C++
linktitle: Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /es/javascript-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Aprende cómo implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal usando Aspose.Cells for JavaScript vía C++. 
---

## **Escenarios de uso posibles**

Las fórmulas de Microsoft Excel pueden tener diferentes nombres en diferentes regiones o idiomas. Por ejemplo, la función **SUM** se llama **SUMME** en alemán. Aspose.Cells no puede trabajar con nombres de funciones que no estén en inglés. En Microsoft Excel VBA, existe la propiedad **Range.FormulaLocal** que devuelve el nombre de la función según su idioma o región. Aspose.Cells for JavaScript vía C++ también proporciona la propiedad [**Cell.formulaLocal**](https://reference.aspose.com/cells/javascript-cpp/cell/#formulaLocal--) para este propósito. Sin embargo, esta propiedad solo funcionará cuando implementes el método [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-).

## **Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal**

El siguiente ejemplo de código explica cómo implementar el método [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-). El método devuelve el nombre local de la función estándar. Si el nombre de la función estándar es **SUM**, devuelve **UserFormulaLocal_SUM**. Puedes modificar el código según tus necesidades y devolver los nombres correctos de las funciones locales, por ejemplo, **SUM** es **SUMME** en alemán y **TEXT** es **ТЕКСТ** en ruso. También ve la salida en consola del ejemplo de código a continuación como referencia.

## **Código de muestra**

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

## **Salida de la consola**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
