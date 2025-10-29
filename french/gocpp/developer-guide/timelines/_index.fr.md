---
title: Insérer une chronologie avec Golang via C++
linktitle: Chronologies
type: docs
weight: 170
url: /fr/go-cpp/create-timeline/
description: Apprenez à créer une chronologie avec Aspose.Cells en utilisant C++.
---

## **Scénarios d'utilisation possibles**

Au lieu d'ajuster les filtres pour afficher les dates, vous pouvez utiliser une Chronologie de Tableau Croisé Dynamique—une option de filtre dynamique qui vous permet de filtrer facilement par date/heure, et de zoomer sur la période souhaitée avec un contrôle de curseur. Microsoft Excel vous permet de créer une chronologie en sélectionnant un tableau croisé dynamique et en cliquant ensuite sur *Insertion > Chronologie*. Aspose.Cells permet également de créer une chronologie en utilisant la méthode [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/go-cpp/timelinecollection/add_pivottable_int_int_string/).

## **Créer une chronologie pour un tableau croisé dynamique**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](input.xlsx) qui contient le tableau croisé dynamique. Ensuite, il crée la chronologie en fonction du premier champ pivot de base. Enfin, il enregistre le classeur au format [XLSX de sortie](output.xlsx). La capture d'écran suivante montre la chronologie créée par Aspose.Cells dans le fichier Excel de sortie.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Timelines.go" >}}
