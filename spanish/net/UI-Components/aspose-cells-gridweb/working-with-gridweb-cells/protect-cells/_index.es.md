---
title: Proteger Cells
type: docs
weight: 50
url: /es/net/protect-cells/
---
{{% alert color="primary" %}} 

En este tema se describen algunas técnicas para proteger las células. El uso de estas técnicas permite a los desarrolladores restringir que los usuarios editen todas las celdas o un rango seleccionado de una hoja de trabajo.

{{% /alert %}} 
## **Protegiendo Cells**
 Aspose.Cells.GridWeb proporciona algunas técnicas diferentes para controlar el nivel de protección en las celdas cuando el control está en[Modo de edición](/cells/es/net/enable-different-gridweb-modes/#edit-mode) (el modo predeterminado). Esto protege las celdas de ser modificadas por los usuarios finales.
### **Hacer que todo Cells sea de solo lectura**
Para configurar todas las celdas de una hoja de cálculo para que sean de solo lectura, llame al método SetAllCellsReadonly de la hoja de cálculo.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Haciendo todo Cells Editable**
Para eliminar la protección de todas las celdas, llame al método SetAllCellsEditable de la hoja de cálculo. Este método tiene el efecto opuesto al método SetAllCellsReadonly.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Hacer seleccionado Cells Solo lectura**
Para proteger solo un rango de celdas:

1. Primero haga que todas las celdas sean editables llamando al método SetAllCellsEditable.
1. Especifique el rango de celdas que desea proteger llamando al método SetReadonlyRange de la hoja de cálculo. Este método toma el número de filas y columnas para especificar el rango de celdas.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Haciendo Editable Cells Seleccionado**
Para desproteger un rango de celdas:

1. Haga que todas las celdas sean de solo lectura llamando al método SetAllCellsReadonly.
1. Especifique el rango de celdas que se pueden editar llamando al método SetEditableRange de la hoja de trabajo. Este método toma el número de filas y columnas para especificar el rango de celdas.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
