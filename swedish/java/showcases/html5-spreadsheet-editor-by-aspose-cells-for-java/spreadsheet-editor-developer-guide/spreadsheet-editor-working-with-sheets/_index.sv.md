---
title: Kalkylbladsredigerare  Arbeta med blad
type: docs
weight: 20
url: /sv/java/spreadsheet-editor-working-with-sheets/
---

Innehållsförteckning

- [Lägga till och ta bort blad?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
  - WorksheetView.onAddNewSheet
  - WorksheetView.onRemoveActiveSheet
- [Byt namn på blad](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
  - WorksheetView.setActiveSheet
- [Växla mellan flikar](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
  - WorksheetView.setActiveSheet
### **Lägga till och ta bort blad?**
Microsoft Excel tillåter flera blad i en enda fil. HTML5-kalkylbladsredigeraren tillåter användaren att lägga till och ta bort blad. På fliken Blad har vi en rullgardinslista över blad. Det valda bladet är det som öppnas av redaktören.

För att lägga till ett nytt blad:

1. Byt till **Flikblad**.
1. Klicka på **+** (plus) knappen.

Ett nytt blad läggs till och redaktören kommer att växla till det.

För att ta bort det aktuellt valda bladet:

1. Byt till **Flikblad**.
1. Klicka på **-** (minus) knappen.

Det aktuellt valda bladet kommer att tas bort och redaktören kommer att växla till det senast valda bladet.

![todo:image_alt_text](4wgvmu8.png)

**Hur fungerar det?**

När användaren klickar på **+** (plus) och **-** (minus) knappen, hanterar JSF backend bean **WorksheetView** händelserna med metoderna **WorksheetView.onAddNewSheet** och **WorksheetView.onRemoveActiveSheet**.
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
### **Byt namn på blad**
För att döpa om ett blad:

1. Byt till **Flikblad**.
1. Klicka på fliknamnet i textrutan för att redigera det.
1. Ändra namnet på fliken.
1. När du är klar, tryck på ENTER-tangenten eller klicka utanför rutan.

Fliken kommer att döpas om.

![todo:image_alt_text](4wgvmu8.png)

**Hur fungerar det?**

När textrutans värde ändras, hanteras händelsen på servern av JSF backend-beanen **WorksheetView** med hjälp av metoden **WorksheetView.setActiveSheet**.
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
### **Växla mellan flikar**
För att växla till en annan flik:

1. Byt till **Flikblad**.
1. Välj en flik från rullgardinsmenyn.

Redigeraren kommer att växla till den valda fliken.

![todo:image_alt_text](4wgvmu8.png)

**Hur fungerar det?**

När rullgardinsväljarens värde ändras, hanteras händelsen på servern av JSF backend-beanen **WorksheetView** med hjälp av metoden **WorksheetView.setActiveSheet**.
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
