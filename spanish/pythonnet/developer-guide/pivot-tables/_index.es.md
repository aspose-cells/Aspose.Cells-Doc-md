---
title: Insertar tabla dinámica
linktitle: Tablas dinámicas
type: docs
weight: 160
url: /es/python-net/create-pivot-table/
description: Crear y formatear tabla dinámica con Aspose.Cells for Python via .NET.
keywords: Crear tabla dinámica, insertar tabla dinámica, formatear tabla dinámica.
---

## **Crear tabla dinámica**

Es posible utilizar Aspose.Cells for Python via .NET para agregar tablas dinámicas a las hojas de cálculo de forma programática.

### **Modelo de Objeto de Tabla Dinámica**

Aspose.Cells for Python via .NET proporciona un conjunto especial de clases en el espacio de nombres [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) que se utilizan para crear y controlar tablas dinámicas. Estas clases se utilizan para crear y establecer objetos [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/), los componentes básicos de una tabla dinámica. Los objetos son:

- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) representa un campo en un [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) representa una colección de todos los objetos [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) en el [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) representa una TablaDinámica en una hoja de cálculo.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) representa una colección de todos los objetos [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) en una hoja de cálculo.

### **Creación de una tabla dinámica sencilla utilizando Aspose.Cells**

1. Agregue datos a una hoja de cálculo utilizando el método [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) del objeto [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).
   Estos datos se utilizarán como origen de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de cálculo llamando al método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) de la colección [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection), que está encapsulada en el objeto HojaDeCálculo.
1. Acceda al nuevo objeto [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) desde la colección [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) pasando el índice de la TablaDinámica.
1. Utilice alguno de los objetos [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) (explicados anteriormente) para gestionar la tabla dinámica.

Después de ejecutar el código de ejemplo, se agrega una tabla dinámica a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

Al asignar un rango de celdas como origen de datos, el rango debe ir de arriba a la derecha. Por ejemplo, "A1:C3" es válido pero "C3:A1" no lo es.

{{% /alert %}}

## **Temas avanzados**
- [Función de consolidación](/cells/es/python-net/consolidation-function/)
- [Orden personalizado en la tabla dinámica](/cells/es/python-net/custom-sorting-in-pivot-table/)
- [Personalizar la configuración de globalización para la tabla dinámica](/cells/es/python-net/customize-globalization-settings-for-pivot-table/)
- [Deshabilitar las cintas de la tabla dinámica](/cells/es/python-net/disable-pivot-table-ribbons/)
- [Encontrar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal](/cells/es/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Dar formato a la tabla dinámica](/cells/es/python-net/formatting-pivot-table/)
- [Obtener origen de datos de conexión externa de la tabla dinámica](/cells/es/python-net/get-external-connection-data-source-of-pivot-table/)
- [Obtener fecha de actualización de la tabla dinámica e información de quién la actualizó](/cells/es/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Agrupar campos de la tabla dinámica](/cells/es/python-net/group-pivot-fields-in-the-pivot-table/)
- [Analizar registros en caché de la tabla dinámica al cargar el archivo de Excel](/cells/es/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Tabla dinámica y datos de origen](/cells/es/python-net/pivot-table-and-source-data/)
- [Ocultar y ordenar datos de la tabla dinámica](/cells/es/python-net/pivot-table-hide-and-sort-data/)
- [Actualizar y Calcular Tabla Dinámica con Elementos Calculados](/cells/es/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Guardar Tabla Dinámica en archivo ODS](/cells/es/python-net/save-pivot-table-in-ods-file/)
- [Mostrar opción de páginas de filtro de reporte](/cells/es/python-net/show-report-filter-pages-option/)
- [Trabajar con formatos de visualización de datos del Campo de Datos en la Tabla Dinámica](/cells/es/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
