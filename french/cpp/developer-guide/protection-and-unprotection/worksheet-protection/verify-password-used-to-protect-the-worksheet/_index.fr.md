---
title: Vérifier le mot de passe utilisé pour protéger la feuille avec C++
linktitle: Vérifiez le mot de passe utilisé pour protéger la feuille de calcul
type: docs
weight: 370
url: /fr/cpp/verify-password-used-to-protect-the-worksheet/
description: Apprenez comment vérifier le mot de passe utilisé pour protéger une feuille avec Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Les API Aspose.Cells ont amélioré la classe [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) en introduisant certaines propriétés et méthodes utiles. Une telle méthode est la [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) qui permet de spécifier un mot de passe en tant qu'instance de *chaîne* et de vérifier si le même mot de passe a été utilisé pour protéger le [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

{{% /alert %}}

La méthode [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) retourne **true** si le mot de passe spécifié correspond au mot de passe utilisé pour protéger la feuille donnée, et **false** s'il ne correspond pas. Le code suivant utilise la méthode [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) en conjonction avec la propriété [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) pour détecter la protection par mot de passe et vérifier le mot de passe.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"Sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        // Verify the password used to protect the Worksheet
        if (sheet.GetProtection().VerifyPassword(u"1234"))
        {
            std::cout << "Specified password has matched" << std::endl;
        }
        else
        {
            std::cout << "Specified password has not matched" << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
