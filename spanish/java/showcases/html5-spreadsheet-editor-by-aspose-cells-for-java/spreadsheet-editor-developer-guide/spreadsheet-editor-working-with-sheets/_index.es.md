---
title: Editor de hojas de cálculo - Trabajar con hojas
type: docs
weight: 20
url: /es/java/spreadsheet-editor-working-with-sheets/
---
**Tabla de contenido**

- [¿Agregar y quitar hojas?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
 - WorksheetView.onAddNewSheet
 - WorksheetView.onRemoveActiveSheet
- [Renombrar hojas](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
 - WorksheetView.setActiveSheet
- [Cambiar entre hojas](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
 - WorksheetView.setActiveSheet
### **¿Agregar y quitar hojas?**
Microsoft Excel permite múltiples hojas en un solo archivo. El editor de hojas de cálculo HTML5 permite al usuario agregar y eliminar hojas. En la pestaña Hojas tenemos una lista desplegable de hojas. La hoja seleccionada es la que abre el editor.

Para agregar una nueva hoja:

1.  Cambiar a**Pestaña Hojas**.
1. Haga clic en el botón **+** (más).

Se agregará una nueva hoja y el editor cambiará a ella.

Para eliminar la hoja seleccionada actualmente:

1.  Cambiar a**Pestaña Hojas**.
1. Haga clic en el botón **-** (menos).

La hoja seleccionada actualmente se eliminará y el editor cambiará a la última seleccionada.

![todo:imagen_alternativa_texto](4wgvmu8.png)

**¿Cómo funciona?**

 Cuando el usuario hace clic en** +** (más) y**-** Se hace clic en el botón (menos), el bean backend JSF**Vista de hoja de trabajo** maneja los eventos usando**WorksheetView.onAddNewSheet** y**Métodos WorksheetView.onRemoveActiveSheet**.
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
### **Renombrar hojas**
Para cambiar el nombre de una hoja:

1.  Cambiar a**Pestaña Hojas**.
1. Haga clic en el nombre de la hoja en el cuadro de texto para editarlo.
1. Cambia el nombre de la hoja.
1. Cuando termine, presione la tecla ENTER o haga clic en cualquier lugar fuera del cuadro.

Se cambiará el nombre de la hoja.

![todo:imagen_alternativa_texto](4wgvmu8.png)

**¿Cómo funciona?**

 Cuando se cambia el valor del cuadro de texto, el bean backend JSF maneja el evento en el servidor**Vista de hoja de trabajo** utilizando el método**WorksheetView.setActiveSheet**.
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
### **Cambiar entre hojas**
Para cambiar a otra hoja:

1.  Cambiar a**Pestaña Hojas**.
1. Seleccione una hoja del menú desplegable.

El editor cambiará a la hoja seleccionada.

![todo:imagen_alternativa_texto](4wgvmu8.png)

**¿Cómo funciona?**

 Cuando se cambia el valor del selector desplegable, el bean backend JSF maneja el evento en el servidor**Vista de hoja de trabajo** utilizando el método**WorksheetView.setActiveSheet**.
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
