---
title: Cargar archivo de Excel origen sin gráficos con C++
linktitle: Cargar archivo de Excel de origen sin gráficos
type: docs
weight: 420
url: /es/cpp/load-source-excel-file-without-charts/
description: Aprenda cómo cargar un archivo de Excel sin gráficos usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells le permite cargar su archivo de Excel sin gráficos. Por favor, utilice la propiedad [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) para este fin.

{{% /alert %}}

## **Cargar hojas de cálculo específicas en un libro de Excel**

El siguiente código de ejemplo carga el archivo de Excel de muestra sin gráficos y lo guarda en formato PDF de salida.

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

    // Specify the load options and filter the data
    LoadOptions options;

    // Include everything except charts
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xlsx";

    // Load the workbook with specified load options
    Workbook workbook(inputFilePath, options);

    // Path of output PDF file
    U16String outputFilePath = outDir + u"ResultWithoutChart.pdf";

    // Save the workbook in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully without charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
