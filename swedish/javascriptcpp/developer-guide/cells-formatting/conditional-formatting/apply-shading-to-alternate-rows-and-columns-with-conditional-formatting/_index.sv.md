---
title: Tillämpa skuggning på alternerande rader och kolumner med villkorlig formatering
linktitle: Tillämpa skuggning på alternerande rader och kolumner med villkorlig formatering
description: Hur man använder Aspose.Cells biblioteket i JavaScript via C++ för att tillämpa villkorsstyrd skuggning för alternerande rader och kolumner. Genom att justera dessa kriterier har du mer kontroll över hur cellerna ser ut och framstår.
keywords: Aspose.Cells, Villkorsstyrd formatering, JavaScript via C++, Alternativa rader, Alternativa kolumner, Skuggor
type: docs
weight: 30
url: /sv/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API:er ger möjligheten att lägga till och manipulera regler för villkorsstyrd formatering för [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-objektet. Dessa regler kan anpassas på flera sätt för att få önskad formatering baserat på villkor eller regler. Denna artikel kommer att demonstrera användningen av Aspose.Cells for JavaScript via C++ API:er för att tillämpa skuggning på alternativa rader och kolumner med hjälp av regler för villkorsstyrd formatering och Excels inbyggda funktioner.

{{% /alert %}}

Denna artikel använder Excels inbyggda funktioner såsom RAD, KOLUMN och MOD. Här är några detaljer om dessa funktioner för en bättre förståelse av kodsnutten som följer.

- **RAD()** funktionen returnerar radnumret för en cellreferens. Om referensparametern utelämnas, antar den att referensen är celladressen där RAD()-funktionen har använts.
- **KOLON()** funktionen returnerar kolumnnumret för en cellreferens. Om referensparametern utelämnas, antar den att referensen är celladressen där KOLON()-funktionen har använts.
- **MOD()**-funktionen returnerar resten efter att ett nummer har delats av en divisor, där det första parametern till funktionen är det numeriska värdet vars rest du vill hitta och det andra parametern är det tal som används för att dela in i nummerparametern. Om divisorn är 0 kommer den att returnera felen #DIV/0!.

Låt oss börja skriva kod för att uppnå detta mål med hjälp av Aspose.Cells for JavaScript via C++ API.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Conditional Formatting</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, Utils } = AsposeCells;

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
            // Create an instance of Workbook
            const book = new Workbook();

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Add FormatConditions to the instance of Worksheet
            let idx = sheet.conditionalFormattings.add();

            // Access the newly added FormatConditions via its index
            const conditionCollection = sheet.conditionalFormattings.get(idx);

            // Define a CellsArea on which conditional formatting will be applicable (A1 to I20)
            const area = CellArea.createCellArea("A1", "I20");

            // Add area to the instance of FormatConditions
            conditionCollection.addArea(area);

            // Add a condition to the instance of FormatConditions (Expression type)
            idx = conditionCollection.addCondition(AsposeCells.FormatConditionType.Expression);

            // Access the newly added FormatCondition via its index
            const formatCondition = conditionCollection.get(idx);

            // Set the formula for the FormatCondition
            formatCondition.formula1 = "=MOD(ROW(),2)=0";

            // Set the background color and pattern for the FormatCondition's Style
            formatCondition.style.backgroundColor = AsposeCells.Color.Blue;
            formatCondition.style.pattern = AsposeCells.BackgroundType.Solid;

            // Save the result and provide a download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


Följande ögonblicksbild visar det resulterande kalkylarket som är laddat i Excel-applikationen.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

För att applicera nyanser på alternativa kolumner, behöver du bara ändra formeln **=MOD(RAD(),2)=0** till **=MOD(KOLUMN(),2)=0**, det vill säga; istället för att få radindexet, modifiera formeln för att hämta kolumnindexet.  
Det resulterande kalkylarket kommer i detta fall att se ut som följer.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
