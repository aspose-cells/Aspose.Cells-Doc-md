---
title: Insérer une chronologie
linktitle: Chronologies
type: docs
weight: 170
url: /fr/net/create-timeline/
description: Apprenez à créer une chronologie avec Aspose.Cells.
---

## **Scénarios d'utilisation possibles**

Au lieu d'ajuster les filtres pour montrer les dates, vous pouvez utiliser une chronologie de tableau croisé dynamique - une option de filtre dynamique qui vous permet de filtrer facilement par date/heure et de zoomer sur la période que vous voulez avec un contrôle curseur. Microsoft Excel vous permet de créer une chronologie en sélectionnant un tableau croisé dynamique, puis en cliquant sur *Insérer > Chronologie*. Aspose.Cells vous permet également de créer une chronologie en utilisant la méthode [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/net/aspose.cells.timelines/timelinecollection/methods/index).

## **Créer une chronologie pour un tableau croisé dynamique**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](input.xlsx) qui contient le tableau croisé dynamique. Ensuite, il crée la chronologie en fonction du premier champ pivot de base. Enfin, il enregistre le classeur au format [XLSX de sortie](output.xlsx). La capture d'écran suivante montre la chronologie créée par Aspose.Cells dans le fichier Excel de sortie.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-CreateTimelineToPivotTable.cs" >}}

