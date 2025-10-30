---
title: Mostrar y ocultar hojas de trabajo y pestañas con C++
linktitle: Mostrar y Ocultar Hojas de Cálculo y Pestañas
type: docs
weight: 10
url: /es/cpp/show-and-hide-worksheets-and-tabs/
description: Este artículo proporciona código de ejemplo para usar la API o biblioteca C++ para mostrar y ocultar programáticamente una hoja de cálculo de Excel. Además, cómo mostrar y ocultar pestañas de libros de Excel.
---

{{% alert color="primary" %}}

Aspose.Cells permite al usuario mostrar y ocultar elementos de un libro de trabajo, incluidas las hojas de cálculo y las pestañas.

{{% /alert %}}

## **Mostrar y ocultar una hoja de cálculo**

Un archivo de Excel puede tener una o más hojas de cálculo. Siempre que creamos un archivo de Excel, agregamos hojas de cálculo al archivo de Excel en el que trabajamos. Cada hoja de cálculo en un archivo de Excel es independiente de las demás hojas de cálculo al tener sus propios datos, configuraciones de formato, etc. A veces, los desarrolladores pueden necesitar ocultar algunas hojas de cálculo y mostrar otras en el archivo de Excel por su propio interés. Entonces, **Aspose.Cells** permite a los desarrolladores controlar la visibilidad de las hojas de cálculo en sus archivos de Excel.

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de trabajo en el archivo Excel.

Una hoja de trabajo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ofrece una amplia variedad de propiedades y métodos para gestionar hojas de trabajo. Para controlar la visibilidad de una hoja de trabajo, use la propiedad [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) es una propiedad booleana, lo que significa que solo puede almacenar un valor **verdadero** o **falso**.

### **Hacer visible una hoja de cálculo**

Haz visible una hoja de trabajo configurando la propiedad [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) a **true**.

### **Ocultar una hoja de trabajo**

Oculta una hoja de trabajo configurando la propiedad [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) a **false**.

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

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the first worksheet of the Excel file
    worksheet.SetIsVisible(false);

    // Save the modified Excel file in default (Excel 2003) format
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Worksheet hidden and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Mostrar y Ocultar Pestañas**

Si observas detenidamente en la parte inferior de un archivo de Microsoft Excel, verás una serie de controles. Estos incluyen:

- Pestañas de hojas.
- Botones de desplazamiento de pestañas.

Las pestañas de hojas representan las hojas de cálculo en el archivo de Excel. Haz clic en cualquier pestaña para cambiar a esa hoja de cálculo. Cuantas más hojas de cálculo tenga el libro, más pestañas de hojas habrá. Si el archivo de Excel tiene un buen número de hojas de cálculo, necesitas botones para navegar a través de ellas. Por lo tanto, Microsoft Excel proporciona botones de desplazamiento de pestañas para desplazarse por las pestañas de hojas.

Utilizando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de las pestañas de hojas y los botones de desplazamiento en archivos de Excel.

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) ofrece una amplia gama de propiedades y métodos para administrar un archivo de Excel. Para controlar la visibilidad de las pestañas en un archivo de Excel, los desarrolladores pueden usar la propiedad [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) de la clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) es una propiedad Booleana, lo que significa que solo puede almacenar un valor de **true** o **false**.

### **Hacer pestañas visibles**

Haz visibles las pestañas con la propiedad [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) de la clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) configurada a **true**.

### **Ocultar pestañas**

Oculta las pestañas en un archivo de Excel configurando la propiedad [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) de la clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) a **false**.

A continuación, se muestra un ejemplo completo que abre un archivo de Excel (book1.xls), oculta sus pestañas y guarda el archivo modificado como output.xls. Después de la ejecución del código, verás que las pestañas del libro están ocultas.

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
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Hiding the tabs of the Excel file
    settings.SetShowTabs(false);

    // Shows the tabs of the Excel file
    // settings.SetShowTabs(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Controlando el Ancho de la Barra de Pestañas**

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
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Show tabs in the Excel file
    settings.SetShowTabs(true);

    // Adjust the sheet tab bar width
    settings.SetSheetTabBarWidth(800);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
