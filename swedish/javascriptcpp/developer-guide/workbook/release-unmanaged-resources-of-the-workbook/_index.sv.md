---
title: Frigör ohanterade resurser i arbetsboken med JavaScript via C++
linktitle: Frigör ohanterade resurser i arbetsboken
type: docs
weight: 310
url: /sv/javascript-cpp/release-unmanaged-resources-of-the-workbook/
description: Lär dig att frigöra ohanterade resurser i arbetsboksobjektet med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--)-metoden för att frigöra de oanvände resurserna för [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-objektet. Disposeringsmönstret används endast för objekt som tillgång till oanvänt resurser, som fil- och rörhandtag, registretaggar, väntande handtag eller pekare till block av oanvänt minne. Detta beror på att garbage collection är mycket effektiv på att återvinna oanvända hanterade objekt, men kan inte återvinna oanvänt minne.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-objekt implementerar nu *System.IDisposable*-gränssnittet som har en metod [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--). Du kan antingen kalla [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--)-metoden direkt eller använda *Using*-satsen för att automatiskt kalla denna metod.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Dispose Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create workbook object
            const wb1 = new Workbook();

            // Call Dispose method
            wb1.dispose();

            // Call Dispose method via a scoped approach
            (async () => {
                const wb2 = new Workbook();
                // Any other code goes here
                wb2.dispose();
            })();

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully!</p>';
        });
    </script>
</html>
```
