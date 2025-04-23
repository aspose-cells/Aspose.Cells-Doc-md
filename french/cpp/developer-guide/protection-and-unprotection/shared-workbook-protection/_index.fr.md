---
title: Protéger ou déprotéger par mot de passe le classeur partagé avec C++
linktitle: Protéger par mot de passe ou désactiver la protection de la feuille de calcul partagée
type: docs
weight: 10
url: /fr/cpp/password-protect-or-unprotect-the-shared-workbook/
description: Apprenez comment protéger ou déprotéger par mot de passe un classeur partagé en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez protéger ou déprotéger le classeur partagé avec Microsoft Excel comme le montre la capture d'écran suivante. Aspose.Cells prend également en charge cette fonctionnalité avec les méthodes [**Workbook::ProtectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/protectsharedworkbook/) et [**Workbook::UnprotectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/unprotectsharedworkbook/).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Protéger par mot de passe ou désactiver la protection de la feuille de calcul partagée**

Le code d'exemple suivant crée un classeur et le protège tout en activant le partage, puis le sauvegarde en tant que [fichier Excel de sortie](55541777.xlsx). La capture d'écran montre que lorsque vous essayez de le déprotéger, Microsoft Excel vous invite à entrer le mot de passe pour le déprotéger.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty Excel file
    Workbook wb;

    // Protect the Shared Workbook with Password
    wb.ProtectSharedWorkbook(u"1234");

    // Uncomment this line to Unprotect the Shared Workbook
    // wb.UnprotectSharedWorkbook(u"1234");

    // Save the output Excel file
    wb.Save(u"outputProtectSharedWorkbook.xlsx");

    std::cout << "Shared workbook protection applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
