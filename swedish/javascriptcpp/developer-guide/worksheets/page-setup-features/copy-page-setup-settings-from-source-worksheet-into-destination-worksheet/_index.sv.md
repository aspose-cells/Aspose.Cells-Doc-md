---
title: Kopiera sidinställningsinställningar från kälvark till måvark med JavaScript via C++
linktitle: Kopiera siduppsättning inställningar från kälark till destinationsark
type: docs
weight: 80
url: /sv/javascript-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Denna artikel förklarar hur man använder JavaScript API eller C++ bibliotek exempel för att kopiera sidinställningsinställningar från ett kälvark till ett målark programmatisk.
keywords: kopiera sidinställningar JavaScript via C++, kopiera sidinställningar till målark JavaScript via C++
---

## **Möjliga användningsscenario**

När du lägger till ett nytt blad i en arbetsbok, innehåller det standard *Sidinställningar*. Det kan finnas tillfällen när du behöver överföra inställningarna ([**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)) från ett arbetsblad till ett annat. Denna dokument förklarar hur man kopierar sidinställningsinställningar från ett arbetsblad till ett annat med hjälp av Aspose.Cells for JavaScript via C++ API:er.

## **Kopiera siduppsättning inställningar från källkalkylblad till destinations kalkylblad**

Följande exempelkod illustrerar hur man kopierar *sidlayoutinställningar* från ett blad till ett annat med hjälp av [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#copy-pagesetup-copyoptions-)-metoden. Se följande exempelkod och dess konsolresultat som referens.

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Copy</title>
    </head>
    <body>
        <h1>PageSetup Copy Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CopyOptions, PaperSizeType, Utils } = AsposeCells;

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
            // Create workbook
            const wb = new Workbook();

            // Add two test worksheets
            wb.worksheets.add("TestSheet1");
            wb.worksheets.add("TestSheet2");

            // Access both worksheets as TestSheet1 and TestSheet2
            const TestSheet1 = wb.worksheets.get("TestSheet1");
            const TestSheet2 = wb.worksheets.get("TestSheet2");

            // Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
            TestSheet1.pageSetup.paperSize = PaperSizeType.PaperA3ExtraTransverse;

            // Print the Paper Size of both worksheets (before copy)
            const before1 = TestSheet1.pageSetup.paperSize;
            const before2 = TestSheet2.pageSetup.paperSize;

            // Copy the PageSetup from TestSheet1 to TestSheet2
            TestSheet2.pageSetup.copy(TestSheet1.pageSetup, new CopyOptions());

            // Print the Paper Size of both worksheets (after copy)
            const after1 = TestSheet1.pageSetup.paperSize;
            const after2 = TestSheet2.pageSetup.paperSize;

            // Display results
            document.getElementById('result').innerHTML =
                '<pre>' +
                'Before Paper Size (TestSheet1): ' + before1 + '\n' +
                'Before Paper Size (TestSheet2): ' + before2 + '\n\n' +
                'After Paper Size (TestSheet1): ' + after1 + '\n' +
                'After Paper Size (TestSheet2): ' + after2 +
                '</pre>';

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
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

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
