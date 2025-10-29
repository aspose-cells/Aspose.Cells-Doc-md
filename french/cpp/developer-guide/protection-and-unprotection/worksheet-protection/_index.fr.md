---
title: Protéger et déprotéger la feuille de calcul avec C++
linktitle: Protéger et déprotéger la feuille de calcul
type: docs
weight: 40
url: /fr/cpp/protect-and-unprotect-worksheets/
description: Protéger et déprotéger la feuille de calcul des fichiers Excel avec Aspose.Cells for C++.
---

{{% alert color="primary" %}}
Pour empêcher d'autres utilisateurs de modifier, déplacer ou supprimer accidentellement ou délibérément des données dans une feuille de calcul, vous pouvez verrouiller les cellules de votre feuille de calcul Excel, puis protéger la feuille avec un mot de passe. 
{{% /alert %}}

## **Protéger et déprotéger la feuille de calcul dans MS Excel**

**![Protéger et déprotéger la feuille de calcul](protéger-et-déprotéger-la-feuille-de-calcul.png)**

1. Cliquez sur **Révision > Protéger la feuille**.
1. Entrez un mot de passe dans **la boîte de mot de passe**.
1. Sélectionnez les options **autoriser**.
1. Sélectionnez **OK**, saisissez à nouveau le mot de passe pour le confirmer, puis sélectionnez à nouveau **OK**.

## **Protéger la feuille de calcul en utilisant Aspose.Cells for C++**
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

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Protect contents of the worksheet
    sheet.Protect(ProtectionType::Contents);

    // Protect worksheet with password
    sheet.GetProtection().SetPassword(u"test");

    // Save as Excel file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Déprotéger la feuille de calcul en utilisant Aspose.Cells for C++**
La déprotection de la feuille de calcul est facile avec l'API Aspose.Cells. Si la feuille de calcul est protégée par mot de passe, un mot de passe correct est requis.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet with password
    sheet.Unprotect(u"password");

    // Save the workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Worksheet unprotected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Paramètres de protection avancés depuis Excel XP](/cells/fr/cpp/advanced-protection-settings-since-excel-xp/)
- [Détecter si la feuille de calcul est protégée par mot de passe](/cells/fr/cpp/detect-if-worksheet-is-password-protected/)
- [Protection des feuilles de calcul](/cells/fr/cpp/protecting-worksheets/)
- [Déprotéger une feuille de calcul](/cells/fr/cpp/unprotect-a-worksheet/)
- [Vérifier le mot de passe utilisé pour protéger la feuille de calcul](/cells/fr/cpp/verify-password-used-to-protect-the-worksheet/)
{{< app/cells/assistant language="cpp" >}}
