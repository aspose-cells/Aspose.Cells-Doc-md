---
title: Aspose.Cells for Java - Kesilebilir Kitaplık
type: docs
weight: 1090
url: /tr/java/aspose-cells-for-java-interruptible-library/
---
{{% alert color="primary" %}}

 Aspose.Cells for Java, büyük Excel dosyalarıyla çalışırken yükleme/kaydetme işleminin kesilmesini destekler. Bazen kitaplıkları/bileşenleri kesintiye uğratılabilir yapmak istersiniz. Bu kesinlikle hizmetlerinizin/süreçlerinizin verimliliğini ve güvenilirliğini artıracaktır. Çok uzun sürdüğünü fark ettiğinizde, bir dönüşümden kısmen vazgeçebilirsiniz. Bu, CPU kullanımından, RAM'den vs.
{{% /alert %}}

## **Örnek:**

 Aşağıdaki program, kullanarak kaydetme işleminin nasıl kesileceğini gösterir.**InterruptMonitor.interrupt()** yöntem.

[**Java**]{{< highlight "java" >}}

 //Yeni bir Çalışma Kitabı oluştur

son Çalışma Kitabı wb = yeni Çalışma Kitabı();

// Çalışma Sayfalarını Alın

WorksheetCollection wss = wb.getWorksheets();

// Sayfa hücrelerini verilerle doldurmak için bir döngü çalıştırın

 için (int ben = 0; ben< 50; i++) {

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
