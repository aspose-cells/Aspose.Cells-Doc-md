---
title: Skydda PDF dokument med C++
linktitle: Säkra PDF dokument
type: docs
weight: 120
url: /sv/cpp/secure-pdf-documents/
description: Lär dig hur du säkrar PDF dokument med ägar och användarlösenord med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Ibland behöver utvecklare arbeta med krypterade PDF-filer. Till exempel:

- Säkra dokumenten med ägar- och användarlösenord så att inte vem som helst kan öppna dem.
- Ange begränsningar eller behörigheter för dokumentet efter att dokumentet har öppnats. t.ex. begränsa om dokumentinnehållet kan skrivas ut eller extraheras.

Den här artikeln förklarar hur man skickar in PDF-säkerhetsalternativ när man sparar kalkylblad till PDF.

{{% /alert %}}

Aspose.Cells tillhandahåller [**PdfSecurityOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) för att arbeta med säkerhet. Du kan ange ägar- och användarlösenord vid sparning till PDF. Ägarlösenord eller användarlösenord krävs för att öppna den krypterade PDF-dokumentet för visning.

- Användarlösenordet kan vara null eller en tom sträng, i så fall kommer inget lösenord att krävas från användaren vid öppning av PDF-dokumentet.
- Att öppna PDF-dokumentet med rätt ägarlösenord ger full tillgång (utan några tillgångsrestriktioner angivna) till dokumentet.
- Öppning av PDF-dokumentet med det korrekta användarlösenordet (eller öppnande av ett dokument som inte har ett användarlösenord) tillåter begränsad åtkomst enligt de angivna behörigheterna.

Exempelkoden nedan beskriver hur du säkrar PDF:er med Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;
using namespace Aspose::Cells::Rendering::PdfSecurity;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"securepdf_test.out.pdf";

    // Open an Excel file
    Workbook workbook(inputFilePath);

    // Instantiate PDFSaveOptions to manage security attributes
    PdfSaveOptions saveOption;

    // Create and configure PDF security options
    PdfSecurityOptions securityOptions;
    securityOptions.SetUserPassword(u"user");
    securityOptions.SetOwnerPassword(u"owner");
    securityOptions.SetExtractContentPermission(false);
    securityOptions.SetPrintPermission(false);

    // Assign security options to save options
    saveOption.SetSecurityOptions(securityOptions);

    // Save the PDF document with encrypted settings
    workbook.Save(outputFilePath, saveOption);

    std::cout << "PDF saved with security settings successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Om kalkbladet innehåller formler är det bäst att ringa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) precis innan det renderas till PDF. Detta säkerställer att värden beroende av formler omberäknas och de korrekta värdena visas i PDF:en.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
