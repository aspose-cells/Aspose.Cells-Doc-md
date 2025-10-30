---
title: Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas
linktitle: Establecer fórmula de tabla
type: docs
weight: 260
url: /es/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Escenarios de uso posibles**
A veces, deseas que una fórmula en tu Tabla o Lista Propiedad se propague automáticamente a nuevas filas al ingresar nuevos datos. Este es el comportamiento predeterminado de Microsoft Excel. Para lograr lo mismo con Aspose.Cells para Python via .NET, por favor usa la propiedad [**ListColumn.formula**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listcolumn/formula).

## **Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas**
El siguiente código de ejemplo crea una tabla u objeto de lista de tal manera que la fórmula en la columna B se propagará automáticamente a las nuevas filas cuando ingreses nuevos datos. Por favor verifica el [archivo de excel de salida](5115469.xlsx) generado con este código. Si ingresas algún número en la celda A3, verás que la fórmula en la celda B2 se propaga automáticamente a la celda B3.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-PropagateFormulaInTable-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
