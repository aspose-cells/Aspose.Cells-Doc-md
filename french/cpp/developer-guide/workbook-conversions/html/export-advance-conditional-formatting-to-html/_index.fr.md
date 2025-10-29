---
title: Exporter la mise en forme conditionnelle DataBar, ColorScale et IconSet lors de la conversion d Excel en HTML avec C++
linktitle: Exporter la mise en forme conditionnelle en HTML
type: docs
weight: 30
url: /fr/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
description: Apprenez comment exporter la mise en forme conditionnelle DataBar, ColorScale et IconSet lors de la conversion de fichiers Excel en HTML en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Vous pouvez exporter la mise en forme conditionnelle DataBar, ColorScale, et IconSet lors de la conversion de votre fichier Excel en HTML. Cette fonctionnalité est partiellement supportée par Microsoft Excel, mais Aspose.Cells for C++ la supporte complètement.

{{% /alert %}} 

## **Exporter la mise en forme conditionnelle DataBar, ColorScale, et IconSet lors de la conversion Excel en HTML**
La capture d'écran ci-dessous montre le [fichier Excel d'exemple](5115558.xlsx) avec la mise en forme conditionnelle DataBar, ColorScale, et IconSet. Vous pouvez télécharger le [fichier Excel d'exemple](5115558.xlsx) à partir du lien fourni.

![todo:image_alt_text](conversion_1.png)

La capture d'écran ci-dessous montre le fichier HTML de sortie Aspose.Cells affichant la mise en forme conditionnelle DataBar, ColorScale, et IconSet. Comme vous pouvez le voir, il ressemble exactement au [fichier Excel d'exemple](5115558.xlsx).

![todo:image_alt_text](conversion_2.png)

### **Code d'exemple**
Le code d'exemple ci-dessous convertit le fichier Excel d'exemple en HTML, ce qui représente simplement une conversion [Excel vers HTML] classique.

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
    U16String filePath = srcDir + u"sample.xlsx";

    // Load your sample excel file in a workbook object
    Workbook wb(filePath);

    // Save it in HTML format
    wb.Save(outDir + u"ConvertingToHTMLFiles_out.html", SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
