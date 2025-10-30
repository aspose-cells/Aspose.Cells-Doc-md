---
title: Digitale Signatur zu einer bereits signierten Excel Datei mit C++ hinzufügen
linktitle: Fügen Sie eine digitale Signatur zu einer bereits signierten Excel Datei hinzu
type: docs
weight: 20
url: /de/cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ digitale Signaturen zu bereits signierten Excel Dateien hinzufügen. Bewahren Sie die Integrität des Dokuments mit mehreren Signaturen.
keywords: Digitale Signatur zu einer bereits signierten Excel Datei hinzufügen, C++ digitale Signaturen, Sicherheit von Excel Dokumenten
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells bietet die [**Workbook::AddDigitalSignature(DigitalSignatureCollectionPtr digitalSignatureCollection)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/)-Methode zum Hinzufügen digitaler Signaturen zu bereits signierten Excel-Dateien.

{{% alert color="primary" %}}

Bitte beachten Sie beim Hinzufügen einer digitalen Signatur zu einem bereits signierten Excel-Dokument: Wenn das Originaldokument mit Aspose.Cells erstellt wurde, funktioniert es korrekt. Wenn das Dokument jedoch von anderen Engines (z.B. Microsoft Excel) erstellt wurde, kann Aspose.Cells for C++ die genaue Dateistruktur nach Laden und erneuter Speicherung nicht bewahren, was die bestehenden Signaturen ungültig machen kann.

{{% /alert %}}

## **Wie fügt man eine digitale Signatur zu einer bereits signierten Excel-Datei hinzu**

Das folgende Code-Beispiel zeigt, wie man [**Workbook::AddDigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) verwendet, um digitale Signaturen zu signierten Excel-Dateien hinzuzufügen. Die [Beispieldatei Excel](50528280.xlsx) ist vorverschlüsselt. Die [Ausgabedatei](50528281.xlsx) zeigt das Ergebnis. Wir verwenden ein Dem-Zertifikat [AsposeDemo.pfx](50528279.pfx) mit Passwort **aspose**.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Certificate and workbook paths
    U16String certFilePath = srcDir + u"AsposeDemo.pfx";
    U16String inputFilePath = srcDir + u"sampleDigitallySignedByCells.xlsx";
    U16String outputFilePath = outDir + u"outputDigitallySignedByCells.xlsx";

    // Load digitally signed workbook
    Workbook workbook(inputFilePath);

    // Create digital signature collection
    DigitalSignatureCollection dsCollection;

    // Create digital signature using PFX certificate
    U16String password = u"aspose";
    U16String comments = u"Aspose.Cells added new digital signature in existing digitally signed workbook.";
    DigitalSignature signature(certFilePath, password, comments, Date());

    // Add signature to collection
    dsCollection.Add(signature);

    // Apply digital signatures to workbook
    workbook.AddDigitalSignature(dsCollection);

    // Save modified workbook
    workbook.Save(outputFilePath);

    std::cout << "Digital signature added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
