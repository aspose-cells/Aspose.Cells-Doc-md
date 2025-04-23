---
title: Insérer un segmentateur
linktitle: Segmentateurs
type: docs
weight: 170
url: /fr/net/create-slicer/
description: Gérer les segmentateurs des fichiers Excel avec Aspose.Cells.
---

## **Scénarios d'utilisation possibles**

Un segmentateur est utilisé pour filtrer rapidement les données. Il peut être utilisé pour filtrer les données dans un tableau ou un tableau croisé dynamique. Microsoft Excel vous permet de créer un segmentateur en sélectionnant un tableau ou un tableau croisé dynamique, puis en cliquant sur *Insérer > Segmentateur*. Aspose.Cells vous permet également de créer un segmentateur en utilisant la méthode [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/add/index).

## **Créer un segmentateur pour un tableau croisé dynamique**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel exemple](67338470.xlsx) qui contient le tableau croisé dynamique. Il crée ensuite le segmentateur en fonction du premier champ de base du tableau croisé dynamique. Enfin, il enregistre le classeur au format [XLSX de sortie](67338471.xlsx) et [XLSB de sortie](67338472.xlsb). La capture d'écran suivante montre le segmentateur créé par Aspose.Cells dans le fichier Excel de sortie.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-CreateSlicerToPivotTable.cs" >}}

## **Créer un segmentateur pour un tableau Excel**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel exemple](sampleCreateSlicerToExcelTable.xlsx) qui contient un tableau. Il crée ensuite le segmentateur en fonction de la première colonne. Enfin, il enregistre le classeur au format [XLSX de sortie](outputCreateSlicerToExcelTable.xlsx).

### **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.cs" >}}

## **Sujets avancés**
- [Modifier les propriétés du segmentateur](/cells/fr/net/change-slicer-properties/)
- [Dessiner un tronçonneur lors du rendu Excel en PDF](/cells/fr/net/draw-slicer-while-rendering-excel-to-pdf/)
- [Formatage d'un tronçonneur](/cells/fr/net/formatting-slicer/)
- [Suppression du tronçonneur](/cells/fr/net/removing-slicer/)
- [Rendu du tronçonneur](/cells/fr/net/rendering-slicer/)
- [Mise à jour du tronçonneur](/cells/fr/net/updating-slicer/)
{{< app/cells/assistant language="csharp" >}}
