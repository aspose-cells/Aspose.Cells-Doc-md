---
title: Insérer une chronologie
linktitle: Chronologies
type: docs
weight: 170
url: /fr/nodejs-cpp/create-timeline/
description: Apprenez à créer une chronologie avec Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Au lieu d'ajuster les filtres pour afficher des dates, vous pouvez utiliser une Timeline de Tableau Croisé Dynamique — une option de filtre dynamique qui vous permet de filtrer facilement par date/heure, et de zoomer sur la période souhaitée avec un contrôle de curseur. Microsoft Excel permet de créer une chronologie en sélectionnant un tableau croisé dynamique puis en cliquant sur *Insérer > Chronologie*. Aspose.Cells for Node.js via C++ permet également de créer une chronologie en utilisant la méthode [**Worksheet.getTimelines().add()**](https://reference.aspose.com/cells/nodejs-cpp/timelinecollection/#add-pivottable-number-number-string-).

## **Créer une chronologie pour un tableau croisé dynamique**

Veuillez voir l'exemple de code ci-dessous. Il charge le [fichier Excel d'exemple](input.xlsx) contenant le tableau croisé dynamique. Ensuite, il crée la chronologie en se basant sur le premier champ de tableau croisé dynamique de base. Enfin, il enregistre le classeur au format [XLSX de sortie](output.xlsx). La capture d'écran suivante montre la chronologie créée par Aspose.Cells for Node.js via C++ dans le fichier Excel de sortie.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Code d'exemple**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-CreateTimelineToPivotTable.js" >}}

