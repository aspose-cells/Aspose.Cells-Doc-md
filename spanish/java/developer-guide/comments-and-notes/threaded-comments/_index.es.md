---
title: Comentarios encadenados
type: docs
weight: 140
url: /es/java/threaded-comments/
---
# **Comentarios encadenados**
MS Excel 365 proporciona una función para agregar comentarios encadenados. Estos comentarios funcionan como conversaciones y pueden usarse para discusiones. Los comentarios ahora vienen con un cuadro de respuesta que permite conversaciones encadenadas. Los comentarios antiguos se denominan Notas en Excel 365. La siguiente captura de pantalla muestra cómo se muestran los comentarios encadenados cuando se abren en Excel.

![todo:imagen_alternativa_texto](threaded-comments_1.jpg)

Los comentarios encadenados se muestran así en versiones anteriores de Excel. Las siguientes imágenes se tomaron abriendo el archivo de muestra en Excel 2016.

![todo:imagen_alternativa_texto](threaded-comments_2.jpg)



![todo:imagen_alternativa_texto](threaded-comments_3.jpg)



Aspose.Cells también proporciona la función para administrar comentarios encadenados.
## **Agregar comentarios encadenados**
### **Agregar comentario encadenado con Excel**
Para agregar comentarios encadenados en Excel 365, siga los siguientes pasos.

- Método 1
 - Haga clic en el**Revisar**Pestaña
 - Haga clic en el**Nuevo comentario**botón
 - Esto abrirá un diálogo para ingresar comentarios en la celda activa.
  - ![todo:imagen_alternativa_texto](threaded-comments_4.jpg)
- Método 2
 - Haz clic derecho en la celda donde quieres insertar el comentario.
 - Haga clic en el**Nuevo comentario**opción.
 - Esto abrirá un diálogo para ingresar comentarios en la celda activa.
  - ![todo:imagen_alternativa_texto](threaded-comments_5)
### **Agregar comentario en hilo usando Aspose.Cells**
Aspose.Cells proporciona[Comentarios.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) para agregar comentarios encadenados.[Comentarios.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) El método acepta los siguientes tres parámetros.

- Cell Nombre: El nombre de la celda donde se insertará el comentario.
- Texto del comentario: El texto del comentario.
- [ThreadedCommentAuthor](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): El autor del comentario.

El siguiente ejemplo de código demuestra el uso de[Comentarios.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) para agregar un comentario encadenado a la celda A1. Por favor vea el[archivo de salida de Excel](AddThreadedComments_out.xlsx)generado por el código como referencia.
#### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **Leer comentarios encadenados**
### **Leer comentarios encadenados con Excel**
Para leer comentarios encadenados en Excel, simplemente pase el mouse sobre la celda que contiene los comentarios para verlos. La vista de comentarios se verá como la vista en la siguiente imagen.

![todo:imagen_alternativa_texto](threaded-comments_1.jpg)
### **Leer comentarios encadenados usando Aspose.Cells**
Aspose.Cells proporciona[Comentarios.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) para recuperar comentarios encadenados para la columna especificada.[Comentarios.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)acepta el nombre de la columna como parámetro y devuelve el[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Puede iterar sobre el[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)para ver los comentarios.

El siguiente ejemplo demuestra la lectura de comentarios de la columna A1 cargando el[ejemplo de archivo de Excel](ThreadedCommentsSample.xlsx). Consulte la salida de la consola generada por el código como referencia.
#### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Salida de consola**
Comentario: comentario de prueba

Autor: Aspose Prueba
### **Leer tiempo de creación de comentarios encadenados**
Aspose.Cells proporciona[Comentarios.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) para recuperar comentarios encadenados para la columna especificada.[Comentarios.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)acepta el nombre de la columna como parámetro y devuelve el[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Puede iterar sobre el[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)y usa el[ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime)propiedad.

El siguiente ejemplo demuestra la lectura del tiempo creado de comentarios encadenados cargando el[ejemplo de archivo de Excel](ThreadedCommentsSample.xlsx). Consulte la salida de la consola generada por el código como referencia.
#### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Salida de consola**
Comentario: comentario de prueba

Autor: Aspose Prueba

Hora de creación: 2019-05-15T12:46:23
## **Editar comentarios encadenados**
### **Editar comentario encadenado con Excel**
Para editar un comentario encadenado en Excel, haga clic en el**Editar**enlace en el comentario como se muestra en la siguiente imagen.

![todo:imagen_alternativa_texto](threaded-comments_7.jpg)
### **Editar comentario en hilo usando Aspose.Cells**
Aspose.Cells proporciona[Comentarios.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) para recuperar comentarios encadenados para la columna especificada.[Comentarios.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)acepta el nombre de la columna como parámetro y devuelve el[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Puede actualizar el comentario requerido en el[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)y guardar el libro de trabajo.

El siguiente ejemplo muestra la edición del primer comentario encadenado en la columna A1 cargando el[ejemplo de archivo de Excel](ThreadedCommentsSample.xlsx). Por favor vea el[archivo de salida de Excel](EditThreadedComments.xlsx)generado por el código que muestra el comentario actualizado como referencia.
#### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Eliminar comentarios encadenados**
### **Eliminar comentarios encadenados con Excel**
Para eliminar comentarios encadenados en Excel, haga clic derecho en la celda que contiene los comentarios y haga clic en el**Eliminar comentario**opción como se muestra en la siguiente imagen.

![todo:imagen_alternativa_texto](threaded-comments_8.jpg)
### **Quitar comentarios encadenados usando Aspose.Cells**
Aspose.Cells proporciona[Comentarios.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) para eliminar los comentarios de la columna especificada.[Comentarios.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) acepta el nombre de la columna como parámetro y elimina los comentarios de esa columna.

El siguiente ejemplo demuestra la eliminación de comentarios en la columna A1 cargando el[ejemplo de archivo de Excel](ThreadedCommentsSample.xlsx). Por favor vea el[archivo de salida de Excel](ThreadedCommentsSample_Out.xlsx)generado por el código como referencia.
#### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

 Tenga en cuenta que al eliminar el comentario con Aspose.Cells, el autor no se elimina automáticamente. Si también necesita eliminar al autor, utilice el[ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt\(int\)como se muestra en el ejemplo anterior.

{{% /alert %}}
