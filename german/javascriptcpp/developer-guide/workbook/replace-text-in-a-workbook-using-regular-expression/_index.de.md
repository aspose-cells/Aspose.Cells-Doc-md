---
title: Text in einem Arbeitsbuch mit regulärem Ausdruck in JavaScript über C++ ersetzen
linktitle: Ersetzen von Text in einer Arbeitsmappe mittels regulären Ausdrücken
type: docs
weight: 90
url: /de/javascript-cpp/replace-text-in-a-workbook-using-regular-expression/
description: Text in einem Arbeitsbuch mit regulärem Ausdruck in JavaScript über C++ ersetzen.
---

Aspose.Cells bietet die Funktion, Text in einer Arbeitsmappe mithilfe eines regulären Ausdrucks zu ersetzen. Dafür stellt die API die [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) Eigenschaft der [**ReplaceOptions**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions) Klasse bereit. Wenn Sie [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--) auf **true** setzen, bedeutet dies, dass der gesuchte Schlüssel ein regulärer Ausdruck ist.

Das folgende Codebeispiel demonstriert die Verwendung der [**ReplaceOptions.regexKey**](https://reference.aspose.com/cells/javascript-cpp/replaceoptions/#regexKey--)-Eigenschaft anhand der [Beispieldatei](101089318.xlsx). Die [Ausgabedatei](101089319.xlsx), die durch das folgende Codebeispiel generiert wurde, ist zur Referenz beigefügt.

## **Beispielcode**

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
