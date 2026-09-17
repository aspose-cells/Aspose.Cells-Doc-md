---
title: Insertar tabla dinámica
description: Crear y formatear tabla dinámica con Aspose.Cells for Python via .NET.
linktitle: Tablas dinámicas
url: /es/python-net/create-pivot-table/
type: docs
weight: 160
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
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

{{< app/cells/assistant language="python-net" >}}