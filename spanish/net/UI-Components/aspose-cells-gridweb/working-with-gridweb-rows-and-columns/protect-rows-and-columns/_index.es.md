---
title: Proteger Filas y Columnas
type: docs
weight: 60
url: /es/net/aspose-cells-gridweb/protect-rows-and-columns/
keywords: GridWeb,proteger
description: Este artículo presenta cómo proteger filas y columnas en GridWeb.
---

{{% alert color="primary" %}} 

Este tema discute algunas técnicas para proteger celdas en filas y columnas de cualquier tipo de acción realizada por los usuarios finales. Los desarrolladores pueden implementar esta protección utilizando dos técnicas: haciendo que las celdas en filas y columnas sean de solo lectura, o restringiendo las opciones del menú contextual de Aspose.Cells.GridWeb. Ambas técnicas se discuten a continuación con la ayuda de ejemplos.

{{% /alert %}} 
## **Proteger Celdas en Filas y Columnas**
### **Hacer Filas y Columnas de Solo Lectura**
Una forma de proteger filas y columnas en una hoja de cálculo es hacer que las celdas sean de solo lectura. Entonces no pueden ser eliminadas por los usuarios finales.

Para hacer filas y columnas de solo lectura:

1. Agregue el control Aspose.Cells.GridWeb a un Formulario Web.
1. Acceda a la cuadrícula de trabajo (GridWorksheet) en la colección.
1. Establezca las celdas deseadas en filas o columnas como de solo lectura.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **Restricción de las opciones del menú contextual**
Aspose.Cells.GridWeb proporciona un menú contextual que los usuarios finales pueden utilizar para realizar operaciones en el control. El menú proporciona muchas opciones para manipular celdas, filas y columnas.

**Opciones contextuales completas** 

![todo:image_alt_text](protect-rows-and-columns_1.png)

Es posible restringir cualquier tipo de operación del lado del cliente en filas y columnas al restringir las opciones disponibles en el menú contextual. Se puede hacer configurando las propiedades EnableClientColumnOperations y EnableClientRowOperations del control GridWeb en falso. También es posible restringir a los usuarios congelar filas y columnas configurando la propiedad EnableClientFreeze del control GridWeb en falso.

**Menú contextual después de restringir las opciones de filas y columnas** 

![todo:image_alt_text](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
