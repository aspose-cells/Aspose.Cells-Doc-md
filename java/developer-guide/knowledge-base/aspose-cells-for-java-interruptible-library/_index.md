---
title: Aspose.Cells for Java - Interruptible Library
type: docs
weight: 20
url: /java/aspose-cells-for-java-interruptible-library/
---

{{% alert color="primary" %}} 

Aspose.Cells for Java supports to interrupt loading/saving process while working with large Excel files. Sometimes, you want to to make the libraries /components interruptible. This would surely improve the efficiency and reliability of your services/processes. You can reliably give up on a conversion part way through when you discover it is taking too long. That would save the CPU usage, RAM etc. It means you don't have to take drastic steps like killing the whole server just to cancel the conversion. 

{{% /alert %}} 
##### **Example:**
The following program shows how to interrupt the save process using **InterruptMonitor.interrupt()** method. 

[**Java**](/pages/createpage.action?spaceKey=cellsjava&title=Java&linkCreation=true&fromPageId=5276486)

{{< highlight csharp >}}

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
