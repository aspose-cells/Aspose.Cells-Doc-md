---  
title: ODS dosyalarını C++ ile Şifrele ve Çöz  
linktitle: ODS Dosyalarını Şifreleme ve Şifre Çözme  
type: docs  
weight: 10  
url: /tr/cpp/encrypt-and-decrypt-ods-files/  
description: Aspose.Cells for C++ kullanarak ODS dosyalarını parola korumalı ve şifreli yapabilirsiniz. Bu, saf bir C++ kitaplığıdır.  
---  

{{% alert color="primary" %}}  
OpenOffice.org, şifre koruma ve şifreleme desteği sunan tam özellikli bir ofis paketidir. Ancak, şifreli ODS dosyası sadece parola girildikten sonra OpenOffice tarafından açılabilir. Excel, şifreli ODS dosyasını açamaz ve uyarı mesajı verebilir. Şifreleme seçenekleri diğer dosya türlerine göre ODS dosyalarında geçerli değildir.  
Aspose.Cells, ODS dosyalarını şifreleme ve şifresini çözme imkanı sağlar. Şifre çözülen ODS dosyaları hem Excel hem de OpenOffice ile açılabilir.  
{{% /alert %}}  

## **OpenOffice Calc ile Şifrele**  
1. **Save as** seçeneğini belirleyin ve **Save With Password** kutusuna tıklayın.  
1. **Kaydet** düğmesini tıklayın.  
1. Açılan Set Parola penceresinde, hem **Açmak için Parolayı Girin** hem de **Parolayı Onaylayın** alanlarına istediğiniz parolayı yazın.  
1. Dosyayı kaydetmek için **Tamam** düğmesini tıklayın.  

## **Aspose.Cells for C++ kullanarak ODS dosyasını şifrele**  
Bir ODS dosyasını şifrelemek için dosyayı yükleyin ve kaydetmeden önce [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) değerini gerçek parolaya ayarlayın. Oluşturulan şifrelenmiş ODS dosyası yalnızca OpenOffice'de açılabilir.  

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

## **Aspose.Cells for C++ kullanarak ODS dosyasını şifresini çöz**  

Bir ODS dosyasını şifre çözmek için, [**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getpassword/) özelliğine şifre girerek dosyayı yükleyin. Dosya yüklendikten sonra, [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) dizesini null yapın.  

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
