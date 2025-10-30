---
title: Insertar y eliminar filas y columnas en archivos de Excel con C++
linktitle: Inserción y Eliminación de Filas y Columnas
type: docs
weight: 70
url: /es/cpp/inserting-and-deleting-rows-and-columns/
description: Este artículo muestra cómo insertar y eliminar filas y columnas usando la API Aspose.Cells for C++.
keywords: Aspose.Cells C++ gestiona filas y columnas, inserta filas y columnas, elimina filas y columnas
---

## **Introducción**

Ya sea creando una nueva hoja de cálculo desde cero o trabajando en una hoja de cálculo existente, puede ser necesario agregar filas o columnas adicionales para acomodar más datos. Inversamente, también puede ser necesario eliminar filas o columnas de posiciones específicas en la hoja de cálculo.
Para cumplir estos requisitos, Aspose.Cells proporciona un conjunto muy sencillo de clases y métodos, discutidos a continuación.

### **Gestionar Filas y Columnas**

Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ofrece una colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) que representa todas las celdas en la hoja de cálculo.

La colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) proporciona varios métodos para gestionar filas y columnas en una hoja de cálculo. Algunos de estos se discuten a continuación.

{{% alert color="primary" %}}

Cuando se añaden filas o columnas, el contenido en la hoja de cálculo se desplaza hacia abajo o hacia la derecha, y si se eliminan filas o columnas, el contenido se desplaza hacia arriba o hacia la izquierda.

{{% /alert %}}

## **Insertar Filas y Columnas**

### **Cómo insertar una fila**

Insertar una fila en la hoja de cálculo en cualquier ubicación llamando al método [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) de la colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). El método [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) toma el índice de la fila donde se insertará la nueva fila.

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Instantiating a Workbook object
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRow(2);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Cómo insertar múltiples filas**

Para insertar varias filas en una hoja de cálculo, llame al método [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) de la colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). El método [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) toma dos parámetros:

- Índice de la fila, el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas, el número total de filas que se deben insertar.

```c++
#include <iostream>
#include <fstream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows into the worksheet starting from 3rd row
    worksheet.GetCells().InsertRows(2, 10);

    // Path of output excel file
    U16String outputFilePath = srcDir + u"output.out.xls";

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Cómo insertar una fila con formato**

Para insertar una fila con opciones de formato, use la sobrecarga [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) que recibe [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) como parámetro. Configure la propiedad [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) de la clase [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) con [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) la Enumeración. La enumeración [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) tiene tres miembros, listados a continuación.

- SameAsAbove: Da formato a la fila igual que la fila superior.
- SameAsBelow: Da formato a la fila igual que la fila inferior.
- Clear: Borra el formato.

```c++
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"InsertingARowWithFormatting_out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting Formatting options
    InsertOptions insertOptions;
    insertOptions.SetCopyFormatType(CopyFormatType::SameAsAbove);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRows(2, 1, insertOptions);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully with formatting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Cómo Insertar una Columna**

Los desarrolladores también pueden insertar una columna en la hoja de cálculo en cualquier ubicación llamando al método [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) de la colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). El método [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) recibe el índice de la columna donde se insertará la nueva columna.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a column into the worksheet at 2nd position
    worksheet.GetCells().InsertColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Column inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Eliminar Filas y Columnas**

### **Cómo borrar múltiples filas**

Para eliminar varias filas de una hoja de cálculo, llame al método [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) de la colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). El método [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) toma dos parámetros:

- Índice de fila, el índice de la fila desde donde se eliminarán las filas.
- Número de filas, el número total de filas que deben ser eliminadas.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete 10 rows from the worksheet starting from 3rd row
    worksheet.GetCells().DeleteRows(2, 10);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Rows deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Cómo eliminar una columna**

Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llame al método [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) de la colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). El método [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) toma el índice de la columna a eliminar.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete a column from the worksheet at 5th position (index 4)
    worksheet.GetCells().DeleteColumn(4);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
