---
title: Gestión de Comentarios en una Hoja de Cálculo
type: docs
weight: 110
url: /es/net/aspose-cells-griddesktop/manage-comments-in-a-worksheet/
keywords: GridDesktop, comentario, comentarios
description: Este artículo presenta cómo trabajar con comentarios en GridDesktop.
---

{{% alert color="primary" %}} 

En MS Excel, es posible que esté familiarizado con la función de comentarios que permite a los usuarios agregar comentarios a las celdas. Esta función es útil en aquellos casos en que se requiere proporcionar información a los usuarios cuando están a punto de ingresar valores en las celdas. Cada vez que un usuario coloca el cursor del mouse sobre una celda comentada, aparece un pequeño mensaje emergente para proporcionar alguna información al usuario. Usando Aspose.Cells.GridDesktop, los desarrolladores pueden crear comentarios en las celdas. En este tema, explicaremos detalladamente el uso de esta función.

{{% /alert %}} 
## **Añadir Comentarios**
Para agregar un comentario a una celda utilizando Aspose.Cells.GridDesktop, siga los pasos a continuación:

- Agregar el control Aspose.Cells.GridDesktop a su **Formulario**
- Acceda a cualquier **Hoja de Cálculo** deseada
- Agregar un **Comentario** a la hoja de cálculo especificando la celda (usando su nombre o número de fila y columna) en la que se añadirá el comentario.

El código a continuación agregará comentarios a las celdas **b2** y **b4** de la hoja de cálculo.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


La colección de **Comentarios** en el objeto **Hoja de Cálculo** proporciona un método **Agregar** sobrecargado. Los desarrolladores pueden utilizar cualquier versión sobrecargada del método **Agregar** según sus necesidades específicas.
## **Acceso a Comentarios**
Para acceder y modificar un comentario existente en la hoja de cálculo, los desarrolladores pueden acceder al comentario desde la colección **Comentarios** de la **Hoja de Cálculo** especificando la celda (usando el nombre de la celda o su ubicación en términos de números de fila y columna) en la que se inserta el comentario. Una vez que se accede al comentario, los desarrolladores pueden modificar su texto en tiempo de ejecución.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **Eliminación de Comentarios**
Para eliminar un comentario existente, los desarrolladores pueden simplemente acceder a la hoja de cálculo deseada y luego eliminar el comentario de la colección **Comentarios** de la **Hoja de Cálculo** especificando la celda (usando su nombre o número de fila y columna) que contiene el comentario.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
