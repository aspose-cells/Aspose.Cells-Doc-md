---
title: Aspose.Cells for Java - 中断可能なライブラリ
type: docs
weight: 1090
url: /ja/java/aspose-cells-for-java-interruptible-library/
---
{{% alert color="primary" %}}

Aspose.Cells for Java は、大きな Excel ファイルの操作中にロード/保存プロセスを中断することをサポートします。ライブラリ /components を割り込み可能にしたい場合があります。これにより、サービス/プロセスの効率と信頼性が確実に向上します。変換に時間がかかりすぎることがわかった場合、変換を途中で確実にあきらめることができます。これにより、CPU 使用率、RAM などを節約できます。変換をキャンセルするためだけにサーバー全体を強制終了するなどの抜本的な手順を実行する必要がないことを意味します。
{{% /alert %}}

## **例：**

次のプログラムは、次のコマンドを使用して保存プロセスを中断する方法を示しています。**InterruptMonitor.interrupt()**方法。

[**Java**]{{< highlight "java" >}}

 //新しいワークブックを作成

最終ワークブック wb = 新しいワークブック();

// ワークシートを取得

WorksheetCollection wss = wb.getWorksheets();

// ループを実行してシート セルにデータを入力します

for (int i = 0; i< 50; i++) {

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
