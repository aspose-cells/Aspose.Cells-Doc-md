---
title: Establece el ancho de columna en unidades escalables como em o porcentaje con C++
linktitle: Establezca el ancho de columna en una unidad escalable como em o porcentaje
type: docs
weight: 130
url: /es/cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Aprende cómo establecer el ancho de columna en unidades escalables como em o porcentaje usando Aspose.Cells for C++.
---

Generar un archivo HTML a partir de una hoja de cálculo es muy común. El tamaño de las columnas está definido en "pt", lo cual funciona en muchos casos. Sin embargo, puede haber casos en los que no se requiera este tamaño fijo. Por ejemplo, si el ancho de un panel contenedor es de 600px donde se muestra esta página HTML. En este caso, es posible que aparezca una barra de desplazamiento horizontal si el ancho de la tabla generada es mayor. Es necesario cambiar este tamaño fijo a una unidad escalable como em o porcentaje para obtener una mejor presentación. El siguiente código de ejemplo se puede utilizar donde [**HtmlSaveOptions.GetWidthScalable()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getwidthscalable/) se establece como **true** para crear un ancho escalable.

Se pueden descargar archivos fuente de muestra y archivos de salida desde los siguientes enlaces:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

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

    // Load sample source file
    Workbook wb(srcDir + u"sampleForScalableColumns.xlsx");

    // Specify Html Save Options
    HtmlSaveOptions options;

    // Set the property for scalable width
    options.SetWidthScalable(true);

    // Specify image save format
    options.SetExportImagesAsBase64(true);

    // Save the workbook in Html format with specified Html Save Options
    wb.Save(outDir + u"outsampleForScalableColumns.html", options);

    std::cout << "Workbook saved successfully with scalable columns!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
