---
title: Aspose.Cells for Java  Kesintili Kütüphane
type: docs
weight: 1090
url: /tr/java/aspose-cells-for-java-interruptible-library/
---

{{% alert color="primary" %}}

Aspose.Cells for Java, büyük Excel dosyalarıyla çalışırken yükleme/kaydetme sürecini kesintiye uğratmayı destekler. Bazen, kütüphaneleri/bileşenleri kesintiye uğratmak istersiniz. Bu kesinlikle hizmetlerinizin/süreçlerinizin verimliliğini ve güvenilirliğini artıracaktır. Uzun sürdüğünü fark ettiğinizde dönüşümün bir noktasında güvenle vazgeçebilirsiniz. Bu, CPU kullanımını, RAM'i vb. kaydeder. Bu, dönüşümü iptal etmek için tüm sunucuyu öldürme gibi drastik adımlar atmamanız anlamına gelir. 
{{% /alert %}}

## **Örnek:**

Aşağıdaki program, **InterruptMonitor.interrupt()** yöntemini kullanarak kaydetme sürecini kesintiye uğratmayı nasıl gösterir.

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
