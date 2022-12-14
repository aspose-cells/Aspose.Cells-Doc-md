---
title: Insérer la chronologie
linktitle: Délais
type: docs
weight: 170
url: /fr/java/create-timeline/
description: Apprenez à créer une chronologie avec Aspose.Cells pour java.
---
## **Scénarios d'utilisation possibles**

 Au lieu d'ajuster les filtres pour afficher les dates, vous pouvez utiliser une chronologie de tableau croisé dynamique —— une option de filtre dynamique qui vous permet de filtrer facilement par date/heure et de zoomer sur la période souhaitée avec un curseur. Microsoft Excel vous permet de créer une chronologie en sélectionnant un tableau croisé dynamique, puis en cliquant sur le*Insertion > Chronologie*. Aspose.Cells pour Java vous permet également de créer une chronologie à l'aide de la méthode [**Worksheet.getTimelines.add()**].

## **Créer une chronologie dans un tableau croisé dynamique**

 Veuillez consulter l'exemple de code suivant. Il charge le[exemple de fichier Excel](input.xlsx) qui contient le tableau croisé dynamique. Il crée ensuite la chronologie basée sur le premier champ pivot de base. Enfin, il enregistre le classeur dans[sortie XLSX](output.xlsx) format. La capture d'écran suivante montre la chronologie créée par Aspose.Cells dans le fichier Excel de sortie.

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

