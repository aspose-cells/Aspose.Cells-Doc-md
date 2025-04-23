---
title: Vérifier le mot de passe des fichiers chiffrés avec C++
linktitle: Vérifier le mot de passe des fichiers chiffrés
type: docs
weight: 10
url: /fr/cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Vérifiez le mot de passe des fichiers Excel chiffrés (xlsx, xlsb, xls, xlsm) et Open Office (ODS) en utilisant des codes C++.
---

{{% alert color="primary" %}} 
Si des fichiers Excel (xlsx, xlsb, xls, xlsm) et Open Office (ODS) sont verrouillés avec un mot de passe, Aspose supporte une vérification simple du mot de passe sans analyser les données spécifiques des fichiers.
{{% /alert %}} 

## **Vérifiez le mot de passe du fichier chiffré**

Pour vérifier le mot de passe du fichier crypté, Aspose.Cells for C++ fournit la méthode [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/). Cette méthode accepte deux paramètres, le flux de fichier et le mot de passe à vérifier.
Le code d'exemple suivant démontre l'utilisation de la méthode [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) pour vérifier si le mot de passe fourni est valide ou non.

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
