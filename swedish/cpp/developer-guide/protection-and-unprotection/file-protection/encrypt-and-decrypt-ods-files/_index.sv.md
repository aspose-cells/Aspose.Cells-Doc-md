---  
title: Kryptera och dekryptera ODS filer med C++  
linktitle: Kryptera och dekryptera ODS filer  
type: docs  
weight: 10  
url: /sv/cpp/encrypt-and-decrypt-ods-files/  
description: Lösenordsskydda och kryptera ODS filer med Aspose.Cells for C++, ett rent C++ bibliotek.  
---  

{{% alert color="primary" %}}  
OpenOffice.org är en fullt utrustad kontorssvit som stöder lösenordsskydd och kryptering av filer. Dock kan en krypterad ODS-fil bara öppnas av OpenOffice efter att ha angett lösenordet. Excel kan inte öppna den krypterade ODS-filen och kan visa en varningsmeddelande. Krypteringsalternativen är inte tillämpliga för ODS-filer till skillnad från andra filtyper.  
Aspose.Cells tillåter dig att kryptera och dekryptera ODS-filer. Dekrypterade ODS-filer kan öppnas i både Excel och OpenOffice.  
{{% /alert %}}  

## **Kryptera med OpenOffice Calc**  
1. Välj **Spara som** och klicka på **Spara med lösenord** rutan.  
1. Klicka på **Spara**-knappen.  
1. Skriv ditt önskade lösenord i både **Ange lösenord för att öppna** och **Bekräfta lösenord**-fälten i dialogrutan Ange lösenord som öppnas.  
1. Klicka på **OK**-knappen för att spara filen.  

## **Kryptera ODS-fil med Aspose.Cells for C++**  
För att kryptera en ODS-fil, ladda in filen och ställ in [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/)-värdet till det faktiska lösenordet innan du sparar den. Den utmatade krypterade ODS-filen kan öppnas i OpenOffice endast.  

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

## **Dekryptera ODS-fil med Aspose.Cells for C++**  

För att dekryptera en ODS-fil, ladda filen genom att ange ett lösenord i [**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getpassword/)-egenskapen. När filen är laddad, ställ in [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) till null.  

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
