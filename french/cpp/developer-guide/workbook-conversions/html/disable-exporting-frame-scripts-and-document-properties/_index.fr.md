---
title: Désactiver l’exportation des scripts de cadre et des propriétés du document avec C++
type: docs
weight: 310
url: /fr/cpp/disable-exporting-frame-scripts-and-document-properties/
description: Désactiver l’exportation des scripts de cadre et des propriétés du document en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

 Aspose.Cells exporte les scripts de cadre et les propriétés du document lors de la conversion d’un classeur en HTML. La version 8.6.0 de Aspose.Cells for C++ introduit une option permettant de désactiver l’exportation des scripts de cadre et des propriétés du document. Veuillez utiliser la propriété HtmlSaveOptions.ExportFrameScriptsAndProperties pour désactiver l’export.

{{% /alert %}}

## **Désactiver l'exportation des scripts de trame et des propriétés du document**

Le code d'exemple suivant vous permet de désactiver l'exportation des scripts de trame et des propriétés du document. Une fois que vous avez converti un classeur en HTML, le fichier de sortie ne contiendra aucun script de trame et aucune propriété du document.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the required workbook to convert
    U16String inputFilePath = srcDir + u"Sample1.xlsx";
    Workbook workbook(inputFilePath);

    // Disable exporting frame scripts and document properties
    HtmlSaveOptions options;
    options.SetExportFrameScriptsAndProperties(false);

    // Save workbook as HTML
    workbook.Save(outDir + u"output.out.html", options);

    std::cout << "Workbook saved successfully as HTML!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
