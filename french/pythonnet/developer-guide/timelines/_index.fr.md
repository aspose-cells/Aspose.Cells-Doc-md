---
title: Insérer une chronologie
linktitle: Chronologies
type: docs
weight: 170
url: /fr/python-net/create-timeline/
description: Apprenez à créer une timeline avec Aspose.Cells pour Python via .NET.
keywords: Aspose.Cells pour Python Excel, bibliothèque Python Excel, Python Créer une timeline sans Excel, Ajouter une timeline via Aspose.Cells pour Python, Insérer une timeline en utilisant Aspose.Cells pour Python.
---

## **Scénarios d'utilisation possibles**

Au lieu d'ajuster les filtres pour afficher les dates, vous pouvez utiliser une chronologie de tableau croisé dynamique - une option de filtre dynamique qui vous permet de filtrer facilement par date/heure et de zoomer sur la période souhaitée avec un curseur. Microsoft Excel vous permet de créer une chronologie en sélectionnant un tableau croisé dynamique, puis en cliquant sur *Insérer > Chronologie*. Aspose.Cells pour Python via .NET vous permet également de créer une chronologie en utilisant la méthode [**Worksheet.timelines.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods).

## **Comment créer une chronologie pour un tableau croisé dynamique en utilisant la bibliothèque Aspose.Cells pour Python Excel**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](input.xlsx) qui contient le tableau croisé dynamique. Il crée ensuite la chronologie en fonction du premier champ de base du tableau croisé dynamique. Enfin, il enregistre le classeur au format [XLSX de sortie](output.xlsx). La capture d'écran suivante montre la chronologie créée par Aspose.Cells pour Python via .NET dans le fichier Excel de sortie.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}

