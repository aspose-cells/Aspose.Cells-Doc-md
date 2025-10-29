---
title: Vérifier le mot de passe pour modifier en utilisant Aspose.Cells avec C++
linktitle: Vérifier le mot de passe pour modifier
type: docs
weight: 2400
url: /fr/cpp/check-password-to-modify-using-aspose-cells/
description: Vérifier si le mot de passe donné correspond au mot de passe pour modifier en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Parfois, vous devez vérifier si le mot de passe donné correspond au **Mot de passe pour modifier** de manière programmatique. Aspose.Cells fournit la méthode WorkbookSettings.WriteProtection.ValidatePassword() que vous pouvez utiliser pour vérifier si le mot de passe pour modifier est correct ou non.

{{% /alert %}}

## **Vérifiez le mot de passe pour modifier dans Microsoft Excel**

Vous pouvez attribuer **Mot de passe pour ouvrir** et **Mot de passe pour modifier** lors de la création de vos classeurs dans Microsoft Excel. Veuillez consulter cette capture d'écran qui montre l'interface fournie par Microsoft Excel pour spécifier ces mots de passe.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Vérifier le mot de passe pour modifier à l'aide d'Aspose.Cells**

Les codes d'exemple suivants chargent le [fichier Excel source](5112232.xlsx). Il y a un Mot de passe pour ouvrir comme 1234 et un Mot de passe pour modifier comme 5678. Le code vérifie d'abord si 567 est le bon mot de passe pour modifier et il renvoie faux, puis il vérifie si 5678 est le mot de passe pour modifier et il renvoie vrai.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleBook.xlsx";

    // Specify password to open inside the load options
    LoadOptions opts;
    opts.SetPassword(u"1234");

    // Open the source Excel file with load options
    Workbook workbook(inputFilePath, opts);

    // Check if "567" is the password to modify
    bool ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"567");
    std::wcout << L"Is 567 correct Password to modify: " << ret << std::endl;

    // Check if "5678" is the password to modify
    ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"5678");
    std::wcout << L"Is 5678 correct Password to modify: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus après le chargement du [fichier Excel source](5112232.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
