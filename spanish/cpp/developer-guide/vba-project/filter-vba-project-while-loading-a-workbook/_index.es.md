---
title: Filtrar proyecto VBA al cargar un libro con C++
linktitle: Filtrar proyecto VBA al cargar un libro de trabajo
type: docs
weight: 140
url: /es/cpp/filter-vba-project-while-loading-a-workbook/
description: Aprenda cómo filtrar proyectos VBA al cargar un libro de Excel usando Aspose.Cells con C++.
---

## **Filtrar proyecto VBA al cargar un libro de Excel en C++**

Algunos archivos .xlsm/.xslb contienen una cantidad extremadamente grande de macros (o macros muy, muy largas). Aspose.Cells cargará incondicionalmente estos datos (meta) al abrir dichos libros. Es posible que necesite controlar esto mediante [**LoadDataFilterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions) cuando solo necesite extraer nombres de hojas para una gran cantidad de libros, omitiendo así contenido no necesario. Este filtro se proporciona mediante la introducción de una nueva opción, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions).

## **Código de muestra**

El siguiente código de muestra carga un libro de trabajo de manera que solo VBA está filtrado. Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Set the load options, we do not want to load VBA
    LoadOptions loadOptions(LoadFormat::Auto);
    LoadFilter loadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::VBA);
    loadOptions.SetLoadFilter(&loadFilter);

    // Create workbook object from sample excel file using load options
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleMacroEnabledWorkbook.xlsm";
    Workbook book(inputFilePath, loadOptions);

    // Save the output in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    U16String outputFilePath = outputDir + u"OutputSampleMacroEnabledWorkbook.xlsm";
    book.Save(outputFilePath, SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
