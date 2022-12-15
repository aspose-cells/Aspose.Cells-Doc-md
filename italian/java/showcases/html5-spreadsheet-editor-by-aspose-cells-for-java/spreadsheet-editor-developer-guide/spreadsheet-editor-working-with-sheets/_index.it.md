---
title: Editor di fogli di calcolo - Lavorare con i fogli
type: docs
weight: 20
url: /it/java/spreadsheet-editor-working-with-sheets/
---
**Sommario**

- [Aggiungere e rimuovere fogli?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
 - WorksheetView.onAddNewSheet
 - WorksheetView.onRemoveActiveSheet
- [Rinomina Fogli](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
 - WorksheetView.setActiveSheet
- [Passa da un foglio all'altro](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
 - WorksheetView.setActiveSheet
### **Aggiungere e rimuovere fogli?**
Microsoft Excel consente più fogli in un singolo file. HTML5 Spreadsheet Editor consente all'utente di aggiungere e rimuovere fogli. Nella scheda Fogli abbiamo un elenco a discesa di fogli. Il foglio selezionato è quello che viene aperto dall'editor.

Per aggiungere un nuovo foglio:

1.  Passa a**Scheda Fogli**.
1. Fai clic sul pulsante **+** (più).

Verrà aggiunto un nuovo foglio e l'editor passerà ad esso.

Per rimuovere il foglio attualmente selezionato:

1.  Passa a**Scheda Fogli**.
1. Fare clic sul pulsante **-** (meno).

Il foglio attualmente selezionato verrà rimosso e l'editor passerà all'ultimo selezionato.

![cose da fare:immagine_alt_testo](4wgvmu8.png)

**Come funziona?**

 Quando l'utente fa clic su** +** (più) e**-** (meno) vengono cliccati, il bean backend JSF**Foglio di lavoroVisualizza** gestisce gli eventi utilizzando**WorksheetView.onAddNewSheet** e**Metodi WorksheetView.onRemoveActiveSheet**.
#### **WorksheetView.onAddNewSheet**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
### **Rinomina Fogli**
Per rinominare un foglio:

1.  Passa a**Scheda Fogli**.
1. Fare clic sul nome del foglio nella casella di testo per modificarlo.
1. Cambia il nome del foglio.
1. Al termine, premere il tasto INVIO o fare clic in un punto qualsiasi all'esterno della casella.

Il foglio verrà rinominato.

![cose da fare:immagine_alt_testo](4wgvmu8.png)

**Come funziona?**

 Quando il valore della casella di testo viene modificato, l'evento viene gestito sul server dal bean backend JSF**Foglio di lavoroVisualizza** utilizzando il metodo**WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight "java" >}}

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
### **Passa da un foglio all'altro**
Per passare a un altro foglio:

1.  Passa a**Scheda Fogli**.
1. Seleziona un foglio dal menu a discesa.

L'editor passerà al foglio selezionato.

![cose da fare:immagine_alt_testo](4wgvmu8.png)

**Come funziona?**

 Quando il valore del selettore a discesa viene modificato, l'evento viene gestito sul server dal bean backend JSF**Foglio di lavoroVisualizza** utilizzando il metodo**WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight "java" >}}

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
