---
title: Passwortüberprüfung verschlüsselter Dateien mit C++
linktitle: Passwort von verschlüsselten Dateien verifizieren
type: docs
weight: 10
url: /de/cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Überprüfen Sie das Passwort verschlüsselter Excel Dateien (xlsx, xlsb, xls, xlsm) und Open Office (ODS) Dateien mit C++ Code.
---

{{% alert color="primary" %}} 
Wenn Excel- (xlsx, xlsb, xls, xlsm) und Open Office- (ODS) Dateien mit einem Passwort geschützt sind, unterstützt Aspose eine einfache Passwortüberprüfung, ohne spezifische Daten der Dateien zu analysieren.
{{% /alert %}} 

## **Das Passwort der verschlüsselten Datei verifizieren**

Um das Passwort der verschlüsselten Datei zu überprüfen, bietet Aspose.Cells for C++ die [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) Methode an. Diese Methode akzeptiert zwei Parameter, den Dateistream und das zu überprüfende Passwort.
Der folgende Code-Schnipsel zeigt die Verwendung der Methode [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformatutil/verifypassword/) zur Überprüfung, ob das angegebene Passwort gültig ist oder nicht.

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
