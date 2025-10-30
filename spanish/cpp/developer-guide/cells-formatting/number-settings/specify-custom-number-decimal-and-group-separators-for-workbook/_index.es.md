---
title: Especificar separadores personalizados de decimales y agrupación para Libros de trabajo con C++
linktitle: Especificar separadores personalizados de decimales y agrupación
type: docs
weight: 110
url: /es/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Cambiar el separador decimal y de grupo en MS Excel y con código C++ usando la API Aspose.Cells for C++.
keywords: especificar separador decimal personalizado en excel, especificar separador decimal personalizado en excel c++, especificar separador de grupo personalizado en excel, especificar separador de grupo personalizado en excel c++, especificar separador decimal y de grupo personalizados en excel, especificar separador decimal y de grupo en excel c++, cambiar separador decimal en excel, cambiar separador de grupo en excel, cambiar separador decimal en excel c++, cambiar separador de grupo en excel c++
---

{{% alert color="primary" %}}

En Microsoft Excel, puedes especificar los Separadores de Decimales y Miles Personalizados en lugar de usar Separadores de Sistema de las **Opciones Avanzadas de Excel** como se muestra en la captura de pantalla a continuación.

Aspose.Cells proporciona las propiedades [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumberdecimalseparator/) y [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) para establecer los separadores personalizados para el formato/análisis de números.

{{% /alert %}}

## **Especificar Separadores Personalizados usando Microsoft Excel**

La siguiente captura de pantalla muestra las **Opciones Avanzadas de Excel** y destaca la sección para especificar los **Separadores Personalizados**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Especificar Separadores Personalizados usando Aspose.Cells**

El siguiente código de ejemplo ilustra cómo especificar los separadores personalizados utilizando la API de Aspose.Cells. Especifica los Separadores de Decimal y Grupo Personalizados como punto y espacio, respectivamente.

### Código en C++ para especificar separadores personalizados de decimal y grupo

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

    // Create a new workbook
    Workbook workbook;

    // Specify custom separators
    workbook.GetSettings().SetNumberDecimalSeparator(u'.');
    workbook.GetSettings().SetNumberGroupSeparator(u' ');

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell value
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(123456.789);

    // Set custom cell style
    Style style = cell.GetStyle();
    style.SetCustom(u"#,##0.000;[Red]#,##0.000", true);
    cell.SetStyle(style);

    // Auto-fit columns
    worksheet.AutoFitColumns();

    // Save workbook as PDF
    workbook.Save(outDir + u"CustomSeparator_out.pdf");

    std::cout << "Workbook saved successfully with custom separators!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
