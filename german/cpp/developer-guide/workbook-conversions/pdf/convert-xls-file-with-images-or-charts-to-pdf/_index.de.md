---
title: XLS Datei mit Bildern oder Diagrammen in PDF mit C++ konvertieren
linktitle: Konvertierung von XLS Datei mit Bildern oder Diagrammen in PDF
type: docs
weight: 50
url: /de/cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: XLS Dateien, die Bilder oder Diagramme enthalten, mit Aspose.Cells und C++ in PDF Dokumente konvertieren.
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die Konvertierung von XLS-Dateien, die Bilder und Diagramme enthalten, in PDF-Dokumente. Aspose.Cells for C++ kann unabhängig arbeiten, um eine Tabelle in PDF zu konvertieren: Für die Konvertierung ist kein Aspose.PDF für C++ erforderlich. Der Vorgang kann im Speicher durchgeführt werden, da er nicht von temporären oder Zwischen-XML-Dateien abhängt. Das bedeutet, dass große Excel-Dateien, z. B. solche mit Bildern, Diagrammen und anderen Zeichenobjekten, schnell und effizient konvertiert werden können.

{{% /alert %}} 
## **Beispielcode**

```c++
#include <iostream>
#include <memory>
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

    // Path of input excel file
    U16String designerFile = srcDir + u"SampleInput.xls";

    // Path of output pdf file
    U16String pdfFile = outDir + u"Output.out.pdf";

    try
    {
        // Open the template excel file
        std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(designerFile);

        // Save the pdf file
        wb->Save(pdfFile, SaveFormat::Pdf);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}} 

Wenn die Tabelle Formeln enthält, ist es am besten, die Methode [Calculate(CalculationData data)]([https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/)) kurz vor der Renderung nach PDF aufzurufen. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet werden und die richtigen Werte im PDF angezeigt werden.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
