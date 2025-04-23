---
title: Crear, Acceder y Copiar Rangos Nombrados con C++
linktitle: Crear, acceder y copiar rangos nombrados
type: docs
weight: 200
url: /es/cpp/create-access-and-copy-named-ranges/
description: Aprende cómo crear, acceder y copiar rangos nombrados en archivos de Excel usando Aspose.Cells con C++.
---

## **Introducción**

Normalmente, las etiquetas de columnas y filas se usan para referirse a celdas individuales. Es posible crear nombres descriptivos para representar celdas, rangos de celdas, fórmulas o valores constantes. La palabra **nombre** puede referirse a una cadena de caracteres que representa una celda, rango de celdas, fórmula o valor constante. Asignar un nombre a un rango significa que ese rango de celdas puede ser referenciado por su nombre. Usa nombres fáciles de entender, como Productos, para referirte a rangos difíciles de entender, como Ventas!C20:C30. Las etiquetas pueden usarse en fórmulas que hacen referencia a datos en la misma hoja de cálculo; si deseas representar un rango en otra hoja, puedes usar un nombre. *Los rangos con nombres son algunas de las funciones más poderosas de Microsoft Excel, especialmente cuando se usan como la fuente para controles de listas, tablas dinámicas, gráficos, y más.

## **Trabajar con Rangos con Nombre Usando Microsoft Excel**

### **Crear Rangos con Nombre**

Los siguientes pasos describen cómo nombrar una celda o rango de celdas usando **MS Excel**. Este método se aplica a **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** y **2002**.

1. Selecciona la celda o rango de celdas que deseas nombrar.
1. Haga clic en la **Caja de Nombre** en el extremo izquierdo de la barra de fórmulas.
1. Escribe el nombre para las celdas.
1. Presiona ENTER.

{{% alert color="primary" %}}

No puedes nombrar una celda mientras estás cambiando el contenido de la celda.

{{% /alert %}}

## **Trabajar con Rangos con Nombre Usando Aspose.Cells**

Aquí, usamos la API de Aspose.Cells para realizar la tarea.
Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

### **Crear Rango con Nombre**

Es posible crear un rango con nombre llamando al método sobrecargado [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) de la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Una versión típica del método [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) acepta los siguientes parámetros:

- Nombre de la celda superior izquierda, el nombre de la celda superior izquierda en el rango.
- Nombre de la celda inferior derecha, el nombre de la celda inferior derecha en el rango.

Cuando se llama al método [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/), devuelve el rango recién creado como una instancia de la clase [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). Utilice este objeto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) para configurar el rango con nombre. Por ejemplo, establezca el nombre del rango utilizando la propiedad [**GetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getname/). El siguiente ejemplo muestra cómo crear un rango con nombre de celdas que se extiende sobre B4:G14.

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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating a named range
    Range range = worksheet.GetCells().CreateRange(u"B4", u"G14");

    // Setting the name of the named range
    range.SetName(u"TestRange");

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Named range created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ingresar Datos en las Celdas en el Rango Nombrado**

Puedes insertar datos en las celdas individuales de un rango siguiendo el patrón:

- **C++**: Rango(fila, columna)

Suponga que tiene un rango con nombre que abarca A1:C4. La matriz hace 4 * 3 = 12 celdas. Las celdas individuales del rango están dispuestas secuencialmente: Rango(0, 0), Rango(0, 1), Rango(0, 2), Rango(1, 0), Rango(1, 1), Rango(1, 2), Rango(2, 0), Rango(2, 1), Rango(2, 2), Rango(3, 0), Rango(3, 1), Rango(3, 2).

Utiliza las siguientes propiedades para identificar las celdas en el rango:

