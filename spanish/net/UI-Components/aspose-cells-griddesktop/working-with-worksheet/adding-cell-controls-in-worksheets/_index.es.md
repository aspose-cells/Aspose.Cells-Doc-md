---
title: Añadir controles de celda en hojas de cálculo
type: docs
weight: 120
url: /es/net/aspose-cells-griddesktop/add-cell-controls-in-worksheets/
keywords: GridDesktop,add,control,button,checkbox,combobox
description: Este artículo presenta cómo añadir un control en una hoja de cálculo en GridDesktop.
---

{{% alert color="primary" %}} 

Los controles de celda son, de hecho, los controles que pueden añadirse a las hojas de cálculo. Les llamamos **Controles de Celda** porque estos controles se muestran en celdas. En este tema, discutiremos acerca de cómo añadir y manejar los eventos de estos controles de celda.

{{% /alert %}} 
## **Introducción**
Actualmente, Aspose.Cells.GridDesktop soporta añadir tres tipos de controles de celda, que incluyen lo siguiente:

- **Botón**
- **CheckBox**
- **ComboBox**

Todos estos controles se derivan de una clase abstracta, **CellControl**. Cada hoja de cálculo contiene una colección de **Controles**. Nuevos controles de celda se pueden agregar y los existentes se pueden acceder fácilmente utilizando esta colección **Controles**.

**IMPORTANTE:** Si desea agregar controles de celda a todas las celdas de una columna en lugar de agregar uno por uno, puede consultar [Gestión de Controles de Celda en Columnas](/cells/es/net/aspose-cells-griddesktop/adding-cell-controls-in-worksheets/)
### **Añadiendo Botón**
Para agregar un botón a la hoja de cálculo usando Aspose.Cells.GridDesktop, siga los siguientes pasos:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceder a cualquier **Hoja de trabajo** deseada
- Agregue un **Botón** a la colección de **Controles** de la **Hoja de Cálculo**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


Al agregar un **Botón**, podemos especificar la ubicación de la celda (dónde mostrarlo), el ancho y alto, y la leyenda del botón.
#### **Manejo de eventos del Botón**
Hemos discutido cómo agregar un control de **Botón** a la **Hoja de Cálculo**, pero ¿cuál es la ventaja de tener un botón en la hoja de cálculo si no podemos usarlo? Aquí es donde surge la necesidad de manejar el evento del botón.

Para manejar el evento **Click** del control de **Botón**, Aspose.Cells.GridDesktop proporciona el evento **CellButtonClick** que debe ser implementado por los desarrolladores según sus necesidades. Por ejemplo, simplemente mostramos un mensaje cuando se hace clic en el botón como se muestra a continuación:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Especificar una Imagen de Fondo para el Control de Botón**
Podemos establecer una imagen de fondo para el control de botón con su etiqueta/ texto como se muestra en el código a continuación:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**IMPORTANTE:** Todos los eventos de controles de celda contienen un argumento **CellControlEventArgs** que proporciona los números de fila y columna de la celda que contiene el control de celda (cuyo evento es desencadenado).
### **Añadiendo CheckBox**
Para agregar un casilla de verificación a la hoja de cálculo usando Aspose.Cells.GridDesktop, siga los siguientes pasos:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceder a cualquier **Hoja de trabajo** deseada
- Agregar **CheckBox** a la colección de **Controles** de la **Hoja de trabajo**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


Al agregar **CheckBox**, podemos especificar la ubicación de la celda (dónde mostrarlo) y el estado de la casilla de verificación.
#### **Manipulación de eventos de CheckBox**
Aspose.Cells.GridDesktop proporciona el evento **CellCheckedChanged** que se desencadena cuando se cambia el estado **Checked** de la casilla de verificación. Los desarrolladores pueden manejar este evento según sus requisitos. Por ejemplo, hemos mostrado un mensaje para mostrar el estado **Checked** de la casilla de verificación en el código a continuación:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **Agregar ComboBox**
Para agregar un cuadro combinado en la hoja de cálculo usando Aspose.Cells.GridDesktop, siga los siguientes pasos:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceder a cualquier **Hoja de trabajo** deseada
- Crear una matriz de elementos (o valores) que se agregarán al **ComboBox**
- Agregar **ComboBox** a la colección de **Controles** de la **Hoja de trabajo** especificando la ubicación de la celda (dónde se mostrará el cuadro combinado) y los elementos/valores que se mostrarán al hacer clic en el cuadro combinado



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **Manipulación de eventos de ComboBox**
Aspose.Cells.GridDesktop proporciona el evento **CellSelectedIndexChanged** que se desencadena cuando se cambia el **Índice seleccionado** del cuadro combinado. Los desarrolladores pueden manejar este evento según sus deseos. Por ejemplo, hemos mostrado un mensaje para mostrar el **Ítem seleccionado** del cuadro combinado:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
