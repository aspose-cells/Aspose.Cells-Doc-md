---
title: Чтение значений ячеек в нескольких потоках одновременно
linktitle: Несколько потоков
type: docs
weight: 1800
url: /ru/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Узнайте, как читать значения ячеек одновременно в нескольких потоках через скрипт Aspose.Cells for Java на C++ API.
keywords: Читать значения ячеек одновременно в нескольких потоках на JavaScript через C++, Aspose.Cells C++ множественные потоки, чтение данных в нескольких потоках
---

{{% alert color="primary" %}}

Необходимость чтения значений ячеек в нескольких потоках одновременно - это распространенная потребность. В этой статье объясняется, как использовать Aspose.Cells для этой цели.

{{% /alert %}}

Для чтения значений ячеек в нескольких потоках одновременно установите [**Cells.multiThreadReading(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#multiThreadReading-boolean-) в **true**. Иначе вы можете получить неправильные значения ячеек.

Следующий код:

1. Создает рабочую книгу.
1. Добавляет лист.
1. Заполняет лист строковыми значениями.
1. Затем создает два потока, которые одновременно читают значения из случайных ячеек.
   Если прочитанные значения правильные, ничего не происходит. Если прочитанные значения неправильные, то отображается сообщение.

Если вы закомментируете эту строку:

{{< highlight javascript >}}

testWorkbook.worksheets.get(0).cells.multiThreadReading(true);

{{< /highlight >}}

тогда отображается следующее сообщение:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

В противном случае программа работает без отображения любого сообщения, что означает, что все значения, считываемые из ячеек, являются правильными.

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
