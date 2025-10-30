---
title: Configuración de relleno con C++
linktitle: Configuración de relleno
description: Aspose.Cells es una biblioteca C++ para trabajar con archivos de hojas de cálculo. Soporta establecer configuraciones de relleno de celdas, permitiendo a los usuarios personalizar el fondo y estilo de las celdas. Este artículo introducirá cómo usar la biblioteca Aspose.Cells para configurar el relleno de celdas.
keywords: Aspose.Cells, Celdas, Configuración de relleno, Fondo, Estilo
type: docs
weight: 50
url: /es/cpp/cells-fill-settings/
---

## **Colores y patrones de fondo**

Microsoft Excel puede establecer los colores de primer plano (contorno) y fondo (relleno) de las celdas y los patrones de fondo.

Aspose.Cells también admite estas características de manera flexible. En este tema, aprenderemos a usar estas características utilizando Aspose.Cells.

### **Estableciendo colores y patrones de fondo**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

La clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) tiene los métodos [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) y [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) que se utilizan para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) proporciona propiedades para establecer los colores de primer plano y fondo de las celdas. Aspose.Cells proporciona una enumeración [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) que contiene un conjunto de tipos predefinidos de patrones de fondo que se indican a continuación.

|**Patrones de fondo**|**Descripción**|
| :- | :- |
|DiagonalCrosshatch|Representa un patrón de entrecruzado diagonal|
|DiagonalStripe|Representa un patrón de rayas diagonales|
|Gray6|Representa un patrón gris del 6.25%|
|Gray12|Representa un patrón gris del 12.5%|
|Gray25|Representa un patrón gris del 25%|
|Gray50|Representa un patrón gris del 50%|
|Gray75|Representa un patrón gris del 75%|
|HorizontalStripe|Representa un patrón de rayas horizontales|
|None|Representa ningún fondo|
|ReverseDiagonalStripe|Representa un patrón de rayas diagonales inversas|
|Solid|Representa un patrón sólido|
|ThickDiagonalCrosshatch|Representa un patrón de entrecruzado diagonal grueso|
|ThinDiagonalCrosshatch|Representa un patrón de entrecruzado diagonal delgado|
|ThinDiagonalStripe|Representa un patrón de rayas diagonales delgado|
|ThinHorizontalCrosshatch|Representa un patrón de entrecruzado horizontal delgado|
|ThinHorizontalStripe|Representa un patrón de rayas horizontales delgado|
|ThinReverseDiagonalStripe|Representa un patrón de rayas diagonales inversas delgado|
|ThinVerticalStripe|Representa un patrón de rayas verticales delgado|
|VerticalStripe|Representa un patrón de rayas verticales|

En el ejemplo a continuación, el color de primer plano de la celda A1 está establecido pero A2 está configurada para tener tanto el color de primer plano como el color de fondo con un patrón de fondo de rayas verticales.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Define a Style and get the A1 cell style
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    // Setting the foreground color to yellow
    style.SetForegroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A1 cell
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    // Get the A2 cell style
    style = worksheet.GetCells().Get(u"A2").GetStyle();

    // Setting the foreground color to blue
    style.SetForegroundColor(Color::Blue());

    // Setting the background color to yellow
    style.SetBackgroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A2 cell
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Importante saber**

{{% alert color="primary" %}}

- Para establecer el color de primer plano o fondo de una celda, utilice las propiedades [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) o [**GetBackgroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundcolor/) del objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Ambas propiedades solo tendrán efecto si la propiedad [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) del objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) está configurada.
- La propiedad [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) establece el color de sombreado de la celda.
  La propiedad [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) especifica el tipo de patrón de fondo utilizado para el color de primer plano o fondo. Aspose.Cells proporciona una enumeración, [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/), que contiene un conjunto de tipos predefinidos de patrones de fondo.
- Si selecciona el valor *BackgroundType.None* de la enumeración [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/), el color de primer plano no se aplicará.
  Del mismo modo, el color de fondo no se aplicará si selecciona los valores *BackgroundType.None* o *BackgroundType.Solid*.
- Al recuperar el color de sombreado de la celda, si [**Style.GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) es *BackgroundType.None*, [**Style.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) devolverá *Color.Empty*.

{{% /alert %}}

### **Aplicar efectos de relleno de degradado**

Para aplicar sus efectos deseados de relleno de degradado a la celda, utilice el método [**SetTwoColorGradient**](https://reference.aspose.com/cells/cpp/aspose.cells/style/settwocolorgradient/) del objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) según corresponda.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::System;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(2, 1).PutValue(u"test");

    Cell cell = worksheet.GetCells().Get(u"B3");
    Style style = cell.GetStyle();
    style.SetIsGradient(true);
    style.SetTwoColorGradient(
        Color{ 0xFF, 0xFF, 0xFF, 0xFF },
        Color{ 0xFF, 0x4F, 0x81, 0xBD },
        GradientStyleType::Horizontal,
        1
    );

    style.GetFont().SetColor(Color::Red());
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    worksheet.GetCells().SetRowHeightPixel(2, 53);
    worksheet.GetCells().Merge(2, 1, 1, 2);

    workbook.Save(outDir + u"output.xlsx");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Colores y paleta**

Una paleta es el número de colores disponibles para utilizar en la creación de una imagen. El uso de una paleta estandarizada en una presentación permite al usuario crear un aspecto consistente. Cada archivo de Microsoft Excel (97-2003) tiene una paleta de 56 colores que se pueden aplicar a celdas, fuentes, líneas de cuadrícula, objetos gráficos, rellenos y líneas en un gráfico.

Con Aspose.Cells es posible no solo utilizar los colores existentes de la paleta, sino también colores personalizados. Antes de utilizar un color personalizado, agréguelo primero a la paleta.

Este tema trata sobre cómo agregar colores personalizados a la paleta.

### **Agregar colores personalizados a la paleta**

Aspose.Cells soporta la paleta de colores de Microsoft Excel con 56 colores. Para utilizar un color personalizado que no está definido en la paleta, agregue el color a la paleta.

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) proporciona un método [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) que toma los siguientes parámetros para agregar un color personalizado y modificar la paleta:

- Color personalizado, el color personalizado que se agregará.
- Índice, el índice del color en la paleta que el color personalizado reemplazará. Debe estar entre 0-55.

El siguiente ejemplo agrega un color personalizado (Orchid) a la paleta antes de aplicarlo a una fuente.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid color is now in the palette
    std::cout << "Is Orchid in palette after change: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

La paleta solo contiene 56 colores. Cuando agrega un color personalizado a la paleta, la paleta cambia y cualquier elemento en el archivo formateado con el color anterior cambia. Por lo tanto, tenga mucho cuidado al cambiar la paleta. Además, esta es una limitación solo en el formato de archivo XLS (Excel 97 - 2003) ya que no hay tal limitación para formatos de archivo XLSX o más avanzados de MS Excel (2007/2010 o 2013).

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
