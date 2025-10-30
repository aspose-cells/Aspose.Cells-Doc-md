---
title: Bevara Enkelkavot Prefix of Cell Value or Range
type: docs
weight: 310
url: /sv/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Lär dig att bevara enkel citat prefix av cellvärde eller område genom Aspose.Cells for JavaScript via C++ API.
keywords: Bevara enkel citat prefix av cellvärde eller område JavaScript via C++, göm ledande apostrof eller enkel citattecken JavaScript via C++, visa ledande apostrof eller enkel citattecken JavaScript via C++
---

## **Möjliga användningsscenario**

När du sätter ett värde i cellen som har ledande apostrof eller citattecken, döljer sedan Microsoft Excel det, men när du väljer cellen visas den ledande apostrof eller citattecken i en formlerad som visas i följande skärmbild.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for JavaScript via C++ döljer även det ledande apostrofen eller enkla citattecknet likt Microsoft Excel men ställer in [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-) som **true** för den cellen. Om du tilldelar ett tomt stilark till cellen blir [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) återigen **false**. För att hantera detta tillhandahåller Aspose.Cells for JavaScript via C++ egenskapen [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-). När den är satt till **false**, uppdateras inte [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) alls och dess gamla värde behålls. Det betyder att om det gamla värdet av [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) var **true**, förblir det **true** och om det var **false**, förblir det **false**.

## **Bevara enskild citattecken prefiks av cellvärde eller område**

Följande kod förklarar användningen av [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-) som beskrivs tidigare. Läs gärna kommentarerna i koden och se utmatningen i konsolen för mer hjälp.

## **Exempelkod**

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



## **Konsoloutput**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
