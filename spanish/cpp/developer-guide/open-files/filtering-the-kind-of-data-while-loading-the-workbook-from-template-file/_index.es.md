---
title: Filtrado del tipo de datos al cargar el libro desde un archivo de plantilla con C++
linktitle: Filtrar datos al cargar un libro de Excel
type: docs
weight: 400
url: /es/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Aprenda cómo filtrar tipos específicos de datos al cargar un libro desde un archivo de plantilla usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A veces, desea especificar qué tipo de datos debe cargarse al construir el libro desde el archivo de plantilla. El filtrado de datos cargados puede mejorar el rendimiento para su propósito especial, especialmente al usar las API de [LightCells](/cells/es/cpp/using-lightcells-api/). Por favor, use la propiedad [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) para este propósito.

{{% /alert %}}

El siguiente código de muestra carga solo objetos de forma al cargar el libro desde el [archivo de plantilla](5115552.xlsx) que puede descargar desde el enlace dado. La siguiente captura de pantalla muestra los contenidos del [archivo de plantilla](5115552.xlsx) y también explica que los datos de color rojo y fondo amarillo no se cargarán porque se ha ajustado la propiedad [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) a [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La siguiente captura de pantalla muestra el [PDF de salida](5115555.pdf) que puede descargar desde el enlace dado. Aquí puede ver que los datos de color rojo y fondo amarillo no están presentes pero todas las formas sí lo están.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

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

    // Set the load options, we only want to load shapes and do not want to load data
    LoadOptions loadOptions(LoadFormat::Xlsx);
    loadOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Create workbook object from sample excel file using load options
    Workbook workbook(srcDir + u"sampleFilterChars.xlsx", loadOptions);

    // Save the output in pdf format
    workbook.Save(outDir + u"sampleFilterChars_out.pdf", SaveFormat::Pdf);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
