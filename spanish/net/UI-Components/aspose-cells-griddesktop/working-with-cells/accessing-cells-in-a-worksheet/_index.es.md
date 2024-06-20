---
title: Acceder a GridCell en un Libro de Trabajo
type: docs
weight: 10
url: /es/net/aspose-cells-griddesktop/access-cell-in-a-worksheet/
keywords: GridDesktop,GridCell,get cell
description: Este artículo introduce cómo obtener el objeto de celda (GridCell) en la Hoja de cálculo en GridDesktop.
---

{{% alert color="primary" %}} 

Hasta ahora hemos discutido sobre el trabajo con hojas de cálculo, filas y columnas, pero ahora es el momento de profundizar más y hablar sobre las celdas. Así que, en este tema, comenzaríamos nuestra discusión sobre las celdas con una característica básica de acceso a las celdas.

{{% /alert %}} 
## **Acceso a la celda en una hoja de cálculo**
Podemos acceder a cualquier celda de una hoja de cálculo utilizando la API de Aspose.Cells.GridDesktop. Podría haber tres posibles formas de acceder a la celda de la siguiente manera:

- **Usando el nombre de la celda**
- **Usando los índices de fila y columna**
- **Obteniendo la celda enfocada**

Discutamos cada una de las tres formas mencionadas anteriormente una por una.
### **Usando el nombre de la celda**
Todas las celdas en una hoja de cálculo tienen un nombre único. Por ejemplo, A1, A2, B1, B2, etc. Aspose.Cells.GridDesktop permite a los desarrolladores acceder a cualquier celda deseada utilizando su nombre de celda. Todo lo que tenemos que hacer es pasar el nombre de la celda (como un índice) a la colección **Cells** de la **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}

**Aviso**

Acceder a GridCell usando cells[cellName] puede consumir más memoria. Siempre creará un nuevo objeto de celda (GridCell) sin importar si la celda es nula.

### **Usando los índices de fila y columna de la celda**

**Mejores Prácticas**:

Si queremos obtener el valor o el estilo de la celda y no queremos realizar la operación de actualización, podemos usar el método **CheckCell** que devolverá nulo si la celda no existe. Esto **ahorrará memoria**.
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Acceso a una celda usando sus índices de fila y columna
GridCell cell = sheet.Cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~

Una celda en una hoja de cálculo también puede ser reconocida usando su ubicación en términos de sus índices de fila y columna. Todo lo que tenemos que hacer es pasar los índices de fila y columna de la celda a la colección **Cells** de la **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}

**Aviso**

Acceder a GridCell usando cells[rowIndex, columnIndex] puede consumir más memoria. Siempre creará un nuevo objeto celda (GridCell) sin importar si la celda es nula.


### **Obtener Celda Focalizada**
Si no sabes con precisión qué celda debe ser accedida. Entonces Aspose.Cells.GridDesktop también te permite acceder a una celda que actualmente está en el foco de un usuario. Usando esta función, puedes permitir que un usuario seleccione cualquier celda y luego puedes acceder a esa celda en el backend. Simplemente se puede lograr utilizando el método **GetFocusedCell** de la **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}

**Mejores Prácticas**:
### Iterar sobre las celdas
si queremos acceder a todas las celdas en la hoja de cálculo una por una, podemos usar **iteradores** para recorrer las celdas existentes. Esto nos ayudará a **ahorrar memoria**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();

   GridCells cells = sheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
compara el siguiente código que es **malo**, esto creará todos los objetos de celda sin importar si es nulo, por lo tanto causará problemas de memoria, así que por favor **no** uses esta forma
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 for(int r=0;r< sheet.RowsCount;r++)
 {
     for(int c=0;c< sheet.ColumnsCount; c++)
     {
         Console.WriteLine(sheet.Cells[r,c].ToString());
     }
 }
~~~

