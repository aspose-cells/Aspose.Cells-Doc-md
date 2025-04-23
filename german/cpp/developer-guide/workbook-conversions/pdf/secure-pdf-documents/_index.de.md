---
title: PDF Dokumente mit C++ sichern
linktitle: Sichere PDF Dokumente
type: docs
weight: 120
url: /de/cpp/secure-pdf-documents/
description: Lernen Sie, wie Sie PDF Dokumente mit Besitzer und Benutzerkennwörtern mit Aspose.Cells und C++ sichern.
---

{{% alert color="primary" %}}

Manchmal müssen Entwickler mit verschlüsselten PDF-Dateien arbeiten. Zum Beispiel:

- Sichern Sie die Dokumente mit Besitzer- und Benutzerpasswörtern, so dass nicht jeder es öffnen kann.
- Legen Sie nach dem Öffnen des Dokuments Einschränkungen oder Berechtigungen für das Dokument fest. z.B. Beschränkung, ob der Dokumentinhalt gedruckt oder extrahiert werden kann.

In diesem Artikel wird erklärt, wie Sie PDF-Sicherheitsoptionen beim Speichern von Tabellen in PDF übergeben können.

{{% /alert %}}

Aspose.Cells bietet [**PdfSecurityOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) für die Arbeit mit Sicherheit. Sie können Besitzer- und Benutzerkennwörter beim Speichern in PDF festlegen. Das Besitzer- oder Benutzerkennwort ist erforderlich, um das verschlüsselte PDF-Dokument zu öffnen.

- Das Benutzerpasswort kann null oder leer sein. In diesem Fall ist kein Passwort vom Benutzer erforderlich, wenn das PDF-Dokument geöffnet wird.
- Das Öffnen des PDF-Dokuments mit dem richtigen Besitzerkennwort gewährt vollen Zugriff (ohne Zugriffsrestriktionen) auf das Dokument.
- Das Öffnen des PDF-Dokuments mit dem korrekten Benutzerpasswort (oder das Öffnen eines Dokuments, das kein Benutzerpasswort hat) ermöglicht eingeschränkten Zugriff entsprechend den festgelegten Berechtigungen.

Der unten stehende Beispielcode beschreibt, wie PDFs mit Aspose.Cells gesichert werden können.

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

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) direkt vor dem Rendern in PDF aufzurufen. Dadurch werden die formelabhängigen Werte neu berechnet und die korrekten Werte im PDF angezeigt.

{{% /alert %}}
