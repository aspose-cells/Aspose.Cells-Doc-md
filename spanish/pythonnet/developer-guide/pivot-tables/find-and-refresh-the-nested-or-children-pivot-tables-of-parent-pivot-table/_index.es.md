---
title: Busque y actualice las tablas dinámicas anidadas o secundarias de la tabla dinámica principal
type: docs
weight: 60
url: /es/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Cómo encontrar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal con Aspose.Cells for Python via .NET.
keywords: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table.
---
##  **Posibles escenarios de uso**

veces, una tabla dinámica utiliza otra tabla dinámica como fuente de datos, por lo que se denomina tabla dinámica secundaria o tabla dinámica anidada. Puede encontrar las tablas dinámicas secundarias de una tabla dinámica principal utilizando el[**Tabla dinámica.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)método.

##  **Busque y actualice las tablas dinámicas anidadas o secundarias de la tabla dinámica principal**

 El siguiente código de muestra carga el[archivo de Excel de muestra](61767747.xlsx) que contiene tres tablas dinámicas. Las dos tablas dinámicas inferiores son las hijas de la tabla dinámica anterior, como se muestra en esta captura de pantalla. El código encuentra la tabla dinámica de los niños usando el[**Tabla dinámica.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)método y luego los actualiza uno por uno.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
