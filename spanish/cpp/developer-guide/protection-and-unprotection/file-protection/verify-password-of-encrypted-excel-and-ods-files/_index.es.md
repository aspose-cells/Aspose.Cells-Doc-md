---
title: Verificar contraseña de archivos cifrados con C++
linktitle: Verificar contraseña de archivos cifrados
type: docs
weight: 10
url: /es/cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Verificar la contraseña de archivos cifrados de Excel (xlsx, xlsb, xls, xlsm) y OpenOffice (ODS) usando códigos C++.
---

{{% alert color="primary" %}} 
Si los archivos de Excel (xlsx, xlsb, xls, xlsm) y OpenOffice (ODS) están bloqueados con una contraseña, Aspose admite la verificación simple de contraseña sin analizar datos específicos de los archivos.
{{% /alert %}} 

## **Verificar la contraseña del archivo cifrado**

Para verificar la contraseña del archivo cifrado, Aspose.Cells for C++ proporciona el método [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/). Este método acepta dos parámetros, el flujo del archivo y la contraseña que necesita ser verificada.
El siguiente fragmento de código muestra el uso del método [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) para verificar si la contraseña proporcionada es válida o no.

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
