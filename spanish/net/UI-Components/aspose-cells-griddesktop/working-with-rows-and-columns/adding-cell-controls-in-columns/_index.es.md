---
title: Adición de controles Cell en columnas
type: docs
weight: 90
url: /es/net/adding-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

En nuestras discusiones posteriores, hemos discutido sobre agregar y administrar controles de celda en la hoja de trabajo. Pero, usando esos enfoques, podemos agregar controles de celda a celdas individuales uno por uno. ¿Qué pasa si alguien quisiera agregar controles de celda a todas las celdas de una o más columnas? En tales casos, para reducir los esfuerzos de los desarrolladores, Aspose.Cells.GridDesktop ofrece la función de agregar controles de celda por columna. Significa que los desarrolladores solo pueden seleccionar una columna deseada y especificar cualquier control de celda. El control de celda especificado se agregará a todas las celdas de la columna especificada. Veamos cómo podemos usar esta función.

{{% /alert %}} 
## **Introducción**
Actualmente, Aspose.Cells.GridDesktop admite la adición de tres tipos de controles de celda, que incluyen lo siguiente:

- **Botón**
- **Caja**
- **Caja combo**

 Todos estos controles se derivan de una clase abstracta,**CellControl**.

**IMPORTANTE:** Si desea agregar controles de celda a una sola celda en lugar de a toda la columna, puede consultar[Adición de controles Cell en hojas de trabajo.](/cells/es/net/adding-cell-controls-in-worksheets/)
### **Añadir botón**
Para agregar botones en una columna usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

-  Agregue el control Aspose.Cells.GridDesktop a su**Formulario**
-  Accede a cualquier deseado**Hoja de cálculo**
-  Agregar**Botón** a cualquier especificado**Columna** del**Hoja de cálculo**

**NOTA:** Mientras agrega**Botón**, podemos especificar el ancho, alto y título del botón.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingButton.cs" >}}


 El fragmento de código anterior agrega botones a todas las celdas de la columna especificada. Cada vez que se selecciona cualquier celda de esa columna específica, se hace visible un botón. Para obtener más información sobre el manejo de eventos de los botones, consulte el[Manejo de eventos de un control de botón.](/cells/es/net/adding-cell-controls-in-worksheets/#event-handling-of-button)
### **Agregar casilla de verificación**
Para agregar casillas de verificación en una columna usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

-  Agregue el control Aspose.Cells.GridDesktop a su**Formulario**
-  Accede a cualquier deseado**Hoja de cálculo**
-  Agregar**Caja** a cualquier especificado**Columna** del**Hoja de cálculo**

**NOTA:** Mientras agrega**Caja**, también podemos especificar el estado de la casilla de verificación.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCheckbox.cs" >}}


 El fragmento de código anterior agrega casillas de verificación a todas las celdas de la columna especificada. Para obtener más información sobre el manejo de eventos de casillas de verificación, consulte el[Manejo de eventos de un control CheckBox.](/cells/es/net/adding-cell-controls-in-worksheets/#event-handling-of-checkbox)
### **Agregar cuadro combinado**
Para agregar cuadros combinados en una columna usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

-  Agregue el control Aspose.Cells.GridDesktop a su**Formulario**
-  Accede a cualquier deseado**Hoja de cálculo**
-  Cree una matriz de elementos (o valores) que se agregarán a**Caja combo**
-  Agregar**Caja combo** (que contiene elementos o valores) a cualquier especificado**Columna** del**Hoja de cálculo**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddingCellControlsInColumns-AddingCombobox.cs" >}}


 El fragmento de código anterior agrega cuadros combinados a todas las celdas de la columna especificada. Cada vez que se selecciona cualquier celda de esa columna específica, se hace visible un cuadro combinado. Para obtener más información sobre el manejo de eventos de los cuadros combinados, consulte el[Manejo de eventos de un control ComboBox.](/cells/es/net/adding-cell-controls-in-worksheets/#event-handling-of-combobox)
