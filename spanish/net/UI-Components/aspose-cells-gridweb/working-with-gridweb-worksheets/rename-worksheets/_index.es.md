---
title: Cambiar el nombre de las hojas de trabajo
type: docs
weight: 40
url: /es/net/rename-worksheets/
---
{{% alert color="primary" %}} 

Cambiar el nombre de una hoja de trabajo puede ser muy útil cuando se trabaja con muchas hojas de trabajo en Aspose.Cells.GridWeb y decide cambiar sus nombres para que sean más significativas. Por ejemplo, se puede cambiar el nombre de una hoja de trabajo que contiene una factura a Factura en lugar de Hoja1. Este tema describe esta característica simple pero útil.

{{% /alert %}} 
## **Cambiar el nombre de una hoja de trabajo**
Todas las hojas de trabajo contienen una propiedad Nombre que permite a los desarrolladores acceder o modificar los nombres de las hojas de trabajo. Para cambiar el nombre de una hoja de trabajo:

1. Acceda a una hoja de trabajo desde GridWorksheetCollection.
1. Cambiar el nombre de la hoja de cálculo seleccionada.



{{% alert color="primary" %}} 

 Para obtener más detalles sobre cómo acceder a las hojas de trabajo en Aspose.Cells.GridWeb, consulte[Acceder a hojas de trabajo](/cells/es/net/access-worksheets/).

{{% /alert %}} 

Antes de ejecutar el código, la hoja de cálculo tiene un nombre predeterminado, como Hoja1.

**Archivo de entrada: una hoja de trabajo con un nombre predeterminado Hoja1** 

![todo:imagen_alternativa_texto](rename-worksheets_1.png)

Después de ejecutar el código, la hoja de trabajo se renombra como Estudiantes.

**Salida: la hoja de trabajo se renombra Estudiantes** 

![todo:imagen_alternativa_texto](rename-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RenameWorksheets.aspx-RenameWorksheet.cs" >}}
