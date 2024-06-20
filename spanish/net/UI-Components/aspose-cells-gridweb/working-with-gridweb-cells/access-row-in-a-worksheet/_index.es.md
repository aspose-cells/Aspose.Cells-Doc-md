---
title: Acceder a GridRow en una hoja de cálculo
type: docs
weight: 10
url: /es/net/aspose-cells-gridweb/access-row-in-a-worksheet/
keywords: GridWeb,Fila de cuadrícula,obtener fila
description: Este artículo presenta cómo obtener un objeto de fila (GridRow) en la hoja de cálculo en GridWeb.
---
### Iterar sobre las filas
**Mejores Prácticas**:
Si queremos acceder a todas las filas en la hoja de cálculo una por una, podemos usar **iteradores** para recorrer las filas existentes. Esto **ahorrará memoria**.
~~~C#

// Acceder a una fila usando iteradores
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
compara el siguiente código, esto creará todos los objetos de fila sin importar si es nulo, por lo tanto, causará problemas de memoria, así que por favor **no** uses esta forma
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
sin embargo, puedes utilizar el método CheckRow para verificar si la fila está vacía
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.CheckRow(r);
     if(row==null){
       Console.WriteLine("the row is empty:"+r);
     }else{
       Console.WriteLine(row.Index+" "+row.Height);
     }
 }
~~~
