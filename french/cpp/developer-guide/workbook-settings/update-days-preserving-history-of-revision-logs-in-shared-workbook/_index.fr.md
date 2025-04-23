---
title: Mettre à jour les jours en conservant l historique des journaux de révision dans le classeur partagé avec C++
linktitle: Mettre à jour les jours en préservant l historique des journaux de révision dans un classeur partagé
type: docs
weight: 80
url: /fr/cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Apprenez comment mettre à jour le nombre de jours pour la conservation de l historique dans un classeur partagé en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**

Lorsque vous partagez un classeur, vous obtenez une option indiquant ***Conserver l'historique des modifications pendant N jours*** comme indiqué dans la capture d'écran suivante. Vous pouvez mettre à jour le nombre de jours pour conserver l'historique en utilisant Aspose.Cells avec la propriété [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/cpp/aspose.cells.revisions/revisionlogcollection/getdayspreservinghistory/).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Mettre à jour les jours en préservant l'historique des journaux de révision dans un classeur partagé**

Le code d'exemple suivant crée un classeur vide, le partage, puis met à jour les journaux de révision pour conserver l'historique à 7 jours, ce qui est normalement 30 jours. Veuillez consulter le [fichier Excel de sortie](60489773.xlsx) généré par le code à titre de référence.

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Share the workbook
    wb.GetSettings().SetShared(true);

    // Update DaysPreservingHistory of RevisionLogs
    wb.GetWorksheets().GetRevisionLogs().SetDaysPreservingHistory(7);

    // Save the workbook
    wb.Save(u"outputShared_DaysPreservingHistory.xlsx");

    std::cout << "Workbook shared and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
