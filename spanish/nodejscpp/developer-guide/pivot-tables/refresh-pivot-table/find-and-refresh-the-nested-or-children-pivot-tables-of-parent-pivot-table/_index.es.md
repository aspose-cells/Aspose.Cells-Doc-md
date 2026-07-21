---
title: Encontrar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal
type: docs
weight: 60
url: /es/nodejs-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Cómo encontrar y actualizar las tablas dinámicas anidadas o hijas de la tabla dinámica principal con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells para Node.js Excel, biblioteca de Excel para Node.js, encontrar y actualizar las tablas dinámicas anidadas o hijas de la tabla dinámica principal usando la biblioteca de Excel Aspose.Cells para Node.js.
---

## **Escenarios de uso posibles**

A veces, una tabla dinámica utiliza otra tabla dinámica como origen de datos, por lo que se le llama tabla dinámica secundaria o tabla dinámica anidada. Puede encontrar las tablas dinámicas secundarias de una tabla dinámica principal utilizando el método [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--).

## **Cómo Encontrar y Actualizar las Tablas Dinámicas Anidadas o Hijas de una Tabla Dinámica Principal**

El siguiente código de muestra carga el [archivo Excel de muestra](61767747.xlsx) que contiene tres tablas dinámicas. Las dos tablas dinámicas inferiores son las hijas de la tabla dinámica anterior, como se muestra en esta captura de pantalla. El código encuentra las tablas dinámicas secundarias utilizando el método [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--) y luego las actualiza una por una.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
