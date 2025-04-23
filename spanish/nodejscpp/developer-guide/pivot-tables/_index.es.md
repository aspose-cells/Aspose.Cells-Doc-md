---
title: Insertar tabla dinámica
linktitle: Tablas dinámicas
type: docs
weight: 160
url: /es/nodejs-cpp/create-pivot-table/
description: Crear y dar formato a tablas dinámicas de archivos de hojas de cálculo de Excel.
---

## **Crear tabla dinámica**

Es posible usar Aspose.Cells for Node.js via C++ para agregar tablas dinámicas a hojas de cálculo programáticamente.

### **Modelo de Objeto de Tabla Dinámica**

Aspose.Cells for Node.js via C++ proporciona un conjunto especial de clases que se usan para crear y controlar tablas dinámicas. Estas clases se usan para crear y establecer objetos [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable), los bloques de construcción de una tabla dinámica. Los objetos son:

- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) representa un campo en un [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) representa una colección de todos los objetos [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) en el [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) representa una TablaDinámica en una hoja de cálculo.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) representa una colección de todos los objetos [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) en una hoja de cálculo.

### **Creación de una tabla dinámica sencilla utilizando Aspose.Cells**

1. Agregue datos a una hoja de cálculo utilizando el método [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) del objeto [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).
   Estos datos se utilizarán como origen de datos de la tabla dinámica.
1. Agregue una tabla dinámica a la hoja de cálculo llamando al método [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) de la colección [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection), que está encapsulada en el objeto HojaDeCálculo.
1. Acceda al nuevo objeto [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) desde la colección [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) pasando el índice de la TablaDinámica.
1. Utilice alguno de los objetos [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) (explicados anteriormente) para gestionar la tabla dinámica.

Después de ejecutar el código de ejemplo, se agrega una tabla dinámica a la hoja de cálculo.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-create-pivot-table.js" >}}

{{% alert color="primary" %}}

Al asignar un rango de celdas como origen de datos, el rango debe ir de arriba a la derecha. Por ejemplo, "A1:C3" es válido pero "C3:A1" no lo es.

{{% /alert %}}
