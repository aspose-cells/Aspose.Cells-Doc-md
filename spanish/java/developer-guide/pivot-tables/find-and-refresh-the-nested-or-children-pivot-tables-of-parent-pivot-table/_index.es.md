---
title: Encontrar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal
type: docs
weight: 50
url: /es/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Escenarios de uso posibles**

A veces, una tabla dinámica utiliza otra tabla dinámica como origen de datos, por lo que se le llama tabla dinámica secundaria o tabla dinámica anidada. Puede encontrar las tablas dinámicas secundarias de una tabla dinámica principal utilizando el método [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--).

## **Encontrar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal**

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](61767766.xlsx) que contiene tres tablas dinámicas. Las dos tablas dinámicas inferiores son las secundarias de la tabla dinámica superior como se muestra en esta captura de pantalla. El código encuentra las tablas dinámicas secundarias utilizando el método [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--) y luego las actualiza una por una.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
{{< app/cells/assistant language="java" >}}
