---
title: Spara arbetsboken i strikt Open XML kalkylbladsformat med JavaScript via C++
linktitle: Spara arbetsbok till strikt öppet XML kalkylbladsformat
type: docs
weight: 150
url: /sv/javascript-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Lär dig hur du sparar en arbetsbok i strikt Open XML kalkylbladsformat med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**

Aspose.Cells for JavaScript via C++ tillåter dig att spara arbetsboken i *Strikt Open XML Kalkylblad* format. För detta syfte tillhandahålls egenskapen [**WorkbookSettings.compliance**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#compliance--). Om du sätter dess värde till [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompliance) kommer den utgående Excel-filen att sparas i Strikt Open XML Kalkylblad-format.

## **Spara arbetsbok i strikt öppet XML-kalkylbladsformat**

Följande exempel skapar en arbetsbok och ställer in värdet av egenskapen [**WorkbookSettings.compliance**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#compliance--) till [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompliance) och sparar den som [utdata Excel-fil](67338272.xlsx). Om du öppnar den genererade Excel-filen i Microsoft Excel och öppnar Spara Som... dialogrutan, kommer du att se dess format som *Strict Open XML Kalkylblad* som visas i denna skärmbild.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Save Workbook to Strict Open XML Spreadsheet Format</title>
    </head>
    <body>
        <h1>Save Workbook to Strict Open XML Spreadsheet Format</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OoxmlCompliance, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();

            // Specify - Strict Open XML Spreadsheet - Format.
            workbook.settings.compliance = OoxmlCompliance.Iso29500_2008_Strict;

            // Access first worksheet and set value in B4
            const worksheet = workbook.worksheets.get(0);
            const b4 = worksheet.cells.get("B4");
            b4.value = "This Excel file has Strict Open XML Spreadsheet format.";

            // Save to output Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved to Strict Open XML Spreadsheet format. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
