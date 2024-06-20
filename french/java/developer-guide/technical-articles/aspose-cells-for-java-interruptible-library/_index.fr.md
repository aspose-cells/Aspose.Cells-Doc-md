---
title: Aspose.Cells for Java  Bibliothèque Interruption
type: docs
weight: 1090
url: /fr/java/aspose-cells-for-java-interruptible-library/
---

{{% alert color="primary" %}}

Aspose.Cells for Java prend en charge l'interruption du processus de chargement/sauvegarde lors de la manipulation de gros fichiers Excel. Parfois, vous voulez rendre les bibliothèques/composants interruptibles. Cela améliorerait sûrement l'efficacité et la fiabilité de vos services/processus. Vous pouvez abandonner de manière fiable une conversion en cours lorsque vous découvrez qu'elle prend trop de temps. Cela économiserait l'utilisation du processeur, de la RAM, etc. Cela signifie que vous n'avez pas à prendre des mesures drastiques comme tuer tout le serveur juste pour annuler la conversion. 
{{% /alert %}}

## **Exemple :**

Le programme suivant montre comment interrompre le processus de sauvegarde en utilisant la méthode **InterruptMonitor.interrupt()**.

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
