---  
title: Шифрование и дешифрование ODS файлов с помощью C++  
linktitle: Шифрование и дешифрование файлов ODS  
type: docs  
weight: 10  
url: /ru/cpp/encrypt-and-decrypt-ods-files/  
description: Парольная защита и шифрование файлов ODS с использованием Aspose.Cells for C++ — чистой библиотеки C++.  
---  

{{% alert color="primary" %}}  
OpenOffice.org — полнофункциональный офисный пакет, поддерживающий парольную защиту и шифрование файлов. Однако зашифрованный файл ODS можно открыть только в OpenOffice после ввода пароля. Excel не может открыть зашифрованный файл ODS и может вывести предупреждающее сообщение. Варианты шифрования не применимы к файлам ODS, в отличие от других типов файлов.  
Aspose.Cells позволяет шифровать и дешифровать файлы ODS. Расшифрованные файлы ODS могут быть открыты как в Excel, так и в OpenOffice.  
{{% /alert %}}  

## **Шифровать с помощью OpenOffice Calc**  
1. Выберите **Сохранить как** и установите флажок **Сохранить с паролем**.  
1. Нажмите кнопку **Сохранить**.  
1. Введите желаемый пароль в поля **Введите пароль для открытия** и **Подтвердите пароль** в окне установки пароля, которое откроется.  
1. Нажмите кнопку **OK**, чтобы сохранить файл.  

## **Зашифровать файл ODS с помощью Aspose.Cells for C++**  
Для шифрования файла ODS загрузите файл и установите значение [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) в фактический пароль перед его сохранением. Зашифрованный файл ODS можно открыть только в OpenOffice.  

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

## **Дешифровать файл ODS с помощью Aspose.Cells for C++**  

Для дешифровки файла ODS загрузите его, указав пароль в свойстве [**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getpassword/). После загрузки установите строку [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) в null.  

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
