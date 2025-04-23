---
title: Détecter si une feuille de calcul est protégée par mot de passe avec C++
linktitle: Détecter si la feuille de calcul est protégée par mot de passe
type: docs
weight: 360
url: /fr/cpp/detect-if-worksheet-is-password-protected/
description: Apprenez comment détecter si une feuille de calcul est protégée par mot de passe en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Il est possible de protéger séparément les classeurs et les feuilles de calcul. Par exemple, une feuille de calcul peut contenir une ou plusieurs feuilles protégées par mot de passe, mais le classeur lui-même peut ou non être protégé. Les API Aspose.Cells permettent de détecter si une feuille de calcul donnée est protégée par mot de passe ou non. Cet article montre comment utiliser l'API Aspose.Cells for C++ pour atteindre ce but.

{{% /alert %}}

Aspose.Cells for C++ expose la propriété [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) pour détecter si une feuille de calcul est protégée par mot de passe ou non. La propriété de type booléen [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) renvoie **true** si [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) est protégée par mot de passe et **false** sinon.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        std::cout << "Worksheet is password protected" << std::endl;
    }
    else
    {
        std::cout << "Worksheet is not password protected" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
