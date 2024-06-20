---
title: Insérer une chronologie
linktitle: Chronologies
type: docs
weight: 170
url: /fr/java/create-timeline/
description: Apprenez à créer un chronogramme avec Aspose.Cells pour Java.
---

## **Scénarios d'utilisation possibles**

Au lieu d'ajuster les filtres pour afficher des dates, vous pouvez utiliser une chronologie de tableau croisé dynamique - une option de filtre dynamique qui vous permet de filtrer facilement par date/heure et de zoomer sur la période souhaitée à l'aide d'un curseur de contrôle. Microsoft Excel vous permet de créer un chronogramme en sélectionnant un tableau croisé dynamique, puis en cliquant sur *Insérer > Chronologie*. Aspose.Cells pour Java vous permet également de créer un chronogramme en utilisant la méthode [**Worksheet.getTimelines.add()**].

## **Créer une chronologie pour un tableau croisé dynamique**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](input.xlsx) qui contient le tableau croisé dynamique. Ensuite, il crée la chronologie en fonction du premier champ pivot de base. Enfin, il enregistre le classeur au format [XLSX de sortie](output.xlsx). La capture d'écran suivante montre la chronologie créée par Aspose.Cells dans le fichier Excel de sortie.

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

