---
title: Lägg till digital signatur i en redan signerad Excel fil med C++
linktitle: Lägg till digital signatur i en redan signerad Excelfil
type: docs
weight: 20
url: /sv/cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Lär dig hur man lägger till digitala signaturer i signerade Excel filer med hjälp av Aspose.Cells for C++. Upprätthåll dokumentets integritet med flera signaturer.
keywords: Lägg till digital signatur i en redan signerad Excel fil, C++ digitala signaturer, Excel dokumentsäkerhet
---

## **Möjliga användningsscenario**

Aspose.Cells erbjuder metoden [**Workbook::AddDigitalSignature(DigitalSignatureCollectionPtr digitalSignatureCollection)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) för att lägga till digitala signaturer i redan signerade Excel-filer.

{{% alert color="primary" %}}

Vänligen notera vid tillägg av en digital signatur till ett redan signerat Excel-dokument: om det ursprungliga dokumentet genererades av Aspose.Cells fungerar det korrekt. Men om dokumentet skapades av andra motorer (t.ex. Microsoft Excel) kan Aspose.Cells for C++ inte bevara den exakta filstrukturen efter laddning och omlagring, vilket kan ogiltigförklara befintliga signaturer.

{{% /alert %}}

## **Hur man lägger till en digital signatur till en redan signerad Excel-fil**

Följande kodexempel visar hur man använder [**Workbook::AddDigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) för att lägga till digitala signaturer i signerade Excel-filer. [Exempel-Excel-fil](50528280.xlsx) är förhandsignerad. [Utdatafil](50528281.xlsx) visar resultatet. Vi använder ett demo-certifikat [AsposeDemo.pfx](50528279.pfx) med lösenord **aspose**.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Exempelkod**

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
