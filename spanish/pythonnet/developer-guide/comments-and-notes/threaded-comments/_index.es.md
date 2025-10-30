---
title: Comentarios enhebrados
type: docs
weight: 140
url: /es/python-net/threaded-comments/
---

## **Comentarios enhebrados**

MS Excel 365 proporciona una característica para agregar comentarios enhebrados. Estos comentarios funcionan como conversaciones y se pueden utilizar para discusiones. Los comentarios ahora vienen con un cuadro de respuesta que permite conversaciones enhebradas. Los comentarios antiguos se llaman Notas en Excel 365. La captura de pantalla a continuación muestra cómo se muestran los comentarios enhebrados cuando se abren en Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Los comentarios enhebrados se muestran así en versiones anteriores de Excel. Las siguientes imágenes se han tomado al abrir el archivo de muestra en Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells para Python via .NET también ofrece la función de gestionar comentarios con hilo.

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

### **Agregar Comentario con Hilo usando Aspose.Cells para Python via .NET**

Aspose.Cells para Python via .NET proporciona el método [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment/) para agregar comentarios con hilo. El método [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) acepta los siguientes tres parámetros.

- Nombre de la celda: El nombre de la celda donde se insertará el comentario.
- Texto del comentario: El texto del comentario.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentauthor): El autor del comentario

El siguiente código de ejemplo demuestra el uso del método [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) para agregar un comentario en hilo a la celda A1. Consulte el [archivo de Excel de salida](89849859.xlsx) generado por el código como referencia.

#### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-AddThreadedComments-1.py" >}}

## **Leer comentarios en hilo**

### **Leer comentarios en hilo con Excel**

Para leer comentarios en hilo en Excel, simplemente coloque el mouse sobre la celda que contiene comentarios para ver los comentarios. La vista de los comentarios se verá como en la siguiente imagen.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Leer comentarios con hilo usando Aspose.Cells para Python via .NET**

Aspose.Cells para Python via .NET proporciona el método [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) para recuperar comentarios con hilo de la columna especificada. El método [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) acepta el nombre de la columna como parámetro y devuelve el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). Puedes iterar sobre el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) para ver los comentarios.

El siguiente ejemplo demuestra la lectura de comentarios desde la columna A1 cargando el [Archivo de Excel de muestra](89849861.xlsx). Por favor, revisa la salida en la consola generada por el código para referencia.

#### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedComments-1.py" >}}

#### **Salida de la consola**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Leer el Tiempo de Creación de comentarios en hilo**

Aspose.Cells para Python via .NET proporciona el método [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) para recuperar comentarios con hilo de la columna especificada. El método [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) acepta el nombre de la columna como parámetro y devuelve el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). Puedes iterar sobre el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) y usar la propiedad [**ThreadedComment.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcomment/created_time).

El siguiente ejemplo demuestra la lectura del tiempo de creación de comentarios en hilo cargando el [Archivo de Excel de muestra](89849861.xlsx). Por favor, revisa la salida en la consola generada por el código para referencia.

#### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedCommentCreatedTime-1.py" >}}

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

### **Editar comentario con hilo usando Aspose.Cells para Python via .NET**

Aspose.Cells para Python via .NET proporciona el método [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) para recuperar comentarios con hilo de la columna especificada. El método [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) acepta el nombre de la columna como parámetro y devuelve el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). Puedes actualizar el comentario requerido en el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) y guardar el libro de trabajo.

El siguiente ejemplo demuestra la edición del primer comentario en hilo de la columna A1 cargando el [Archivo de Excel de muestra](89849861.xlsx). Por favor, revisa el [archivo Excel de salida](89849862.xlsx) generado por el código mostrando el comentario actualizado para referencia.

#### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-EditThreadedComments-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
