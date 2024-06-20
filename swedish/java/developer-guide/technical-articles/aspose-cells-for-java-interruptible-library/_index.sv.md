---
title: Aspose.Cells for Java  Avbrytbar bibliotek
type: docs
weight: 1090
url: /sv/java/aspose-cells-for-java-interruptible-library/
---

{{% alert color="primary" %}}

Aspose.Cells for Java stöder avbrytning av laddnings/sparningsprocessen vid arbete med stora Excelfiler. Ibland vill du göra biblioteken/komponenterna avbrytbara. Detta skulle säkerligen förbättra effektiviteten och tillförlitligheten av dina tjänster/processer. Du kan pålitligt avbryta en konvertering mitt i processen när du upptäcker att det tar för lång tid. Det skulle spara CPU-användning, RAM osv. Det betyder att du inte behöver ta drastiska åtgärder som att döda hela servern bara för att avbryta konverteringen. 
{{% /alert %}}

## **Exempel:**

Följande program visar hur du avbryter sparprocessen med hjälp av **InterruptMonitor.interrupt()**-metoden.

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
