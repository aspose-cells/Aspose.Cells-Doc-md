---
title: Empêcher l exportation du contenu des feuilles de calcul masquées lors de l enregistrement en HTML avec C++
linktitle: Empêcher l exportation du contenu des feuilles de calcul masquées
type: docs
weight: 210
url: /fr/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Apprenez comment empêcher l exportation du contenu des feuilles masquées lors de la sauvegarde des classeurs Excel en HTML en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Vous pouvez enregistrer des classeurs Excel en HTML. Cependant, si le classeur contient des feuilles de calcul masquées, Aspose.Cells exporte par défaut le contenu des feuilles de calcul masquées dans le répertoire de sortie HTML (_files) qui contient des fichiers tels que des feuilles de calcul, des images, tabstrip.htm, stylesheet.css, etc. Parfois, exporter le contenu des feuilles de calcul masquées de cette manière n'est pas approprié. Par exemple, si la feuille de calcul masquée contient des images qui ne doivent pas être exportées dans le répertoire _files.

{{% /alert %}}

Aspose.Cells fournit la propriété [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexporthiddenworksheet/). Par défaut, elle est définie sur **true** et les feuilles de calcul masquées sont exportées en HTML. Si vous la définissez sur **false**, Aspose.Cells n'exportera pas le contenu des feuilles de calcul masquées.

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
    U16String inputFilePath = srcDir + u"WorkbookWithHiddenContent.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"HtmlWithoutHiddenContent_out.html";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Create HTML save options
    HtmlSaveOptions options;

    // Do not export hidden worksheet contents
    options.SetExportHiddenWorksheet(false);

    // Save the workbook
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully without hidden content!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
