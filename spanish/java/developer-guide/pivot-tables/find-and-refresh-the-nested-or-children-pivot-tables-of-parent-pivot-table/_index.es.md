---
title: Buscar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal
type: docs
weight: 50
url: /es/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **Posibles escenarios de uso**

A veces, una tabla dinámica utiliza otra tabla dinámica como fuente de datos, por lo que se denomina tabla dinámica secundaria o tabla dinámica anidada. Puede encontrar las tablas dinámicas secundarias de una tabla dinámica principal utilizando el[**Tabla dinámica.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()) método.

## **Buscar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal**

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](61767766.xlsx)que contiene tres tablas dinámicas. Las dos tablas dinámicas inferiores son las secundarias de la tabla dinámica anterior, como se muestra en esta captura de pantalla. El código encuentra la tabla dinámica de niños usando el[**Tabla dinámica.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()) y luego los actualiza uno por uno.

![todo:imagen_alternativa_texto](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
