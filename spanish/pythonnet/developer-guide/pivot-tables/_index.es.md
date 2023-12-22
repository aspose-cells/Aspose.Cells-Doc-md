---
title: Insertar tabla dinámica
linktitle: Tablas dinamicas
type: docs
weight: 160
url: /es/python-net/create-pivot-table/
description: Cree y formatee una tabla dinámica con Aspose.Cells for Python via .NET.
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
---
##  **Crear tabla dinámica**

Es posible utilizar Aspose.Cells for Python via .NET para agregar tablas dinámicas a hojas de cálculo mediante programación.

###  **Modelo de objetos de tabla dinámica**

 Aspose.Cells for Python via .NET proporciona un conjunto especial de clases en el[**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) espacio de nombres que se utilizan para crear y controlar tablas dinámicas. Estas clases se utilizan para crear y establecer[**Tabla dinámica**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)objetos, los componentes básicos de una tabla dinámica. Los objetos son:

- [**Campo dinámico**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) representa un campo en un[**Tabla dinámica**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**Colección de campos dinámicos**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) representa una colección de todos los[**Campo dinámico**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) objetos en el[**Tabla dinámica**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**Tabla dinámica**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)representa una tabla dinámica en una hoja de trabajo.
- [**Colección de tabla dinámica**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) representa una colección de todos los[**Tabla dinámica**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)objetos en una hoja de trabajo.

###  **Crear una tabla dinámica simple usando Aspose.Cells**

1.  Agregue datos a una hoja de trabajo usando el[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) objetos[**poner_valor**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) método.
 Estos datos se utilizarán como fuente de datos de la tabla dinámica.
1.  Agregue una tabla dinámica a la hoja de trabajo llamando al[**Tablas dinamicas**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) colección[**agregar**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str)método, que está encapsulado en el objeto Hoja de trabajo.
1.  Accede a lo nuevo[**Tabla dinámica**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) objeto de la[**Tablas dinamicas**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)colección pasando el índice de la tabla dinámica.
1.  Utilice cualquiera de los[**Tabla dinámica**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)objetos (explicados anteriormente) para administrar la tabla dinámica.

Después de ejecutar el código de ejemplo, se agrega una tabla dinámica a la hoja de trabajo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

Al asignar un rango de celdas como fuente de datos, el rango debe ir de arriba a la izquierda a abajo a la derecha. Por ejemplo, "A1:C3" es válido pero "C3:A1" no lo es.

{{% /alert %}}

##  **Temas avanzados**
- [Función de consolidación](/cells/es/python-net/consolidation-function/)
- [Clasificación personalizada en tabla dinámica](/cells/es/python-net/custom-sorting-in-pivot-table/)
- [Personalizar la configuración de globalización para la tabla dinámica](/cells/es/python-net/customize-globalization-settings-for-pivot-table/)
- [Deshabilitar las cintas de la tabla dinámica](/cells/es/python-net/disable-pivot-table-ribbons/)
- [Busque y actualice las tablas dinámicas anidadas o secundarias de la tabla dinámica principal](/cells/es/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Formato de tabla dinámica](/cells/es/python-net/formatting-pivot-table/)
- [Obtener fuente de datos de conexión externa de la tabla dinámica](/cells/es/python-net/get-external-connection-data-source-of-pivot-table/)
- [Obtenga la fecha de actualización de la tabla dinámica y actualice la información de quién](/cells/es/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Agrupar campos dinámicos en la tabla dinámica](/cells/es/python-net/group-pivot-fields-in-the-pivot-table/)
- [Análisis de registros en caché dinámicos mientras se carga un archivo de Excel](/cells/es/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Tabla dinámica y datos de origen](/cells/es/python-net/pivot-table-and-source-data/)
- [Tabla dinámica Ocultar y ordenar datos](/cells/es/python-net/pivot-table-hide-and-sort-data/)
- [Actualizar y calcular la tabla dinámica con elementos calculados](/cells/es/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Guardar tabla dinámica en el archivo ODS](/cells/es/python-net/save-pivot-table-in-ods-file/)
- [Mostrar opción de páginas de filtro de informes](/cells/es/python-net/show-report-filter-pages-option/)
- [Trabajar con formatos de visualización de datos de DataField en tabla dinámica](/cells/es/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
