---
title: Acceso a las Celdas de una Hoja de Cálculo
type: docs
weight: 10
url: /es/net/accessing-cells-of-a-worksheet/
description: Este artículo muestra cómo obtener el rango de visualización máximo de la hoja de cálculo y acceder a las celdas a través de la API Aspose.Cells for .NET.
keywords: Obtener objeto Cell, Acceso a Celdas, Obtener rango de visualización máximo de la hoja de cálculo. 
---

{{% alert color="primary" %}}

Sabemos que todas las hojas de cálculo pueden contener datos que básicamente se almacenan en celdas (con las que está compuesta una hoja de cálculo). Una celda es una parte básica de una hoja de cálculo que se utiliza para construir toda la hoja de cálculo como una secuencia de filas y columnas. Antes de intentar acceder a los datos de una hoja de cálculo, necesitaríamos acceder a sus celdas. Por lo tanto, en este tema, discutiremos algunos enfoques básicos para acceder a las celdas de la hoja de cálculo en tiempo de ejecución utilizando Aspose.Cells.

{{% /alert %}}

## **Cómo Acceder a las Celdas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección de [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) que representa todas las celdas en la hoja de cálculo.

Podemos usar la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) para acceder a las celdas en una hoja de cálculo. Aspose.Cells proporciona tres enfoques básicos para acceder a las celdas en una hoja de cálculo:

1. Utilizando el nombre de la celda.
1. Utilizando el índice de fila y columna de una celda.
1. Utilizando el índice de una celda en la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)

**IMPORTANTE:** Hemos mencionado que el tercer enfoque es el más rápido y el primer enfoque es el más lento. La diferencia de rendimiento entre los enfoques es muy pequeña, así que no te preocupes por la degradación del rendimiento, sea cual sea el enfoque que uses.

### **Cómo obtener el objeto de celda por su nombre.**

Los desarrolladores pueden acceder a cualquier celda específica pasando su nombre de celda a la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) como un índice.

Si creas una hoja de cálculo en blanco al principio, el recuento de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) es cero. Cuando utilizas este enfoque para acceder a una celda, verificará si esta celda existe en la colección o no. Si sí, devolverá el objeto de la celda en la colección; de lo contrario, creará un nuevo objeto [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell), agregará el objeto a la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) y luego devolverá el objeto. Este enfoque es la forma más sencilla de acceder a la celda si estás familiarizado con Microsoft Excel, pero es el más lento en comparación con otros enfoques.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **Cómo obtener el objeto de celda por el índice de fila y columna de la celda.**

Los desarrolladores pueden acceder a cualquier celda específica pasando los índices de su fila y columna a la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

Este enfoque funciona de la misma manera que el primer enfoque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **Cómo obtener el objeto de celda por el índice de celda en la colección de celdas.**

Una celda también puede ser accedida pasando el índice numérico de la celda a la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

Si utilizas este enfoque para acceder a las celdas, se puede lanzar una excepción si el índice numérico de la celda está fuera de rango. Este enfoque es el más rápido para acceder a las celdas, pero algo importante a tener en cuenta es que si utilizas este enfoque para acceder a un objeto de celda, el índice numérico puede cambiar después de que se agreguen nuevas celdas a la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Los objetos de celda en la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) están internamente ordenados por índices de fila y columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **Cómo obtener el rango de visualización máximo de la hoja de cálculo**

Aspose.Cells permite a los desarrolladores acceder al rango de visualización máximo de una hoja de cálculo. El rango de visualización máximo - el rango de celdas entre la primera y la última celda con contenido - es útil cuando necesitas copiar, seleccionar o mostrar todo el contenido de una hoja de cálculo en una imagen.

Puedes acceder al rango de visualización máximo de una hoja de cálculo usando [**Worksheet.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange). El siguiente código de ejemplo ilustra cómo acceder a la propiedad [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
