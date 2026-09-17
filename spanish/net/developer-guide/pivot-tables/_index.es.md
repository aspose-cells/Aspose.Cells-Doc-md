---
title: Insertar tabla dinámica
description: Crear y dar formato a tablas dinámicas de archivos de hojas de cálculo de Excel.
linktitle: Tablas dinámicas
url: /es/net/create-pivot-table/
type: docs
weight: 160
keywords: Crear tabla dinámica, insertar tabla dinámica, formatear tabla dinámica.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
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

{{< app/cells/assistant language="csharp" >}}