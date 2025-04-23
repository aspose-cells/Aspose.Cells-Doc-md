---
title: Insertar tabla dinámica
linktitle: Tablas dinámicas
type: docs
weight: 160
url: /es/net/create-pivot-table/
description: Crear y dar formato a tablas dinámicas de archivos de hojas de cálculo de Excel.
---

## **Crear tabla dinámica**

Es posible usar Aspose.Cells para añadir tablas dinámicas a hojas de cálculo de forma programática.

### **Modelo de Objeto de Tabla Dinámica**

Aspose.Cells proporciona un conjunto especial de clases en el espacio de nombres [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) que se utilizan para crear y controlar tablas dinámicas. Estas clases se utilizan para crear y establecer objetos [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable), los bloques de construcción de una tabla dinámica. Los objetos son:

- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) representa un campo en un [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) representa una colección de todos los objetos [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) en el [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) representa una TablaDinámica en una hoja de cálculo.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) representa una colección de todos los objetos [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) en una hoja de cálculo.

### **Creación de una tabla dinámica sencilla utilizando Aspose.Cells**

1. Agregue datos a una hoja de cálculo utilizando el método [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) del objeto [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).
   Estos datos se utilizarán como origen de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de cálculo llamando al método [**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) de la colección [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection), que está encapsulada en el objeto HojaDeCálculo.
1. Acceda al nuevo objeto [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) desde la colección [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) pasando el índice de la TablaDinámica.
1. Utilice alguno de los objetos [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) (explicados anteriormente) para gestionar la tabla dinámica.

Después de ejecutar el código de ejemplo, se agrega una tabla dinámica a la hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

Al asignar un rango de celdas como origen de datos, el rango debe ir de arriba a la derecha. Por ejemplo, "A1:C3" es válido pero "C3:A1" no lo es.

{{% /alert %}}

## **Temas avanzados**
- [Función de consolidación](/cells/es/net/consolidation-function/)
- [Orden personalizado en la tabla dinámica](/cells/es/net/custom-sorting-in-pivot-table/)
- [Personalizar la configuración de globalización para la tabla dinámica](/cells/es/net/customize-globalization-settings-for-pivot-table/)
- [Deshabilitar las cintas de la tabla dinámica](/cells/es/net/disable-pivot-table-ribbons/)
- [Encontrar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal](/cells/es/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Dar formato a la tabla dinámica](/cells/es/net/formatting-pivot-table/)
- [Obtener origen de datos de conexión externa de la tabla dinámica](/cells/es/net/get-external-connection-data-source-of-pivot-table/)
- [Obtener fecha de actualización de la tabla dinámica e información de quién la actualizó](/cells/es/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Agrupar campos de la tabla dinámica](/cells/es/net/group-pivot-fields-in-the-pivot-table/)
- [Analizar registros en caché de la tabla dinámica al cargar el archivo de Excel](/cells/es/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Tabla dinámica y datos de origen](/cells/es/net/pivot-table-and-source-data/)
- [Ocultar y ordenar datos de la tabla dinámica](/cells/es/net/pivot-table-hide-and-sort-data/)
- [Actualizar y Calcular Tabla Dinámica con Elementos Calculados](/cells/es/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Guardar Tabla Dinámica en archivo ODS](/cells/es/net/save-pivot-table-in-ods-file/)
- [Mostrar opción de páginas de filtro de reporte](/cells/es/net/show-report-filter-pages-option/)
- [Trabajar con formatos de visualización de datos del Campo de Datos en la Tabla Dinámica](/cells/es/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
