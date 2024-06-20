---
title: Acceder a GridRow en una hoja de cálculo
type: docs
weight: 10
url: /es/net/aspose-cells-griddesktop/access-row-in-a-worksheet/
keywords: GridDesktop,GridRow,obtener fila
description: Este artículo presenta cómo obtener el objeto de fila (GridRow) en la hoja de cálculo en GridDesktop.
---
### Iterar sobre las filas
**Mejores Prácticas**:
Si queremos acceder a todas las filas en la hoja de cálculo una por una, podemos usar **iteradores** para recorrer las filas existentes. Esto **ahorrará memoria**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Acceder a una fila usando iteradores
   GridCells cells = sheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
compara el siguiente código, esto creará todos los objetos de fila sin importar si es nulo, por lo tanto, causará problemas de memoria, así que por favor **no** uses esta forma
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
sin embargo, puedes utilizar el método CheckRow para verificar si la fila está vacía
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.CheckRow(r);
     if(row==null){
       Console.WriteLine("the row is empty:"+r);
     }else{
       Console.WriteLine(row.Index+" "+row.Height);
     }
 }
~~~
