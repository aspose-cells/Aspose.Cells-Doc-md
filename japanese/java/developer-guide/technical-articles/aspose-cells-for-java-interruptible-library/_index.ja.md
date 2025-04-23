---
title: Aspose.Cells for Java  中断可能ライブラリ
type: docs
weight: 1090
url: /ja/java/aspose-cells-for-java-interruptible-library/
---

{{% alert color="primary" %}}

Aspose.Cells for Javaは大きなExcelファイルを扱う際の読み込みや保存処理を中断するサポートを提供しています。時々、ライブラリやコンポーネントを中断可能にしたいことがあります。これにより、サービス/プロセスの効率と信頼性が向上します。時間がかかりすぎることがわかった場合、変換を中途で中断できます。これにより、CPU使用率やRAMの使用量を節約できます。つまり、変換をキャンセルするためにサーバ全体を停止するなどの緊急の措置を取る必要はありません。 
{{% /alert %}}

## **例:**

次のプログラムは、**InterruptMonitor.interrupt()**メソッドを使用して保存処理を中断する方法を示しています。

[**Java**]

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
{{< app/cells/assistant language="java" >}}
