---
title: Acceso a Cells de una hoja de trabajo
type: docs
weight: 10
url: /es/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Sabemos que todas las hojas de cálculo pueden contener datos que básicamente se almacenan en celdas (con las que se compone una hoja de cálculo). Una celda es una parte básica de una hoja de trabajo que se utiliza para construir la hoja de trabajo completa como una secuencia de filas y columnas. Antes de intentar acceder a los datos de una hoja de trabajo, necesitaríamos acceder a sus celdas. Entonces, en este tema, discutiremos algunos enfoques básicos para acceder a las celdas de la hoja de trabajo en tiempo de ejecución usando Aspose.Cells.

{{% /alert %}} 
## **Accediendo al Cells**
 Aspose.Cells proporciona una clase[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel. los[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) colección que permite acceder a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. los[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la clase proporciona un[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)colección que representa todas las celdas de la hoja de trabajo.

 Nosotros podemos usar[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)colección para acceder a las celdas de una hoja de cálculo. Aspose.Cells proporciona tres enfoques básicos para acceder a las celdas en una hoja de trabajo:

1. Usando el nombre de la celda.
1. Usando el índice de fila y columna de una celda.
1.  Usando un índice de celda en el[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)recopilación

{{% alert color="primary" %}} 

Hemos mencionado que el tercer enfoque es el más rápido y el primer enfoque es el más lento. La diferencia de rendimiento entre los enfoques es muy pequeña, así que no se preocupe por la degradación del rendimiento, independientemente del enfoque que utilice.

{{% /alert %}} 
### **Usando Cell Nombre**
 Los desarrolladores pueden acceder a cualquier celda específica pasando su nombre de celda al[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) colección de la[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)clase como un índice.

 Si crea una hoja de cálculo en blanco al inicio, el recuento de[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) la recaudación es cero. Cuando utiliza este enfoque para acceder a una celda, verificará si esta celda existe en la colección o no. En caso afirmativo, devuelve el objeto de celda en la colección; de lo contrario, crea una nueva[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) objeto, añade el objeto al[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)colección y luego devuelve ese objeto. Este enfoque es la forma más fácil de acceder a la celda si está familiarizado con Microsoft Excel, pero es el más lento en comparación con otros enfoques.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName.cpp" >}}
### **Uso del índice de filas y columnas del Cell**
 Los desarrolladores pueden acceder a cualquier celda específica pasando los índices de su fila y columna al[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) colección de la[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)clase. Este enfoque funciona de la misma manera que el primer enfoque.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell.cpp" >}}
## **Acceso al rango máximo de visualización de la hoja de trabajo**
Aspose.Cells permite a los desarrolladores acceder al rango máximo de visualización de una hoja de trabajo. El rango de visualización máximo, el rango de celdas entre la primera y la última celda con contenido, es útil cuando necesita copiar, seleccionar o mostrar todo el contenido de una hoja de cálculo en una imagen.

 Puede acceder al rango máximo de visualización de una hoja de trabajo usando[MaxDisplayIRango](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad351277ccaa0a4e1e8cd0693a1e2e988) metodo de la[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)recopilación.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet.cpp" >}}
