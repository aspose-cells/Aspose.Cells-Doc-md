---
title: Encontrar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal
type: docs
weight: 60
url: /es/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Escenarios de uso posibles**

A veces, una tabla dinámica utiliza otra tabla dinámica como origen de datos, por lo que se le llama tabla dinámica secundaria o tabla dinámica anidada. Puede encontrar las tablas dinámicas secundarias de una tabla dinámica principal utilizando el método [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren).

## **Encontrar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal**

El siguiente código de muestra carga el [archivo Excel de muestra](61767747.xlsx) que contiene tres tablas dinámicas. Las dos tablas dinámicas inferiores son las hijas de la tabla dinámica anterior, como se muestra en esta captura de pantalla. El código encuentra las tablas dinámicas secundarias utilizando el método [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren) y luego las actualiza una por una.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}
{{< app/cells/assistant language="csharp" >}}
