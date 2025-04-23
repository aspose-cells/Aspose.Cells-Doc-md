---
title: Documenti PDF sicuri con C++
linktitle: Documenti PDF sicuri
type: docs
weight: 120
url: /it/cpp/secure-pdf-documents/
description: Scopri come proteggere i documenti PDF con password proprietarie e utente usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte, gli sviluppatori devono lavorare con file PDF criptati. Ad esempio:

- Proteggere i documenti con password per proprietario e utente in modo che non possa aprirlo chiunque.
- Impostare restrizioni o autorizzazioni al documento dopo l'apertura del documento, ad esempio limitare se È possibile stampare o estrarre il contenuto del documento.

Questo articolo spiega come passare le opzioni di sicurezza PDF durante il salvataggio dei fogli di calcolo in PDF.

{{% /alert %}}

Aspose.Cells fornisce [**PdfSecurityOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) per lavorare sulla sicurezza. Puoi impostare password proprietarie e utente durante il salvataggio in PDF. La password proprietaria o la password utente sarà richiesta per aprire il documento PDF criptato per la visualizzazione.

- La password dell'utente può essere nulla o una stringa vuota, in questo caso non sarà richiesta alcuna password all'utente durante l'apertura del documento PDF.
- Aprire il documento PDF con la corretta password proprietaria consente l'accesso completo (senza restrizioni di accesso specificate) al documento.
- L'apertura del documento PDF con la corretta password dell'utente (o l'apertura di un documento che non ha una password utente) consente l'accesso limitato come le autorizzazioni specificate.

Il codice di esempio qui sotto descrive come proteggere i PDF con Aspose.Cells.

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

Se il foglio di calcolo contiene formule, è consigliabile chiamare [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) appena prima di convertirlo in PDF. Ciò garantisce che i valori dipendenti dalle formule siano ricalcolati e vengano visualizzati i valori corretti nel PDF.

{{% /alert %}}
