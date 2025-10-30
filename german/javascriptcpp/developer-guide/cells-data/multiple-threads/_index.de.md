---
title: Lesen von Zellwerten in mehreren Threads gleichzeitig.
linktitle: Mehrere Threads.
type: docs
weight: 1800
url: /de/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Lernen Sie, wie man Zellwerte in mehreren Threads gleichzeitig liest, mithilfe des Aspose.Cells for JavaScript via C++ API.
keywords: Zellwerte gleichzeitig in mehreren Threads lesen JavaScript via C++, Aspose.Cells C++ Mehrere Threads, Lesen von Daten in mehreren Threads
---

{{% alert color="primary" %}}

Es ist häufig erforderlich, Zellwerte gleichzeitig in mehreren Threads zu lesen. Dieser Artikel erläutert, wie Sie Aspose.Cells zu diesem Zweck verwenden.

{{% /alert %}}

 Um Zellwerte in mehreren Threads gleichzeitig zu lesen, setzen Sie [**Cells.multiThreadReading(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#multiThreadReading-boolean-) auf **true**. Andernfalls könnten Sie falsche Zellwerte erhalten.

Der folgende Code:

1. Erstellt ein Arbeitsblatt.
1. Fügt ein Arbeitsblatt hinzu.
1. Befüllt das Arbeitsblatt mit Zeichenfolgen.
1. Es erstellt dann zwei Threads, die gleichzeitig Werte aus zufälligen Zellen lesen.
   Wenn die gelesenen Werte korrekt sind, passiert nichts. Wenn die gelesenen Werte inkorrekt sind, wird eine Meldung angezeigt.

Wenn Sie diese Zeile kommentieren:

{{< highlight javascript >}}

testWorkbook.worksheets.get(0).cells.multiThreadReading(true);

{{< /highlight >}}

dann wird die folgende Nachricht angezeigt:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

Ansonsten läuft das Programm ohne Anzeige einer Meldung, was bedeutet, dass alle Werte, die aus den Zellen gelesen wurden, korrekt sind.

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
