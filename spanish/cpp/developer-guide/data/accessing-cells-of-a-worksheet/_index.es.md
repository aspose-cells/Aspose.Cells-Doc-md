---
title: Acceso a las Celdas de una Hoja de Cálculo
type: docs
weight: 10
url: /es/cpp/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Sabemos que todas las hojas de cálculo pueden contener datos que básicamente se almacenan en celdas (con las que está compuesta una hoja de cálculo). Una celda es una parte básica de una hoja de cálculo que se utiliza para construir toda la hoja de cálculo como una secuencia de filas y columnas. Antes de intentar acceder a los datos de una hoja de cálculo, necesitaríamos acceder a sus celdas. Por lo tanto, en este tema, discutiremos algunos enfoques básicos para acceder a las celdas de la hoja de cálculo en tiempo de ejecución utilizando Aspose.Cells.

{{% /alert %}} 
## **Accediendo a las celdas**
Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Excel. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección de [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) que representa todas las celdas en la hoja de cálculo.

Podemos utilizar la colección de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) para acceder a celdas en una hoja de cálculo. Aspose.Cells proporciona tres enfoques básicos para acceder a celdas en una hoja de cálculo:

1. Utilizando el nombre de la celda.
1. Utilizando el índice de fila y columna de una celda.
3. Utilizando un índice de celda en la colección de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)

{{% alert color="primary" %}} 

Hemos mencionado que el tercer enfoque es el más rápido y el primer enfoque es el más lento. La diferencia de rendimiento entre los enfoques es muy pequeña, así que no se preocupe por la degradación del rendimiento, cualquiera que sea el enfoque que utilice.

{{% /alert %}} 
### **Usando el nombre de la celda**
Los desarrolladores pueden acceder a una celda específica pasando su nombre de celda a la colección de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) de la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) como un índice.

Si crea una hoja de cálculo en blanco al principio, el recuento de la colección de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) es cero. Cuando utiliza este enfoque para acceder a una celda, verifica si esta celda existe en la colección o no. Si sí, devuelve el objeto de la celda en la colección; de lo contrario, crea un nuevo objeto de [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), agrega el objeto a la colección de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) y luego devuelve ese objeto. Este enfoque es la forma más fácil de acceder a la celda si está familiarizado con Microsoft Excel, pero es el más lento en comparación con otros enfoques.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
### **Usando el índice de fila y columna de la celda**
Los desarrolladores pueden acceder a una celda específica pasando los índices de su fila y columna a la colección de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) de la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Este enfoque funciona de la misma manera que el primer enfoque.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
## **Acceso al rango de visualización máxima de la hoja de cálculo**
Aspose.Cells permite a los desarrolladores acceder al rango máximo de visualización de una hoja de cálculo. El rango máximo de visualización - el rango de celdas entre la primera y la última celda con contenido - es útil cuando se necesita copiar, seleccionar o mostrar todo el contenido de una hoja de cálculo en una imagen.

Puede acceder al rango máximo de visualización de una hoja de cálculo utilizando el método [MaxDisplayRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) de la colección de [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
