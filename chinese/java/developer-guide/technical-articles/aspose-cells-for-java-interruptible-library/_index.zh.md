---
title: Aspose.Cells for Java - 可中断库
type: docs
weight: 1090
url: /zh/java/aspose-cells-for-java-interruptible-library/
---
{{% alert color="primary" %}}

Aspose.Cells for Java 支持在处理大型 Excel 文件时中断加载/保存过程。有时，您想使库/组件可中断。这肯定会提高您的服务/流程的效率和可靠性。当您发现转换花费的时间太长时，您可以可靠地中途放弃转换。这将节省 CPU 使用率、RAM 等。这意味着您不必为了取消转换而采取像杀死整个服务器这样的激烈步骤。
{{% /alert %}}

## **例子：**

以下程序显示了如何使用中断保存过程**中断监视器.interrupt()**方法。

[**Java**]{{< highlight "java" >}}

 //创建一个新的工作簿

最终工作簿 wb = new Workbook();

// 获取工作表

WorksheetCollection wss = wb.getWorksheets();

// 运行一个循环以用数据填充工作表单元格

对于 (int i = 0; i< 50; i++) {

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
