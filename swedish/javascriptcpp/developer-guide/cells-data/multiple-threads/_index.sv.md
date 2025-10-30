---
title: Läs cellvärden i flera trådar samtidigt
linktitle: Flera trådar
type: docs
weight: 1800
url: /sv/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Lär dig hur man läser cellvärden i flera trådar samtidigt med Aspose.Cells for JavaScript via C++ API.
keywords: Läs cellvärden i flera trådar samtidigt JavaScript via C++, Aspose.Cells C++ Flera trådar, Läs data i flera trådar
---

{{% alert color="primary" %}}

Att behöva läsa cellvärden i flera trådar samtidigt är ett vanligt krav. Den här artikeln förklarar hur man använder Aspose.Cells för detta ändamål.

{{% /alert %}}

För att läsa cellvärden i mer än en tråd samtidigt, sätt [**Cells.multiThreadReading(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#multiThreadReading-boolean-) till **true**. Om du inte gör det kan du få felaktiga cellvärden.

Följande kod:

1. Skapar en arbetsbok.
1. Lägger till en arbetsblad.
1. Fyller arbetsbladet med strängvärden.
1. Skapar sedan två trådar som samtidigt läser värden från slumpmässiga celler.
   Om de lästa värdena är korrekta händer ingenting. Om de lästa värdena är inkorrekta visas ett meddelande.

Om du kommenterar denna rad:

{{< highlight javascript >}}

testWorkbook.worksheets.get(0).cells.multiThreadReading(true);

{{< /highlight >}}

visas sedan följande meddelande:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

I annat fall körs programmet utan att visa något meddelande, vilket betyder att alla värden som läses från cellerna är korrekta.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Multi-Threading Read Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        let testWorkbook;

        const threadLoop = () => {
            const random = Math.random;
            while (true) {
                const row = Math.floor(random() * 10000);
                const col = Math.floor(random() * 100);
                const s = testWorkbook.worksheets.get(0).cells.get(row, col).stringValue;
                if (s !== "R" + row + "C" + col) {
                    console.log("This message will show up when cells read values are incorrect.");
                }
            }
        };

        const testMultiThreadingRead = () => {
            testWorkbook = new Workbook();
            testWorkbook.worksheets.clear();
            testWorkbook.worksheets.add("Sheet1");

            for (let row = 0; row < 10000; row++) {
                for (let col = 0; col < 100; col++) {
                    testWorkbook.worksheets.get(0).cells.get(row, col).value = "R" + row + "C" + col;
                }
            }

            // Uncommenting this line will enable multi-threaded reading    
            //testWorkbook.worksheets.get(0).cells.setMultiThreadReading(true);

            const myThread1 = setInterval(threadLoop, 0);
            const myThread2 = setInterval(threadLoop, 0);

            setTimeout(() => {
                clearInterval(myThread1);
                clearInterval(myThread2);
                document.getElementById('result').innerHTML = '<p style="color: green;">Multi-threading read test completed.</p>';
            }, 5 * 1000);
        };

        document.getElementById('runExample').addEventListener('click', async () => {
            await readyPromise;
            document.getElementById('result').innerHTML = '<p style="color: green;">Starting multi-threading read test. This will run for 5 seconds.</p>';
            testMultiThreadingRead();
        });
    </script>
</html>
```
