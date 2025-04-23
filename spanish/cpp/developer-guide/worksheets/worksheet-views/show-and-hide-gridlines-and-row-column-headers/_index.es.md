---
title: Mostrar y ocultar líneas de cuadrícula y encabezados de filas y columnas con C++
linktitle: Mostrar y ocultar las cuadrículas y encabezados de filas y columnas
type: docs
weight: 30
url: /es/cpp/show-and-hide-gridlines-and-row-column-headers/
description: Este artículo proporciona un código de ejemplo para usar la API o Biblioteca en C++ para ocultar o mostrar programáticamente las líneas de cuadrícula, encabezados de fila y columna de una hoja de cálculo de Excel.
---

{{% alert color="primary" %}}

Aspose.Cells admite ocultar y mostrar las cuadrículas de la hoja de cálculo que son visibles de forma predeterminada. También proporciona el control de la visibilidad de los encabezados de filas y columnas de la hoja de cálculo.

{{% /alert %}}

## **Mostrar y ocultar las cuadrículas**

Todas las hojas de cálculo de Excel tienen cuadrículas de forma predeterminada. Ayudan a delimitar las celdas para que sea fácil ingresar datos en celdas particulares. Las cuadrículas nos permiten ver una hoja de cálculo como una colección de celdas, donde cada celda es fácilmente identificable.

### **Controlar la visibilidad de las cuadrículas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite a los desarrolladores acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ofrece una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Para controlar la visibilidad de las líneas de cuadrícula, usa la propiedad [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/). [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) es una propiedad booleana, lo que significa que solo puede almacenar un valor **verdadero** o **falso**.

#### **Hacer visible las líneas de cuadrícula**

Haz visible las líneas de cuadrícula estableciendo en **true** la propiedad [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

#### **Ocultar líneas de cuadrícula**

Oculta las líneas de cuadrícula estableciendo en **false** la propiedad [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

Se proporciona un ejemplo completo que demuestra el uso de la propiedad [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) abriendo un archivo excel (book1.xls), ocultando las líneas de cuadrícula en la primera hoja y guardando el archivo modificado como output.xls.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the grid lines of the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Grid lines hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Mostrar y ocultar los encabezados de filas y columnas**

Todas las hojas de cálculo en un archivo de Excel están compuestas por celdas que están dispuestas en filas y columnas. Todas las filas y columnas tienen valores únicos que se utilizan para identificarlas e identificar celdas individuales. Por ejemplo, las filas están numeradas - 1, 2, 3, 4, etc. - y las columnas están ordenadas alfabéticamente - A, B, C, D, etc. Los valores de filas y columnas se muestran en los encabezados. Con Aspose.Cells, los desarrolladores pueden controlar la visibilidad de estos encabezados de filas y columnas.

### **Controlar la visibilidad de las hojas de cálculo**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite a los desarrolladores acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ofrece una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Para controlar la visibilidad de los encabezados de fila y columna, usa la propiedad [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) es una propiedad booleana, lo que significa que solo puede almacenar un valor **verdadero** o **falso**.

#### **Hacer visibles los encabezados de fila/columna**

Haz visibles los encabezados de fila y columna configurando la propiedad [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) a **verdadero**.

#### **Ocultar encabezados de filas/columnas**

Oculta los encabezados de fila y columna configurando la propiedad [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) a **falso**.

A continuación se presenta un ejemplo completo que muestra cómo usar la propiedad [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) abriendo un archivo de Excel (book1.xls), ocultando los encabezados de fila y columna en la primera hoja de trabajo y guardando el archivo modificado como output.xls.

```cpp
#include <iostream>
#include <memory>
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
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the headers of rows and columns
    worksheet.SetIsRowColumnHeadersVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Headers hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

También es posible usar los métodos [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) y [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) de la clase [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) para hacer visibles múltiples filas y columnas.

{{% /alert %}}
