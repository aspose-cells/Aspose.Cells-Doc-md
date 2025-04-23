---
title: Implementar el sistema de fechas 1904 con C++
linktitle: Implementar el sistema de fecha 1904
description: Aspose.Cells es una biblioteca C++ para trabajar con archivos de hojas de cálculo. Soporta la implementación del sistema de fechas 1904, permitiendo a los usuarios calcular y formatear basado en el sistema de fechas del 1 de enero de 1904. Este artículo explica cómo implementar el sistema de fechas 1904 usando la biblioteca Aspose.Cells.
keywords: Aspose.Cells, sistema de fecha 1904, hoja de cálculo, cálculo, formato
type: docs
weight: 7000
url: /es/cpp/implement-1904-date-system/
---

{{% alert color="primary" %}}

Microsoft Excel soporta dos sistemas de fecha: el sistema de fecha 1900 (el sistema de fecha predeterminado implementado en Excel para Windows) y el sistema de fecha 1904. El sistema de fecha 1904 se utiliza normalmente para proporcionar compatibilidad con los archivos de Excel para Macintosh y es el sistema predeterminado si estás usando Excel para Macintosh. Puedes establecer el sistema de fecha 1904 para los archivos de Excel usando Aspose.Cells.

{{% /alert %}}

Para implementarlo en Microsoft Excel (por ejemplo, Microsoft Excel 2003):

1. Desde el menú **Herramientas**, selecciona **Opciones**, y elige la pestaña **Cálculo**.
1. Selecciona la opción **Sistema de fecha 1904**.
1. Haz clic en **Aceptar**.

|**Seleccionar el sistema de fecha 1904 en Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|
Consulta el siguiente código de muestra sobre cómo lograr esto usando las API de Aspose.Cells.

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
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Mybook.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Implement 1904 date system
    WorkbookSettings settings = workbook.GetSettings();
    settings.SetDate1904(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully with 1904 date system!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
