---
title: Lettura di valori di celle in thread multipli contemporaneamente
linktitle: Thread multipli
type: docs
weight: 1800
url: /it/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Impara come leggere i valori delle celle in più thread contemporaneamente tramite lo Script Aspose.Cells for Java tramite API C++.
keywords: Leggere i valori delle celle in più thread contemporaneamente JavaScript tramite C++, Aspose.Cells C++ multi thread, leggere i dati in più thread
---

{{% alert color="primary" %}}

La necessità di leggere i valori delle celle in thread multipli contemporaneamente è una richiesta comune. Questo articolo spiega come utilizzare Aspose.Cells per questo scopo.

{{% /alert %}}

Per leggere i valori delle celle in più di un thread contemporaneamente, imposta [**Cells.multiThreadReading(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#multiThreadReading-boolean-) su **true**. Se non lo fai, potresti ottenere valori di cella sbagliati.

Il seguente codice:

1. Crea un workbook.
1. Aggiunge un foglio di lavoro.
1. Popola il foglio di lavoro con valori di stringa.
1. Quindi crea due thread che leggono contemporaneamente valori da celle casuali.
   Se i valori letti sono corretti, non succede nulla. Se i valori letti non sono corretti, viene visualizzato un messaggio.

Se si commenta questa riga:

{{< highlight javascript >}}

testWorkbook.worksheets.get(0).cells.multiThreadReading(true);

{{< /highlight >}}

allora viene visualizzato il seguente messaggio:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

In caso contrario, il programma viene eseguito senza mostrare alcun messaggio, il che significa che tutti i valori letti dalle celle sono corretti.

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
