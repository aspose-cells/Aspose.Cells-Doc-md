---
title: Editor de hojas de cálculo  Trabajando con Funciones
type: docs
weight: 60
url: /es/java/spreadsheet-editor-working-with-functions/
---

**Tabla de contenidos**

- [Barra de Fórmulas](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
  - saveFormulaBarContents
- [Insertar una Función](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Barra de Fórmulas**
La barra de fórmulas es un cuadro de texto en la parte superior del área de la hoja. Muestra la fórmula de la celda actual y permite al usuario editarla.

**¿Cómo funciona?**

Cuando se selecciona una celda, la barra de fórmulas se sincroniza con la celda y se muestra la fórmula. Se permite al usuario editarla. Cuando el usuario edita y presiona la tecla enter, se ejecuta la función de JavaScript **saveFormulaBarContents**
#### **saveFormulaBarContents**
{{< highlight java >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Insertar una Función**
Para insertar una función o fórmula:

1. Haz clic en una celda para seleccionarla.
1. Haz clic en el botón **Insertar Función** en la parte superior.
1. Sigue las instrucciones en el diálogo **Insertar Función**.
{{< app/cells/assistant language="java" >}}
