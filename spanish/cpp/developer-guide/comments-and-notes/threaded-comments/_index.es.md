---
title: Comentarios en Hilo con C++
linktitle: Comentarios enhebrados
type: docs
weight: 140
url: /es/cpp/threaded-comments/
description: Aprende cómo agregar, leer, editar y eliminar comentarios en hilo en archivos de Excel usando Aspose.Cells con C++.
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

Aspose.Cells proporciona el método [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) para agregar comentarios en hilo. El método [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) acepta los siguientes tres parámetros.

- Nombre de la celda: El nombre de la celda donde se insertará el comentario.
- Texto del comentario: El texto del comentario.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthor/): El autor del comentario

El siguiente código de ejemplo demuestra el uso del método [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) para agregar un comentario en hilo a la celda A1. Consulte el [archivo de Excel de salida](89849859.xlsx) generado por el código como referencia.

#### **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add Author
    int authorIndex = workbook.GetWorksheets().GetThreadedCommentAuthors().Add(u"Aspose Test", u"", u"");
    ThreadedCommentAuthor author = workbook.GetWorksheets().GetThreadedCommentAuthors().Get(authorIndex);

    // Add Threaded Comment
    workbook.GetWorksheets().Get(0).GetComments().AddThreadedComment(u"A1", u"Test Threaded Comment", author);

    // Save the workbook
    workbook.Save(outDir + u"AddThreadedComments_out.xlsx");

    std::cout << "Threaded comment added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Leer comentarios en hilo**

### **Leer comentarios en hilo con Excel**

Para leer comentarios en hilo en Excel, simplemente coloque el mouse sobre la celda que contiene comentarios para ver los comentarios. La vista de los comentarios se verá como en la siguiente imagen.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Leer comentarios en hilo usando Aspose.Cells**

Aspose.Cells proporciona el método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) para recuperar los comentarios en hilo para la columna especificada. El método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) acepta el nombre de la columna como parámetro y devuelve el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Puedes iterar sobre el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) para ver los comentarios.

El siguiente ejemplo demuestra la lectura de comentarios desde la columna A1 cargando el [Archivo de Excel de muestra](89849861.xlsx). Por favor, revisa la salida en la consola generada por el código para referencia.

#### **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook
    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get Threaded Comments
    ThreadedCommentCollection threadedComments = worksheet.GetComments().GetThreadedComments(u"A1");

    // Iterate through threaded comments
    for (int i = 0; i < threadedComments.GetCount(); i++)
    {
        ThreadedComment comment = threadedComments.Get(i);
        cout << "Comment: " << comment.GetNotes().ToUtf8() << endl;
        cout << "Author: " << comment.GetAuthor().GetName().ToUtf8() << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

#### **Salida de la consola**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Leer el Tiempo de Creación de comentarios en hilo**

Aspose.Cells proporciona el método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) para recuperar comentarios en hilo para la columna especificada. El método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) acepta el nombre de la columna como parámetro y devuelve el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Puedes iterar sobre el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) y utilizar la propiedad [**ThreadedComment.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcomment/getcreatedtime/).

El siguiente ejemplo demuestra la lectura del tiempo de creación de comentarios en hilo cargando el [Archivo de Excel de muestra](89849861.xlsx). Por favor, revisa la salida en la consola generada por el código para referencia.

#### **Código de muestra**

```cpp
#include <iostream>
#include <iomanip>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ThreadedCommentCollection threadedComments = worksheet.GetComments().GetThreadedComments(u"A1");

    for (int i = 0; i < threadedComments.GetCount(); i++)
    {
        ThreadedComment comment = threadedComments.Get(i);
        cout << "Comment: " << comment.GetNotes().ToUtf8() << endl;
        cout << "Author: " << comment.GetAuthor().GetName().ToUtf8() << endl;
        Date createdTime = comment.GetCreatedTime();
        ostringstream oss;
        oss << setfill('0') 
            << setw(4) << createdTime.year << "-"
            << setw(2) << createdTime.month << "-"
            << setw(2) << createdTime.day << " "
            << setw(2) << createdTime.hour << ":"
            << setw(2) << createdTime.minute << ":"
            << setw(2) << createdTime.second;
        cout << "Created Time: " << oss.str() << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

#### **Salida de la consola**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Editar Comentarios en Hilo**

### **Editar comentario en hilo con Excel**

Para editar un comentario en hilo en Excel, haz clic en el enlace **Editar** en el comentario según se muestra en la siguiente imagen.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Editar comentario en hilo usando Aspose.Cells**

Aspose.Cells proporciona el método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) para recuperar comentarios en hilo para la columna especificada. El método [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) acepta el nombre de la columna como parámetro y devuelve el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Puedes actualizar el comentario necesario en el [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) y guardar el libro de trabajo.

El siguiente ejemplo demuestra la edición del primer comentario en hilo de la columna A1 cargando el [Archivo de Excel de muestra](89849861.xlsx). Por favor, revisa el [archivo Excel de salida](89849862.xlsx) generado por el código mostrando el comentario actualizado para referencia.

#### **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the threaded comment from cell A1
    ThreadedComment comment = worksheet.GetComments().GetThreadedComments(u"A1").Get(0);

    // Update the comment text
    comment.SetNotes(u"Updated Comment");

    // Save the workbook
    workbook.Save(outDir + u"EditThreadedComments.xlsx");

    std::cout << "Threaded comment updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Eliminar Comentarios en Hilo**

### **Eliminar comentarios en hilo con Excel**

Para eliminar comentarios en hilo en Excel, haz clic derecho en la celda que contiene los comentarios y selecciona la opción **Eliminar Comentario** como se muestra en la siguiente imagen.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Eliminar comentarios enhebrados usando Aspose.Cells**

Aspose.Cells proporciona el método [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) para eliminar comentarios para la columna especificada. El método [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) acepta el nombre de la columna como parámetro y elimina los comentarios en esa columna.

El siguiente ejemplo muestra cómo eliminar comentarios en la columna A1 cargando el [archivo de Excel de muestra](89849861.xlsx). Por favor, consulte el [archivo de Excel de salida](89849864.xlsx) generado por el código para referencia.

#### **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the comments collection
    CommentCollection comments = worksheet.GetComments();

    // Get the author of the first threaded comment in cell A1
    ThreadedCommentAuthor author = worksheet.GetComments().GetThreadedComments(u"A1").Get(0).GetAuthor();

    // Remove the comment at cell A1
    comments.RemoveAt(u"A1");

    // Get the threaded comment authors collection
    ThreadedCommentAuthorCollection authors = workbook.GetWorksheets().GetThreadedCommentAuthors();

    // Save the workbook
    workbook.Save(outDir + u"ThreadedCommentsSample_Out.xlsx");

    std::cout << "Threaded comments processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Tenga en cuenta que al eliminar un comentario con Aspose.Cells, el autor no se elimina automáticamente. Si necesita eliminar también el autor, por favor utilice el método RemoveAt de la clase [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthorcollection/) como se muestra en el ejemplo anterior.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
