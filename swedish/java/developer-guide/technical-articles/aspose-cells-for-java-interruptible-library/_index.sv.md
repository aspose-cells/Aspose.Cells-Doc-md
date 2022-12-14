---
title: Aspose.Cells för Java - Avbrottsbart bibliotek
type: docs
weight: 1090
url: /sv/java/aspose-cells-for-java-interruptible-library/
---
{{% alert color="primary" %}}

 Aspose.Cells för Java stöder för att avbryta laddnings-/sparprocessen när du arbetar med stora Excel-filer. Ibland vill du göra biblioteken/komponenterna avbrottsbara. Detta skulle säkerligen förbättra effektiviteten och tillförlitligheten för dina tjänster/processer. Du kan på ett tillförlitligt sätt ge upp en konvertering halvvägs när du upptäcker att det tar för lång tid. Det skulle spara CPU-användning, RAM etc. Det betyder att du inte behöver ta drastiska steg som att döda hela servern bara för att avbryta konverteringen.
{{% /alert %}}

## **Exempel:**

 Följande program visar hur man avbryter sparprocessen med**InterruptMonitor.interrupt()** metod.

[**Java**]{{< highlight "java" >}}

 //Skapa en ny arbetsbok

final Workbook wb = new Workbook();

// Skaffa arbetsbladen

WorksheetCollection wss = wb.getWorksheets();

// Kör en slinga för att fylla arkceller med data

 för (int i = 0; i< 50; i++) {

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
