---
title: Filtrado de datos con C++
linktitle: Filtrado de Datos
type: docs
weight: 85
url: /es/cpp/data-filtering/
description: Aprende cómo agregar un filtro de datos usando la API Aspose.Cells for C++.
keywords: Agregar filtro por color, agregar filtros de fecha, agregar filtros de números, agregar filtro dinámico, agregar filtros de texto, agregar filtro personalizado con Contiene, agregar filtro personalizado con NoContiene, agregar filtro personalizado con ComienzaCon, agregar filtro personalizado con TerminaCon
---

{{% alert color="primary" %}}

Microsoft Excel proporciona algunas funciones buenas para el autofiltrado de datos en hojas de trabajo. Aspose.Cells es compatible completamente con las funciones de autofiltrado de Microsoft Excel. Este artículo explica cómo usar las funciones en Microsoft Excel y cómo codificarlas usando Aspose.Cells.

{{% /alert %}}

## **Datos de Autofiltro**

El autofiltrado es la forma más rápida de seleccionar solo aquellos elementos de la hoja de cálculo que desea mostrar en una lista. La función de autofiltro permite a los usuarios filtrar elementos en una lista según un criterio establecido. Filtrar según texto, números o fechas.

### **Autofiltro en Microsoft Excel**

Para activar la función de autofiltro en Microsoft Excel:

1. Haz clic en la fila de encabezado en una hoja de cálculo.
1. Desde el menú **Datos**, selecciona **Filtrar** y luego **Autofiltro**.

Cuando aplicas un autofiltro a una hoja de cálculo, aparecen interruptores de filtro (flechas negras) a la derecha de los encabezados de las columnas.

1. Haz clic en una flecha de filtro para ver una lista de opciones de filtro.

Algunas de las opciones de autofiltro son:

|**Opciones**|**Descripción**|
| :- | :- |
|All|Mostrar todos los elementos en la lista una vez.|
|Custom|Personalizar criterios de filtro como contiene/no contiene|
|Filter by Color|Filtros basados en el color rellenado|
|Date Filters|Filtrar filas basadas en diferentes criterios en la fecha|
|Number Filters|Diferentes tipos de filtro en números como comparación, promedios y Top 10, etc.|
|Text Filters|Diferentes filtros como comienza con, termina con, contiene, etc,|
|Blanks/Non Blanks|Estos filtros pueden implementarse a través de Filtro de Texto en Blanco|

Los usuarios filtran manualmente sus datos de hoja de cálculo en Microsoft Excel utilizando estas opciones.

### **Autofiltro con Aspose.Cells**

Aspose.Cells proporciona una clase, `Workbook` que representa un archivo de Excel. La clase `Workbook` contiene una colección `Worksheets` que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase `Worksheet`. La clase `Worksheet` ofrece una amplia gama de propiedades y métodos para administrar hojas de cálculo. Para crear un autofiltro, use la propiedad `AutoFilter` de la clase `Worksheet`. La propiedad `AutoFilter` es un objeto de la clase `AutoFilter`, que proporciona la propiedad `Range` para especificar el rango de celdas que conforman una fila de encabezado. Se aplica un autofiltro al rango de celdas que es la fila de encabezado.

En cada hoja de cálculo, solo puede especificar un rango de filtro. Esto está limitado por Microsoft Excel. Para filtrado de datos personalizado, use el método `AutoFilter.Custom`.

En el ejemplo dado a continuación, hemos creado el mismo Autofiltro utilizando Aspose.Cells como lo creamos utilizando Microsoft Excel en la sección anterior.

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
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range of the heading row
    worksheet.GetAutoFilter().SetRange(u"A1:B1");

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Diferentes tipos de filtro**

Aspose.Cells ofrece múltiples opciones para aplicar diferentes tipos de filtros como Filtro de Color, Filtro de Fecha, Filtro de Número, Filtro de Texto, Filtros en Blanco y Filtros no en Blanco.

##### **Color de relleno**

Aspose.Cells proporciona una función `AddFillColorFilter` para filtrar datos basándose en el color de relleno de las celdas. En el ejemplo a continuación, se utiliza un archivo plantilla que tiene diferentes colores de relleno en la primera columna de la hoja para probar la función de filtrado por color. Los archivos de muestra se pueden descargar de los siguientes enlaces.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

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

    // Instantiating a Workbook object
    Workbook workbook(srcDir + u"ColouredCells.xlsx");

    // Instantiating a CellsColor object for foreground color
    CellsColor clrForeground = workbook.CreateCellsColor();
    clrForeground.SetColor(Color::Red());

    // Instantiating a CellsColor object for background color
    CellsColor clrBackground = workbook.CreateCellsColor();
    clrBackground.SetColor(Color::White());

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddFillColorFilter function to apply the filter
    worksheet.GetAutoFilter().AddFillColorFilter(0, BackgroundType::Solid, clrForeground, clrBackground);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredColouredCells.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Fecha**

