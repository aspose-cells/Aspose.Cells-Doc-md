---
title: Administrar comentarios en la hoja de trabajo
type: docs
weight: 110
url: /es/net/manage-comments-in-worksheet/
---
{{% alert color="primary" %}} 

Este tema trata sobre la adición, el acceso y la eliminación de comentarios de las hojas de trabajo. Los comentarios son útiles para agregar notas o información útil para los usuarios que trabajarán con la hoja. Los desarrolladores tienen la flexibilidad de agregar comentarios a cualquier celda de la hoja de trabajo.

{{% /alert %}} 
## **Trabajar con comentarios**
### **Adición de comentarios**
Para agregar un comentario a la hoja de trabajo, siga los pasos a continuación:

1. Agregue el control Aspose.Cells.GridWeb al formulario web.
1. Acceda a la hoja de trabajo a la que está agregando comentarios.
1. Agregar un comentario a una celda.
1. Establezca una nota para el nuevo comentario.

**Se ha añadido un comentario a la hoja de cálculo.** 

![todo:imagen_alternativa_texto](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Acceso a comentarios**
Para acceder a un comentario:

1. Accede a la celda que contiene el comentario.
1. Obtenga la referencia de la celda.
1. Pase la referencia a la colección de comentarios para acceder al comentario.
1. Ahora es posible modificar las propiedades del comentario.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Eliminar comentarios**
Para eliminar un comentario:

1. Acceda a la celda como se explicó anteriormente.
1. Utilice el método RemoveAt de la colección de comentarios para eliminar el comentario.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
