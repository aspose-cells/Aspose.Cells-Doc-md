---
title: التحقق من كلمة مرور الملفات المشفرة باستخدام C++
linktitle: التحقق من كلمة مرور الملفات المشفرة
type: docs
weight: 10
url: /ar/cpp/verify-password-of-encrypted-excel-and-ods-files/
description: التحقق من كلمة مرور ملفات Excel المشفرة (xlsx، xlsb، xls، xlsm وملفات Open Office (ODS) باستخدام أكواد C++.
---

{{% alert color="primary" %}} 
إذا كانت ملفات Excel (xlsx، xlsb، xls، xlsm) وملفات Open Office (ODS) محمية بكلمة مرور، يدعم Aspose التحقق من كلمة المرور بشكل بسيط دون الحاجة إلى تحليل البيانات المحددة للملفات.
{{% /alert %}} 

## **تحقق من كلمة المرور للملف المُشفر**

للتحقق من كلمة مرور الملف المشفر، يوفر Aspose.Cells for C++ الطريقة [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/). تقبل هذه الطريقة معلمين، التيار الخاص بالملف والكلمة المرور التي يجب التحقق منها.
يوضح مقتطف الشيفرة التالي استخدام الطريقة [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) للتحقق مما إذا كانت كلمة المرور المقدمة صالحة أم لا.

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
{{< app/cells/assistant language="cpp" >}}
