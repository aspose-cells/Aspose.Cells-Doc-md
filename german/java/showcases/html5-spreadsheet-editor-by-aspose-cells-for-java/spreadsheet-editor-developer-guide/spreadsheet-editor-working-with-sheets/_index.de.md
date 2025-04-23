---
title: Tabellenkalkulation  Arbeiten mit Tabellen
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
- [Zwischen Blättern wechseln](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
  - WorksheetView.setActiveSheet
### **Blätter hinzufügen und entfernen?**
Microsoft Excel ermöglicht mehrere Blätter in einer einzelnen Datei. Der HTML5 Spreadsheet Editor ermöglicht es dem Benutzer, Blätter hinzuzufügen und zu entfernen. Auf dem Registerblatt 'Blätter' haben wir eine Dropdown-Liste von Blättern. Das ausgewählte Blatt ist dasjenige, das vom Editor geöffnet wird.

Um ein neues Blatt hinzuzufügen:

1. Wechseln Sie zum **Blätter-Tab**.
1. Klicken Sie auf die Schaltfläche **+** (Plus).

Ein neues Blatt wird hinzugefügt und der Editor wechselt zu diesem.

Um das aktuell ausgewählte Blatt zu entfernen:

1. Wechseln Sie zum **Blätter-Tab**.
1. Klicken Sie auf die Schaltfläche **-** (Minus).

Das aktuell ausgewählte Blatt wird entfernt und der Editor wechselt zum zuletzt ausgewählten.

![todo:image_alt_text](4wgvmu8.png)

**Wie funktioniert es?**

Wenn der Benutzer auf die Schaltfläche **+** (Plus) und **-** (Minus) klickt, behandelt das JSF-Backend-Bean **WorksheetView** die Ereignisse mithilfe der Methoden **WorksheetView.onAddNewSheet** und **WorksheetView.onRemoveActiveSheet**.
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
### **Blätter umbenennen**
Um ein Blatt umzubenennen:

1. Wechseln Sie zum **Blätter-Tab**.
1. Klicken Sie auf den Blattnamen im Textfeld, um ihn zu bearbeiten.
1. Ändern Sie den Namen des Blattes.
1. Drücken Sie die EINGABETASTE, oder klicken Sie außerhalb des Feldes, wenn Sie fertig sind.

Das Blatt wird umbenannt.

![todo:image_alt_text](4wgvmu8.png)

**Wie funktioniert es?**

Wenn der Textfeldwert geändert wird, wird das Ereignis auf dem Server von JSF-Backend-Bean **WorksheetView** mit der Methode **WorksheetView.setActiveSheet** verarbeitet.
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
### **Zwischen Blättern wechseln**
Um zu einem anderen Blatt zu wechseln:

1. Wechseln Sie zum **Blätter-Tab**.
1. Wählen Sie ein Blatt aus dem Dropdown-Menü aus.

Der Editor wechselt zu dem ausgewählten Blatt.

![todo:image_alt_text](4wgvmu8.png)

**Wie funktioniert es?**

Wenn der Wert des Dropdown-Selectors geändert wird, wird das Ereignis auf dem Server von JSF-Backend-Bean **WorksheetView** mit der Methode **WorksheetView.setActiveSheet** verarbeitet.
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
{{< app/cells/assistant language="java" >}}
