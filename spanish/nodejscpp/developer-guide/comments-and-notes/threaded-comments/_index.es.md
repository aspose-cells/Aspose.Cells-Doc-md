---  
title: Comentarios en hilos con Node.js a través de C++  
linktitle: Comentarios enhebrados  
type: docs  
weight: 140  
url: /es/nodejs-cpp/threaded-comments/  
description: Gestiona los comentarios en hilos en documentos Excel usando Aspose.Cells for Node.js via C++. Aprende a agregar, leer, editar y eliminar comentarios en hilos.  
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

Aspose.Cells proporciona el método [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) para agregar comentarios en hilo. El método [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) acepta los siguientes tres parámetros.  

- Nombre de la celda: El nombre de la celda donde se insertará el comentario.  
- Texto del comentario: El texto del comentario.  
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentauthor): El autor del comentario  

El siguiente ejemplo de código demuestra el uso del método [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) para agregar un comentario en hilo a la celda A1. Consulta el [archivo Excel de salida](89849859.xlsx) generado por el código para referencia.  

#### **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();

// Add Author
const authorIndex = workbook.getWorksheets().getThreadedCommentAuthors().add("Aspose Test", "", "");
const author = workbook.getWorksheets().getThreadedCommentAuthors().get(authorIndex);

// Add Threaded Comment
workbook.getWorksheets().get(0).getComments().addThreadedComment("A1", "Test Threaded Comment", author);

workbook.save(outDir + "AddThreadedComments_out.xlsx");
```  

## **Leer comentarios en hilo**  

### **Leer comentarios en hilo con Excel**  

Para leer comentarios en hilo en Excel, simplemente coloque el mouse sobre la celda que contiene comentarios para ver los comentarios. La vista de los comentarios se verá como en la siguiente imagen.  

![todo:image_alt_text](threaded-comments_1.jpg)  

### **Leer comentarios en hilo usando Aspose.Cells**  

Aspose.Cells proporciona el método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) para recuperar los comentarios en hilo para la columna especificada. El método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) acepta el nombre de la columna como parámetro y devuelve el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Puedes iterar sobre el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) para ver los comentarios.  

El siguiente ejemplo demuestra la lectura de comentarios desde la columna A1 cargando el [Archivo de Excel de muestra](89849861.xlsx). Por favor, revisa la salida en la consola generada por el código para referencia.  

#### **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data"); // Adjust as necessary

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook which contains threaded comments
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();
for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
}
```  

#### **Salida de la consola**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

{{< /highlight >}}  

### **Leer el Tiempo de Creación de comentarios en hilo**  

Aspose.Cells proporciona el método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) para recuperar los comentarios en hilo para la columna especificada. El método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) acepta el nombre de la columna como parámetro y devuelve el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Puedes iterar sobre el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) y usar la propiedad [**ThreadedComment.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/threadedcomment/#getCreatedTime--).  

El siguiente ejemplo demuestra la lectura del tiempo de creación de comentarios en hilo cargando el [Archivo de Excel de muestra](89849861.xlsx). Por favor, revisa la salida en la consola generada por el código para referencia.  

#### **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();

for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
console.log("Created Time: " + comment.getCreatedTime());
}
```  

#### **Salida de la consola**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

Created Time: 5/15/2019 12:46:23 PM  

{{< /highlight >}}  

## **Editar Comentarios en Hilo**  

### **Editar comentario en hilo con Excel**  

Para editar un comentario en hilo en Excel, haz clic en el enlace **Editar** en el comentario según se muestra en la siguiente imagen.  

![todo:image_alt_text](threaded-comments_7.jpg)  

### **Editar comentario en hilo usando Aspose.Cells**  

Aspose.Cells proporciona el método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) para recuperar los comentarios en hilo de la columna especificada. El método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) acepta el nombre de la columna como parámetro y devuelve el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Puedes actualizar el comentario requerido en el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) y guardar el libro de trabajo.  

El siguiente ejemplo demuestra la edición del primer comentario en hilo de la columna A1 cargando el [Archivo de Excel de muestra](89849861.xlsx). Por favor, revisa el [archivo Excel de salida](89849862.xlsx) generado por el código mostrando el comentario actualizado para referencia.  

#### **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comment
const comment = worksheet.getComments().getThreadedComments("A1").get(0);
comment.setNotes("Updated Comment");

workbook.save(outDir + "EditThreadedComments.xlsx");
```  

## **Eliminar Comentarios en Hilo**  

### **Eliminar comentarios en hilo con Excel**  

Para eliminar comentarios en hilo en Excel, haz clic derecho en la celda que contiene los comentarios y selecciona la opción **Eliminar Comentario** como se muestra en la siguiente imagen.  

![todo:image_alt_text](threaded-comments_8.jpg)   


