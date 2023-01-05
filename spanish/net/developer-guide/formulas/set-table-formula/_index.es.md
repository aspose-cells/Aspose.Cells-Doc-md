---
title: Propague la fórmula en la tabla o el objeto de la lista automáticamente al ingresar datos en nuevas filas
linktitle: Fórmula de tabla de conjuntos
type: docs
weight: 260
url: /es/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---
## **Posibles escenarios de uso**
 A veces, desea que una fórmula en su tabla o lista de objetos se propague automáticamente a nuevas filas al ingresar nuevos datos. Este es el comportamiento predeterminado de Microsoft Excel. Para lograr lo mismo con Aspose.Cells, utilice[ListColumn.Fórmula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula)propiedad.
## **Propague la fórmula en la tabla o el objeto de la lista automáticamente al ingresar datos en nuevas filas**
El siguiente código de ejemplo crea un objeto de tabla o lista de tal manera que la fórmula en la columna B se propagará automáticamente a filas nuevas cuando ingrese datos nuevos. Por favor, checa el[archivo de salida de Excel](5115469.xlsx) generado con este código. Si ingresa cualquier número en la celda A3, verá que la fórmula en la celda B2 se propaga automáticamente a la celda B3.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
