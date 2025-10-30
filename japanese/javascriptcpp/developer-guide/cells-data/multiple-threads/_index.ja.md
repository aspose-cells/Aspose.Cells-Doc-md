---
title: 複数のスレッドで同時にセル値を読み取る
linktitle: 複数のスレッド
type: docs
weight: 1800
url: /ja/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: C++を通じてAspose.Cells for JavaScriptを使い、複数のスレッドでセルの値を同時に読む方法を学びます。
keywords: JavaScriptを通じてC++で複数スレッドでセルの値を同時に読む方法、Aspose.Cells C++のマルチスレッド対応、複数スレッドでデータを読む
---

{{% alert color="primary" %}}

複数のスレッドで同時にセル値を読み取る必要がある場合がよくあります。この記事ではその目的で Aspose.Cells の使用方法を説明します。

{{% /alert %}}

複数のスレッドでセル値を同時に読み取るには、[**Cells.multiThreadReading(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#multiThreadReading-boolean-)を**true**に設定します。そうしないと、誤ったセル値を取得する可能性があります。

次のコード:

1. ワークブックを作成します。
1. ワークシートを追加します。
1. 文字列値でワークシートを埋めます。
1. 次に、ランダムなセルから同時に値を読み取る2つのスレッドを作成します。
   読み取った値が正しい場合、何も起こりません。読み取った値が間違っている場合は、メッセージが表示されます。

この行をコメントアウトすると、次のメッセージが表示されます:

{{< highlight javascript >}}

testWorkbook.worksheets.get(0).cells.multiThreadReading(true);

{{< /highlight >}}

それ以外の場合、すべてのセルから読み取った値が正しいことを意味するメッセージが表示されずにプログラムが実行されます。

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

それ以外の場合、セルから読み取ったすべての値が正しい場合、プログラムはメッセージを表示せずに実行されます。

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
