---
title: Kalkylarksredigerare - Arbeta med Kalkylark
type: docs
weight: 20
url: /sv/java/spreadsheet-editor-working-with-sheets/
---
**Innehållsförteckning**

- [Lägg till och ta bort ark?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
 - WorksheetView.onAddNewSheet
 - WorksheetView.onRemoveActiveSheet
- [Byt namn på ark](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
 - WorksheetView.setActiveSheet
- [Växla mellan ark](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
 - WorksheetView.setActiveSheet
### **Lägg till och ta bort ark?**
Microsoft Excel tillåter flera ark i en enda fil. HTML5 Spreadsheet Editor låter användaren lägga till och ta bort ark. På fliken Ark har vi en rullgardinslista med ark. Det valda arket är det som öppnas av redaktören.

Så här lägger du till ett nytt blad:

1.  Byta till**Fliken Ark**.
1. Klicka på **+** (plus)-knappen.

Ett nytt ark läggs till och redigeraren byter till det.

Så här tar du bort det för närvarande valda arket:

1.  Byta till**Fliken Ark**.
1. Klicka på knappen **-** (minus).

Det för närvarande valda arket kommer att tas bort och redigeraren växlar till det senast valda arket.

![todo:image_alt_text](4wgvmu8.png)

**Hur det fungerar?**

 När användaren klickar på** +** (plus) och**-** (minus) knappen klickas, JSF backend bean**Arbetsbladsvy** hanterar händelserna med hjälp av**WorksheetView.onAddNewSheet** och**WorksheetView.onRemoveActiveSheet** metoder.
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
### **Byt namn på ark**
Så här byter du namn på ett arbetsblad:

1.  Byta till**Fliken Ark**.
1. Klicka på arkets namn i textrutan för att redigera det.
1. Ändra namnet på arket.
1. När du är klar, tryck på ENTER-tangenten eller klicka var som helst utanför rutan.

Arket kommer att döpas om.

![todo:image_alt_text](4wgvmu8.png)

**Hur det fungerar?**

 När textboxens värde ändras, hanteras händelsen på servern av JSF backend bean**Arbetsbladsvy** använder metoden**WorksheetView.setActiveSheet**.
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
### **Växla mellan ark**
Så här byter du till ett annat blad:

1.  Byta till**Fliken Ark**.
1. Välj ett ark från rullgardinsmenyn.

Redaktören växlar till det valda arket.

![todo:image_alt_text](4wgvmu8.png)

**Hur det fungerar?**

 När den nedrullningsbara väljarens värde ändras, hanteras händelsen på servern av JSF backend bean**Arbetsbladsvy** använder metoden**WorksheetView.setActiveSheet**.
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
