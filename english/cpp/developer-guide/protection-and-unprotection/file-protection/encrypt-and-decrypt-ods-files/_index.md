---  
title: Encrypt And Decrypt ODS files with C++  
linktitle: Encrypt And Decrypt ODS files  
type: docs  
weight: 10  
url: /cpp/encrypt-and-decrypt-ods-files/  
description: Password-protect and encrypt ODS files using Aspose.Cells for C++ which is a pure C++ library.  
---  
  
{{% alert color="primary" %}}  
OpenOffice.org is a full-featured office suite that supports password-protecting and encrypting files. However, an encrypted ODS file can only be opened by OpenOffice after providing the password. Excel cannot open the encrypted ODS file and may raise a warning message. The encryption options are not applicable for ODS files unlike other file types.  
Aspose.Cells allows you to encrypt and decrypt ODS files. Decrypted ODS files can be opened in both Excel and OpenOffice.  
{{% /alert %}}  
  
## **Encrypt with OpenOffice Calc**  
1. Select **Save as** and click the **Save With Password** box.  
1. Click the **Save** button.  
1. Type your desired password into both the **Enter Password to Open** and **Confirm Password** fields in the Set Password window that opens.  
1. Click the **OK** button to save the file.  
  
## **Encrypt ODS file with Aspose.Cells for C++**  
For encrypting an ODS file, load the file and set the [**WorkbookSettings.Password**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/password/) value to the actual password before saving it. The output encrypted ODS file can be opened in OpenOffice only.  
  
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
  
## **Decrypt ODS file with Aspose.Cells for C++**  
  
For decrypting an ODS file, load the file by providing a password in the [**LoadOptions.Password**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/password/) property. Once the file is loaded, set the [**WorkbookSettings.Password**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/password/) string to null.  
  
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