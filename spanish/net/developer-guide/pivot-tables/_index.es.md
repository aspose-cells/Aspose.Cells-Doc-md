---
title: Insertar tabla dinámica
linktitle: Tablas dinamicas
type: docs
weight: 160
url: /es/net/create-pivot-table/
description: Cree y formatee tablas dinámicas de archivos de hojas de cálculo de Excel.
---
## **Crear tabla dinámica**

Es posible usar Aspose.Cells para agregar tablas dinámicas a hojas de cálculo mediante programación.

### **Modelo de objetos de tabla dinámica**

Aspose.Cells proporciona un conjunto especial de clases en el[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) espacio de nombres que se utilizan para crear y controlar tablas dinámicas. Estas clases se utilizan para crear y establecer[**Tabla dinámica**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)objetos, los componentes básicos de una tabla dinámica. Los objetos son:

- [**campo pivote**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) representa un campo en un[**Tabla dinámica**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) representa una colección de todos los[**campo pivote**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) objetos en el[**Tabla dinámica**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**Tabla dinámica**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)representa una tabla dinámica en una hoja de cálculo.
- [**Colección de tabla dinámica**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) representa una colección de todos los[**Tabla dinámica**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)objetos en una hoja de trabajo.

### **Crear una tabla dinámica simple usando Aspose.Cells**

1. Agregar datos a una hoja de trabajo usando el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) objetos[**poner valor**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) método.
 Estos datos se utilizarán como fuente de datos de la tabla dinámica.
1.  Agregue una tabla dinámica a la hoja de trabajo llamando al[**Tablas dinamicas**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) colección[**agregar**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)método, que está encapsulado en el objeto Worksheet.
1.  Accede al nuevo[**Tabla dinámica**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) objeto de la[**Tablas dinamicas**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)colección pasando el índice de la tabla dinámica.
1.  Usa cualquiera de los[**Tabla dinámica**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)objetos (explicados anteriormente) para administrar la tabla dinámica.

Después de ejecutar el código de ejemplo, se agrega una tabla dinámica a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

Al asignar un rango de celdas como fuente de datos, el rango debe ir de arriba a la izquierda a abajo a la derecha. Por ejemplo, "A1:C3" es válido pero "C3:A1" no lo es.

{{% /alert %}}

## **Temas avanzados**
- [Función de consolidación](/cells/es/net/consolidation-function/)
- [Clasificación personalizada en la tabla dinámica](/cells/es/net/custom-sorting-in-pivot-table/)
- [Personalizar la configuración de globalización para la tabla dinámica](/cells/es/net/customize-globalization-settings-for-pivot-table/)
- [Deshabilitar cintas de tabla dinámica](/cells/es/net/disable-pivot-table-ribbons/)
- [Buscar y actualizar las tablas dinámicas anidadas o secundarias de la tabla dinámica principal](/cells/es/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Formato de tabla dinámica](/cells/es/net/formatting-pivot-table/)
- [Obtener fuente de datos de conexión externa de tabla dinámica](/cells/es/net/get-external-connection-data-source-of-pivot-table/)
- [Obtenga la fecha de actualización de la tabla dinámica y actualice la información de quién](/cells/es/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Agrupar campos dinámicos en la tabla dinámica](/cells/es/net/group-pivot-fields-in-the-pivot-table/)
- [Análisis de registros en caché de pivote al cargar un archivo de Excel](/cells/es/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Tabla dinámica y datos de origen](/cells/es/net/pivot-table-and-source-data/)
- [Tabla dinámica Ocultar y ordenar datos](/cells/es/net/pivot-table-hide-and-sort-data/)
- [Actualizar y calcular tabla dinámica con elementos calculados](/cells/es/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Guardar tabla dinámica en el archivo ODS](/cells/es/net/save-pivot-table-in-ods-file/)
- [Mostrar opción de páginas de filtro de informe](/cells/es/net/show-report-filter-pages-option/)
- [Trabajar con formatos de visualización de datos de DataField en Pivot Table](/cells/es/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
