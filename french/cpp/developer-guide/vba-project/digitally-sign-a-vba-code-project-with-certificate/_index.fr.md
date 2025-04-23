---
title: Signer numériquement un projet de code VBA avec un certificat dans C++
linktitle: Signer numériquement un projet de code VBA avec un certificat
type: docs
weight: 110
url: /fr/cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Apprenez comment signer numériquement votre projet de code VBA en utilisant Aspose.Cells for C++ avec un certificat.
---

{{% alert color="primary" %}} 

Vous pouvez signer numériquement votre projet de code VBA avec Aspose.Cells en utilisant sa méthode [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/). Suivez ces étapes pour vérifier si votre fichier Excel est signé numériquement avec un certificat.

- Cliquez sur **Visual Basic** dans l'onglet **Développeur** pour ouvrir **VBA IDE**.
- Cliquez sur **Outils** > **Signatures numériques...** dans **VBA IDE**.

Cela affichera le **Formulaire de signature numérique** indiquant si le document est signé numériquement avec un certificat ou non.

{{% /alert %}} 

## **Signer numériquement un projet de code VBA avec un certificat dans C++**

Le code d'exemple suivant illustre comment utiliser la méthode [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/). Voici les fichiers d'entrée et de sortie de l'exemple de code. Vous pouvez utiliser n'importe quel fichier Excel et tout certificat pour tester ce code.

- [Fichier Excel source](5115028.xlsm) utilisé dans le code d'exemple.
- [Fichier pfx de l'exemple](5115039.pfx) pour créer une signature numérique. Veuillez l'installer sur votre ordinateur pour exécuter ce code. Son mot de passe est 1234.
- [Fichier Excel de sortie](5115029.xlsm) généré par le code d'exemple.

```cpp
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String password(u"1234");
    U16String pfxPath = srcDir + u"sampleDigitallySignVbaProjectWithCertificate.pfx";
    U16String comment(u"Signing Digital Signature using Aspose.Cells");

    Vector<uint8_t> certData;

    std::time_t now = std::time(nullptr);
    std::tm* now_tm = std::localtime(&now);
    int year = now_tm->tm_year + 1900;
    int month = now_tm->tm_mon + 1;
    int day = now_tm->tm_mday;
    int hour = now_tm->tm_hour;
    int minute = now_tm->tm_min;
    int second = now_tm->tm_sec;

    DigitalSignature digitalSignature(certData, password, comment, Date{year, month, day, hour, minute, second, 0});

    U16String inputFilePath = srcDir + u"sampleDigitallySignVbaProjectWithCertificate.xlsm";
    Workbook workbook(inputFilePath);

    workbook.GetVbaProject().Sign(digitalSignature);

    U16String outputFilePath = outDir + u"outputDigitallySignVbaProjectWithCertificate.xlsm";
    workbook.Save(outputFilePath);

    std::cout << "VBA project digitally signed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
