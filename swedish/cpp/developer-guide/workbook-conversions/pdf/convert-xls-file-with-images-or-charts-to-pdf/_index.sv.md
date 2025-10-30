---
title: Konvertera XLS fil med bilder eller diagram till PDF med C++
linktitle: Konvertera XLS fil med bilder eller diagram till PDF
type: docs
weight: 50
url: /sv/cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Konvertera XLS filer som innehåller bilder eller diagram till PDF dokument med Aspose.Cells och C++.
---

{{% alert color="primary" %}} 

Aspose.Cells stödjer konvertering av XLS-filer som innehåller bilder och diagram till PDF-dokument. Aspose.Cells for C++ kan fungera självständigt för att konvertera ett kalkylblad till PDF: Aspose.PDF för C++ krävs inte för konverteringen. Processen kan göras i minnet eftersom den inte är beroende av tillfälliga eller mellanliggande XML-filer. Detta innebär att stora Excel-filer, till exempel de som innehåller bilder, diagram och andra ritobjekt, kan konverteras snabbt och effektivt.

{{% /alert %}} 
## **Exempelkod**

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

Om kalkylbladet innehåller formler, är det bäst att kalla på [Calculate(CalculationData data)](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/) metoden strax före rendering till PDF. Det säkerställer att formelberoende värden räknas om, och att rätt värden visas i PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
