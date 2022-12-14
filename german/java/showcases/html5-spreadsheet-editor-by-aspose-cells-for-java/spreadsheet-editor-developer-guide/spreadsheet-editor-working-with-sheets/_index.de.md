---
title: Tabelleneditor - Arbeiten mit Tabellen
type: docs
weight: 20
url: /de/java/spreadsheet-editor-working-with-sheets/
---
**Inhaltsverzeichnis**

- [Blätter hinzufügen und entfernen?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
 - WorksheetView.onAddNewSheet
 - WorksheetView.onRemoveActiveSheet
- [Blätter umbenennen](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
 - WorksheetView.setActiveSheet
- [Wechseln Sie zwischen Blättern](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
 - WorksheetView.setActiveSheet
### **Blätter hinzufügen und entfernen?**
Microsoft Excel erlaubt mehrere Blätter in einer einzigen Datei. Mit dem HTML5-Tabellen-Editor kann der Benutzer Blätter hinzufügen und entfernen. Auf der Registerkarte Blätter haben wir eine Dropdown-Liste mit Blättern. Das ausgewählte Blatt ist dasjenige, das vom Editor geöffnet wird.

So fügen Sie ein neues Blatt hinzu:

1.  Wechseln zu**Registerkarte "Blätter".**.
1. Klicken Sie auf die Schaltfläche **+** (Plus).

Ein neues Blatt wird hinzugefügt und der Editor wechselt zu diesem.

So entfernen Sie das aktuell ausgewählte Blatt:

1.  Wechseln zu**Registerkarte "Blätter".**.
1. Klicken Sie auf die Schaltfläche **-** (Minus).

Das aktuell ausgewählte Blatt wird entfernt und der Editor wechselt zum zuletzt ausgewählten Blatt.

![todo: Bild_alt_Text](4wgvmu8.png)

**Wie es funktioniert?**

 Wenn der Benutzer auf klickt** +** (plus) und**-** (Minus)-Schaltfläche angeklickt werden, die JSF-Backend-Bean**Arbeitsblattansicht** behandelt die Ereignisse mit**WorksheetView.onAddNewSheet** und**WorksheetView.onRemoveActiveSheet**-Methoden.
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
### **Blätter umbenennen**
So benennen Sie ein Blatt um:

1.  Wechseln zu**Registerkarte "Blätter".**.
1. Klicken Sie auf den Blattnamen im Textfeld, um es zu bearbeiten.
1. Ändern Sie den Namen des Blatts.
1. Wenn Sie fertig sind, drücken Sie die EINGABETASTE oder klicken Sie irgendwo außerhalb des Felds.

Das Blatt wird umbenannt.

![todo: Bild_alt_Text](4wgvmu8.png)

**Wie es funktioniert?**

 Wenn der Textfeldwert geändert wird, wird das Ereignis auf dem Server von der JSF-Backend-Bean verarbeitet**Arbeitsblattansicht** Methode verwenden**WorksheetView.setActiveSheet**.
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
### **Wechseln Sie zwischen Blättern**
So wechseln Sie zu einem anderen Blatt:

1.  Wechseln zu**Registerkarte "Blätter".**.
1. Wählen Sie ein Blatt aus dem Dropdown-Menü aus.

Der Editor wechselt zum ausgewählten Blatt.

![todo: Bild_alt_Text](4wgvmu8.png)

**Wie es funktioniert?**

 Wenn der Wert des Dropdown-Selektors geändert wird, wird das Ereignis auf dem Server von der JSF-Back-End-Bean verarbeitet**Arbeitsblattansicht** Methode verwenden**WorksheetView.setActiveSheet**.
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
