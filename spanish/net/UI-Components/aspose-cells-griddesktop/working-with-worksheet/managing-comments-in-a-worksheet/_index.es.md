---
title: Gestión de comentarios en una hoja de trabajo
type: docs
weight: 110
url: /es/net/managing-comments-in-a-worksheet/
---
{{% alert color="primary" %}} 

En MS Excel, debe estar familiarizado con la función de comentarios que permite a los usuarios agregar comentarios a las celdas. Esta función es útil en aquellos casos en los que se requiere proporcionar cierta información a los usuarios cuando están a punto de ingresar valores en las celdas. Cada vez que un usuario coloca el cursor del mouse en una celda comentada, aparece un pequeño mensaje emergente para proporcionar información al usuario. Usando Aspose.Cells.GridDesktop, los desarrolladores pueden crear comentarios en las celdas. En este tema, explicaremos el uso de esta función en detalle.

{{% /alert %}} 
## **Adición de comentarios**
Para agregar un comentario a una celda usando Aspose.Cells.GridDesktop, siga los pasos a continuación:

-  Agregue el control Aspose.Cells.GridDesktop a su**Forma**
-  Accede a cualquier deseado**Hoja de cálculo**
-  Agregar**Comentario** a la hoja de trabajo especificando la celda (usando su nombre o número de fila y columna) en la que se agregará el comentario.

 El siguiente código agregará comentarios al**b2** y**b4** celdas de la hoja de trabajo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**Comentarios** colección en el**Hoja de cálculo** objeto proporciona una sobrecarga**Agregar** método. Los desarrolladores pueden usar cualquier versión sobrecargada de**Agregar** método de acuerdo a sus necesidades específicas.
## **Acceso a comentarios**
Para acceder y modificar un comentario existente en la hoja de trabajo, los desarrolladores pueden acceder al comentario desde el**Comentarios** colección de la**Hoja de cálculo** especificando la celda (utilizando el nombre de celda o su ubicación en términos de número de fila y columna) en la que se inserta el comentario. Una vez que se accede al comentario, los desarrolladores pueden modificar su texto en tiempo de ejecución.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **Eliminar comentarios**
 Para eliminar un comentario existente, los desarrolladores simplemente pueden acceder a la hoja de trabajo deseada y luego**Remover** comentario del**Comentarios** colección de la**Hoja de cálculo** especificando la celda (usando su nombre o número de fila y columna) que contiene el comentario.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
