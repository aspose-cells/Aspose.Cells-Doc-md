---
title: Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas
type: docs
weight: 980
url: /es/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Escenarios de uso posibles**
A veces, deseas que una fórmula en tu tabla u objeto Lista se propague automáticamente a nuevas filas al ingresar nuevos datos. Este es el comportamiento predeterminado de Microsoft Excel. Para lograr lo mismo con Aspose.Cells, utiliza la propiedad [Fórmula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula) de ListaColumna.
## **Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas**
El siguiente código de ejemplo crea una Tabla u Objeto Lista de tal manera que la fórmula en la columna B se propague automáticamente a nuevas filas cuando ingreses nuevos datos. Por favor, verifica el [archivo de Excel de salida](5472519.xlsx) generado con este código. Si ingresas un número en la celda A3, verás que la fórmula en la celda B2 se propaga automáticamente a la celda B3.
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
{{< app/cells/assistant language="java" >}}
