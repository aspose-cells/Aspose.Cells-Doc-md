---
title: Acceso a las Celdas de una Hoja de Cálculo
type: docs
weight: 10
url: /es/nodejs-cpp/accessing-cells-of-a-worksheet/
description: Este artículo muestra cómo obtener el rango máximo de visualización de la hoja de trabajo y acceder a las celdas a través de la API Aspose.Cells for Node.js via C++.
keywords: Obtener objeto Cell, Acceso a Celdas, Obtener rango de visualización máximo de la hoja de cálculo. 
---

{{% alert color="primary" %}}

Sabemos que todas las hojas de trabajo pueden contener datos que se almacenan básicamente en celdas (con las cuales se compone una hoja de trabajo). Una celda es una parte básica de una hoja de trabajo que se usa para construir toda la hoja de trabajo como una secuencia de filas y columnas. Antes de intentar acceder a los datos de una hoja, necesitamos acceder a sus celdas. Por lo tanto, en este tema, discutiremos algunos enfoques básicos para acceder a las celdas de la hoja de trabajo en tiempo de ejecución usando Aspose.Cells for Node.js via C++.

{{% /alert %}}

## **Cómo Acceder a las Celdas**

Aspose.Cells for Node.js via C++ proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) que permite acceder a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) que representa todas las celdas en la hoja de trabajo.

Podemos usar la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) para acceder a las celdas en una hoja de trabajo. Aspose.Cells for Node.js via C++ proporciona tres enfoques básicos para acceder a las celdas en una hoja de trabajo:

1. Utilizando el nombre de la celda.
1. Utilizando el índice de fila y columna de una celda.
1. Utilizando el índice de una celda en la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)

**IMPORTANTE:** Hemos mencionado que el tercer enfoque es el más rápido y el primer enfoque es el más lento. La diferencia de rendimiento entre los enfoques es muy pequeña, así que no te preocupes por la degradación del rendimiento, sea cual sea el enfoque que uses.

### **Cómo obtener el objeto de celda por su nombre.**

Los desarrolladores pueden acceder a cualquier celda específica pasando su nombre de celda a la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) como un índice.

Si creas una hoja de cálculo en blanco al principio, el recuento de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) es cero. Cuando utilizas este enfoque para acceder a una celda, verificará si esta celda existe en la colección o no. Si sí, devolverá el objeto de la celda en la colección; de lo contrario, creará un nuevo objeto [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell), agregará el objeto a la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) y luego devolverá el objeto. Este enfoque es la forma más sencilla de acceder a la celda si estás familiarizado con Microsoft Excel, pero es el más lento en comparación con otros enfoques.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellName-1.js" >}}

### **Cómo obtener el objeto de celda por el índice de fila y columna de la celda.**

Los desarrolladores pueden acceder a cualquier celda específica pasando los índices de su fila y columna a la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) de la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

Este enfoque funciona de la misma manera que el primer enfoque.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.js" >}}

### **Cómo obtener el objeto de celda por el índice de celda en la colección de celdas.**

Una celda también puede ser accedida pasando el índice numérico de la celda a la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).

Si utilizas este enfoque para acceder a las celdas, se puede lanzar una excepción si el índice numérico de la celda está fuera de rango. Este enfoque es el más rápido para acceder a las celdas, pero algo importante a tener en cuenta es que si utilizas este enfoque para acceder a un objeto de celda, el índice numérico puede cambiar después de que se agreguen nuevas celdas a la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Los objetos de celda en la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) están internamente ordenados por índices de fila y columna.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.js" >}}

## **Cómo obtener el rango de visualización máximo de la hoja de cálculo**

Aspose.Cells for Node.js via C++ para Node.js vía C++ permite a los desarrolladores acceder al rango máximo de visualización de una hoja de trabajo. El rango de visualización máximo, es decir, el rango de celdas entre la primera y la última con contenido, es útil cuando necesitas copiar, seleccionar o mostrar todo el contenido de una hoja en una imagen.

Puedes acceder al rango de visualización máximo de una hoja de cálculo usando [**Cells.getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--). El siguiente código de ejemplo ilustra cómo acceder a la propiedad [**getMaxDisplayRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
