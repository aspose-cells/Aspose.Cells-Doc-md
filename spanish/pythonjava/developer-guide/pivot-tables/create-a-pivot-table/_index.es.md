---
title: Crear una tabla dinámica
type: docs
weight: 10
url: /es/python-java/create-a-pivot-table/
---
## **Crear una tabla dinámica**
Aspose.Cells para Python a través de Java proporciona la función para crear tablas dinámicas. Para crear una tabla dinámica usando Aspose.Cells, siga los pasos a continuación:

1. Agregue algunos datos a las celdas de la hoja de trabajo usando el[Cell](https://reference.aspose.com/cells/python/asposecells.api/Cell)objetos[valor ajustado](https://reference.aspose.com/cells/python/asposecells.api/cell#Value)propiedad. Estos datos se utilizarán como fuente de datos para la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de trabajo llamando al[Colección de tabla dinámica](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)[agregar](https://reference.aspose.com/cells/python/asposecells.api/pivottablecollection#add\(java.lang.Object\)) método, encapsulado en el[Hoja de cálculo](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)objeto.
1. Acceder al[Tabla dinámica](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)objeto de la[Colección de tabla dinámica](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)al pasar el[Tabla dinámica](https://reference.aspose.com/cells/python/asposecells.api/PivotTable)índice.
1. Utilice cualquiera de los objetos de la tabla dinámica (explicados anteriormente) encapsulados en el[Colección de tabla dinámica](https://reference.aspose.com/cells/python/asposecells.api/PivotTableCollection)objeto para gestionar la tabla dinámica.

El siguiente fragmento de código muestra la creación de una tabla dinámica con Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-CreatePivotTable.py" >}}
