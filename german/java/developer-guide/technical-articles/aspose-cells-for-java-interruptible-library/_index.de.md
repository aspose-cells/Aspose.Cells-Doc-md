---
title: Aspose.Cells for Java  Unterbrechbare Bibliothek
type: docs
weight: 1090
url: /de/java/aspose-cells-for-java-interruptible-library/
---

{{% alert color="primary" %}}

Aspose.Cells for Java unterstützt das Unterbrechen des Lade-/Speicherprozesses beim Arbeiten mit großen Excel-Dateien. Manchmal möchten Sie die Bibliotheken/Komponenten unterbrechbar machen. Dies würde sicherlich die Effizienz und Zuverlässigkeit Ihrer Dienste/Prozesse verbessern. Sie können zuverlässig einen Konvertierungsvorgang abbrechen, wenn Sie feststellen, dass er zu lange dauert. Das würde die CPU-Auslastung, den RAM usw. sparen. Es bedeutet, dass Sie nicht drastische Schritte wie das Beenden des gesamten Servers unternehmen müssen, nur um die Konvertierung abzubrechen. 
{{% /alert %}}

## **Beispiel:**

Das folgende Programm zeigt, wie man den Speicherprozess mithilfe der Methode **InterruptMonitor.interrupt()** unterbricht.

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
