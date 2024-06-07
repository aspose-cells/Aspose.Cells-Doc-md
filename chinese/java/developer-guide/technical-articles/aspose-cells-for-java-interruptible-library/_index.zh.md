---
title: Aspose.Cells for Java - 可中断的库
type: docs
weight: 1090
url: /zh/java/aspose-cells-for-java-interruptible-library/
---

{{% alert color="primary" %}}

Aspose.Cells for Java支持在处理大型Excel文件时中断加载/保存进程。有时，您希望使库/组件可中断。这肯定会改善服务/流程的效率和可靠性。当您发现转换过程太长时，可以可靠地放弃转换的一部分。这将节省CPU使用率、内存等。这意味着您不必采取像终止整个服务器一样的激进步骤来取消转换。 
{{% /alert %}}

## **示例：**

以下程序展示了如何使用**InterruptMonitor.interrupt()**方法中断保存过程。

【**Java**】

{{< highlight java >}}

 //Create a new Workbook  

final Workbook wb = new Workbook();

// Get the Worksheets

WorksheetCollection wss = wb.getWorksheets();

// Run a loop to fill sheet cells with data

for (int i = 0; i < 50; i++) {

    Worksheet sheet = wss.get(wss.add());

    Cells cells = sheet.getCells();

    for (int row = 0; row < 5000; row++) {

        for (int col = 0; col < 10; col++) {

            cells.get(row, col).setValue(i * 5000 + row * 500 + col);

        }

    }

}

final InterruptMonitor monitor = new InterruptMonitor();

wb.setInterruptMonitor(monitor);

new Thread(new Runnable() {

    public void run() {

        try {

            Thread.sleep(Math.round(Math.random() * 3000));

        } catch (InterruptedException e) {

        }

        // Interrupt the process

        monitor.interrupt();

        System.out.println("Interrupting the save thread at "

                + System.currentTimeMillis());

    }

}).start();

try {

    wb.save("makeinterrupted.xlsx", FileFormatType.XLSX);

} catch (CellsException e) {

    if (e.getCode() == ExceptionType.INTERRUPTED) {

        System.out.println(e.getMessage());

        System.out.println("The save thread finishes at "

                + System.currentTimeMillis());

    } else {

        throw e;

    }

}

{{< /highlight >}}
