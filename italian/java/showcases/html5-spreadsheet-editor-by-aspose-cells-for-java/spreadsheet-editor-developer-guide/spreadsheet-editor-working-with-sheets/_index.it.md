---
title: Editor del foglio elettronico  Lavorare con i fogli
type: docs
weight: 20
url: /it/java/spreadsheet-editor-working-with-sheets/
---

**Tabella dei contenuti**

- [Aggiungere e Rimuovere schede?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
  - WorksheetView.onAddNewSheet
  - WorksheetView.onRemoveActiveSheet
- [Rinominare schede](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
  - WorksheetView.setActiveSheet
- [Passa tra i fogli](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
  - WorksheetView.setActiveSheet
### **Aggiungere e Rimuovere schede?**
Microsoft Excel consente più schede in un unico file. L'editor di fogli HTML5 consente all'utente di aggiungere e rimuovere schede. Sulla scheda Schede abbiamo un elenco a discesa delle schede. La scheda selezionata è quella aperta dall'editore.

Per aggiungere una nuova scheda:

1. Passa a **schede foglio**.
1. Fare clic sul pulsante **+** (più).

Verrà aggiunta una nuova scheda e l'editore passerà ad essa.

Per rimuovere la scheda attualmente selezionata:

1. Passa a **schede foglio**.
1. Fare clic sul pulsante **-** (meno).

La scheda attualmente selezionata verrà rimossa e l'editore passerà a quella selezionata per ultima.

![todo:image_alt_text](4wgvmu8.png)

**Come funziona?**

Quando l'utente fa clic su **+** (più) e **-** (meno), il bean backend JSF **WorksheetView** gestisce gli eventi utilizzando i metodi **WorksheetView.onAddNewSheet** e **WorksheetView.onRemoveActiveSheet**.
#### **WorksheetView.onAddNewSheet**
{{< highlight java >}}

     public void onAddNewSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().add();

                getAsposeWorksheets().setActiveSheetIndex(i);

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("New Worksheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}

#### **WorksheetView.onRemoveActiveSheet**
{{< highlight java >}}

     public void onRemoveActiveSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().getActiveSheetIndex();

                getAsposeWorksheets().removeAt(i);

                if (getAsposeWorksheets().getCount() == 0) {

                    int j = getAsposeWorksheets().add();

                    getAsposeWorksheets().setActiveSheetIndex(j);

                }

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("Could not remove sheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}
### **Rinominare schede**
Per rinominare una scheda:

1. Passa a **schede foglio**.
1. Fare clic sul nome della scheda nella casella di testo per modificarlo.
1. Cambia il nome del foglio.
1. Quando hai finito, premi il tasto INVIO, oppure fai clic altrove fuori dalla casella.

Il foglio verrà rinominato.

![todo:image_alt_text](4wgvmu8.png)

**Come funziona?**

Quando il valore della casella di testo viene modificato, l'evento è gestito sul server dal bean del backend JSF **WorksheetView** utilizzando il metodo **WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight java >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
### **Passa tra i fogli**
Per passare a un altro foglio:

1. Passa a **schede foglio**.
1. Seleziona un foglio dal menu a discesa.

L'editor passerà al foglio selezionato.

![todo:image_alt_text](4wgvmu8.png)

**Come funziona?**

Quando il valore del selettore a discesa viene modificato, l'evento è gestito sul server dal bean del backend JSF **WorksheetView** utilizzando il metodo **WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight java >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
