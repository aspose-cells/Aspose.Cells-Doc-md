---
title: Aynı Anda Birden Fazla İş Parçacığından Hücre Değerlerini Okuma
linktitle: Çoklu İş Parçacıkları
type: docs
weight: 1800
url: /tr/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Çoklu iş parçacığında aynı anda hücre değerlerini okuma nasıl yapılır, Aspose.Cells for JavaScript kullanarak C++ API ile öğrenin.
keywords: Çoklu iş parçacığında hücre değerlerini okuma, JavaScript ile C++, Aspose.Cells C++ Çoklu İş Parçacığı, Çoklu İş Parçacığında Veri Okuma
---

{{% alert color="primary" %}}

Aynı Anda Birden Fazla İş Parçacığında hücre değerlerini okuma ihtiyacı yaygın bir gereksinimdir. Bu makale bu amaçla Aspose.Cells'in nasıl kullanılacağını açıklar.

{{% /alert %}}

Birden fazla iş parçacığında aynı anda hücre değerleri okumak için, [**Cells.multiThreadReading(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#multiThreadReading-boolean-) değerini **doğru** olarak ayarlayın. Aksi takdirde yanlış hücre değerleri alabilirsiniz.

Aşağıdaki kod:

1. Bir çalışma kitabı oluşturur.
1. Bir çalışma sayfası ekler.
1. Çalışma sayfasını dize değerleriyle doldurur.
1. Sonra rastgele hücrelerden aynı anda değer okuyan iki iş parçacığı oluşturur.
   Okunan değerler doğru ise hiçbir şey olmaz. Okunan değerler yanlışsa bir mesaj görüntülenir.

Eğer bu satırı yorumlarsanız:

{{< highlight javascript >}}

testWorkbook.worksheets.get(0).cells.multiThreadReading(true);

{{< /highlight >}}

o zaman aşağıdaki mesaj görüntülenir:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

Aksi takdirde, program herhangi bir mesaj göstermeden çalışır, bu da demek olur ki tüm hücrelerden okunan değerler doğrudur.

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
