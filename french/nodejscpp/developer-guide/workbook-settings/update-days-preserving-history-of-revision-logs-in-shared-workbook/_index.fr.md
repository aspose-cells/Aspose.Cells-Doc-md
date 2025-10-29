---  
title: Mettre à jour les jours en conservant l historique des journaux de révision dans un classeur partagé avec Node.js via C++  
linktitle: Mettre à jour les jours en préservant l historique des journaux de révision dans un classeur partagé  
type: docs  
weight: 80  
url: /fr/nodejs-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/  
description: Apprenez à mettre à jour le nombre de jours pour conserver l historique des journaux de révision dans les classeurs partagés avec Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**

 Lorsque vous partagez un classeur, vous avez une option disant ***Conserver l'historique des changements pendant N jours*** comme indiqué dans la capture d'écran suivante. Vous pouvez mettre à jour le nombre de jours pour conserver l'historique en utilisant Aspose.Cells for Node.js via C++ avec la propriété [**WorksheetCollection.getDaysPreservingHistory()**](https://reference.aspose.com/cells/nodejs-cpp/revisionlogcollection/#getDaysPreservingHistory--).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Mettre à jour les jours en préservant l'historique des journaux de révision dans un classeur partagé**

Le code d'exemple suivant crée un classeur vide, le partage, puis met à jour les journaux de révision pour conserver l'historique à 7 jours, ce qui est normalement 30 jours. Veuillez consulter le [fichier Excel de sortie](60489773.xlsx) généré par le code à titre de référence.

## **Code d'exemple**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Share the workbook
workbook.getSettings().setShared(true);

// Update DaysPreservingHistory of RevisionLogs
workbook.getWorksheets().getRevisionLogs().setDaysPreservingHistory(7);

// Save the workbook
workbook.save("outputShared_DaysPreservingHistory.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
