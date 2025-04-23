---
title: Ställa in stark krypteringstyp med C++
linktitle: Ställa in stark krypteringstyp
type: docs
weight: 60
url: /sv/cpp/setting-strong-encryption-type/
description: Lär dig hur du tillämpar stark kryptering och lösenordsskydd på Excel filer med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) möjliggör kryptering och lösenordsskydd av kalkylblad. Det använder algoritmer som tillhandahålls av en kryptotjänsteleverantör. En kryptotjänsteleverantör (eller CSP) är en uppsättning kryptografiska algoritmer med olika egenskaper. Standard-CSP är "Office 97/2000 Compatible". Detta är en CSP med vissa allmänt kända säkerhetsproblem. Kalkylblad som är säkrade med "svag kryptering (XOR)" eller med "Office 97/2000 Compatible"-krypteringstyp kan enkelt knäckas.

För att övervinna detta problem, använd en av de starka krypteringstyper som tillhandahålls av Microsoft Excel. Du kan ändra krypteringstypen till den starkaste tillgängliga CSP. För stark kryptering krävs en miniminyckellängd på 128 bitar, till exempel 'Microsoft Strong Cryptographic Provider'.

Du kan också kryptera och lösenordsskydda Excel-filer med stark krypteringstyp med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Tillämpa kryptering med Microsoft Excel**
För att implementera filkryptering i Microsoft Excel (till exempel 2007):

1. Från menyn **Verktyg** väljer du **Alternativ**.
1. Välj fliken **Säkerhet**.
1. Ange ett värde för fältet **Lösenord för att öppna**.
1. Klicka på **Avancerat**.
1. Välj krypteringstyp och bekräfta lösenordet.

## **Tillämpa kryptering med Aspose.Cells**
Kodexemplen nedan tillämpar stark kryptering på en fil och anger ett lösenord.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"encryptedBook1.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider)
    workbook.SetEncryptionOptions(EncryptionType::StrongCryptographicProvider, 128);

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "File encrypted and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
