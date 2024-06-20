---
title: Aspose.Cells for Java  Libreria Interrompibile
type: docs
weight: 1090
url: /it/java/aspose-cells-for-java-interruptible-library/
---

{{% alert color="primary" %}}

Aspose.Cells for Java supporta l'interruzione del processo di caricamento/salvataggio durante il lavoro con file Excel di grandi dimensioni. A volte desideri rendere le librerie/componenti interrompibili. Ciò migliorerebbe sicuramente l'efficienza e l'affidabilità dei tuoi servizi/processi. Puoi rinunciare in modo affidabile a una conversione a metà strada quando scopri che sta richiedendo troppo tempo. Questo permetterebbe di risparmiare l'utilizzo della CPU, della RAM, ecc. Significa che non è necessario prendere misure drastiche come terminare l'intero server solo per annullare la conversione. 
{{% /alert %}}

## **Esempio:**

Il seguente programma mostra come interrompere il processo di salvataggio utilizzando il metodo **InterruptMonitor.interrupt()**.

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
