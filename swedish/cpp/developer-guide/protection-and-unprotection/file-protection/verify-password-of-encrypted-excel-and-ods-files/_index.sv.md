---
title: Verifiera lösenord för krypterade filer med C++
linktitle: Verifiera lösenordet för krypterade filer
type: docs
weight: 10
url: /sv/cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Verifiera lösenordet för krypterade Excel (xlsx, xlsb, xls, xlsm) och Open Office (ODS) filer med C++ kod.
---

{{% alert color="primary" %}} 
Om Excel (xlsx, xlsb, xls, xlsm) och Open Office (ODS) filer är låsta med ett lösenord, stöder Aspose enkel lösenordverifiering utan att analysera specifik data i filerna.
{{% /alert %}} 

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
{{< app/cells/assistant language="cpp" >}}
