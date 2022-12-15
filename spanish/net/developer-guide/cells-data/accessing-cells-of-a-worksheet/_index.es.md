---
title: Acceso a Cells de una hoja de trabajo
type: docs
weight: 10
url: /es/net/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}}

Sabemos que todas las hojas de cálculo pueden contener datos que básicamente se almacenan en celdas (con las que se compone una hoja de cálculo). Una celda es una parte básica de una hoja de trabajo que se utiliza para construir la hoja de trabajo completa como una secuencia de filas y columnas. Antes de intentar acceder a los datos de una hoja de trabajo, necesitaríamos acceder a sus celdas. Entonces, en este tema, discutiremos algunos enfoques básicos para acceder a las celdas de la hoja de trabajo en tiempo de ejecución usando Aspose.Cells.

{{% /alert %}}

## **Accediendo al Cells**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la clase contiene un[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección que representa todas las celdas de la hoja de cálculo.

 Nosotros podemos usar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección para acceder a las celdas de una hoja de cálculo. Aspose.Cells proporciona tres enfoques básicos para acceder a las celdas en una hoja de cálculo:

1. Usando el nombre de la celda.
1. Usando el índice de fila y columna de una celda.
1.  Usando un índice de celda en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)recopilación

**IMPORTANTE:**Hemos mencionado que el tercer enfoque es el más rápido y el primer enfoque es el más lento. La diferencia de rendimiento entre los enfoques es muy pequeña, así que no se preocupe por la degradación del rendimiento, independientemente del enfoque que utilice.

### **Usando Cell Nombre**

 Los desarrolladores pueden acceder a cualquier celda específica pasando su nombre de celda al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección de la[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)clase como un índice.

 Si crea una hoja de cálculo en blanco al principio, el recuento de[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)la recaudación es cero. Cuando utiliza este enfoque para acceder a una celda, verificará si esta celda existe en la colección o no. En caso afirmativo, devuelve el objeto de celda en la colección; de lo contrario, crea una nueva[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) objeto, añade el objeto al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección y luego devuelve el objeto. Este enfoque es la forma más fácil de acceder a la celda si está familiarizado con Microsoft Excel, pero es el más lento en comparación con otros enfoques.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

### **Uso del índice de filas y columnas del Cell**

 Los desarrolladores pueden acceder a cualquier celda específica pasando los índices de su fila y columna al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección de la[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)clase.

Este enfoque funciona de la misma manera que el primer enfoque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

### **Uso del índice Cell en la colección Cells**

 También se puede acceder a una celda pasando el índice numérico de la celda al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)recopilación.

 Si utiliza este enfoque para acceder a las celdas, se puede generar una excepción si el índice numérico de la celda está fuera de rango. Este enfoque es el más rápido para acceder a las celdas, pero algo importante que debe saber es que si usa este enfoque para acceder a un objeto de celda, el índice numérico puede cambiar después de agregar nuevas celdas al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) recopilación. Los objetos de celda en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección se ordenan internamente por índices de fila y columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

## **Acceso al rango máximo de visualización de la hoja de trabajo**

Aspose.Cells permite a los desarrolladores acceder al rango máximo de visualización de una hoja de trabajo. El rango de visualización máximo, el rango de celdas entre la primera y la última celda con contenido, es útil cuando necesita copiar, seleccionar o mostrar todo el contenido de una hoja de trabajo en una imagen.

 Puede acceder al rango máximo de visualización de una hoja de trabajo usando[**Hoja de trabajo.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . El siguiente código de ejemplo ilustra cómo acceder a la[**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
