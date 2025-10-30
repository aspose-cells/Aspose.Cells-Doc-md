---
title: Hitta om arbetsbladet är ett Dialogark med JavaScript via C++
linktitle: Ta reda på om kalkylbladet är Dialog sheet
type: docs
weight: 90
url: /sv/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Denna artikel innehåller instruktioner och exempel på kod för att programmässigt avgöra om ett Excel arbetsblad är ett dialogark med Aspose.Cells for JavaScript via C++.
keywords: hitta excel arbetsblad dialogtyp JavaScript via C++, arbetsblad dialog JavaScript via C++
---

## **Möjliga användningsscenario**

Dialogark är ett gammalt format av blad som innehåller en dialogruta. Ett sådant blad kan infogas av en äldre version av Microsoft Excel, t.ex. 2003, som visas i skärmbilden. Det kan också infogas med VBA i nyare versioner, t.ex. Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Du kan hitta om arket är ett dialogark eller någon annan typ av blad med [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--) egenskapen som tillhandahålls av Aspose.Cells for JavaScript via C++. Om det returnerar enum-värdet [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype), betyder det att du har att göra med ett dialogark.

## **Ta reda på om kalkylbladet är Dialog sheet**

Följande exempel på kod laddar [exempelfil](64716820.xlsx) som innehåller ett dialogblad. Den kontrollerar egenskapen [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--), jämför den med [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype) och skriver ut ett meddelande. Se konsolutdata för exemplet nedan för mer hjälp.

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Detect Dialog Sheet</title>
    </head>
    <body>
        <h1>Detect if Worksheet Is a Dialog Sheet</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Find if the sheet type is dialog and print the message
            if (ws.type === AsposeCells.SheetType.Dialog) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet is a Dialog Sheet.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is NOT a Dialog Sheet.</p>';
            }
        });
    </script>
</html>
```

## **Konsoloutput**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
