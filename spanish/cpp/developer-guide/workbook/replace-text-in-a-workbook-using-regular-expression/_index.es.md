--- 
title: Reemplazar texto en un libro usando expresiones regulares con C++
linktitle: Reemplazar texto en un libro usando expresiones regulares
type: docs 
weight: 90 
url: /es/cpp/replace-text-in-a-workbook-using-regular-expression/ 
description: Reemplazar texto en un libro usando expresiones regulares con Aspose.Cells en C++. 
--- 

Aspose.Cells ofrece la función de reemplazar texto en un libro usando una expresión regular. Para ello, la API proporciona la propiedad [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) de la clase [**ReplaceOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/). Configurar [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) como **verdadero** indica que la clave buscada será una expresión regular.

El siguiente fragmento de código demuestra el uso de la propiedad [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) mediante el uso del [archivo de Excel de muestra](101089318.xlsx). El [archivo de salida](101089319.xlsx) generado por el siguiente fragmento de código está adjunto para referencia.

## **Código de muestra** 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook from the input file
    Workbook workbook(sourceDir + u"SampleRegexReplace.xlsx");

    // Create replace options
    ReplaceOptions replace;
    replace.SetCaseSensitive(false);
    replace.SetMatchEntireCellContents(false);
    // Set to true to indicate that the searched key is regex
    replace.SetRegexKey(true);

    // Perform the regex replace operation
    workbook.Replace(u"\\bKIM\\b", u"^^^TIM^^^", replace);

    // Save the modified workbook
    workbook.Save(outputDir + u"RegexReplace_out.xlsx");

    std::cout << "Regex replace operation completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
