---
title: Fuente de tema de encabezados y cuerpo con C++
linktitle: Fuente de tema para encabezados y cuerpo
description: Aspose.Cells es una biblioteca C++ para trabajar con archivos de hojas de cálculo. Soporta establecer fuentes de tema para encabezados y cuerpo en documentos de Excel, permitiendo a los usuarios personalizar la apariencia y estilo del documento. Este artículo mostrará cómo usar la biblioteca Aspose.Cells para trabajar con fuentes de tema en encabezados y cuerpo en documentos de Excel.
keywords: Aspose.Cells, Documento de Excel, Encabezado, Cuerpo, Fuente de tema, Apariencia, Estilo
type: docs
weight: 120
url: /es/cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

La fuente predeterminada cambiará automáticamente cuando se modifique la configuración regional.

Si se cambia la fuente predeterminada, también se cambiará la altura de la fila y el ancho de la columna e incluso puede desconfigurar el diseño de la página.

¿Qué causó el cambio de la fuente predeterminada?

Si se establece una fuente de tema de Excel, Excel cambiará automáticamente entre fuentes diferentes según el entorno de idioma actual.

{{% /alert %}}

## **Fuente de tema para encabezados y cuerpo en Excel**

En Excel, selecciona la pestaña Inicio, haz clic en la caja desplegable de fuente, verás "Fuentes de tema" con dos fuentes de tema: Calibri Light (Encabezados) y Calibri (Cuerpo) en la parte superior con la configuración regional en inglés.

**![Fuentes del tema](Theme-Fonts.png)**

Si se selecciona Fuente de tema, el nombre de la fuente se mostrará de manera diferente en diferentes regiones.
Si no deseas que la fuente cambie automáticamente en diferentes regiones, no selecciones las dos Fuentes de tema.

## **Cambiar fuentes de encabezados y cuerpo de forma programática**
Con Aspose.Cells for C++, podemos verificar si la fuente predeterminada es una fuente de tema o establecer la fuente de tema con la propiedad [**Font.GetSchemeType()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getschemetype/).

El siguiente código de muestra muestra cómo manipular la fuente del tema de forma programática.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook(u"Book1.xlsx");

    // Get the default style
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the font scheme type
    FontSchemeType schemeType = defaultStyle.GetFont().GetSchemeType();

    // Check if the font is a theme font
    if (schemeType == FontSchemeType::Major || schemeType == FontSchemeType::Minor)
    {
        std::cout << "It's theme font" << std::endl;
    }

    // Change theme font to normal font
    defaultStyle.GetFont().SetSchemeType(FontSchemeType::None);

    // Set the modified default style back to the workbook
    workbook.SetDefaultStyle(defaultStyle);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Obtiene dinámicamente la fuente del tema local de forma programática**
A veces, nuestros servidores y las máquinas de los usuarios no están en la misma región. ¿Cómo podemos obtener la misma fuente que los usuarios desean para el procesamiento de archivos?

Debemos configurar las configuraciones regionales del sistema antes de cargar el archivo con la propiedad [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getregion/).

El siguiente ejemplo de código muestra cómo obtener la fuente de tema local.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new LoadOptions
    LoadOptions options;

    // Set the customer's region to Japan
    options.SetRegion(CountryCode::Japan);

    // Instantiate a new Workbook with the specified options
    Workbook workbook(u"Book1.xlsx", options);

    // Get the default style of the workbook
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the customer's local font name
    U16String localFontName = defaultStyle.GetFont().GetName();

    std::cout << "Local Font Name: " << localFontName.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
