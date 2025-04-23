---
title: Changer le type de cible du lien HTML avec C++
linktitle: Changer le type de lien HTML cible
type: docs
weight: 320
url: /fr/cpp/change-the-html-link-target-type/
description: Apprenez comment changer le type de cible du lien HTML en utilisant Aspose.Cells for C++. Contrôlez l attribut cible dans les liens HTML de manière programmatique.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de changer le type de lien HTML cible. Le lien HTML ressemble à ceci

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Comme vous pouvez le voir, l'attribut cible dans le lien HTML ci-dessus est **_self**. Vous pouvez contrôler cet attribut cible en utilisant la propriété [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/). Cette propriété prend l'énumération [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) qui a les valeurs suivantes.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

Le code suivant illustre l'utilisation de la propriété [**GetLinkTargetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getlinktargettype/). Il change le type de cible du lien en **blank**. Par défaut, c'est le **parent**.

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

    // Path of input Excel file
    U16String inputPath = srcDir + u"Sample1.xlsx";

    // Path of output HTML file
    U16String outputPath = outDir + u"Output.out.html";

    // Create workbook
    Workbook workbook(inputPath);

    // Create HTML save options
    HtmlSaveOptions opts;
    opts.SetLinkTargetType(HtmlLinkTargetType::Self);

    // Save the workbook to HTML format
    workbook.Save(outputPath, opts);

    std::cout << "File saved: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
