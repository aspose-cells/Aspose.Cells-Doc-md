---
title: Hücreden HTML5 dizesi al
type: docs
weight: 90
url: /tr/javascript-cpp/get-html5-string-from-cell/
description: 12345678Script aracılığıyla C++ API üzerinden Hücre den HTML5 dizesi almayı öğrenin.
keywords: C++ ile Hücre den HTML5 dizesini alın, JavaScript ile Hücre den HTML5 dizesini alın, C++ ile Hücre JavaScript in HTML5 dizesini yönetin
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, boolean parametre kabul eden [**Cell.htmlString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#htmlString-boolean-) yöntemiyle hücrenin HTML dizgesini döndürür. Eğer **false** parametre olarak geçerseniz, Normal HTML döner, **true** geçerseniz HTML5 dizgisi döner.

## **Hücreden HTML5 dizesi al**

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur ve ilk çalışma sayfasındaki A1 hücresine bazı metinler ekler. Daha sonra A1 hücresinden Normal HTML ve HTML5 dizgilerini alır, ve bunları konsola yazdırır.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Get HTML String from Cell</h1>
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
            // This example creates a new workbook, writes text to A1 and retrieves HTML strings.
            const wb = new Workbook();

            const ws = wb.worksheets.get(0);

            const cell = ws.cells.get("A1");
            cell.value = "This is some text.";

            const strNormal = cell.htmlString;
            const strHtml5 = cell.htmlString;

            console.log("Normal:\r\n" + strNormal);
            console.log();
            console.log("Html5:\r\n" + strHtml5);

            document.getElementById('result').innerHTML =
                '<h2>Results</h2>' +
                '<p><strong>Normal:</strong></p><pre>' + escapeHtml(strNormal) + '</pre>' +
                '<p><strong>Html5:</strong></p><pre>' + escapeHtml(strHtml5) + '</pre>' +
                '<p style="color: green;">Operation completed successfully!</p>';
        });

        function escapeHtml(text) {
            if (text === null || text === undefined) return "";
            return String(text)
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
        }
    </script>
</html>
```


## **Konsol Çıktısı**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
