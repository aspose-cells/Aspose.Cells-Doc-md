---
title: Aspose.Cells for Java - Biblioteca interrumpible
type: docs
weight: 1090
url: /es/java/aspose-cells-for-java-interruptible-library/
---
{{% alert color="primary" %}}

 Aspose.Cells for Java admite la interrupción del proceso de carga/guardado mientras se trabaja con archivos grandes de Excel. A veces, desea hacer que las bibliotecas/componentes sean interrumpibles. Esto seguramente mejoraría la eficiencia y confiabilidad de sus servicios/procesos. Puede renunciar de manera confiable a una conversión a mitad de camino cuando descubre que está tomando demasiado tiempo. Eso ahorraría el uso de CPU, RAM, etc. Significa que no tiene que tomar medidas drásticas como eliminar todo el servidor solo para cancelar la conversión.
{{% /alert %}}

## **Ejemplo:**

 El siguiente programa muestra cómo interrumpir el proceso de guardado usando**InterrumpirMonitor.interrupt()** método.

[**Java**]{{< highlight "java" >}}

 //Crear un nuevo libro de trabajo

libro de trabajo final wb = nuevo libro de trabajo ();

// Obtener las hojas de trabajo

WorksheetCollection wss = wb.getWorksheets();

// Ejecutar un ciclo para llenar las celdas de la hoja con datos

 para (int i = 0; i< 50; i++) {

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
