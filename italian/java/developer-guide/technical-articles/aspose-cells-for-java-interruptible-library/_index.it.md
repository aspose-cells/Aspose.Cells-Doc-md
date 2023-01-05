---
title: Aspose.Cells for Java - Biblioteca Interrompibile
type: docs
weight: 1090
url: /it/java/aspose-cells-for-java-interruptible-library/
---
{{% alert color="primary" %}}

 Aspose.Cells for Java supporta l'interruzione del processo di caricamento/salvataggio mentre si lavora con file Excel di grandi dimensioni. A volte, vuoi rendere le librerie/componenti interrompibili. Ciò migliorerebbe sicuramente l'efficienza e l'affidabilità dei tuoi servizi/processi. Puoi tranquillamente rinunciare a una conversione a metà strada quando scopri che sta impiegando troppo tempo. Ciò salverebbe l'utilizzo della CPU, della RAM, ecc. Significa che non devi prendere misure drastiche come uccidere l'intero server solo per annullare la conversione.
{{% /alert %}}

## **Esempio:**

 Il seguente programma mostra come interrompere il processo di salvataggio utilizzando**InterruptMonitor.interrupt()** metodo.

[**Java**]{{< highlight "java" >}}

 //Crea una nuova cartella di lavoro

cartella di lavoro finale wb = nuova cartella di lavoro();

// Ottieni i fogli di lavoro

WorksheetCollection wss = wb.getWorksheets();

// Esegue un ciclo per riempire le celle del foglio con i dati

 per (int i = 0; i< 50; i++) {

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
