---
title: Reading Cell Values in Multiple Threads Simultaneously
linktitle: Multiple Threads
type: docs
weight: 1800
url: /javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Learn how to read cell values in multiple threads simultaneously through the Aspose.Cells for JavaScript via C++ API.
keywords: Read Cell Values in Multiple Threads Simultaneously JavaScript via C++, Aspose.Cells C++ Multiple Threads, Read data in Multiple Threads
---

{{% alert color="primary" %}}

Needing to read cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.

{{% /alert %}}

To read cell values in more than one thread simultaneously, set [**Cells.multiThreadReading(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#multiThreadReading-boolean-) to **true**. If you do not set it, you might get incorrect cell values.

The following code:

1. Creates a workbook.
2. Adds a worksheet.
3. Populates the worksheet with string values.
4. It then creates two threads that simultaneously read values from random cells. If the values read are correct, nothing happens. If the values read are incorrect, a message is displayed.

If you comment this line:

{{< highlight javascript >}}

testWorkbook.worksheets.get(0).cells.multiThreadReading(true);

{{< /highlight >}}

then the following message is displayed:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cell values are incorrect.");
}

{{< /highlight >}}

Otherwise, the program runs without showing any message, which means all values read from cells are correct.

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
                    console.log("This message will show up when cell values are incorrect.");
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

            // Uncommenting this line will enable multithreaded reading    
            //testWorkbook.worksheets.get(0).cells.setMultiThreadReading(true);

            const myThread1 = setInterval(threadLoop, 0);
            const myThread2 = setInterval(threadLoop, 0);

            setTimeout(() => {
                clearInterval(myThread1);
                clearInterval(myThread2);
                document.getElementById('result').innerHTML = '<p style="color: green;">Multithreaded read test completed.</p>';
            }, 5 * 1000);
        };

        document.getElementById('runExample').addEventListener('click', async () => {
            await readyPromise;
            document.getElementById('result').innerHTML = '<p style="color: green;">Starting multithreaded read test. This will run for 5 seconds.</p>';
            testMultiThreadingRead();
        });
    </script>
</html>
```