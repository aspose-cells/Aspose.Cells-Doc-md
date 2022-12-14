---
title: Propague la fórmula en la tabla o el objeto de la lista automáticamente al ingresar datos en nuevas filas
type: docs
weight: 980
url: /es/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---
## **Posibles escenarios de uso**
 A veces, desea que una fórmula en su tabla o lista de objetos se propague automáticamente a nuevas filas al ingresar nuevos datos. Este es el comportamiento predeterminado de Microsoft Excel. Para lograr lo mismo con Aspose.Cells, utilice[ListColumn.Fórmula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula)propiedad.
## **Propague la fórmula en la tabla o el objeto de la lista automáticamente al ingresar datos en nuevas filas**
El siguiente código de ejemplo crea un objeto de tabla o lista de tal manera que la fórmula en la columna B se propagará automáticamente a filas nuevas cuando ingrese datos nuevos. Por favor, checa el[archivo de salida de Excel](5472519.xlsx) generado con este código. Si ingresa cualquier número en la celda A3, verá que la fórmula en la celda B2 se propaga automáticamente a la celda B3.
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
