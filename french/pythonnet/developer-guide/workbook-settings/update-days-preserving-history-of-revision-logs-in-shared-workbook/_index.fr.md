---
title: Mettre à jour les jours en préservant l historique des journaux de révision dans un classeur partagé
type: docs
weight: 80
url: /fr/python-net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Scénarios d'utilisation possibles**

Lorsque vous partagez un classeur, vous avez une option indiquant ***Garder l'historique des modifications pendant N jours*** comme montré dans la capture d'écran suivante. Vous pouvez mettre à jour le nombre de jours pour conserver l'historique en utilisant Aspose.Cells pour Python via .NET avec la propriété [**WorksheetCollection.revision_logs.days_preserving_history**](https://reference.aspose.com/cells/python-net/aspose.cells.revisions/revisionlogcollection/days_preserving_history).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Mettre à jour les jours en préservant l'historique des journaux de révision dans un classeur partagé**

Le code d'exemple suivant crée un classeur vide, le partage, puis met à jour les journaux de révision pour conserver l'historique à 7 jours, ce qui est normalement 30 jours. Veuillez consulter le [fichier Excel de sortie](60489773.xlsx) généré par le code à titre de référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.py" >}}

