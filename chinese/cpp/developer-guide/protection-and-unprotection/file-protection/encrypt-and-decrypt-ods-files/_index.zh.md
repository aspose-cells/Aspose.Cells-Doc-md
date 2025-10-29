---  
title: 使用C++加密和解密ODS文件  
linktitle: 加密和解密ODS文件  
type: docs  
weight: 10  
url: /zh/cpp/encrypt-and-decrypt-ods-files/  
description: 使用纯C++库Aspose.Cells for C++对ODS文件进行密码保护和加密。  
---  

{{% alert color="primary" %}}  
OpenOffice.org是一款功能齐全的办公套件，支持对文件进行密码保护和加密。但加密的ODS文件只能通过OpenOffice在提供密码后打开。Excel无法打开加密的ODS文件，可能会弹出警告信息。加密选项不适用于ODS文件，不同于其他文件类型。  
Aspose.Cells允许加密和解密ODS文件。解密后的ODS文件可以在Excel和OpenOffice中打开。  
{{% /alert %}}  

## **在OpenOffice Calc中加密**  
1. 选择**另存为**，并点击**带密码保存**框。  
1. 点击**保存**按钮。  
1. 在打开密码窗口中的**输入打开文件的密码**和**确认密码**字段中键入所需的密码。  
1. 点击**确定**按钮以保存文件。  

## **使用Aspose.Cells for C++加密ODS文件**  
要对ODS文件进行加密，加载文件并在保存之前将[**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/)值设置为实际密码。加密的输出ODS文件只能在OpenOffice中打开。  

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

## **用Aspose.Cells for C++解密ODS文件**  

对于解密ODS文件，加载文件时在[**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getpassword/)属性中提供密码。一旦加载完成，将[**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/)字符串设置为null。  

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
