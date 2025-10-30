---
title: Kryptera Excel filer med C++
linktitle: Kryptering av Excel filer
type: docs
weight: 90
url: /sv/cpp/encrypting-excel-files/
description: Lär dig hur du krypterar och skyddar Excel filer med lösenord med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) gör det möjligt för dig att kryptera och lösenordsskydda dina kalkylblad. Det använder algoritmer som tillhandahålls av en kryptografisk tjänsteleverantör, eller CSP, en uppsättning krypteringsalgoritmer med olika egenskaper. Standard-CSP är 'Kontors 97/2000-kompatibel' eller 'Svag kryptering (XOR)'. Det är viktigt att välja rätt krypteringsnyckellängd. Vissa CSP:er stöder inte mer än 40 eller 56 bitar. Det anses vara svag kryptering. För stark kryptering krävs en minsta nyckellängd på 128 bitar. Microsoft Windows innehåller också CSP:er som erbjuder starka krypteringstyper, till exempel 'Microsoft Strong Cryptographic Provider'. För att ge dig en uppfattning, 128 bitar kryptering är vad banker använder för att kryptera anslutningen med sina internetbankssystem.

Aspose.Cells gör det möjligt för dig att kryptera och lösenordsskydda Microsoft Excel-filer med önskad krypteringstyp.

{{% /alert %}}

## **Använda Microsoft Excel**

För att ställa in filkrypteringsinställningar i Microsoft Excel (här Microsoft Excel 2003):

1. Från menyn **Verktyg**, välj **Alternativ**. En dialogruta kommer att visas.
1. Välj fliken **Säkerhet**.
1. Ange ett lösenord och klicka på **Avancerat**
1. Välj krypteringstyp och bekräfta lösenordet.

## **Kryptering med Aspose.Cells**

Följande exempel visar hur man krypterar och lösenordsskyddar en Excel-fil med Aspose.Cells API.

```c++
#include <iostream>
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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"encryptedBook1.out.xls";

    // Instantiate a Workbook object and open the excel file
    Workbook workbook(inputFilePath);

    // Specify XOR encryption type
    workbook.SetEncryptionOptions(EncryptionType::XOR, 40);

    // Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider)
    workbook.SetEncryptionOptions(EncryptionType::StrongCryptographicProvider, 128);

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the encrypted excel file
    workbook.Save(outputFilePath);

    std::cout << "File encrypted and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ange lösenord för att ändra alternativ**

Följande exempel visar hur man ställer in alternativet **Lösenord för att ändra** i Microsoft Excel för en befintlig fil med hjälp av Aspose.Cells API.

```c++
#include <iostream>
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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"SpecifyPasswordToModifyOption.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Set the password for modification
    workbook.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Password for modification set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Verifiera lösenordet för den krypterade filen**

För att verifiera lösenordet för den krypterade filen, tillhandahåller Aspose.Cells for C++ metoden [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/). Denna metod tar emot två parametrar, filströmmen och lösenordet som ska verifieras.
Följande kodavsnitt demonstrerar användningen av metod [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) för att verifiera om det angivna lösenordet är giltigt eller inte.

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputPath = srcDir + u"EncryptedBook1.xlsx";
    std::vector<uint8_t> fileData;

    std::ifstream file(inputPath.ToUtf8(), std::ios::binary);
    if (file)
    {
        file.seekg(0, std::ios::end);
        fileData.resize(file.tellg());
        file.seekg(0, std::ios::beg);
        file.read(reinterpret_cast<char*>(fileData.data()), fileData.size());
    }
    Vector<uint8_t> data(fileData.data(), static_cast<int32_t>(fileData.size()));
    bool isPasswordValid = FileFormatUtil::VerifyPassword(data, u"123456");
    std::cout << "Password is Valid: " << std::boolalpha << isPasswordValid << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Kryptering/Dekryptering av ODS-fil med Aspose.Cells**

Aspose.Cells gör det möjligt att kryptera och dekryptera ODS-filer. Dekrypterade ODS-filer kan öppnas både i Excel och OpenOffice, men krypterade ODS-filer kan endast öppnas i OpenOffice efter att ha angett lösenordet. Excel kan inte öppna den krypterade ODS-filen och kan visa en varningsmeddelande. Krypteringsalternativen gäller inte för ODS-filer, till skillnad från andra filtyper. För att kryptera en ODS-fil, ladda filen och ställ in [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/)-värdet till det faktiska lösenordet innan du sparar den. Den krypterade ODS-filen kan endast öppnas i OpenOffice.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C++

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an ODS file
    Workbook workbook(sourceDir + u"sampleODSFile.ods");

    // Password protect the file
    workbook.GetSettings().SetPassword(u"1234");

    // Save the ODS file
    workbook.Save(outputDir + u"outputEncryptedODSFile.ods");

    std::cout << "ODS file password protected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

För att dekryptera en ODS-fil, ladda in filen genom att ange ett lösenord i [**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getpassword/). När filen har laddats, ställ in strängen för [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) till null.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the source directory
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an encrypted ODS file
    LoadOptions loadOptions(LoadFormat::Ods);

    // Set original password
    loadOptions.SetPassword(u"1234");

    // Load the encrypted ODS file with the appropriate load options
    Workbook workbook(sourceDir + u"sampleEncryptedODSFile.ods", loadOptions);

    // Set the password to null
    workbook.GetSettings().SetPassword(nullptr);

    // Save the decrypted ODS file
    workbook.Save(outputDir + u"outputDecryptedODSFile.ods");

    std::cout << "Decrypted ODS file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
