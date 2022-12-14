---
title: Editor de hojas de cálculo - Trabajar con funciones
type: docs
weight: 60
url: /es/java/spreadsheet-editor-working-with-functions/
---
**Tabla de contenido**

- [Barra de formulas](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
 - saveFormulaBarContents
- [Insertar una función](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Barra de formulas**
La barra de fórmulas es un cuadro de texto en la parte superior del área de la hoja. Muestra la fórmula de la celda actual y permite al usuario editarla.

**¿Cómo funciona?**

 Cuando se selecciona una celda, la barra de fórmulas se sincroniza con la celda y se muestra la fórmula. El usuario puede editar. Cuando el usuario edita y presiona la tecla Intro, la función de JavaScript**guardarFormulaBarContents** es ejecutado
#### **guardarFormulaBarContents**
{{< highlight "java" >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Insertar una función**
Para insertar una función o fórmula:

1. Haga clic en una celda para seleccionarla.
1.  Hacer clic**Función de inserción** botón en la parte superior.
1.  Siga las instrucciones en el**Función de inserción**diálogo.
