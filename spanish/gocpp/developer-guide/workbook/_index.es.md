---
title: Gestionar Libro con Golang vía C++
linktitle: Libro de trabajo
type: docs
weight: 60
url: /es/go-cpp/managing-workbooks-and-worksheets/
description: Aprende cómo gestionar libros de trabajo mediante las API Aspose.Cells for C++.
keywords: Cómo gestionar un libro de trabajo en C++, gestionar libros y hojas de trabajo usando C++, operar libros y hojas de trabajo en C++.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ proporciona una API poderosa y flexible para gestionar libros y hojas de trabajo. Esta sección explica cómo crear, abrir y manipular libros y hojas de trabajo programáticamente.

{{% /alert %}}

## **Creando un libro de trabajo nuevo**
Para crear un libro de trabajo nuevo:

1. Crea una instancia de la clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/).
2. Añade hojas de trabajo usando la clase [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
3. Guarda el libro usando el método [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook.go" >}}
## **Abrir un libro de trabajo existente**
Para abrir un libro de trabajo existente:

1. Crea una instancia de la clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) y pasa la ruta del archivo al constructor.
2. Accede a las hojas usando la clase [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/).
3. Modifica el libro según sea necesario.
4. Guarda el libro usando el método [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-1.go" >}}
## **Gestionando hojas de trabajo**
Aspose.Cells for C++ ofrece una amplia gama de métodos para gestionar hojas de trabajo, incluyendo agregar, eliminar y renombrar hojas.

### **Agregando una hoja de cálculo**
Para agregar una nueva hoja de cálculo:

1. Accede a la clase [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) del libro.
2. Usa el método [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_sheettype/) para agregar una hoja de trabajo nueva.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-2.go" >}}
### **Eliminación de una hoja de cálculo**
Para eliminar una hoja de cálculo:

1. Accede a la clase [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) del libro.
2. Usa el método [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat_string/) para eliminar una hoja de trabajo por índice.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-3.go" >}}
### **Cambiar el nombre de una hoja de cálculo**
Para cambiar el nombre de una hoja de cálculo:

1. Accede a la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) del libro.
2. Usa el método [SetName](https://reference.aspose.com/cells/go-cpp/worksheet/setname/) para renombrar la hoja de trabajo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-4.go" >}}
## **Conclusión**
Aspose.Cells for C++ ofrece un conjunto completo de herramientas para gestionar libros y hojas de cálculo. Ya sea que necesite crear un nuevo libro, abrir uno existente o manipular hojas de cálculo, Aspose.Cells facilita trabajar con archivos de Excel mediante programación.