- FirstRow devuelve el índice de la primera fila en el rango con nombre.
- FirstColumn devuelve el índice de la primera columna en el rango con nombre.
- RowCount devuelve el número total de filas en el rango con nombre.
- ColumnCount devuelve el número total de columnas en el rango con nombre.

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas de un rango especificado.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Create a range of cells based on H1:J4
    Range range = worksheet1.GetCells().CreateRange(u"H1", u"J4");

    // Name the range
    range.SetName(u"MyRange");

    // Input some data into cells in the range
    range.Get(0, 0).PutValue(u"USA");
    range.Get(0, 1).PutValue(u"SA");
    range.Get(0, 2).PutValue(u"Israel");
    range.Get(1, 0).PutValue(u"UK");
    range.Get(1, 1).PutValue(u"AUS");
    range.Get(1, 2).PutValue(u"Canada");
    range.Get(2, 0).PutValue(u"France");
    range.Get(2, 1).PutValue(u"India");
    range.Get(2, 2).PutValue(u"Egypt");
    range.Get(3, 0).PutValue(u"China");
    range.Get(3, 1).PutValue(u"Philipine");
    range.Get(3, 2).PutValue(u"Brazil");

    // Save the excel file
    workbook.Save(outDir + u"rangecells.out.xls");

    std::cout << "Range cells created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Identificar Celdas en el Rango con Nombre**

Puedes insertar datos en las celdas individuales de un rango siguiendo el patrón:

- **C++**: Rango(fila, columna)

Si tienes un rango con nombre que abarca A1:C4. La matriz hace 4 * 3 = 12 celdas. Las celdas individuales del rango están dispuestas secuencialmente: Rango(0, 0), Rango(0, 1), Rango(0, 2), Rango(1, 0), Rango(1, 1), Rango(1, 2), Rango(2, 0), Rango(2, 1), Rango(2, 2), Rango(3, 0), Rango(3, 1), Rango(3, 2).

Utiliza las siguientes propiedades para identificar las celdas en el rango:

- FirstRow devuelve el índice de la primera fila en el rango con nombre.
- FirstColumn devuelve el índice de la primera columna en el rango con nombre.
- RowCount devuelve el número total de filas en el rango con nombre.
- ColumnCount devuelve el número total de columnas en el rango con nombre.

El siguiente ejemplo muestra cómo ingresar algunos valores en las celdas de un rango especificado.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    // Identify range cells
    std::cout << "First Row : " << range.GetFirstRow() << std::endl;
    std::cout << "First Column : " << range.GetFirstColumn() << std::endl;
    std::cout << "Row Count : " << range.GetRowCount() << std::endl;
    std::cout << "Column Count : " << range.GetColumnCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Acceder a rangos con nombres**

#### **Acceder a un Rango Nombrado Específico**

Llame al método [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) de la colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) para obtener un rango por el nombre especificado. Un método [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) típico toma el nombre del rango con nombre y devuelve el rango con nombre especificado como una instancia de la clase [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). El siguiente ejemplo muestra cómo acceder a un rango especificado por su nombre.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Getting the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    if (range)
    {
        std::cout << "Named Range : " << range.GetRefersTo().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

#### **Acceder a todos los rangos con nombres en una hoja de cálculo**

Llame al método [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) de la colección [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) para obtener todos los rangos con nombre en una hoja de cálculo. El método [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) devuelve una matriz de todos los rangos con nombre en la colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).

El siguiente ejemplo muestra cómo acceder a todos los rangos nombrados en un libro de trabajo.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    WorksheetCollection sheets = workbook.GetWorksheets();
    Vector<Range> ranges = sheets.GetNamedRanges();

    std::cout << "Total Number of Named Ranges: " << ranges.GetLength() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Copiar rangos con nombres**

Aspose.Cells proporciona el método [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) para copiar un rango de celdas con formato en otro rango.

El siguiente ejemplo muestra cómo copiar un rango de celdas fuente en otro rango con nombre.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");
    range1.SetName(u"MyRange");

	Color borderColor = Color{ 0,0, 0, 128 };
    range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, borderColor);

    range1.Get(0, 0).PutValue(u"Test");
    range1.Get(0, 4).PutValue(u"123");

    Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");
    range2.SetName(u"testrange");
    range2.Copy(range1);

    workbook.Save(outDir + u"copyranges.out.xls");

    std::cout << "Ranges copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
