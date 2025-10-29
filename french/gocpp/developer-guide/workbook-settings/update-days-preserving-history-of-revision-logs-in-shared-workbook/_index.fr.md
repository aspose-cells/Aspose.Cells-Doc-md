---
title: Mettre à jour les jours en conservant l historique des journaux de révision dans un classeur partagé avec Golang via C++
linktitle: Mettre à jour les jours en préservant l historique des journaux de révision dans un classeur partagé
type: docs
weight: 80
url: /fr/go-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Apprenez à mettre à jour le nombre de jours pour conserver l historique dans un classeur partagé en utilisant Aspose.Cells avec Golang via C++
---

## **Scénarios d'utilisation possibles**

Lorsque vous partagez un classeur, vous obtenez une option indiquant ***Conserver l'historique des modifications pendant N jours*** comme indiqué dans la capture d'écran suivante. Vous pouvez mettre à jour le nombre de jours pour conserver l'historique en utilisant Aspose.Cells avec la propriété [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/go-cpp/revisionlogcollection/getdayspreservinghistory/).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Mettre à jour les jours en préservant l'historique des journaux de révision dans un classeur partagé**

Le code d'exemple suivant crée un classeur vide, le partage, puis met à jour les journaux de révision pour conserver l'historique à 7 jours, ce qui est normalement 30 jours. Veuillez consulter le [fichier Excel de sortie](60489773.xlsx) généré par le code à titre de référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.go" >}}
