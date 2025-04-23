---
title: Editor de hojas de cálculo  Trabajando con hojas
type: docs
weight: 20
url: /es/java/spreadsheet-editor-working-with-sheets/
---

**Tabla de contenidos**

- [¿Agregar y quitar hojas?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
  - WorksheetView.onAddNewSheet
  - WorksheetView.onRemoveActiveSheet
- [Renombrar hojas](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
  - WorksheetView.setActiveSheet
- [Cambiar entre hojas](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
  - WorksheetView.setActiveSheet
### **¿Agregar y quitar hojas?**
Microsoft Excel permite múltiples hojas en un solo archivo. El editor de hojas de cálculo HTML5 permite al usuario agregar y quitar hojas. En la pestaña Hojas, tenemos una lista desplegable de hojas. La hoja seleccionada es la que está abierta en el editor.

Para agregar una nueva hoja:

1. Cambiar a la pestaña de **Hojas**.
2. Haga clic en el botón **+** (más).

Se agregará una nueva hoja y el editor cambiará a ella.

Para eliminar la hoja actualmente seleccionada:

1. Cambiar a la pestaña de **Hojas**.
1. Hacer clic en el botón **-** (menos).

La hoja actualmente seleccionada será eliminada y el editor cambiará a la última seleccionada.

![todo:image_alt_text](4wgvmu8.png)

**¿Cómo funciona?**

Cuando el usuario hace clic en los botones **+** (más) y **-** (menos), el bean de backend de JSF **WorksheetView** maneja los eventos utilizando los métodos **WorksheetView.onAddNewSheet** y **WorksheetView.onRemoveActiveSheet**.
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
### **Renombrar hojas**
Para renombrar una hoja:

1. Cambiar a la pestaña de **Hojas**.
1. Hacer clic en el nombre de la hoja en el cuadro de texto para editarlo.
1. Cambiar el nombre de la hoja.
1. Cuando haya terminado, presionar la tecla ENTER o hacer clic en cualquier parte fuera del cuadro.

La hoja se habrá renombrado.

![todo:image_alt_text](4wgvmu8.png)

**¿Cómo funciona?**

Cuando el valor del cuadro de texto cambia, el evento es manejado en el servidor por el bean de backend de JSF **WorksheetView** utilizando el método **WorksheetView.setActiveSheet**.
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
### **Cambiar entre hojas**
Para cambiar a otra hoja:

1. Cambiar a la pestaña de **Hojas**.
1. Seleccionar una hoja desde el menú desplegable.

El editor cambiará a la hoja seleccionada.

![todo:image_alt_text](4wgvmu8.png)

**¿Cómo funciona?**

Cuando el valor del selector desplegable cambia, el evento es manejado en el servidor por el bean de backend JSF **WorksheetView** utilizando el método **WorksheetView.setActiveSheet**.
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
