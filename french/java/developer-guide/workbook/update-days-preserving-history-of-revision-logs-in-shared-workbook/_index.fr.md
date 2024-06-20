---
title: Mettre à jour les jours en préservant l historique des journaux de révision dans un classeur partagé
type: docs
weight: 90
url: /fr/java/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Scénarios d'utilisation possibles**

Lorsque vous partagez un classeur, vous avez une option disant ***Conserver l'historique des modifications pendant N jours*** comme le montre la capture d'écran suivante. Vous pouvez mettre à jour le nombre de jours pour conserver l'historique en utilisant Aspose.Cells avec la propriété [**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/java/com.aspose.cells/revisionlogcollection#DaysPreservingHistory).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Mettre à jour les jours en préservant l'historique des journaux de révision dans un classeur partagé**

Le code suivant crée un classeur vide, le partage puis met à jour les jours de préservation de l'historique des révisions à 7 jours, alors qu'il est normalement de 30 jours. Veuillez consulter le [fichier Excel de sortie](60489784.xlsx) généré par le code pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.java" >}}
