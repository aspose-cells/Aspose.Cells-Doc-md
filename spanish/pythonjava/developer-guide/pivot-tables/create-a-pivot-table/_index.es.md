---
title: Crear una tabla dinámica
type: docs
weight: 10
url: /es/python-java/create-a-pivot-table/
---

## **Crear una tabla dinámica**
Aspose.Cells for Python via Java proporciona la función para crear tablas dinámicas. Para crear una tabla dinámica usando Aspose.Cells, sigue los siguientes pasos:

1. Agrega algunos datos a las celdas de la hoja de trabajo utilizando la propiedad [setValue](https://reference.aspose.com/cells/python/asposecells.api/cell#Value) del objeto [Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell). Estos datos se utilizarán como fuente de datos para la tabla dinámica.
1. Agrega una tabla dinámica a la hoja de trabajo llamando al método [add](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)) de [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection), encapsulado en el objeto [Worksheet](https://reference.aspose.com/cells/python/asposecells.api/Worksheet).
1. Accede al objeto [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable) desde [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) pasando el índice de [PivotTable](https://reference.aspose.com/cells/python/asposecells.api/PivotTable).
1. Utiliza cualquiera de los objetos de tabla dinámica (explicados arriba) encapsulados en [PivotTableCollection](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection) para gestionar la tabla dinámica.

El siguiente fragmento de código demuestra cómo crear una tabla dinámica con la API de Aspose.Cells.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
