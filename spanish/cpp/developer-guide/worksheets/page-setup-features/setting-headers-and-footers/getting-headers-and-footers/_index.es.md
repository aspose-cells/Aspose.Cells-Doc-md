---
title: Obteniendo encabezados o pies de página con C++
linktitle: Obteniendo Encabezados o Pies de Página
type: docs
weight: 30
url: /es/cpp/get-headers-or-footers/
description: Este artículo explica cómo obtener programáticamente encabezados y pies de página de archivos de Excel u OpenOffice usando la API o biblioteca en C++.
---

{{% alert color="primary" %}}

Los encabezados y pies de página se muestran solo en la vista Diseño de página, en la vista previa de impresión y en las páginas impresas. 

También puedes usar el cuadro de diálogo Configurar página si deseas ver encabezados o pies de página para más de una hoja de cálculo a la vez. 

Para otros tipos de hojas, como hojas de gráficos o gráficos, solo puedes insertar encabezados y pies de página mediante el cuadro de diálogo Configurar página.

{{% /alert %}}

## **Obteniendo Encabezados y Pies de Página en MS Excel**
1. Haz clic en la hoja de cálculo donde deseas ver o cambiar los encabezados o pies de página.
2. En la pestaña Vista, en el grupo Vistas del libro, haga clic en Diseño de página.
  Excel muestra la hoja de cálculo en la vista Diseño de página.
3. Para ver o editar un encabezado o pie de página, haz clic en el cuadro de texto de encabezado o pie de página izquierdo, central o derecho en la parte superior o inferior de la página de la hoja de cálculo (debajo de Encabezado, o encima de Pie de página).


## **Obteniendo encabezados y pies de página usando Aspose.Cells for C++**
Con los métodos [**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheader/) y [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfooter/), los desarrolladores en C++ pueden simplemente obtener encabezados o pies de página del archivo.

1. Construir un libro de trabajo para abrir el archivo.
2. Obtiene la hoja de cálculo donde deseas obtener encabezados o pie de página.
3. Obtiene el encabezado o pie de página con un identificador de sección específico.

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook workbook(srcDir + u"HeaderFooter.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    std::cout << sheet.GetPageSetup().GetHeader(0).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(1).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(2).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetFooter(1).ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Analizar Encabezados y Pies de Página para Lista de Comandos**
El texto del encabezado o pie de página puede contener  comandos especiales, por ejemplo, un marcador de posición para el número de página, la fecha actual o atributos de formato de texto.

Los comandos especiales están representados por una sola letra con un símbolo ampersand inicial ("&").

Las cadenas de encabezado y pie de página se construyen usando la gramática ABNF. No es fácil de entender sin un visor.

Aspose.Cells for C++ proporciona el método [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcommands/) para analizar encabezados y pies de página como una lista de comandos.

El siguiente código muestra cómo analizar encabezados o pies de página como lista de comandos y procesar los comandos:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"HeaderFooter.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get left section of header
    U16String headerSection = sheet.GetPageSetup().GetHeader(0);

    // Get commands from the header section
    Vector<HeaderFooterCommand> commands = sheet.GetPageSetup().GetCommands(headerSection);

    // Iterate through each command
    for (int i = 0; i < commands.GetLength(); ++i)
    {
        HeaderFooterCommand c = commands[i];
        switch (c.GetType())
        {
            case HeaderFooterCommandType::SheetName:
                // Embedded the name of the sheet to header or footer
                break;
            default:
                break;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
