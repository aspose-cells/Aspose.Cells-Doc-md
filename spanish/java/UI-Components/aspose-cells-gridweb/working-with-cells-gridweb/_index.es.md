---
title: Trabajando con Celdas de GridWeb
type: docs
weight: 50
url: /es/java/working-with-cells-gridweb/
---

## **Accediendo a las Celdas en la Hoja de Cálculo**
Este tema trata sobre las celdas, examinando la característica más básica de GridWeb: acceder a las celdas.

Cada hoja de cálculo contiene un objeto GridCells, una colección de objetos GridCell. Un objeto GridCell representa una celda en Aspose.Cells.GridWeb. Es posible acceder a cualquier celda utilizando GridWeb. Hay dos métodos preferidos:

- [Acceder a la celda por nombre](/cells/es/java/working-with-cells-gridweb/).
- [Acceder a la celda mediante los índices de fila y columna](/cells/es/java/working-with-cells-gridweb/).

A continuación, se discute cada enfoque.
### **Usando el nombre de la celda**
Todas las celdas tienen un nombre único. Por ejemplo, A1, A2, B1, B2, etc. Aspose.Cells.GridWeb permite a los desarrolladores acceder a cualquier celda deseada utilizando el nombre de la celda. Simplemente pase el nombre de la celda (como un índice) a la colección GridCells de la hoja de cálculo del GridWeb.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Usando los índices de fila y columna**
También es posible reconocer una celda por su ubicación en términos de índices de fila y columna. Simplemente pase los índices de fila y columna de una celda a la colección GridCells de la hoja de cálculo del GridWeb. Este enfoque es más rápido que el anterior.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Acceder y modificar el valor de una celda**
[Acceder a las celdas en la hoja de cálculo](/cells/es/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) trata sobre el acceso a las celdas. Este tema amplía esa discusión para mostrar cómo acceder y modificar los valores de las celdas utilizando la API de GridWeb.
### **Acceder y modificar el valor de una celda**
#### **Valores de cadena**
Antes de acceder y modificar el valor de una celda, es necesario saber cómo acceder a las celdas. Para obtener detalles sobre los diferentes enfoques para acceder a las celdas, consulte [Acceder a las celdas en la hoja de cálculo](/cells/es/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Cada celda tiene una propiedad llamada getStringValue(). Una vez que una celda es accedida, los desarrolladores pueden acceder al método getStringValue() para obtener el valor de cadena de las celdas.

{{% alert color="primary" %}} 

IMPORTANTE: Cinco tipos de valores (booleano, int, double, DateTime y cadena) pueden ser almacenados en las celdas, pero el/los método(s) getValue()/setValue() solo se pueden utilizar para acceder/modificar el valor del objeto.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Todos los tipos de valores**
Aspose.Cells.GridWeb también proporciona un método especial, putValue, para cada celda. Con este método, es posible insertar o modificar cualquier tipo de valor (booleano, int, double, DateTime y cadena) en una celda.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



También existe una versión sobrecargada del método putValue que puede tomar cualquier tipo de valor en formato de cadena y convertirlo automáticamente a un tipo de dato adecuado. Para que esto ocurra, pase el valor booleano true a otro parámetro del método putValue como se muestra a continuación en el ejemplo.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Agregar fórmulas a las celdas**
La característica más valiosa ofrecida por Aspose.Cells.GridWeb es el soporte para fórmulas o funciones. Aspose.Cells.GridWeb tiene su propio Motor de Fórmulas que calcula las fórmulas en las hojas de cálculo. Aspose.Cells.GridWeb soporta tanto funciones o fórmulas incorporadas como definidas por el usuario. Este tema discute agregar fórmulas a celdas utilizando la API de Aspose.Cells.GridWeb en detalle.
### **¿Cómo agregar y calcular una fórmula?**
Es posible agregar, acceder y modificar fórmulas en celdas utilizando la propiedad de Fórmula de una celda. Aspose.Cells.GridWeb admite fórmulas definidas por el usuario que van desde simples hasta complejas. Sin embargo, Aspose.Cells.GridWeb también suministra un gran número de funciones o fórmulas incorporadas (similar a Microsoft Excel). Para ver la lista completa de funciones incorporadas, consulte esta [lista de funciones admitidas.](/cells/es/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

La sintaxis de la fórmula debe ser compatible con la sintaxis de Microsoft Excel. Por ejemplo, todas las fórmulas deben comenzar con un signo igual (=).

Para agregar una fórmula programáticamente, Aspose.Cells.GridWeb la reconocerá como una fórmula incluso si no utiliza un **=** signo, pero si los usuarios finales trabajan en la GUI, deben usarlo.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Fórmula agregada a la celda B3 pero no calculada por GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

En la captura de pantalla anterior, puede ver que se ha agregado una fórmula a B3 pero aún no se ha calculado. Para calcular todas las fórmulas, llame al método 'calculateFormula' de la colección GridWorksheet de GridWeb después de agregar fórmulas a las hojas de cálculo como se muestra a continuación.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

Los usuarios también pueden calcular fórmulas haciendo clic en **Enviar**.

**Haciendo clic en el botón Enviar de GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**IMPORTANTE**: Si un usuario hace clic en los botones **Guardar** o **Deshacer**, o en las pestañas de la hoja, todas las fórmulas son calculadas automáticamente por GridWeb.

**Resultado de la fórmula después del cálculo** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
### **Referencia a Celdas de Otras Hojas de Cálculo**
Usando Aspose.Cells.GridWeb, es posible hacer referencia a los valores almacenados en diferentes hojas de cálculo en sus fórmulas, creando fórmulas complejas.

La sintaxis para hacer referencia al valor de una celda de una hoja de cálculo diferente es NombreDeLaHoja!NombreDeLaCelda.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **Crear Validación de Datos en una Celda de GridWeb**
Aspose.Cells.GridWeb le permite agregar **Validación de Datos** utilizando el método GridWorksheet.getValidations().add(). Usando este método, debe especificar el **Rango de Celdas**. Pero si desea crear una Validación de Datos en una sola Celda de GridCell entonces puede hacerlo directamente usando el método GridCell.createValidation(). Del mismo modo, puede eliminar la **Validación de Datos** de una Celda de GridCell utilizando el método GridCell.removeValidation().

El siguiente código de ejemplo crea una **Validación de Datos** en una celda B3. Si ingresa cualquier valor que no esté entre 20 y 40, la celda B3 mostrará **Error de Validación** en forma de **XXX Rojos** como se muestra en esta captura de pantalla.

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Creación de botones de comando personalizados**
Aspose.Cells.GridWeb contiene botones especiales como Enviar, Guardar y Deshacer. Todos estos botones realizan tareas específicas para Aspose.Cells.GridWeb. También es posible agregar botones personalizados que realicen tareas personalizadas. Este tema explica cómo usar esta característica.

El siguiente código de ejemplo explica cómo crear un botón de comando personalizado y cómo manejar su evento de clic. Puede usar cualquier icono para su botón de comando personalizado. A modo de ilustración, usamos esta imagen de icono.

![todo:image_alt_text](working-with-cells-gridweb_5.png)

Como se puede ver en la siguiente captura de pantalla, cuando el usuario hace clic en el botón de comando personalizado, se agrega un texto en la celda A1 que dice **"Mi botón de comando personalizado ha sido clickeado."**

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Manejo de eventos del botón de comando personalizado**
El siguiente código de ejemplo explica cómo realizar el manejo de eventos del botón de comando personalizado.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **Formato de celdas para GridWeb**
### **Escenarios de uso posibles**
GridWeb ahora admite que los usuarios ingresen datos de celda en formato de porcentaje, como 3%, y los datos en la celda se formatearán automáticamente como 3.00%. Sin embargo, deberás establecer el estilo de celda en Formato de Porcentaje, que es el GridTableItemStyle.NumberType 9 o 10. El número 9 formateará el 3% como 3%, pero el número 10 formateará el 3% como 3.00%.

{{% alert color="primary" %}} 

Si no has establecido el estilo de celda en Formato de Porcentaje, entonces el dato de entrada 3% se mostrará como 0.03.

{{% /alert %}} 
### **Ingrese los datos de celda de la hoja de cálculo GridWeb en formato de porcentaje**
El siguiente código de muestra establece el estilo de número de celda A1 GridTableItemStyle.NumberType como 10, por lo tanto, los datos de entrada 3% se formatean automáticamente como 3.00% como se muestra en la captura de pantalla.

![todo:image_alt_text](working-with-cells-gridweb_7.png)
### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
