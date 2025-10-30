---
title: Sätt Arkflikens Färg med JavaScript via C++
linktitle: Ställ in färg på arbetsbladets flik
type: docs
weight: 120
url: /sv/javascript-cpp/set-worksheet-tab-color/
description: Denna artikel visar exempel på kod som ställer in Excel arkflikens färg programmatiskt med JavaScript via C++.
keywords: sätt excel flikfärg JavaScript via C++, kod för att ställa in excel flikfärg JavaScript via C++
---

{{% alert color="primary" %}}

Aspose.Cells låter dig ändra färgen på individuella arbetsbladsflikar för att göra dem framträdande från resten. Till exempel kan du göra Utgifter röda, Försäljning gröna, Tillgångar blå, osv.

{{% /alert %}}
## **Ställa in färg på arbetsbladets flik i Microsoft Excel**
1. Högerklicka på en flik i flikarket längst ned på det aktuella arbetsbladet.
1. Välj **Flikfärg**.
1. Välj en färg från paletten.
1. Klicka på **OK**.
## **Ställa in färg på arbetsbladets flik med Aspose.Cells**
Exempelkoden nedan visar hur man ställer in flikfärg med Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Worksheet Tab Color Example</title>
    </head>
    <body>
        <h1>Set Worksheet Tab Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            worksheet.tabColor = AsposeCells.Color.Red;
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'worksheettabcolor.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet tab color set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
