---
title: Acceder a la celda de la hoja de cálculo
type: docs
weight: 10
url: /es/net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: Este artículo presenta cómo obtener la celda (GridCell) en GridWeb.
---

{{% alert color="primary" %}} 

Este tema discute las celdas, examinando la característica más básica de Aspose.Cells.GridWeb: acceder a las celdas.

{{% /alert %}} 
## **Acceder a las celdas en una hoja de cálculo**
Cada hoja de cálculo contiene una propiedad con el nombre de Cells que es en realidad una colección de objetos GridCell donde un objeto GridCell representa una celda en Aspose.Cells.GridWeb. Es posible acceder a cualquier celda usando Aspose.Cells.GridWeb. Se discuten a continuación dos métodos preferidos, cada uno de los cuales se discute a continuación.


### **Usando el nombre de la celda**
Todas las celdas tienen un nombre único. Por ejemplo, A1, A2, B1, B2, etc. Aspose.Cells.GridWeb permite a los desarrolladores acceder a cualquier celda deseada utilizando el nombre de la celda. Simplemente pase el nombre de la celda (como un índice) a la colección Cells de GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


**Aviso**

Acceder a GridCell usando cells[cellName] puede consumir más memoria. Siempre creará un nuevo objeto de celda (GridCell) sin importar si la celda es nula.


### **Usando los índices de fila y columna**


Una celda también puede ser reconocida por su ubicación en términos de índices de fila y columna. Simplemente pase los índices de fila y columna de una celda a la colección Cells de GridWorksheet. Este enfoque es más rápido que el anterior.

**Mejores Prácticas**:

Si queremos obtener el valor o el estilo de la celda y no queremos realizar la operación de actualización, podemos usar el método **CheckCell** que devolverá nulo si la celda no existe. Esto **ahorrará memoria**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   GridCell cell = cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}



**Mejores Prácticas**:
### Iterar sobre las celdas
si queremos acceder a todas las celdas en la hoja de cálculo una por una, podemos usar **iteradores** para recorrer las celdas existentes. Esto nos ayudará a **ahorrar memoria**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
compara el siguiente código que es **malo**, esto creará todos los objetos de celda sin importar si es nulo, por lo tanto causará problemas de memoria, así que por favor **no** uses esta forma
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r< cells.MaxRow;r++)
 {
     for(int c=0;c< cells.MaxColumn; c++)
     {
         Console.WriteLine(cells[r,c].ToString());
     }
 }
~~~
