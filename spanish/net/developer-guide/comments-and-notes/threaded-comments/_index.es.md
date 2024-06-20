---
title: Comentarios enhebrados
type: docs
weight: 140
url: /es/net/threaded-comments/
---

## **Comentarios enhebrados**

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
  - Haga clic en el botón **Nuevo Comentario**
  - Esto abrirá un diálogo para ingresar comentarios en la celda activa.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Método 2
  - Haga clic derecho en la celda donde quiera insertar el comentario.
  - Haga clic en la opción **Nuevo Comentario**
  - Esto abrirá un diálogo para ingresar comentarios en la celda activa.
  - ![todo:image_alt_text](threaded-comments_5)

### **Agregar comentario en hilo usando Aspose.Cells**

Aspose.Cells proporciona el método [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) para agregar comentarios en hilo. El método [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) acepta los siguientes tres parámetros.

- Nombre de la celda: El nombre de la celda donde se insertará el comentario.
- Texto del comentario: El texto del comentario.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): El autor del comentario

El siguiente código de ejemplo demuestra el uso del método [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) para agregar un comentario en hilo a la celda A1. Consulte el [archivo de Excel de salida](89849859.xlsx) generado por el código como referencia.

#### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **Leer comentarios en hilo**

### **Leer comentarios en hilo con Excel**

Para leer comentarios en hilo en Excel, simplemente coloque el mouse sobre la celda que contiene comentarios para ver los comentarios. La vista de los comentarios se verá como en la siguiente imagen.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Leer comentarios en hilo usando Aspose.Cells**

Aspose.Cells proporciona el método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) para recuperar los comentarios en hilo para la columna especificada. El método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) acepta el nombre de la columna como parámetro y devuelve el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Puedes iterar sobre el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) para ver los comentarios.

El siguiente ejemplo demuestra la lectura de comentarios desde la columna A1 cargando el [Archivo de Excel de muestra](89849861.xlsx). Por favor, revisa la salida en la consola generada por el código para referencia.

#### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **Salida de la consola**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Leer el Tiempo de Creación de comentarios en hilo**

Aspose.Cells proporciona el método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) para recuperar comentarios en hilo para la columna especificada. El método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) acepta el nombre de la columna como parámetro y devuelve el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Puedes iterar sobre el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) y utilizar la propiedad [**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime).

El siguiente ejemplo demuestra la lectura del tiempo de creación de comentarios en hilo cargando el [Archivo de Excel de muestra](89849861.xlsx). Por favor, revisa la salida en la consola generada por el código para referencia.

#### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **Salida de la consola**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Editar Comentarios en Hilo**

### **Editar comentario en hilo con Excel**

Para editar un comentario en hilo en Excel, haz clic en el enlace **Editar** en el comentario según se muestra en la siguiente imagen.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Editar comentario en hilo usando Aspose.Cells**

Aspose.Cells proporciona el método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) para recuperar comentarios en hilo para la columna especificada. El método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) acepta el nombre de la columna como parámetro y devuelve el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Puedes actualizar el comentario necesario en el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) y guardar el libro de trabajo.

El siguiente ejemplo demuestra la edición del primer comentario en hilo de la columna A1 cargando el [Archivo de Excel de muestra](89849861.xlsx). Por favor, revisa el [archivo Excel de salida](89849862.xlsx) generado por el código mostrando el comentario actualizado para referencia.

#### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **Eliminar Comentarios en Hilo**

### **Eliminar comentarios en hilo con Excel**

Para eliminar comentarios en hilo en Excel, haz clic derecho en la celda que contiene los comentarios y selecciona la opción **Eliminar Comentario** como se muestra en la siguiente imagen.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Eliminar comentarios enhebrados usando Aspose.Cells**

Aspose.Cells proporciona el método [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) para eliminar comentarios para la columna especificada. El método [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) acepta el nombre de la columna como parámetro y elimina los comentarios en esa columna.

El siguiente ejemplo muestra cómo eliminar comentarios en la columna A1 cargando el [archivo de Excel de muestra](89849861.xlsx). Por favor, consulte el [archivo de Excel de salida](89849864.xlsx) generado por el código para referencia.

#### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

Tenga en cuenta que al eliminar un comentario con Aspose.Cells, el autor no se elimina automáticamente. Si necesita eliminar también el autor, por favor utilice el método RemoveAt de la clase [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection) como se muestra en el ejemplo anterior.

{{% /alert %}}
