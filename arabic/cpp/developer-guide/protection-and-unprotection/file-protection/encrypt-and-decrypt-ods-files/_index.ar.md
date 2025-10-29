---  
title: تشفير وفك تشفير ملفات ODS باستخدام C++  
linktitle: تشفير وفك تشفير ملفات ODS  
type: docs  
weight: 10  
url: /ar/cpp/encrypt-and-decrypt-ods-files/  
description: حماية كلمات المرور وتشفير ملفات ODS باستخدام Aspose.Cells for C++ وهو مكتبة C++ خالصة.  
---  

{{% alert color="primary" %}}  
OpenOffice.org هو مجموعة مكتبية تحتوي على كافة الميزات ويدعم حماية كلمات المرور وتشفير الملفات. ومع ذلك، لا يمكن فتح ملف ODS مشفر إلا بواسطة OpenOffice بعد إدخال كلمة المرور. لا يمكن لـ Excel فتح ملف ODS المشفر وقد يظهر رسالة تحذيرية. الخيارات الخاصة بالتشفير غير قابلة للتطبيق على ملفات ODS على عكس أنواع الملفات الأخرى.  
تتيح Aspose.Cells لك إمكانية تشفير وفك تشفير ملفات ODS. يمكن فتح ملفات ODS غير المشفرة في كل من Excel وOpenOffice.  
{{% /alert %}}  

## **التشفير باستخدام OpenOffice Calc**  
1. اختر **حفظ باسم** وانقر على مربع **الحفظ بكلمة مرور**.  
1. انقر على زر **حفظ**.  
1. اكتب كلمة المرور المطلوبة في حقلي **أدخل كلمة المرور للفتح** و **تأكيد كلمة المرور** في نافذة تعيين كلمة المرور التي تفتح.  
1. انقر على زر **موافق** لحفظ الملف.  

## **تشفير ملف ODS باستخدام Aspose.Cells for C++**  
لتشفير ملف ODS، قم بتحميل الملف وتعيين القيمة [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) إلى كلمة المرور الفعلية قبل حفظه. يمكن فتح ملف ODS المشفر الناتج في OpenOffice فقط.  

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

## **فك تشفير ملف ODS باستخدام Aspose.Cells for C++**  

لفك تشفير ملف ODS، حمّل الملف عن طريق إدخال كلمة مرور في خاصية [**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getpassword/). بمجرد تحميل الملف، اجعل السلسلة [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getpassword/) فارغة.  

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
