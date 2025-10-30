---
title: Lösenordsskydda eller avskydda delat arbetsbok med JavaScript via C++
linktitle: Lösenordsskydda eller upphäva skyddet för delad arbetsbok
type: docs
weight: 10
url: /sv/javascript-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Möjliga användningsscenario**

Du kan skydda eller avsyna det delade arbetsboken med Microsoft Excel som visas i nästa skärmdump. Aspose.Cells for JavaScript via C++ stöder också denna funktion med metoderna [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#protectSharedWorkbook-string-) och [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Lösenordsskydda eller upplåsa den delade arbetsboken**

Följande exempelkod skapar en arbetsbok och skyddar den medan du aktiverar delning och sparar den som [utdata Excelfil](55541777.xlsx). På skärmbilden visas det att när du försöker avskydda den, ber Microsoft Excel dig att ange lösenordet för att avskydda den.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Shared Workbook Example</h1>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            // Creating an empty Workbook
            const workbook = new Workbook();

            // Protect the Shared Workbook with Password
            workbook.protectSharedWorkbook("1234");

            // Uncomment this line to Unprotect the Shared Workbook
            // workbook.unprotectSharedWorkbook("1234");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputProtectSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
