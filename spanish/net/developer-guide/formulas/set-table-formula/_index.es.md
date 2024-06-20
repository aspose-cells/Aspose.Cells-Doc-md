---
title: Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas
linktitle: Establecer fórmula de tabla
type: docs
weight: 260
url: /es/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Escenarios de uso posibles**
A veces, quieres que una fórmula en tu tabla u objeto de lista se propague automáticamente a las nuevas filas al ingresar nuevos datos. Este es el comportamiento predeterminado de Microsoft Excel. Para lograr lo mismo con Aspose.Cells, por favor utiliza la propiedad [ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula).
## **Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas**
El siguiente código de ejemplo crea una tabla u objeto de lista de tal manera que la fórmula en la columna B se propagará automáticamente a las nuevas filas cuando ingreses nuevos datos. Por favor verifica el [archivo de excel de salida](5115469.xlsx) generado con este código. Si ingresas algún número en la celda A3, verás que la fórmula en la celda B2 se propaga automáticamente a la celda B3.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
