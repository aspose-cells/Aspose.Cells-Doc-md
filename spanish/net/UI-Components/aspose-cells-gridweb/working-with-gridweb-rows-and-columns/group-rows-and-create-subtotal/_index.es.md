---
title: Agrupar filas y crear subtotales
type: docs
weight: 70
url: /es/net/aspose-cells-gridweb/group-rows-and-create-subtotal/
keywords: GridWeb,subtotal,group,ungroup
description: Este artículo introduce cómo agrupar/desagrupar filas/columnas y cómo trabajar con subtotales en GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb puede crear un esquema para sus datos. Esto le permite mostrar y ocultar niveles de detalle haciendo clic en los símbolos de esquema "+" y "-" para mostrar solo las filas que proporcionan resúmenes o encabezados de secciones en una hoja de cálculo. Puede usar los símbolos para ver detalles bajo un resumen o encabezado individual.

Al agrupar filas, es importante seleccionar solo las filas de detalle que conforman el grupo. No incluya la fila de resumen relacionada. Por ejemplo, si la fila 6 contiene totales para los datos en la fila 3 a la 5, seleccione solo la fila 3 a la 5 para definir el grupo. El control Aspose.Cells.GridWeb muestra los símbolos **mostrar detalle** (+) y **ocultar detalle** (-) junto a los encabezados de fila especificando los grupos en la hoja de cálculo.

Aspose.Cells.GridWeb también le permite crear subtotales basados en cualquier campo de datos. Un subtotal no necesariamente es una suma: puede ser un promedio, conteo, mínimo, máximo u otro cálculo estadístico.

Este tema discute cómo agrupar filas y crear subtotales utilizando la API de Aspose.Cells.GridWeb. Los desarrolladores pueden agrupar filas con cualquier nivel de anidamiento y crear subtotales fácilmente.

{{% /alert %}} 
## **Agrupación de filas**
Para agrupar un número específico de filas:

1. Agregue el control Aspose.Cells.GridWeb a un Formulario Web.
1. Acceder a una hoja de cálculo.
1. Seleccione el número deseado de celdas en filas.
1. Agrupe las filas.

Cuando las filas están agrupadas, se muestra un botón de expandir/contraer en la parte superior de la Línea de Resumen de las filas. Puede cambiar la configuración de dirección. La propiedad WebWorksheet.IsSummaryRowBelow es una propiedad booleana. Establézcala en false (predeterminado) y la fila de resumen estará arriba de las filas de detalle. Establézcala en true y la fila de resumen estará debajo de las filas de detalle. Haga clic en el botón de expandir/contraer para expandir o contraer las filas agrupadas.

El siguiente ejemplo agrupa las filas desde la 2da fila hasta la 10ma fila.

**Agrupar filas** 

![todo:image_alt_text](group-rows-and-create-subtotal_1.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **Agrupación de Filas Anidadas**
Puede crear niveles de organización al agrupar un conjunto de filas. Puede agrupar filas entre las filas agrupadas. El siguiente ejemplo muestra la anidación de filas agrupadas.

**Agrupar filas** 

![todo:image_alt_text](group-rows-and-create-subtotal_2.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **Proceso interno: ¿Cómo funciona el control?**
Cada fila de la hoja tiene un número de esquema. El valor predeterminado del número de esquema es cero. Cada vez que agrupa las filas, el número de esquema aumenta en 1. Puede obtener el número de esquema llamando al método GridWorksheet.Cells.GetRowOutlineLevel().
## **Desagrupar Filas**
Aspose.Cells.GridWeb le permite desagrupar filas agrupadas.

Para desagrupar un número específico de filas:

1. Seleccione un número de celdas en las filas de la hoja de cálculo para desagrupar.
1. Desagrupe las filas.

El siguiente ejemplo desagrupa las filas desde la segunda fila hasta la décima fila.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

Cuando llama al método GridWorksheet.Cells.UngroupRows(), el número de esquema de las filas agrupadas se establece en cero.

{{% /alert %}} 
## **Creación de Subtotal**
La función de subtotal del control puede agrupar las filas en la hoja con una columna especificada y calcular el resumen de las columnas. Aspose.Cells.GridWeb puede calcular automáticamente los valores de subtotales para una lista. Al implementar subtotales, el control esquematiza la lista para que pueda mostrar y ocultar las filas de detalles para cada subtotal. Antes de agregar subtotales, ordene en el campo que desea subtotal. Para crear subtotales, use cualquier versión del método sobrecargado WebWorksheet.CreateSubtotal.



{{< highlight java >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[] subtotalColumnIndexList

);

{{< /highlight >}}
### **Lista de Parámetros**

|**Núm.**|**Nombre del Parámetro**|**Descripción**|
| :- | :- | :- |
|1|columnNameRowIndex|El índice de fila de la fila de nombre de columna.|
|2|dataRows|El número de filas de datos.|
|3|groupByColumnIndex|El índice de columna de la columna a agrupar.|
|4|subtotalFunction|El tipo de enumeración de función de subtotal.|
|5|subtotalColumnIndexList|Los índices de columna a subtotalizar.|
### **Lista de Funciones de Resumen**
Hay varios tipos de funciones de resumen admitidas por la enumeración {[SubtotalFunction}}:

|**Núm.**|**Nombre de la Función**|**Descripción**|
| :- | :- | :- |
|1|AVERAGE|Calcula el promedio de los valores.|
|2|COUNT|Cuenta los valores numéricos en las celdas.|
|3|COUNTA|Cuenta los datos no numéricos en las celdas.|
|4|MAX|Calcula el valor más grande.|
|5|MIN|Calcula el valor más pequeño.|
|6|PRODUCT|Calcula el producto de los valores.|
|7|SUM|Calcule la suma de los valores.|
El siguiente ejemplo genera los subtotales que calculan los valores no numéricos agrupados por la segunda columna en la hoja de trabajo.

**Subtotales** 

![todo:image_alt_text](group-rows-and-create-subtotal_3.png)



{{< highlight java >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[] { 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **Eliminación de Subtotal**
Para eliminar un subtotal, utilice el método WebWorksheet.RemoveSubtotal. El siguiente ejemplo elimina los subtotales.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **Acerca de la función SUBTOTAL**
El control GridWeb hace uso de la función de fórmula SUBTOTAL para calcular el valor del subtotal.

Sintaxis: SUBTOTAL(núm_función, ref1, ref2, ...)

núm_función es un número que especifica el tipo de función utilizada en el cálculo del subtotal.

|**1**|**MEDIA**|
| :- | :- |
|2|COUNT|
|3|COUNTA|
|4|MAX|
|5|MIN|
|6|PRODUCT|
|7|SUM|
ref1, ref2, son las áreas que se deben subtotalizar. Si ref1, ref2, ... contienen otras funciones de subtotal, las celdas referenciadas se ignoran para evitar el cálculo duplicado.
