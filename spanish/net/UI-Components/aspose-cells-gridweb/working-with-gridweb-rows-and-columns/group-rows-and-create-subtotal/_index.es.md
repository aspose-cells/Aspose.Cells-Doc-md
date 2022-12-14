---
title: Agrupar filas y crear subtotales
type: docs
weight: 70
url: /es/net/group-rows-and-create-subtotal/
---
{{% alert color="primary" %}} 

Aspose.Cells. GridWeb puede crear un esquema para sus datos. Esto le permite mostrar y ocultar niveles de detalle haciendo clic en los símbolos de esquema "+" y "-" para mostrar solo las filas que proporcionan resúmenes o encabezados para las secciones de una hoja de cálculo. Puede usar los símbolos para ver detalles bajo un resumen o encabezado individual.

Al agrupar filas, es importante seleccionar solo las filas de detalles que componen el grupo. No incluya la fila de resumen relacionada. Por ejemplo, si la fila 6 contiene totales para los datos de las filas 3 a 5, seleccione solo las filas 3 a 5 para definir el grupo. El control Aspose.Cells.GridWeb muestra el**mostrar detalle** (+) y**ocultar detalle** (-) símbolos junto a los encabezados de fila que especifican los grupos en la hoja de trabajo.

Aspose.Cells.GridWeb también le permite crear subtotales basados en cualquier campo de datos. Un subtotal no es necesariamente una suma: puede ser un promedio, un conteo, un mínimo, un máximo u otro cálculo estadístico.

Este tema analiza la agrupación de filas y la creación de subtotales mediante Aspose.Cells.GridWeb API. Los desarrolladores pueden agrupar filas con cualquier nivel de anidamiento y crear subtotales fácilmente.

{{% /alert %}} 
## **Agrupación de filas**
Para agrupar un número específico de filas:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web.
1. Accede a una hoja de trabajo.
1. Seleccione el número deseado de celdas en filas.
1. Agrupa las filas.

Cuando las filas están agrupadas, se muestra un botón para expandir/contraer en la parte superior de la línea de resumen de las filas. Puede cambiar la configuración de dirección. La propiedad WebWorksheet.IsSummaryRowBelow es una propiedad booleana. Establézcalo en falso (predeterminado) y la fila de resumen estará encima de las filas de detalles. Establézcalo en verdadero y la fila de resumen estará debajo de las filas de detalles. Haga clic en el botón expandir/contraer para expandir o contraer filas agrupadas.

El siguiente ejemplo agrupa las filas desde la 2.ª fila hasta la 10.ª fila.

**Agrupación de filas** 

![todo:imagen_alternativa_texto](group-rows-and-create-subtotal_1.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **Anidación de filas agrupadas**
Puede crear niveles de organización mientras agrupa un conjunto de filas. Puede agrupar filas entre las filas agrupadas. El siguiente ejemplo muestra la anidación de filas agrupadas.

**Agrupación de filas** 

![todo:imagen_alternativa_texto](group-rows-and-create-subtotal_2.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **Proceso Interno: ¿Cómo Funciona el Control?**
Cada fila de la hoja tiene un número de esquema. El valor predeterminado del número de esquema es cero. Cada vez que agrupa las filas, el número de esquema aumenta en 1. Puede obtener el número de esquema llamando al método GridWorksheet.Cells.GetRowOutlineLevel().
## **Desagrupar filas**
Aspose.Cells.GridWeb le permite desagrupar filas agrupadas.

Para desagrupar un número específico de filas:

1. Seleccione un número de celdas en las filas de la hoja de trabajo para desagrupar.
1. Desagrupar las filas.

El siguiente ejemplo desagrupa las filas de la 2.ª fila a la 10.ª fila.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

Cuando llama al método GridWorksheet.Cells.UngroupRows(), el número de esquema de las filas agrupadas se establece en cero.

{{% /alert %}} 
## **Creación de subtotales**
La característica de subtotal del control puede agrupar las filas en la hoja con una columna específica y calcular el resumen de las columnas. Aspose.Cells. GridWeb puede calcular automáticamente valores subtotales para una lista. Cuando implementa subtotales, el control delinea la lista para que pueda mostrar y ocultar las filas de detalles para cada subtotal. Antes de agregar subtotales, ordene el campo en el que desea subtotalizar. Para crear subtotales, use cualquier versión del método sobrecargado WebWorksheet.CreateSubtotal.



{{< highlight "java" >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[]subtotalColumnIndexList

);

{{< /highlight >}}
### **Lista de parámetros**

|**No.**|**Nombre del parámetro**|**Descripción**|
|:- |:- |:- |
|1|columnNameRowIndex|El índice de fila de la fila de nombre de columna.|
|2|filas de datos|El número de las filas de datos.|
|3|groupByColumnIndex|El índice de columna de la columna que se va a agrupar.|
|4|subtotalFunción|La enumeración del tipo de función de subtotal.|
|5|subtotalColumnIndexList|Los índices de columna que se subtotalizarán.|
### **Lista de funciones resumidas**
Hay varios tipos de funciones de resumen admitidas por la enumeración {[SubtotalFunction}}:

|**No.**|**Nombre de la función**|**Descripción**|
|:- |:- |:- |
|1|PROMEDIO|Calcula el promedio de los valores.|
|2|CONTAR|Cuenta los valores numéricos en las celdas.|
|3|CONTARA|Cuenta los datos no numéricos en las celdas.|
|4|MÁX.|Calcula el valor más grande.|
|5|MÍN.|Calcula el valor más pequeño.|
|6|PRODUCTO|Calcula el producto de los valores.|
|7|SUMA|Calcula la suma de los valores.|
El siguiente ejemplo genera los subtotales que calculan los valores no numéricos agrupados por la segunda columna en la hoja de trabajo.

**subtotales** 

![todo:imagen_alternativa_texto](group-rows-and-create-subtotal_3.png)



{{< highlight "java" >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[]{ 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **Eliminación de subtotales**
Para eliminar un subtotal, use el método WebWorksheet.RemoveSubtotal. El siguiente ejemplo elimina los subtotales.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **Acerca de la función SUBTOTALES**
El control GridWeb utiliza la función de fórmula SUBTOTAL para calcular el valor del subtotal.

Sintaxis: SUBTOTAL(función_num, ref1, ref2, ...)

function_num es un número que especifica el tipo de función utilizada en el cálculo del subtotal.

|**1**|**PROMEDIO**|
|:- |:- |
|2|CONTAR|
|3|CONTARA|
|4|MÁX.|
|5|MÍN.|
|6|PRODUCTO|
|7|SUMA|
ref1, ref2, son las áreas a subtotalizar. Si ref1, ref2, ... contienen otras funciones de subtotal, las celdas a las que se hace referencia se ignoran para evitar cálculos duplicados.
