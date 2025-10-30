---
title: Arbeitsblatt Registerkartenfarbe mit JavaScript über C++ festlegen
linktitle: Registerkartenfarbe des Arbeitsblatts festlegen
type: docs
weight: 120
url: /de/javascript-cpp/set-worksheet-tab-color/
description: Dieser Artikel zeigt Beispielcode, mit dem die Registerkartenfarbe eines Excel Arbeitsblatts programmatisch mit JavaScript über C++ festgelegt wird.
keywords: Excel Registerkartenfarbe mit JavaScript über C++ festlegen, Code zum Festlegen der Excel Registerkartenfarbe mit JavaScript über C++
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, die Farbe einzelner Arbeitsblattregisterkarten zu ändern, um sie von anderen hervorzuheben. Zum Beispiel können Sie Ausgaben rot, Verkäufe grün, Vermögenswerte blau usw. machen.

{{% /alert %}}
## **Verwenden von Microsoft Excel zur Festlegung der Registerkartenfarbe des Arbeitsblatts**
1. Klicken Sie mit der rechten Maustaste auf eine Registerkarte im Registerblatt am unteren Rand des aktuellen Arbeitsblatts.
1. Wählen Sie **Registerkartenfarbe**.
1. Wählen Sie eine Farbe aus der Palette.
1. Klicken Sie auf **OK**.
## **Festlegen der Registerkartenfarbe mit Aspose.Cells**
Der folgende Beispielscode zeigt, wie Sie die Registerkartenfarbe mit Aspose.Cells festlegen können.

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
