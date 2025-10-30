---
title: Especificar conjunto individual o privado de fuentes para la renderización del libro de trabajo con C++
linktitle: Especificar un Conjunto Individual o Privado de Fuentes para la Representación del Libro
type: docs
weight: 40
url: /es/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Aprende cómo especificar un conjunto individual o privado de fuentes para la renderización del libro de trabajo usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Generalmente, especificas el directorio de fuentes o la lista de fuentes para todos los libros de trabajo, pero a veces, debes especificar un conjunto individual o privado de fuentes para tus libros de trabajo. Aspose.Cells proporciona la clase [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/) que puede usarse para especificar un conjunto individual o privado de fuentes para tu libro de trabajo.

## **Especificar un Conjunto Individual o Privado de Fuentes para la Representación del Libro**

El siguiente código de ejemplo carga el [archivo Excel de ejemplo](67338268.xlsx) con su conjunto individual o privado de fuentes, que se especifican usando la clase [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/). Por favor, vea la [fuente ejemplo](67338271.zip) utilizada dentro del código así como el [PDF de salida](67338269.pdf) generado por él. La siguiente captura de pantalla muestra cómo se ve el PDF de salida si la fuente se encuentra con éxito.

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path of your custom font directory
    U16String customFontsDir(u"C:\\TempDir\\CustomFonts");

    // Specify individual font configs custom font directory
    IndividualFontConfigs fontConfigs;

    // If you comment this line or if custom font directory is wrong or 
    // if it does not contain required font then output pdf will not be rendered correctly
    fontConfigs.SetFontFolder(customFontsDir, false);

    // Specify load options with font configs
    LoadOptions opts(LoadFormat::Xlsx);
    opts.SetFontConfigs(fontConfigs);

    // Load the sample Excel file with individual font configs
    Workbook wb(u"sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx", opts);

    // Save to PDF format
    wb.Save(u"outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved to PDF with custom font configurations successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