Se pueden implementar diferentes tipos de filtros de fechas, como filtrar todas las filas con fechas en enero de 2018. El código de ejemplo siguiente demuestra este filtro usando la función `AddDateFilter`. Los archivos de muestra se proporcionan a continuación.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddDateFilter function to apply the filter
    worksheet.GetAutoFilter().AddDateFilter(0, DateTimeGroupingType::Month, 2018, 1, 0, 0, 0, 0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Date filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Fecha dinámica**

A veces se requieren filtros dinámicos basados en fechas, como todas las celdas con fechas en enero, independientemente del año. En este caso, se utiliza la función `DynamicFilter` como se muestra en el siguiente código de ejemplo. Los archivos de muestra se proporcionan a continuación.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDynamicDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call DynamicFilter function to apply the filter
    worksheet.GetAutoFilter().Dynamic_Filter(0, DynamicFilterType::January);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Dynamic filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Número**

Se pueden aplicar filtros personalizados usando Aspose.Cells, como seleccionar celdas que contienen números en un rango dado. El ejemplo siguiente demuestra el uso de la función `Custom()` para filtrar números. Los archivos de muestra se proporcionan a continuación.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

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
    U16String inputFilePath = srcDir + u"Number.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"FilteredNumber.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Custom function to apply the filter
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::GreaterOrEqual, 5, true, FilterOperatorType::LessOrEqual, 10);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Texto**

Si una columna contiene texto y se desean seleccionar celdas que contienen un texto en particular, se puede usar la función `Filter()`. En el ejemplo siguiente, el archivo plantilla contiene una lista de países y se debe seleccionar la fila que contiene un nombre de país en particular. El código siguiente demuestra cómo filtrar texto. Los archivos de muestra se proporcionan a continuación.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

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
    U16String inputFilePath = srcDir + u"Text.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredText.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Filter function to apply the filter
    worksheet.GetAutoFilter().Filter(0, u"Angola");

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Vacíos**

Si una columna contiene texto y algunas celdas están en blanco, y se requiere filtrar solo aquellas filas donde hay celdas en blanco, se puede usar la función `MatchBlanks()` como se muestra a continuación. Los archivos de muestra se proporcionan a continuación.

1. [EnBlanco.xlsx](72417324.xlsx)
1. [EnBlancoFiltrado.xlsx](72417325.xlsx)

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
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredBlank.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **No vacíos**

Cuando se quieren filtrar celdas que contienen cualquier texto, use la función `MatchNonBlanks` como se demuestra a continuación. Los archivos de muestra se proporcionan a continuación.

1. [EnBlanco.xlsx](72417324.xlsx)
1. [NoVaciosFiltrado.xlsx](72417326.xlsx)

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

    // Create workbook object and open the Excel file
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchNonBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outDir + u"FilteredNonBlank.xlsx");

    std::cout << "Non-blank filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Filtro personalizado con Contiene**

Excel proporciona filtros personalizados como filtrar filas que contienen alguna cadena específica. Esta función está disponible en Aspose.Cells y se demuestra a continuación filtrando los nombres en el archivo de muestra. Se proporcionan archivos de ejemplo a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::Contains, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Filtro personalizado con NoContiene**

Excel proporciona filtros personalizados como filtrar filas que no contienen alguna cadena específica. Esta función está disponible en Aspose.Cells y se demuestra a continuación filtrando los nombres en el archivo de muestra proporcionado a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::NotContains, u"Be");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File filtered and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Filtro personalizado que comienza con**

Excel proporciona filtros personalizados como filtrar filas que comienzan con una cadena específica. Esta función está disponible en Aspose.Cells y se demuestra a continuación filtrando los nombres en el archivo de muestra proporcionado a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows starting with string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Filtro personalizado que termina con**

Excel proporciona filtros personalizados como filtrar filas que terminan con cierta cadena específica. Esta función está disponible en Aspose.Cells y se muestra a continuación filtrando los nombres en el archivo de muestra proporcionado a continuación.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows end with string "ia"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"ia");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Aplicar Filtro Avanzado de Microsoft Excel para Mostrar Registros que Cumplen Criterios Complejos](/cells/es/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro](/cells/es/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
