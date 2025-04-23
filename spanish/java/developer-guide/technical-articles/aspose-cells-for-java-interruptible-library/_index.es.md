---
title: Aspose.Cells for Java  Biblioteca Intercambiable
type: docs
weight: 1090
url: /es/java/aspose-cells-for-java-interruptible-library/
---

{{% alert color="primary" %}}

Aspose.Cells for Java admite interrumpir el proceso de carga/guardado mientras se trabaja con archivos de Excel grandes. A veces, quieres hacer que las bibliotecas/componentes sean interrumpibles. Esto seguramente mejoraría la eficiencia y confiabilidad de tus servicios/procesos. Puedes renunciar de forma fiable a una conversión a mitad de camino cuando descubras que está llevando demasiado tiempo. Eso ahorraría el uso de CPU, RAM, etc. Significa que no tienes que tomar medidas drásticas como matar a todo el servidor solo para cancelar la conversión. 
{{% /alert %}}

## **Ejemplo:**

El siguiente programa muestra cómo interrumpir el proceso de guardado utilizando el método **InterruptMonitor.interrupt()**.

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
{{< app/cells/assistant language="java" >}}
