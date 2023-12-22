---
title: Insérer une chronologie
linktitle: Délais
type: docs
weight: 170
url: /fr/python-net/create-timeline/
description: Apprenez à créer une chronologie avec le Aspose.Cells for Python via .NET.
---
##  **Scénarios d'utilisation possibles**

Au lieu d'ajuster les filtres pour afficher les dates, vous pouvez utiliser une chronologie de tableau croisé dynamique : une option de filtre dynamique qui vous permet de filtrer facilement par date/heure et de zoomer sur la période souhaitée avec un curseur. Microsoft Excel vous permet de créer une chronologie en sélectionnant un tableau croisé dynamique, puis en cliquant sur *Insérer > Chronologie*. Aspose.Cells for Python via .NET vous permet également de créer une chronologie à l'aide du[**Feuille de travail.timelines.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods)méthode.

##  **Créer une chronologie dans un tableau croisé dynamique**

 Veuillez consulter l'exemple de code suivant. Il charge le[exemple de fichier Excel](input.xlsx)qui contient le tableau croisé dynamique. Il crée ensuite la chronologie basée sur le premier champ pivot de base. Enfin, il enregistre le classeur dans[sortie XLSX](output.xlsx) format. La capture d'écran suivante montre la chronologie créée par Aspose.Cells for Python via .NET dans le fichier Excel de sortie.

![tâche : image_alt_text](create-timeline-to-a-pivot-table_1.png)

###  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}

