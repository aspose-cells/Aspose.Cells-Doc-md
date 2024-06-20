---
title: Gestionar comentarios en la hoja de cálculo
type: docs
weight: 110
url: /es/net/aspose-cells-gridweb/manage-comment-in-worksheet/
keywords: GridWeb,comment
description: Este artículo introduce cómo trabajar con comentarios en GridWeb.
---

{{% alert color="primary" %}} 

Este tema trata sobre cómo agregar, acceder y eliminar comentarios de las hojas de cálculo. Los comentarios son útiles para agregar notas o información útil para los usuarios que trabajarán con la hoja. Los desarrolladores tienen la flexibilidad de agregar comentarios a cualquier celda de la hoja de cálculo.

{{% /alert %}} 
## **Trabajando con Comentarios**
### **Añadir Comentarios**
Para agregar un comentario a la hoja de cálculo, por favor sigue los siguientes pasos:

1. Agrega el control Aspose.Cells.GridWeb al Formulario Web.
1. Accede a la hoja de cálculo a la que estás agregando comentarios.
1. Agregar un comentario a una celda.
1. Establece una nota para el nuevo comentario.

**Se ha agregado un comentario a la hoja de cálculo** 

![todo:image_alt_text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Acceso a Comentarios**
Para acceder a un comentario:

1. Accede a la celda que contiene el comentario.
1. Obten la referencia de la celda.
1. Pasa la referencia a la colección de Comentarios para acceder al comentario.
1. Ahora es posible modificar las propiedades del comentario.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Eliminación de Comentarios**
Para eliminar un comentario:

1. Accede a la celda como se explicó anteriormente.
1. Utilice el método RemoveAt de la colección de comentarios para eliminar el comentario.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
