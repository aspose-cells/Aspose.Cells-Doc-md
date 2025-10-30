---
title: Mostrar y ocultar filas, columnas y barras de desplazamiento con C++
linktitle: Mostrar y ocultar filas, columnas y barras de desplazamiento
type: docs
weight: 20
url: /es/cpp/show-and-hide-rows-columns-and-scroll-bars/
description: Este artículo demuestra cómo mostrar y ocultar programáticamente filas y columnas de hojas de cálculo de Excel usando el lenguaje C++ y la API Aspose.Cells. La visibilidad de las barras de desplazamiento puede ajustarse, y varias filas y columnas pueden ocultarse.
---

{{% alert color="primary" %}}

Aspose.Cells proporciona formas de controlar la visibilidad de filas, columnas y barras de desplazamiento de una hoja de cálculo.

{{% /alert %}}

## **Mostrar y ocultar filas y columnas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite a los desarrolladores acceder a cada hoja de trabajo en el archivo Excel. Una hoja de trabajo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) que representa todas las celdas en la hoja de trabajo. La colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) ofrece varios métodos para gestionar filas o columnas en una hoja de trabajo. Algunos de estos se discuten a continuación.

### **Mostrar filas y columnas**

Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando a los métodos [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) y [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) de la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) respectivamente. Ambos métodos requieren dos parámetros:

- **Índice de fila o columna** - el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.
- **Altura de fila o ancho de columna** - la altura de fila o el ancho de columna asignados a la fila o columna después de desocultar.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhiding the 3rd row and setting its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhiding the 2nd column and setting its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Al hacer visible una columna oculta, si necesita restaurarla a su ancho asignado previamente o a su ancho original, por favor desoculte la columna con un ancho negativo. Por ejemplo: `worksheet->GetCells()->UnhideColumn(5, -1)`.

{{% /alert %}}

### **Ocultar filas y columnas**

Los desarrolladores pueden ocultar una fila o columna llamando a los métodos [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) y [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) de la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) respectivamente. Ambos métodos toman el índice de fila y columna como parámetro para ocultar la fila o columna específica.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

También es posible ocultar una fila o columna estableciendo la altura de la fila o el ancho de la columna en 0, respectivamente.

{{% /alert %}}

### **Ocultar múltiples filas y columnas**

Los desarrolladores pueden ocultar varias filas o columnas a la vez llamando a los métodos [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) y [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) de la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) respectivamente. Ambos métodos toman el índice de fila o columna inicial y el número de filas o columnas que deben ocultarse como parámetros.

```c++
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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Mostrar y ocultar barras de desplazamiento**

Las barras de desplazamiento se utilizan para navegar por el contenido de cualquier archivo. Normalmente, hay dos tipos de barras de desplazamiento:

- Barras de desplazamiento verticales
- Barras de desplazamiento horizontales

Microsoft Excel también proporciona barras de desplazamiento horizontales y verticales para que los usuarios puedan desplazarse por el contenido de la hoja de cálculo. Utilizando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de ambos tipos de barras de desplazamiento en los archivos de Excel.

### **Controlar la visibilidad de las barras de desplazamiento**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) ofrece una amplia gama de propiedades y métodos para gestionar un archivo de Excel. Para controlar la visibilidad de las barras de desplazamiento, use las propiedades [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) y [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) de la clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) y [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) son propiedades Boolean, lo que significa que solo pueden almacenar valores **verdadero** o **falso**.

#### **Hacer visibles las Barras de Desplazamiento**

Hacer visibles las barras de desplazamiento estableciendo en **verdadero** las propiedades [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) o [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) de la clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).

#### **Ocultar Barras de Desplazamiento**

Ocultar barras de desplazamiento estableciendo en **falso** las propiedades [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) o [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) de la clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).

**Código de Ejemplo**

A continuación se presenta un código completo que abre un archivo de Excel, `book1.xls`, oculta ambas barras de desplazamiento y luego guarda el archivo modificado como `output.xls`.

```c++
#include <iostream>
#include <fstream>
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

    // Hide the vertical scroll bar of the Excel file
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Hide the horizontal scroll bar of the Excel file
    workbook.GetSettings().SetIsHScrollBarVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Scroll bars hidden successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
