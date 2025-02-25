---
title: Reading Cell Values in Multiple Threads Simultaneously with Node.js via C++
linktitle: Multiple Threads
type: docs
weight: 1800
url: /nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Learn how to read cell values in multiple threads simultaneously using Aspose.Cells for Node.js via C++.
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells Node.js via C++, Read data in Multiple Threads
---

{{% alert color="primary" %}}

Needing to read cell values in multiple threads simultaneously is a common requirement. This article explains how to use Aspose.Cells for this purpose.

{{% /alert %}}

To read cell values in more than one thread simultaneously, set [**Worksheet.Cells.multiThreadReading**](https://reference.aspose.com/cells/nodejs-cpp/cells/#multithreadreading) to **true**. If you do not, you might get the wrong cell values.

The following code:

1. Creates a workbook.
1. Adds a worksheet.
1. Populates the worksheet with string values.
1. It then creates two threads that simultaneously read values from random cells.
   If the values read are correct, nothing happens. If the values read are incorrect, then a message is displayed.

If you comment this line:

{{< highlight javascript >}}

 testWorkbook.worksheets[0].cells.multiThreadReading = true;

{{< /highlight >}}

then the following message is displayed:

{{< highlight javascript >}}

 if (s !== "R" + row + "C" + col) {

    console.log("This message will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Otherwise, the program runs without showing any message which means all values read from cells are correct.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// The workbook for testing
let testWorkbook;

function threadLoop() {
    const random = Math.random;
    while (true) {
        try {
            const row = Math.floor(random() * 10000);
            const col = Math.floor(random() * 100);
            const s = testWorkbook.getWorksheets().get(0).getCells().get(row, col).getStringValue();
            if (s !== `R${row}C${col}`) {
                console.log("This message will show up when cells read values are incorrect.");
            }
        } catch {}
    }
}

async function testMultiThreadingRead() {
    testWorkbook = new AsposeCells.Workbook();
    testWorkbook.getWorksheets().clear();
    testWorkbook.getWorksheets().add("Sheet1");

    for (let row = 0; row < 10000; row++) {
        for (let col = 0; col < 100; col++) {
            testWorkbook.getWorksheets().get(0).getCells().get(row, col).putValue(`R${row}C${col}`);
        }
    }

    // Commenting this line will show a pop-up message
    // testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

    const myThread1 = setInterval(threadLoop, 10);
    const myThread2 = setInterval(threadLoop, 10);

    await new Promise(res => setTimeout(res, 5000));
    clearInterval(myThread1);
    clearInterval(myThread2);
}
```
