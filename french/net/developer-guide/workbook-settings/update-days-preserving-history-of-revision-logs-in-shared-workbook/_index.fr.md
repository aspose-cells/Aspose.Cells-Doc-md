---
title: Mettre à jour les jours en préservant l historique des journaux de révision dans un classeur partagé
type: docs
weight: 80
url: /fr/net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Scénarios d'utilisation possibles**

Lorsque vous partagez un classeur, vous obtenez une option indiquant ***Conserver l'historique des modifications pendant N jours*** comme indiqué dans la capture d'écran suivante. Vous pouvez mettre à jour le nombre de jours pour conserver l'historique en utilisant Aspose.Cells avec la propriété [**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/net/aspose.cells.revisions/revisionlogcollection/properties/dayspreservinghistory).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Mettre à jour les jours en préservant l'historique des journaux de révision dans un classeur partagé**

Le code d'exemple suivant crée un classeur vide, le partage, puis met à jour les journaux de révision pour conserver l'historique à 7 jours, ce qui est normalement 30 jours. Veuillez consulter le [fichier Excel de sortie](60489773.xlsx) généré par le code à titre de référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.cs" >}}
