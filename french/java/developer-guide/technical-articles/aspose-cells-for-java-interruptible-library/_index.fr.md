---
title: Aspose.Cells for Java - Bibliothèque interruptible
type: docs
weight: 1090
url: /fr/java/aspose-cells-for-java-interruptible-library/
---
{{% alert color="primary" %}}

 Aspose.Cells for Java prend en charge l'interruption du processus de chargement/enregistrement tout en travaillant avec de gros fichiers Excel. Parfois, vous souhaitez rendre les bibliothèques/composants interruptibles. Cela améliorerait sûrement l'efficacité et la fiabilité de vos services/processus. Vous pouvez abandonner de manière fiable une conversion en cours de route lorsque vous découvrez que cela prend trop de temps. Cela permettrait d'économiser l'utilisation du processeur, de la RAM, etc. Cela signifie que vous n'avez pas à prendre des mesures drastiques comme tuer tout le serveur juste pour annuler la conversion.
{{% /alert %}}

## **Exemple:**

 Le programme suivant montre comment interrompre le processus de sauvegarde en utilisant**InterruptMonitor.interrupt()** méthode.

[**Java**]{{< highlight "java" >}}

 //Créer un nouveau classeur

classeur final wb = nouveau classeur();

// Récupérer les feuilles de travail

WorksheetCollection wss = wb.getWorksheets();

// Exécuter une boucle pour remplir les cellules de la feuille avec des données

 pour (int je = 0; je< 50; i++) {

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
