---
title: Aspose.Cells for Java - Unterbrechbare Bibliothek
type: docs
weight: 1090
url: /de/java/aspose-cells-for-java-interruptible-library/
---
{{% alert color="primary" %}}

 Aspose.Cells for Java unterstützt das Unterbrechen des Lade-/Speichervorgangs beim Arbeiten mit großen Excel-Dateien. Manchmal möchten Sie die Bibliotheken/Komponenten unterbrechbar machen. Dies würde sicherlich die Effizienz und Zuverlässigkeit Ihrer Dienstleistungen/Prozesse verbessern. Sie können eine Konvertierung zuverlässig aufgeben, wenn Sie feststellen, dass sie zu lange dauert. Das würde CPU-Auslastung, RAM usw. einsparen. Es bedeutet, dass Sie keine drastischen Schritte unternehmen müssen, wie z. B. den gesamten Server zu töten, nur um die Konvertierung abzubrechen.
{{% /alert %}}

## **Beispiel:**

 Das folgende Programm zeigt, wie Sie den Speichervorgang mit unterbrechen**InterruptMonitor.interrupt()** Methode.

[**Java**]{{< highlight "java" >}}

 //Eine neue Arbeitsmappe erstellen

endgültige Arbeitsmappe wb = neue Arbeitsmappe ();

// Holen Sie sich die Arbeitsblätter

WorksheetCollection wss = wb.getWorksheets();

// Führen Sie eine Schleife aus, um Blattzellen mit Daten zu füllen

 für (int i = 0; i< 50; i++) {

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
