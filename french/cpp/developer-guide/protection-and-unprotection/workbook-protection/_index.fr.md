---
title: Protéger et déprotéger la structure du classeur avec C++
linktitle: Protéger et déprotéger la structure du classeur
type: docs
weight: 40
url: /fr/cpp/protect-and-unprotect-workbook-structure/
description: Protéger et déprotéger la structure du classeur des fichiers Excel à l aide de C++ avec Aspose.Cells.
---

{{% alert color="primary" %}}
Pour empêcher les autres utilisateurs de voir des feuilles de calcul cachées, d'ajouter, de déplacer, de supprimer ou de masquer des feuilles de calcul, et de renommer des feuilles de calcul, vous pouvez protéger la structure de votre classeur Excel avec un mot de passe.
{{% /alert %}}

## **Protéger et déprotéger la structure du classeur dans MS Excel**

**![Protéger et déprotéger la structure du classeur](protect-and-unprotect-workbook-structure.png)**

1. Cliquez sur **Relecture > Protéger le classeur**.
1. Entrez un mot de passe dans **la boîte de mot de passe**.
1. Sélectionnez **OK**, saisissez à nouveau le mot de passe pour le confirmer, puis sélectionnez à nouveau **OK**.

## **Protéger la structure du classeur en utilisant Aspose.Cells for C++**
Il suffit d'utiliser les lignes de code suivantes pour implémenter la protection de la structure du classeur Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Protect workbook structure with a password
    workbook.Protect(ProtectionType::Structure, u"password");

    // Save the workbook to a file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Déprotéger la structure du classeur en utilisant Aspose.Cells for C++**
La déprotection de la structure du classeur est facile avec l'API Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open an Excel file which workbook structure is protected.
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Unprotect workbook structure.
    workbook.Unprotect(u"password");

    // Save Excel file.
    workbook.Save(inputFilePath);

    std::cout << "Workbook structure unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}
Remarque : un mot de passe correct est requis.
{{% /alert %}}
