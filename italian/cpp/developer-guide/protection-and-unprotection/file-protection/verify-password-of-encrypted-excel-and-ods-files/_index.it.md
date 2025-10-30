---
title: Verifica la Password dei File Crittografati con C++
linktitle: Verifica password dei file crittografati
type: docs
weight: 10
url: /it/cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Verifica la password dei file Excel crittografati (xlsx, xlsb, xls, xlsm) e Open Office (ODS) usando codici C++.
---

{{% alert color="primary" %}} 
Se i file Excel (xlsx, xlsb, xls, xlsm) e Open Office (ODS) sono bloccati con password, Aspose supporta la verifica semplice della password senza analizzare i dati specifici dei file.
{{% /alert %}} 

## **Verifica la password del file crittografato**

Per verificare la password del file criptato, Aspose.Cells for C++ fornisce il metodo [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/). Questo metodo accetta due parametri, il flusso del file e la password che deve essere verificata.
Il seguente frammento di codice dimostra l'uso del metodo [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) per verificare se la password fornita è valida o meno.

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
