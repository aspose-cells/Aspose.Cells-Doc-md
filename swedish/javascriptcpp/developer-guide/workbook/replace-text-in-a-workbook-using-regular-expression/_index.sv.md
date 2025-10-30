---
title: Ersätt text i en arbetsbok med reguljära uttryck med JavaScript via C++
linktitle: Byt ut text i en arbetsbok med hjälp av reguljärt uttryck
type: docs
weight: 90
url: /sv/javascript-cpp/replace-text-in-a-workbook-using-regular-expression/
description: Ersätt text i en arbetsbok med reguljärt uttryck i JavaScript via C++.
---

Aspose.Cells erbjuder funktionen att byta ut text i en arbetsbok med hjälp av ett reguljärt uttryck. För detta tillhandahåller API:t [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--)-egenskapen i [**ReplaceOptions**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions)-klassen. Att ställa in [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) till **true** indikerar att den sökta nyckeln kommer att vara ett reguljärt uttryck.

Följande kodexempel visar användningen av [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--)-egenskapen med hjälp av [provfilen](101089318.xlsx). Den genererade [utdatafilen](101089319.xlsx) från kodexemplet bifogas för referens.

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Regex Replace Example</title>
    </head>
    <body>
        <h1>Regex Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ReplaceOptions } = AsposeCells;

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

            const replaceOptions = new ReplaceOptions();
            replaceOptions.caseSensitive = false;
            replaceOptions.matchEntireCellContents = false;
            replaceOptions.regexKey = true;

            workbook.replace("\\bKIM\\b", "^^^TIM^^^", replaceOptions);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RegexReplace_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Regex replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
