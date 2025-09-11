---
title: Verify Password of Encrypted Files with C++
linktitle: Verify Password of Encrypted Files
type: docs
weight: 10
url: /cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Verify the password of encrypted Excel (xlsx, xlsb, xls, xlsm) and Open office (ODS) files using C++ codes.
---

{{% alert color="primary" %}} 
If Excel (xlsx, xlsb, xls, xlsm) and Open office (ODS) files are locked with a password, Aspose supports simple password verification without parsing specific data of the files.
{{% /alert %}} 

## **Verify the password of the encrypted file**

To verify the password of the encrypted file, Aspose.Cells for C++ provides the [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) method. This method accepts two parameters, the file stream and the password that needs to be verified.
The following code snippet demonstrates the use of the [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) method to verify whether the provided password is valid or not.

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