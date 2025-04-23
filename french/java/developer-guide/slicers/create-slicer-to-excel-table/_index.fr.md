---
title: Créer une trancheuse pour un tableau Excel
type: docs
weight: 15
url: /fr/java/create-slicer-to-excel-table/
---

## **Scénarios d'utilisation possibles**

Un segmentateur est utilisé pour filtrer rapidement les données. Il peut être utilisé pour filtrer les données dans un tableau ou un tableau croisé dynamique. Microsoft Excel vous permet de créer un segmentateur en sélectionnant un tableau ou un tableau croisé dynamique, puis en cliquant sur *Insérer > Segmentateur*. Aspose.Cells vous permet également de créer un segmentateur en utilisant la méthode [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add-com.aspose.cells.ListObject-com.aspose.cells.ListColumn-int-int-).

## **Créer un segmentateur pour un tableau Excel**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel exemple](sampleCreateSlicerToExcelTable.xlsx) qui contient un tableau. Il crée ensuite le segmentateur en fonction de la première colonne. Enfin, il enregistre le classeur au format [XLSX de sortie](outputCreateSlicerToExcelTable.xlsx).

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Slicers-CreateSlicerToExcelTable-1.java" >}}
{{< app/cells/assistant language="java" >}}
