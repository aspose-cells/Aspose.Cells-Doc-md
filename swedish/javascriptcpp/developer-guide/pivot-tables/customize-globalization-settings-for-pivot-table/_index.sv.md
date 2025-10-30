---
title: Anpassa globaliseringsinställningar för pivottabell med JavaScript via C++
linktitle: Anpassa globaliseringsinställningarna för Pivot tabell
type: docs
weight: 50
url: /sv/javascript-cpp/customize-globalization-settings-for-pivot-table/
---

## **Möjliga användningsscenario**

Ibland vill du anpassa texten för *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* enligt dina krav. Aspose.Cells for JavaScript via C++ tillåter dig att anpassa globaliseringsinställningarna för pivottabellen för att hantera sådana scenarier. Du kan också använda denna funktion för att ändra etiketterna till andra språk som arabiska, hindi, polska, etc.

## **Anpassa globaliseringsinställningarna för Pivot-tabell**

Följande exempelkod visar hur man anpassar globaliseringsinställningar för pivot-tabellen. Det skapar en klass *CustomPivotTableGlobalizationSettings* härledd från en bas<ol>klass [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/pivotglobalizationsettings/) och överskuggar alla nödvändiga metoder. Dessa metoder returnerar den anpassade texten för *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values*. Sedan tilldelas objektet av denna klass till [**WorkbookSettings.pivotSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#pivotSettings--)-egenskapen. Koden laddar det [ursprungliga excel-filen](40468488.xlsx) som innehåller pivot-tabellen, uppdaterar och beräknar dess data och sparar det som [utdata PDF](40468487.pdf). Följande skärmbild visar effekten av exemplet på PDF-filen. Som du kan se har olika delar av pivot-tabellen nu anpassad text som returneras av de överskuggade metoderna i [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/pivotglobalizationsettings/)-klassen.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Globalization Settings Example</title>
    </head>
    <body>
        <h1>Pivot Table Globalization Settings Example</h1>
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

        class CustomPivotTableGlobalizationSettings extends AsposeCells.PivotGlobalizationSettings {
            // Gets the name of "Total" label in the PivotTable.
            getTextOfTotal() {
                console.log("---------GetPivotTotalName-------------");
                return "AsposeGetPivotTotalName";
            }

            // Gets the name of "Grand Total" label in the PivotTable.
            getTextOfGrandTotal() {
                console.log("---------GetPivotGrandTotalName-------------");
                return "AsposeGetPivotGrandTotalName";
            }

            // Gets the name of "(Multiple Items)" label in the PivotTable.
            getTextOfMultipleItems() {
                console.log("---------GetMultipleItemsName-------------");
                return "AsposeGetMultipleItemsName";
            }

            // Gets the name of "(All)" label in the PivotTable.
            getTextOfAll() {
                console.log("---------GetAllName-------------");
                return "AsposeGetAllName";
            }

            // Gets the name of "Column Labels" label in the PivotTable.
            getTextOfColumnLabels() {
                console.log("---------GetColumnLabelsOfPivotTable-------------");
                return "AsposeGetColumnLabelsOfPivotTable";
            }

            // Gets the name of "Row Labels" label in the PivotTable.
            getTextOfRowLabels() {
                console.log("---------GetRowLabelsNameOfPivotTable-------------");
                return "AsposeGetRowLabelsNameOfPivotTable";
            }

            // Gets the name of "(blank)" label in the PivotTable.
            getTextOfEmptyData() {
                console.log("---------GetEmptyDataName-------------");
                return "(blank)AsposeGetEmptyDataName";
            }

            // Gets the name of PivotFieldSubtotalType type in the PivotTable.
            getTextOfSubTotal(subTotalType) {
                console.log("---------GetSubTotalName-------------");

                switch (subTotalType) {
                    case AsposeCells.PivotFieldSubtotalType.Sum:
                        return "AsposeSum";

                    case AsposeCells.PivotFieldSubtotalType.Count:
                        return "AsposeCount";

                    case AsposeCells.PivotFieldSubtotalType.Average:
                        return "AsposeAverage";

                    case AsposeCells.PivotFieldSubtotalType.Max:
                        return "AsposeMax";

                    case AsposeCells.PivotFieldSubtotalType.Min:
                        return "AsposeMin";

                    case AsposeCells.PivotFieldSubtotalType.Product:
                        return "AsposeProduct";

                    case AsposeCells.PivotFieldSubtotalType.CountNums:
                        return "AsposeCount";

                    case AsposeCells.PivotFieldSubtotalType.Stdev:
                        return "AsposeStdDev";

                    case AsposeCells.PivotFieldSubtotalType.Stdevp:
                        return "AsposeStdDevp";

                    case AsposeCells.PivotFieldSubtotalType.Var:
                        return "AsposeVar";

                    case AsposeCells.PivotFieldSubtotalType.Varp:
                        return "AsposeVarp";
                }

                return "AsposeSubTotalName";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Apply globalization settings and custom pivot table globalization settings
            workbook.settings.globalizationSettings = new AsposeCells.GlobalizationSettings();
            workbook.settings.globalizationSettings.pivotSettings = new CustomPivotTableGlobalizationSettings();

            // Hide first worksheet that contains the data of the pivot table
            workbook.worksheets.get(0).isVisible = false;

            // Access second worksheet
            const ws = workbook.worksheets.get(1);

            // Access the pivot table, refresh and calculate its data
            const pt = ws.pivotTables.get(0);
            pt.refreshDataFlag = true;
            pt.refreshData();
            pt.calculateData();
            pt.refreshDataFlag = false;

            // Pdf save options - save entire worksheet on a single pdf page
            const options = new AsposeCells.PdfSaveOptions();
            options.onePagePerSheet = true;

            // Save the output pdf 
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputPivotTableGlobalizationSettings.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
