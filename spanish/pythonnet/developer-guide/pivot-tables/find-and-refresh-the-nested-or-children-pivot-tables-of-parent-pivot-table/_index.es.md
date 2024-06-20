---
title: Encontrar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal
type: docs
weight: 60
url: /es/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Cómo encontrar y actualizar las Tablas Dinámicas anidadas o hijas de una Tabla Dinámica principal con Aspose.Cells for Python via .NET
keywords: Aspose.Cells for Python Excel, biblioteca de Python de Excel, Encontrar y Actualizar las Tablas Dinámicas Anidadas o Hijas de la Tabla Dinámica Principal Usando la Biblioteca Aspose.Cells para Python de Excel
---

## **Escenarios de uso posibles**

A veces, una tabla dinámica utiliza otra tabla dinámica como origen de datos, por lo que se le llama tabla dinámica secundaria o tabla dinámica anidada. Puede encontrar las tablas dinámicas secundarias de una tabla dinámica principal utilizando el método [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#).

## **Cómo Encontrar y Actualizar las Tablas Dinámicas Anidadas o Hijas de una Tabla Dinámica Principal**

El siguiente código de muestra carga el [archivo Excel de muestra](61767747.xlsx) que contiene tres tablas dinámicas. Las dos tablas dinámicas inferiores son las hijas de la tabla dinámica anterior, como se muestra en esta captura de pantalla. El código encuentra las tablas dinámicas secundarias utilizando el método [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#) y luego las actualiza una por una.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
