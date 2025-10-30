---
title: Få alla dolda radindex efter att autofiltreringen har uppdaterats 
type: docs  
weight: 320  
url: /sv/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Lär dig hur du får alla dolda radindex efter att AutoFilter har uppdaterats med hjälp av Aspose.Cells for JavaScript via C++ API.  
keywords: Hämta alla index för dolda rader efter uppdatering av AutoFilter JavaScript via C++, Hämta alla index för dolda rader efter uppdatering av AutoFilter JavaScript via C++, Hämta alla index för dolda rader efter uppdatering av AutoFilter JavaScript via C++  
---

## **Möjliga användningsscenario**  

När du använder auto filter på arbetsbladsceller döljs några rader automatiskt. Men det kan vara så att vissa rader redan är dolda manuellt av Excel-slutanvändaren och de är inte dolda av ett auto filter. Det gör det svårt att veta vilka rader som är dolda av auto filtret och vilka som är manuellt dolda av Excel-slutanvändaren. Aspose.Cells for JavaScript via C++ hanterar detta problem med hjälp av egenskapen `[**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-)`. Denna metod returnerar radindex för alla rader som är dolda av auto filtret och inte manuellt av Excel-slutanvändaren.  

## **Hämta alla dolda radindex efter uppdatering av autofilter**  

Se följande exempel som laddar den [exempel-Excel filen](64716909.xlsx) som innehåller några rader dolda manuellt av användaren. Koden använder autofilter och uppdaterar det med hjälp av `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-) som returnerar radindex för alla dolda rader av autofilter. Den skriver sedan ut indexen för de dolda raderna på konsolen tillsammans med cellnamn och värden.  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Hidden Rows After Refreshing AutoFilter</title>
    </head>
    <body>
        <h1>Get Hidden Rows After Refreshing AutoFilter</h1>
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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Apply autofilter
            worksheet.autoFilter.addFilter(0, "Orange");

            // True means it will refresh autofilter and return hidden rows.
            const rowIndices = worksheet.autoFilter.refresh(true);

            console.log("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.");
            console.log("--------------------------");

            let output = '<p>Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.</p><pre>';
            rowIndices.forEach(r => {
                const cell = worksheet.cells.get(r, 0);
                console.log(`${r}\t${cell.name}\t${cell.stringValue}`);
                output += `${r}\t${cell.name}\t${cell.stringValue}\n`;
            });
            output += '</pre>';

            resultDiv.innerHTML = output;
        });
    </script>
</html>
```


## **Konsoloutput**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}
