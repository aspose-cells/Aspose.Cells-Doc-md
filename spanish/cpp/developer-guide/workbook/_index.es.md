---
title: Gestionar libro de trabajo con C++
linktitle: Libro de trabajo
type: docs
weight: 60
url: /es/cpp/managing-workbooks-and-worksheets/
description: Aprende cómo gestionar libros de trabajo mediante las API Aspose.Cells for C++.
keywords: Cómo gestionar un libro de trabajo en C++, gestionar libros y hojas de trabajo usando C++, operar libros y hojas de trabajo en C++.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ proporciona una API poderosa y flexible para gestionar libros y hojas de trabajo. Esta sección explica cómo crear, abrir y manipular libros y hojas de trabajo programáticamente.

{{% /alert %}}

## **Creando un libro de trabajo nuevo**
Para crear un libro de trabajo nuevo:

1. Cree una instancia de la clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)
2. Agrega hojas de trabajo al libro usando la clase [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
3. Guarda el libro usando el método [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

## **Abrir un libro de trabajo existente**
Para abrir un libro de trabajo existente:

1. Crea una instancia de la clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) y pasa la ruta del archivo al constructor.
2. Accede a las hojas usando la clase [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
3. Modifica el libro según sea necesario.
4. Guarda el libro usando el método [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).SetValue("Hello, World!");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Gestionando hojas de trabajo**
Aspose.Cells for C++ ofrece una amplia gama de métodos para gestionar hojas de trabajo, incluyendo agregar, eliminar y renombrar hojas.

### **Agregando una hoja de cálculo**
Para agregar una nueva hoja de cálculo:

1. Acceda a la clase [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) desde el libro de trabajo.
2. Utilice el método [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) para agregar una nueva hoja de cálculo.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a new worksheet
    workbook.GetWorksheets().Add("NewSheet");

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **Eliminación de una hoja de cálculo**
Para eliminar una hoja de cálculo:

1. Acceda a la clase [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) desde el libro de trabajo.
2. Use el método [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat/) para eliminar una hoja de cálculo por índice.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Open an existing workbook
    Aspose::Cells::Workbook workbook("input.xlsx");

    // Remove the first worksheet
    workbook.GetWorksheets().RemoveAt(0);

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **Cambiar el nombre de una hoja de cálculo**
Para cambiar el nombre de una hoja de cálculo:

1. Acceda a la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) desde el libro de trabajo.
2. Use el método [SetName](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setname/) para cambiar el nombre de la hoja de cálculo.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName("RenamedSheet");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Conclusión**
Aspose.Cells for C++ ofrece un conjunto completo de herramientas para gestionar libros y hojas de cálculo. Ya sea que necesite crear un nuevo libro, abrir uno existente o manipular hojas de cálculo, Aspose.Cells facilita trabajar con archivos de Excel mediante programación.
