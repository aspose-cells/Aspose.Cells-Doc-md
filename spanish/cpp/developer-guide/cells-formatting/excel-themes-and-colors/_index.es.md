---
title: Temas y colores de Excel con C++
linktitle: Temas y colores de Excel
type: docs
weight: 100
url: /es/cpp/excel-themes-and-colors/
description: Código C++ para usar el esquema de colores de Excel con la API Aspose.Cells for C++
keywords: C++ para crear y aplicar esquemas de colores, crear un esquema de colores personalizado programáticamente, cómo aplicar un esquema de color personalizado, cómo usar el esquema de colores en Excel con C++
---

## **Cómo aplicar y crear un esquema de colores en Excel**
Los temas de documento facilitan la coordinación de colores, fuentes y efectos de formato gráfico de los documentos de Excel y su actualización rápida. 
Los temas proporcionan un aspecto unificado con estilos nombrados, efectos gráficos y otros objetos utilizados en un libro. Por ejemplo, el estilo Acento 1, se ve diferente en los temas Oficina y Apex. A menudo, aplicas un tema de documento y luego lo modificas según tus preferencias.

### **Cómo aplicar un esquema de colores en Excel**
1. Abre Excel y ve a la pestaña "Diseño de página" en la cinta de opciones de Excel.
1. Haz clic en el botón "Colores" en la sección de "Temas".
<br>
<img src="color.png" width=70% />
1. Elige una paleta de colores que se ajuste a tus requisitos o pasa el cursor sobre un esquema para ver una vista previa en vivo.

### **Cómo crear un esquema de colores personalizado en Excel**
Puedes crear tu propio conjunto de colores para darle a tu documento un aspecto fresco y único o cumplir con los estándares de marca de tu organización.

1. Abre Excel y ve a la pestaña "Diseño de página" en la cinta de opciones de Excel.
1. Haz clic en el botón "Colores" en la sección de "Temas".
1. Haz clic en el botón "Personalizar colores...".
<br>
<img src="color2.png" width=70% />

1. En el cuadro de diálogo "Crear nuevos colores de tema", puedes seleccionar colores para cada elemento haciendo clic en las listas desplegables de colores junto a ellos. Puedes elegir colores de la paleta o definir colores personalizados usando la opción "Más colores".
<br>
<img src="color3.png" width=70% />
1. Después de seleccionar todos los colores deseados, proporciona un nombre para tu esquema de colores personalizado en el campo de "Nombre".

1. Haz clic en el botón "Guardar" para guardar tu esquema de colores personalizado. Ahora tu esquema de colores personalizado estará disponible en el menú desplegable de "Colores" para uso futuro.

## **Cómo crear y aplicar un esquema de colores en Aspose.Cells**
Aspose.Cells proporciona funciones para personalizar temas y colores.

### **Cómo crear un tema de colores personalizado en Aspose.Cells**
Si se utilizan colores de tema en el archivo, no es necesario modificar cada celda individualmente, solo necesitamos modificar los colores en el tema.

El siguiente ejemplo muestra cómo aplicar temas personalizados con tus colores deseados. Usamos un archivo de plantilla de ejemplo creado manualmente en Microsoft Excel 2007.

El siguiente ejemplo carga un archivo XLSX de plantilla, define colores para diferentes tipos de colores de tema, aplica los colores personalizados y guarda el archivo de Excel.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Define Color array (of 12 colors) for Theme
    Vector<Aspose::Cells::Color> carr(12);
    carr[0] = Color::AntiqueWhite(); // Background1
    carr[1] = Color::Brown();       // Text1
    carr[2] = Color::AliceBlue();   // Background2
    carr[3] = Color::Yellow();      // Text2
    carr[4] = Color::YellowGreen(); // Accent1
    carr[5] = Color::Red();         // Accent2
    carr[6] = Color::Pink();        // Accent3
    carr[7] = Color::Purple();      // Accent4
    carr[8] = Color::PaleGreen();   // Accent5
    carr[9] = Color::Orange();      // Accent6
    carr[10] = Color::Green();      // Hyperlink
    carr[11] = Color::Gray();       // Followed Hyperlink

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Instantiate a Workbook and open the template file
    Workbook workbook(inputFilePath);

    // Set the custom theme with specified colors
    workbook.CustomTheme(u"CustomeTheme1", carr);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Save as the excel file
    workbook.Save(outputFilePath);

    std::cout << "Custom theme applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Cómo aplicar colores de tema en Aspose.Cells**

El siguiente ejemplo aplica colores de primer plano y fuente de una celda basados en los tipos de colors de tema predeterminados (del libro de trabajo). También guarda el archivo de Excel en disco.

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

    // Create workbook
    Workbook workbook;

    // Get cells collection in the first (default) worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Get the D3 cell
    Cell c = cells.Get(u"D3");

    // Get the style of the cell
    Style s = c.GetStyle();

    // Set foreground color for the cell from the default theme Accent2 color
    s.SetForegroundThemeColor(ThemeColor(ThemeColorType::Accent2, 0.5));

    // Set the pattern type
    s.SetPattern(BackgroundType::Solid);

    // Get the font for the style
    Font f = s.GetFont();

    // Set the theme color
    f.SetThemeColor(ThemeColor(ThemeColorType::Accent4, 0.1));

    // Apply style
    c.SetStyle(s);

    // Put a value
    c.PutValue(u"Testing1");

    // Save the excel file
    workbook.Save(outDir + u"output.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Cómo obtener y establecer colores de tema en Aspose.Cells**
 A continuación se presentan algunos métodos y propiedades que implementan los colores de tema.

- [**Style.GetForegroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundthemecolor/): Utilizado para establecer el color de primer plano.
- [**Style.GetBackgroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundthemecolor/): Utilizado para establecer el color de fondo.
- [**Font.GetThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getthemecolor/): Utilizado para establecer el color de fuente.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getthemecolor/): Utilizado para obtener un color de tema.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setthemecolor/): Utilizado para establecer un color de tema.

El siguiente ejemplo muestra cómo obtener y establecer colores de tema.

El siguiente ejemplo utiliza un archivo XLSX de plantilla, obtiene los colores para diferentes tipos de colores de tema, cambia los colores y guarda el archivo de Microsoft Excel.

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
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Background1 theme color
    Color c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the color
    std::cout << "theme color Background1: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Get the Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the color
    std::cout << "theme color Accent2: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Background1 theme color
    workbook.SetThemeColor(ThemeColorType::Background1, Color::Red());

    // Get the updated Background1 theme color
    c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the updated color for confirmation
    std::cout << "theme color Background1 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Accent2 theme color
    workbook.SetThemeColor(ThemeColorType::Accent2, Color::Blue());

    // Get the updated Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the updated color for confirmation
    std::cout << "theme color Accent2 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Save the updated file
    workbook.Save(outputFilePath);

    std::cout << "Theme colors updated and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Extraer datos de tema del archivo de Excel](/cells/es/cpp/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="cpp" >}}
