---
title: Proteger Celdas
type: docs
weight: 50
url: /es/net/aspose-cells-gridweb/protect-cells/
keywords: GridWeb, proteger, solo lectura, editable
description: Este artículo presenta cómo proteger celdas en GridWeb.
---

{{% alert color="primary" %}} 

Este tema describe algunas técnicas para proteger celdas. El uso de estas técnicas permite a los desarrolladores restringir a los usuarios la edición de todas o un rango seleccionado de celdas en una hoja de cálculo.

{{% /alert %}} 
## **Protección de Celdas**
Aspose.Cells.GridWeb proporciona algunas técnicas diferentes para controlar el nivel de protección en celdas cuando el control está en [modo de edición](/cells/es/net/aspose-cells-gridweb/enable-different-gridweb-modes/#edit-mode) (el modo predeterminado). Esto protege las celdas para que no sean modificadas por los usuarios finales.
### **Hacer Todas las Celdas de Solo Lectura**
Para establecer todas las celdas en una hoja de cálculo como de solo lectura, llame al método SetAllCellsReadonly de la hoja de cálculo.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Hacer Todas las Celdas Editables**
Para quitar la protección de todas las celdas, llame al método SetAllCellsEditable de la hoja de cálculo. Este método tiene el efecto opuesto al método SetAllCellsReadonly.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Hacer Celdas Seleccionadas de Solo Lectura**
Para proteger solo un rango de celdas:

1. Primero haga todas las celdas editables llamando al método SetAllCellsEditable.
1. Especifique el rango de celdas a proteger llamando al método SetReadonlyRange de la hoja de cálculo. Este método toma el número de filas y columnas para especificar el rango de celdas.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Haciendo celdas seleccionadas editables**
Para desproteger un rango de celdas:

1. Haga todas las celdas de solo lectura llamando al método SetAllCellsReadonly.
1. Especifique el rango de celdas a editar llamando al método SetEditableRange de la hoja de cálculo. Este método toma el número de filas y columnas para especificar el rango de celdas.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
