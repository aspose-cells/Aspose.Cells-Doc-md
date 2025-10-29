---
title: Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal avec JavaScript via C++
linktitle: Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /fr/javascript-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Apprenez comment implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal en utilisant Aspose.Cells for JavaScript via C++. 
---

## **Scénarios d'utilisation possibles**

 Les formules Microsoft Excel peuvent avoir des noms différents selon les localisations, régions ou langues. Par exemple, la fonction **SUM** s'appelle **SUMME** en allemand. Aspose.Cells ne peut pas fonctionner avec des noms de fonctions non anglais. Dans Microsoft Excel VBA, il existe la propriété **Range.FormulaLocal** qui renvoie le nom de la fonction selon sa langue ou région. Aspose.Cells for JavaScript via C++ fournit également la propriété [**Cell.formulaLocal**](https://reference.aspose.com/cells/javascript-cpp/cell/#formulaLocal--) à cette fin. Cependant, cette propriété ne fonctionnera que lorsque vous implémentez la méthode [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-).

## **Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal**

Le code d'exemple suivant explique comment implémenter la méthode [**GlobalizationSettings.localFunctionName(standardName)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#localFunctionName-string-). La méthode retourne le nom local de la fonction standard. Si le nom de la fonction standard est **SUM**, elle retourne **UserFormulaLocal_SUM**. Vous pouvez modifier le code selon vos besoins et retourner les noms de fonctions locaux corrects, par exemple, **SUM** est **SUMME** en allemand et **TEXT** est **ТЕКСТ** en russe. Veuillez également voir la sortie console du code d'exemple ci-dessous pour référence.

## **Code d'exemple**

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

## **Sortie console**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
