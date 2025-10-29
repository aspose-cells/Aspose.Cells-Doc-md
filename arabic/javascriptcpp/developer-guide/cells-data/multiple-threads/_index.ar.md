---
title: قراءة قيم الخلية في خيوط متعددة بشكل متزامن
linktitle: الخيوط المتعددة
type: docs
weight: 1800
url: /ar/javascript-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: تعلم كيفية قراءة قيم الخلايا في عدة خيوط في آن واحد عبر Aspose.Cells for JavaScript باستخدام C++ API.
keywords: قراءة قيم الخلايا في عدة خيوط في وقت واحد JavaScript عبر C++، Aspose.Cells C++ متعددة الخيوط، قراءة البيانات في عدة خيوط
---

{{% alert color="primary" %}}

من الضروري قراءة قيم الخلية في خيوط متعددة بشكل متزامن ، وهو متطلب شائع. يشرح هذا المقال كيفية استخدام Aspose.Cells لهذا الغرض.

{{% /alert %}}

لقياس قيم الخلايا في أكثر من خيط واحد في نفس الوقت، اضبط [**Cells.multiThreadReading(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#multiThreadReading-boolean-) على **true**. إذا لم تفعل ذلك، قد تحصل على قيم خلايا غير صحيحة.

الكود التالي:

1. ينشئ دفتر عمل.
1. إضافة ورقة عمل.
1. ملء ورقة العمل بقيم السلسلة.
1. ثم ينشئ خيطين يقرأان قيمًا بشكل متزامن من الخلايا العشوائية.
   إذا كانت القيم المقروءة صحيحة، لا يحدث شيء. إذا كانت القيم المقروءة غير صحيحة، يتم عرض رسالة.

إذا قمت بتعليق هذا السطر:

{{< highlight javascript >}}

testWorkbook.worksheets.get(0).cells.multiThreadReading(true);

{{< /highlight >}}

سيتم عرض الرسالة التالية:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

وإلا، يعمل البرنامج بدون عرض أي رسالة مما يعني أن جميع القيم المقروءة من الخلايا صحيحة.

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
