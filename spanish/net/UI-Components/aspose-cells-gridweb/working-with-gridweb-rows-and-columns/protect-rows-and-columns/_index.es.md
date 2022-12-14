---
title: Proteger Filas y Columnas
type: docs
weight: 60
url: /es/net/protect-rows-and-columns/
---
{{% alert color="primary" %}} 

Este tema analiza algunas técnicas para proteger celdas en filas y columnas de cualquier tipo de acción realizada por los usuarios finales. Los desarrolladores pueden implementar esta protección utilizando dos técnicas: haciendo que las celdas en filas y columnas sean de solo lectura, o restringiendo las opciones del menú contextual de Aspose.Cells.GridWeb. Ambas técnicas se analizan a continuación con la ayuda de ejemplos.

{{% /alert %}} 
## **Protegiendo Cells en filas y columnas**
### **Hacer filas y columnas de solo lectura**
Una forma de proteger filas y columnas en una hoja de trabajo es hacer que las celdas sean de solo lectura. Entonces no pueden ser eliminados por los usuarios finales.

Para hacer filas y columnas de solo lectura:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web.
1. Acceda a GridWorksheet en la colección.
1. Configure las celdas que desee en filas o columnas para que sean de solo lectura.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **Restricción de las opciones del menú contextual**
Aspose.Cells.GridWeb proporciona un menú contextual que los usuarios finales pueden usar para realizar operaciones en el control. El menú proporciona muchas opciones para manipular celdas, filas y columnas.

**Opciones contextuales completas** 

![todo:imagen_alternativa_texto](protect-rows-and-columns_1.png)

Es posible restringir cualquier tipo de operaciones del lado del cliente en filas y columnas restringiendo las opciones disponibles en el menú contextual. Se puede hacer configurando las propiedades EnableClientColumnOperations y EnableClientRowOperations del control GridWeb en falso. También es posible impedir que los usuarios congelen filas y columnas configurando la propiedad EnableClientFreeze del control GridWeb en falso.

**Menú contextual después de restringir las opciones de fila y columna** 

![todo:imagen_alternativa_texto](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
