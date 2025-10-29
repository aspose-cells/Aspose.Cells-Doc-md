---
title: Préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage
type: docs
weight: 310
url: /fr/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Apprenez comment préserver le préfixe de guillemet simple de la valeur ou plage de cellules via l API Aspose.Cells for JavaScript via C++.
keywords: Préserver le préfixe de guillemet simple de la valeur ou plage de cellules JavaScript via C++, masquer l apostrophe ou le guillemet simple en tête JavaScript via C++, afficher l apostrophe ou le guillemet simple en tête JavaScript via C++
---

## **Scénarios d'utilisation possibles**

Lorsque vous placez une valeur à l'intérieur de la cellule qui comporte une apostrophe ou un guillemet simple en tête, Microsoft Excel la cache, mais lorsque vous sélectionnez la cellule, elle affiche l'apostrophe ou le guillemet simple en tête dans une barre de formule comme indiqué dans la capture d'écran suivante.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for JavaScript via C++ masque également l'apostrophe ou le guillemet simple en tête comme Microsoft Excel mais il définit [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-) comme **vrai** pour cette cellule. Si vous définissez un style vide pour la cellule, alors [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) devient **faux** à nouveau. Pour gérer cette problématique, Aspose.Cells for JavaScript via C++ fournit la propriété [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-). Lorsqu'elle est définie sur **faux**, alors [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) n'est pas mis à jour du tout et sa valeur ancienne est préservée. Cela signifie que si l'ancienne valeur de [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) était **vrai**, elle restera **vraie** et si elle était **fausse**, elle restera **fausse**.

## **Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage**

Le code suivant explique l'utilisation de [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-) comme décrit précédemment. Veuillez lire les commentaires dans le code et voir la sortie console du code ci-dessous pour plus d'aide.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells QuotePrefix Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>QuotePrefix Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');
            const outputLines = [];

            // Create workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell A1
            const cell = ws.cells.get("A1");

            // Put some text in cell, it does not have Single Quote at the beginning
            cell.value = "Text";

            // Access style of cell A1
            let st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Put some text in cell, it has Single Quote at the beginning
            cell.value = "'Text";

            // Access style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Print information about StyleFlag.QuotePrefix property
            outputLines.push("");
            outputLines.push("When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.");
            outputLines.push("Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.");
            outputLines.push("");

            // Create an empty style
            st = wb.createStyle();

            // Create style flag - set StyleFlag.QuotePrefix as false
            // It means, we do not want to update the Style.QuotePrefix property of cell A1's style.
            let flag = new AsposeCells.StyleFlag();
            flag.quotePrefix = false;

            // Create a range consisting of single cell A1
            const rng = ws.cells.createRange("A1");

            // Apply the style to the range
            rng.applyStyle(st, flag);

            // Access the style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            // It will print True, because we have not updated the Style.QuotePrefix property of cell A1's style.
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Create an empty style
            st = wb.createStyle();

            // Create style flag - set StyleFlag.QuotePrefix as true
            // It means, we want to update the Style.QuotePrefix property of cell A1's style.
            flag = new AsposeCells.StyleFlag();
            flag.quotePrefix = true;

            // Apply the style to the range
            rng.applyStyle(st, flag);

            // Access the style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            // It will print False, because we have updated the Style.QuotePrefix property of cell A1's style.
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Update result div
            resultDiv.innerHTML = "<pre>" + outputLines.join("\n") + "</pre>";

            // Save the modified workbook and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';
        });
    </script>
</html>
```



## **Sortie console**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
