--- 
title: Exportar Comentarios al Guardar un archivo de Excel en HTML con C++ 
linktitle: Exportar Comentarios al Guardar Archivo Excel en HTML 
type: docs 
weight: 40 
url: /es/cpp/export-comments-while-saving-excel-file-to/ 
description: Aprenda cómo exportar comentarios al guardar archivos de Excel en HTML usando Aspose.Cells con C++. 
--- 

## **Escenarios de uso posibles**

Cuando guardas tu archivo de Excel en HTML, los comentarios no se exportan. Sin embargo, Aspose.Cells ofrece esta función usando la propiedad [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/). Si la configuras en **true**, el HTML también mostrará los comentarios presentes en tu archivo de Excel.

## **Exportar comentarios al guardar archivo de Excel como HTML**

El siguiente código de ejemplo explica el uso de la propiedad [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/). La captura de pantalla muestra el efecto del código en el HTML cuando se establece en **true**. Por favor, descarga el [archivo de Excel de ejemplo](50528260.xlsx) y el [HTML generado](5052826.txt) como referencia.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleExportCommentsHTML.xlsx";
    Workbook workbook(inputFilePath);

    // Export comments - set IsExportComments property to true
    HtmlSaveOptions opts;
    opts.SetIsExportComments(true);

    // Save the Excel file to HTML
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outputDir + u"outputExportCommentsHTML.html", opts);

    std::cout << "Excel file exported to HTML with comments successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
