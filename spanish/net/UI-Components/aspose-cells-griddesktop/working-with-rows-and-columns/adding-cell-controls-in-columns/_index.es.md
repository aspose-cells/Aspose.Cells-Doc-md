---
title: Agregando Controles de Celda en Columnas
type: docs
weight: 90
url: /es/net/aspose-cells-griddesktop/add-cell-controls-in-columns/
keywords: GridDesktop,add,control,controls
description: Este artículo introduce cómo agregar control en columna en GridDesktop.
---

{{% alert color="primary" %}} 

En nuestras discusiones posteriores, hemos hablado sobre añadir y gestionar controles de celda en la hoja de cálculo. Pero, usando esos enfoques, podemos añadir controles de celda a una por una. ¿Qué pasa si alguien quisiera añadir controles de celda a todas las celdas de una o más columnas? En tales casos, para reducir los esfuerzos de los desarrolladores, Aspose.Cells.GridDesktop proporciona la función de añadir controles de celda por columna. Significa que los desarrolladores solo pueden seleccionar una columna deseada y especificar algún control de celda. El control de celda especificado se añadirá a todas las celdas de la columna especificada. Veamos cómo podemos usar esta función.

{{% /alert %}} 
## **Introducción**
Actualmente, Aspose.Cells.GridDesktop soporta añadir tres tipos de controles de celda, que incluyen lo siguiente:

- **Botón**
- **CheckBox**
- **ComboBox**

Todos estos controles se derivan de una clase abstracta, **CellControl**.

**IMPORTANTE:** Si desea agregar controles de celda a una sola celda en lugar de toda la columna, puede consultar [Agregar controles de celda en hojas de cálculo.](/cells/es/net/adding-cell-controls-in-worksheets/)
### **Añadiendo Botón**
Para agregar botones en una columna usando Aspose.Cells.GridDesktop, siga los siguientes pasos:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceda a cualquier **Hoja de Cálculo** deseada
- Agregar **Botón** a cualquier **Columna** especificada de la **Hoja de cálculo**

**NOTA:** Mientras se agrega el **Botón**, podemos especificar el ancho, alto y leyenda del botón.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


El fragmento de código anterior añade botones a todas las celdas de la columna especificada. Cuando se selecciona cualquier celda de esa columna específica, un botón se vuelve visible. Para obtener más información sobre el manejo de eventos de los botones, consulte [Manejo de eventos de un control de botón.](/cells/es/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **Añadiendo CheckBox**
Para agregar casillas de verificación en una columna usando Aspose.Cells.GridDesktop, siga los siguientes pasos:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceda a cualquier **Hoja de Cálculo** deseada
- Agregar **CheckBox** a cualquier **Columna** especificada de la **Hoja de trabajo**

**NOTA:** Al agregar **CheckBox**, también podemos especificar el estado de la casilla de verificación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


El fragmento de código anterior agrega casillas de verificación a todas las celdas de la columna especificada. Para obtener más información sobre el manejo de eventos de las casillas de verificación, consulte [Manejo de eventos de un control de CheckBox.](/cells/es/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **Agregar ComboBox**
Para agregar comboboxes en una columna usando Aspose.Cells.GridDesktop, siga los siguientes pasos:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceda a cualquier **Hoja de Cálculo** deseada
- Crear un array de elementos (o valores) que se agregarán a **ComboBox**
- Agregar **ComboBox** (conteniendo elementos o valores) a cualquier **Columna** especificada de la **Hoja de trabajo**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


El fragmento de código anterior agrega comboboxes a todas las celdas de la columna especificada. Cuando se selecciona cualquier celda de esa columna específica, un combobox se vuelve visible. Para obtener más información sobre el manejo de eventos de comboboxes, consulte [Manejo de eventos de un control de ComboBox.](/cells/es/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
