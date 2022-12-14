---
title: Adición de controles Cell en hojas de trabajo
type: docs
weight: 120
url: /es/net/adding-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

 Los controles Cell son, de hecho, aquellos controles que se pueden agregar a las hojas de trabajo. Nosotros los llamamos**Cell Controles** porque estos controles se muestran en celdas. En este tema, hablaremos sobre cómo agregar y manejar los eventos de estos controles de celda.

{{% /alert %}} 
## **Introducción**
Actualmente, Aspose.Cells.GridDesktop admite la adición de tres tipos de controles de celda, que incluyen lo siguiente:

- **Botón**
- **Caja**
- **Caja combo**

Todos estos controles se derivan de una clase abstracta,**CellControl**. Cada hoja de trabajo contiene una colección de**Control S**Se pueden agregar nuevos controles de celda y se puede acceder a los existentes usando este**Control S**colección fácilmente.

**IMPORTANTE:**Si desea agregar controles de celda a todas las celdas de una columna en lugar de agregar uno por uno, puede consultar[Gestión de controles Cell en columnas.](/cells/es/net/adding-cell-controls-in-worksheets/)
### **Añadir botón**
Para agregar un botón a la hoja de trabajo usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

- Agregue el control Aspose.Cells.GridDesktop a su**Forma**
- Accede a cualquier deseado**Hoja de cálculo**
- Agregar**Botón**hacia**Control S**colección de la**Hoja de cálculo**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingButton.cs" >}}


Mientras agrega**Botón**, podemos especificar la ubicación de la celda (dónde mostrarla), ancho y alto y el título del botón.
#### **Gestión de eventos de botón**
Hemos discutido acerca de agregar**Botón**controlar a la**Hoja de cálculo**pero cuál es la ventaja de tener solo un botón en la hoja de trabajo si no podemos usarlo. Entonces, aquí viene la necesidad del manejo de eventos del botón.

para manejar el**Hacer clic**evento de la**Botón**control, Aspose.Cells.GridDesktop proporciona**Clic en el botón de la celda**evento que debe ser implementado por los desarrolladores de acuerdo a sus necesidades. Por ejemplo, acabamos de mostrar un mensaje cuando se hace clic en el botón como se muestra a continuación:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingButton.cs" >}}
#### **Especificación de una imagen de fondo para el control de botón**
Podemos establecer una imagen/imagen de fondo para el control del botón con su etiqueta/texto como se muestra en el código a continuación:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-SetBackground.cs" >}}


**IMPORTANTE:**Todos los eventos de los controles de celda contienen un**CellControlEventArgs**argumento que proporciona los números de fila y columna de la celda que contiene el control de celda (cuyo evento se activa).
### **Agregar casilla de verificación**
Para agregar una casilla de verificación en la hoja de trabajo usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

- Agregue el control Aspose.Cells.GridDesktop a su**Forma**
- Accede a cualquier deseado**Hoja de cálculo**
- Agregar**Caja**hacia**Control S**colección de la**Hoja de cálculo**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCheckbox.cs" >}}


Mientras agrega**Caja**, podemos especificar la ubicación de la celda (dónde mostrarla) y el estado de la casilla de verificación.
#### **Manejo de eventos de CheckBox**
Aspose.Cells.GridDesktop proporciona**CellCheckedChanged**evento que se desencadena cuando el**Comprobado**se cambia el estado de la casilla de verificación. Los desarrolladores pueden gestionar este evento según sus requisitos. Por ejemplo, acabamos de mostrar un mensaje para mostrar el**Comprobado**estado de la casilla de verificación en el siguiente código:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCheckbox.cs" >}}
### **Agregar cuadro combinado**
Para agregar un cuadro combinado a la hoja de trabajo usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

- Agregue el control Aspose.Cells.GridDesktop a su**Forma**
- Accede a cualquier deseado**Hoja de cálculo**
- Cree una matriz de elementos (o valores) que se agregarán a**Caja combo**
- Agregar**Caja combo**hacia**Control S**colección de la**Hoja de cálculo**especificando la ubicación de la celda (donde se mostrará el cuadro combinado) y los elementos/valores que se mostrarán cuando se haga clic en el cuadro combinado



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-AddingCombobox.cs" >}}
#### **Manejo de eventos de ComboBox**
Aspose.Cells.GridDesktop proporciona**CellSelectedIndexChanged**evento que se desencadena cuando el**Índice seleccionado**de cuadro combinado se cambia. Los desarrolladores pueden manejar este evento según sus deseos. Por ejemplo, acabamos de mostrar un mensaje para mostrar el**Item seleccionado**del cuadro combinado:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddingCellControls-HandlingCombobox.cs" >}}
