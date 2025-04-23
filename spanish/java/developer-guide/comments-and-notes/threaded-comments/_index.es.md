---
title: Comentarios enhebrados
type: docs
weight: 140
url: /es/java/threaded-comments/
---

# **Comentarios enhebrados**
MS Excel 365 proporciona una característica para agregar comentarios enhebrados. Estos comentarios funcionan como conversaciones y se pueden utilizar para discusiones. Los comentarios ahora vienen con un cuadro de respuesta que permite conversaciones enhebradas. Los comentarios antiguos se llaman Notas en Excel 365. La captura de pantalla a continuación muestra cómo se muestran los comentarios enhebrados cuando se abren en Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Los comentarios enhebrados se muestran así en versiones anteriores de Excel. Las siguientes imágenes se han tomado al abrir el archivo de muestra en Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)



![todo:image_alt_text](threaded-comments_3.jpg)



Aspose.Cells también proporciona la función para administrar comentarios enhebrados. 
## **Agregar comentarios enhebrados**
### **Agregar comentario en hilo con Excel**
Para agregar comentarios en hilo en Excel 365, siga los siguientes pasos.

- Método 1
  - Haga clic en la pestaña **Revisar**
  - Haga clic en el botón **Nuevo Comentario**
  - Esto abrirá un diálogo para ingresar comentarios en la celda activa.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Método 2
  - Haga clic derecho en la celda donde quiera insertar el comentario.
  - Haga clic en la opción **Nuevo Comentario**
  - Esto abrirá un diálogo para ingresar comentarios en la celda activa.
  - ![todo:image_alt_text](threaded-comments_5)
### **Agregar comentario en hilo usando Aspose.Cells**
Aspose.Cells proporciona el método [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) para agregar comentarios en hilo. El método [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) acepta los siguientes tres parámetros.

- Nombre de la celda: El nombre de la celda donde se insertará el comentario.
- Texto del comentario: El texto del comentario.
- [ThreadedCommentAuthor](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): El autor del comentario

El siguiente ejemplo de código demuestra cómo usar [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) para agregar un comentario en hilo en la celda A1. Consulte el [archivo de Excel de salida](AddThreadedComments_out.xlsx) generado por el código como referencia.
#### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **Leer comentarios en hilo**
### **Leer comentarios en hilo con Excel**
Para leer comentarios en hilo en Excel, simplemente coloque el mouse sobre la celda que contiene comentarios para ver los comentarios. La vista de los comentarios se verá como en la siguiente imagen.

![todo:image_alt_text](threaded-comments_1.jpg)
### **Leer comentarios en hilo usando Aspose.Cells**
Aspose.Cells proporciona el método [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) para recuperar comentarios en hilo para la columna especificada. [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) acepta el nombre de la columna como parámetro y devuelve la colección [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Puede iterar sobre la colección para ver los comentarios.

El siguiente ejemplo demuestra la lectura de comentarios de la columna A1 cargando el [archivo de Excel de ejemplo](ThreadedCommentsSample.xlsx). Por favor, consulte la salida en la consola generada por el código para referencia.
#### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Salida de la consola**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Leer el Tiempo de Creación de comentarios en hilo**
Aspose.Cells proporciona el método [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) para recuperar comentarios en hilo para la columna especificada. [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) acepta el nombre de la columna como parámetro y devuelve la colección [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Puede iterar sobre la colección y usar la propiedad [ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime).

El siguiente ejemplo demuestra la lectura de la fecha de creación de comentarios en hilo cargando el [archivo de Excel de ejemplo](ThreadedCommentsSample.xlsx). Por favor, consulte la salida en la consola generada por el código para referencia.
#### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Salida de la consola**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 2019-05-15T12:46:23

{{< /highlight >}}

## **Editar Comentarios en Hilo**
### **Editar comentario en hilo con Excel**
Para editar un comentario en hilo en Excel, haga clic en el enlace **Editar** en el comentario como se muestra en la siguiente imagen.

![todo:image_alt_text](threaded-comments_7.jpg)
### **Editar comentario en hilo usando Aspose.Cells**
Aspose.Cells proporciona el método [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) para recuperar comentarios en hilo para la columna especificada. [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) acepta el nombre de la columna como parámetro y devuelve la colección [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Puede actualizar el comentario requerido en la colección [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) y guardar el libro de trabajo.

El siguiente ejemplo demuestra cómo editar el primer comentario enhebrado en la columna A1 cargando el [Archivo de Excel de muestra](ThreadedCommentsSample.xlsx). Por favor, consulte el [archivo de Excel de salida](EditThreadedComments.xlsx) generado por el código que muestra el comentario actualizado como referencia.
#### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Eliminar Comentarios en Hilo**
### **Eliminar comentarios en hilo con Excel**
Para eliminar comentarios enhebrados en Excel, haga clic derecho en la celda que contiene los comentarios y seleccione la opción **Eliminar Comentario**, como se muestra en la siguiente imagen.

![todo:image_alt_text](threaded-comments_8.jpg)
### **Eliminar comentarios enhebrados usando Aspose.Cells**
Aspose.Cells proporciona el método [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-) para eliminar comentarios en la columna especificada. [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-) acepta el nombre de la columna como parámetro y elimina los comentarios en esa columna. 

El siguiente ejemplo demuestra la eliminación de comentarios en la columna A1 cargando el [Archivo de Excel de muestra](ThreadedCommentsSample.xlsx). Por favor, consulte el [archivo de Excel de salida](ThreadedCommentsSample_Out.xlsx) generado por el código como referencia.
#### **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

Tenga en cuenta que, al eliminar un comentario con Aspose.Cells, el autor no se elimina automáticamente. Si también necesita eliminar al autor, utilice el método [ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt-int-) como se muestra en el ejemplo anterior.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
