---
title: Trabajando con Cells GridWeb
type: docs
weight: 50
url: /es/java/working-with-cells-gridweb/
---
## **Accediendo a Cells en la hoja de trabajo**
Este tema analiza las celdas y analiza la característica más básica de GridWeb: acceder a las celdas.

Cada hoja de trabajo contiene un objeto GridCells, una colección de objetos GridCell. Un objeto GridCell representa una celda en Aspose.Cells.GridWeb. Es posible acceder a cualquier celda utilizando GridWeb. Hay dos métodos preferidos:

- [Acceso a la celda por nombre](/cells/es/java/working-with-cells-gridweb/).
- [Acceso a la celda por índices de fila y columna](/cells/es/java/working-with-cells-gridweb/).

A continuación, se analiza cada enfoque.
### **Usando Cell Nombre**
Todas las celdas tienen un nombre único. Por ejemplo, A1, A2, B1, B2, etc. Aspose.Cells. GridWeb permite a los desarrolladores acceder a cualquier celda deseada usando el nombre de la celda. Simplemente pase el nombre de la celda (como un índice) a la colección GridCells de GridWorksheet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Uso de índices de fila y columna**
Una celda también se puede reconocer por su ubicación en términos de índices de fila y columna. Simplemente pase los índices de fila y columna de una celda a la colección GridCells de GridWorksheet. Este enfoque es más rápido que el anterior.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Acceso y Modificación del Valor de un Cell**
[Accediendo a Cells en la hoja de trabajo](/cells/es/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) habló sobre el acceso a las celdas. Este tema amplía esa discusión para mostrar cómo acceder y modificar valores de celda usando GridWeb API.
### **Acceso y modificación del valor de Cell**
#### **Valores de cadena**
 Antes de acceder y modificar el valor de una celda, debe saber cómo acceder a las celdas. Para obtener detalles sobre los diferentes enfoques para acceder a las celdas, consulte[Accediendo a Cells en la hoja de trabajo](/cells/es/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Cada celda tiene una propiedad llamada getStringValue(). Una vez que se accede a una celda, los desarrolladores pueden acceder al método getStringValue() para acceder al valor de la cadena de celdas.

{{% alert color="primary" %}} 

IMPORTANTE: Se pueden almacenar cinco tipos de valores (Boolean, int, double, DateTime y string) en las celdas, pero los métodos getValue()/setValue() solo se pueden usar para acceder/modificar el valor del objeto.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Todo tipo de valores**
Aspose.Cells.GridWeb también proporciona un método especial, putValue, para cada celda. Con este método es posible insertar o modificar cualquier tipo de valor (Boolean, int, double, DateTime y string) en una celda.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



También hay una versión sobrecargada del método putValue que puede tomar cualquier tipo de valor en formato de cadena y convertirlo automáticamente a un tipo de datos adecuado. Para que esto suceda, pase el valor booleano verdadero a otro parámetro del método putValue como se muestra a continuación en el ejemplo.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Adición de fórmulas al Cells**
La característica más valiosa que ofrece Aspose.Cells.GridWeb es el soporte para fórmulas o funciones. Aspose.Cells.GridWeb tiene su propio motor de fórmulas que calcula las fórmulas en las hojas de cálculo. Aspose.Cells.GridWeb admite funciones o fórmulas integradas y definidas por el usuario. Este tema trata sobre cómo agregar fórmulas a las celdas mediante Aspose.Cells.GridWeb API en detalle.
### **¿Cómo agregar y calcular una fórmula?**
 Es posible agregar, acceder y modificar fórmulas en celdas usando la propiedad Fórmula de una celda. Aspose.Cells. GridWeb admite fórmulas definidas por el usuario que van desde simples hasta complejas. Sin embargo, una gran cantidad de funciones o fórmulas integradas (similares a Microsoft Excel) también se proporcionan con Aspose.Cells.GridWeb. Para ver la lista completa de funciones integradas, consulte este[lista de funciones compatibles.](/cells/es/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

La sintaxis de la fórmula debe ser compatible con la sintaxis de Excel Microsoft. Por ejemplo, todas las fórmulas deben comenzar con un signo igual (=).

Para agregar una fórmula mediante programación, Aspose.Cells.GridWeb la reconocerá como una fórmula incluso si no usa un signo **=**, pero si los usuarios finales que trabajan en la GUI deben usarla.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Fórmula agregada a la celda B3 pero no calculada por GridWeb** 

![todo:imagen_alternativa_texto](working-with-cells-gridweb_1.png)

En la captura de pantalla anterior, puede ver que se agregó una fórmula a B3 pero aún no se calculó. Para calcular todas las fórmulas, llame al método de cálculo de fórmula de GridWorksheetCollection del control GridWeb después de agregar fórmulas a las hojas de cálculo, como se muestra a continuación.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

 Los usuarios también pueden calcular fórmulas haciendo clic en**Enviar**.

**Al hacer clic en el botón Enviar de GridWeb** 

![todo:imagen_alternativa_texto](working-with-cells-gridweb_2.png)

**IMPORTANTE** : si un usuario hace clic en el**Ahorrar** o**Deshacer** o las pestañas de las hojas, todas las fórmulas son calculadas por GridWeb automáticamente.

**Resultado de la fórmula después del cálculo** 

![todo:imagen_alternativa_texto](working-with-cells-gridweb_3.png)
### **Haciendo referencia a Cells de otras hojas de trabajo**
Usando Aspose.Cells.GridWeb, es posible hacer referencia a valores almacenados en diferentes hojas de trabajo en sus fórmulas, creando fórmulas complejas.

La sintaxis para hacer referencia a un valor de celda de una hoja de trabajo diferente es SheetName!CellName.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **Crear validación de datos en un GridCell de GridWeb**
 Aspose.Cells. GridWeb le permite agregar**Validación de datos** utilizando el método GridWorksheet.getValidations().add(). Usando este método, usted tiene que especificar el**Cell gama** . Pero si desea crear una Validación de datos en un único GridCell, puede hacerlo directamente utilizando el método GridCell.createValidation(). Del mismo modo, puede eliminar**Validación de datos** desde un GridCell utilizando el método GridCell.removeValidation().

 El siguiente código de ejemplo crea un**Validación de datos** en una celda B3. Si ingresa cualquier valor que no esté entre 20 y 40, la celda B3 mostrará**Error de validacion** en forma de**Rojo XXXX** como se muestra en esta captura de pantalla.

![todo:imagen_alternativa_texto](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Creación de botones de comando personalizados**
Aspose.Cells.GridWeb contiene botones especiales como Enviar, Guardar y Deshacer. Todos estos botones realizan tareas específicas para Aspose.Cells.GridWeb. También es posible agregar botones personalizados que realizan tareas personalizadas. Este tema explica cómo utilizar esta función.

El siguiente código de ejemplo explica cómo crear un botón de comando personalizado y cómo controlar su evento de clic. Puede usar cualquier icono para su botón de comando personalizado. Con fines ilustrativos, utilizamos este icono de imagen.

![todo:imagen_alternativa_texto](working-with-cells-gridweb_5.png)

 Como puede ver en la siguiente captura de pantalla, cuando el usuario hace clic en el botón de comando personalizado, agrega un texto en la celda A1 que dice**"Se hace clic en mi botón de comando personalizado".**

![todo:imagen_alternativa_texto](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Gestión de eventos del botón de comando personalizado**
El siguiente código de ejemplo explica cómo realizar el control de eventos del botón de comando personalizado.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **Formateo de celdas para GridWeb**
### **Posibles escenarios de uso**
GridWeb ahora permite a los usuarios ingresar datos de celda en formato de porcentaje como 3% y los datos en la celda se formatearán automáticamente como 3.00%. Sin embargo, tendrá que establecer el estilo de celda en Formato de porcentaje, que es GridTableItemStyle.NumberType a 9 o 10. El número 9 formateará el 3 % como 3 %, pero el número 10 formateará el 3 % como 3,00 %.

{{% alert color="primary" %}} 

Si no ha establecido el estilo de celda en Formato de porcentaje, los datos de entrada 3% se mostrarán como 0,03.

{{% /alert %}} 
### **Ingrese Cell Datos de la hoja de trabajo GridWeb en formato de porcentaje**
El siguiente código de muestra establece la celda A1 GridTableItemStyle.NumberType como 10, por lo tanto, los datos de entrada 3 % se formatearán automáticamente como 3,00 %, como se muestra en la captura de pantalla.

![todo:imagen_alternativa_texto](working-with-cells-gridweb_7.png)
### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
