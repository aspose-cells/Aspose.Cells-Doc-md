---
title: Insérer un segmentateur
linktitle: Segmentateurs
type: docs
weight: 170
url: /fr/python-net/create-slicer/
description: Gérer les segmentateurs des fichiers Excel avec Aspose.Cells.
keywords: Aspose.Cells pour Python Excel, bibliothèque Python Excel, Python Créer un slicer sans Excel, Ajouter un slicer via Aspose.Cells pour Python, Insérer un slicer en utilisant Aspose.Cells pour Python.
---

## **Scénarios d'utilisation possibles**

Un slicer est utilisé pour filtrer rapidement les données. Il peut être utilisé pour filtrer des données dans un tableau ou un tableau croisé dynamique. Microsoft Excel vous permet de créer un slicer en sélectionnant un tableau ou un tableau croisé dynamique, puis en cliquant sur *Insérer > Slicer*. Aspose.Cells pour Python via .NET vous permet également de créer un slicer en utilisant la méthode [**Worksheet.slicers.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercollection/add/#aspose.cells.pivot.PivotTable-int-int-aspose.cells.pivot.PivotField).

## **Comment créer un slicer pour un tableau croisé dynamique en utilisant la bibliothèque Aspose.Cells pour Python Excel**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel exemple](67338470.xlsx) qui contient le tableau croisé dynamique. Il crée ensuite le segmentateur en fonction du premier champ de base du tableau croisé dynamique. Enfin, il enregistre le classeur au format [XLSX de sortie](67338471.xlsx) et [XLSB de sortie](67338472.xlsb). La capture d'écran suivante montre le segmentateur créé par Aspose.Cells dans le fichier Excel de sortie.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-CreateSlicerToPivotTable.py" >}}

## **Comment créer un slicer pour un tableau Excel en utilisant la bibliothèque Aspose.Cells pour Python Excel**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel exemple](sampleCreateSlicerToExcelTable.xlsx) qui contient un tableau. Il crée ensuite le segmentateur en fonction de la première colonne. Enfin, il enregistre le classeur au format [XLSX de sortie](outputCreateSlicerToExcelTable.xlsx).

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.py" >}}

## **Sujets avancés**
- [Modifier les propriétés du segmentateur](/cells/fr/python-net/change-slicer-properties/)
- [Dessiner un tronçonneur lors du rendu Excel en PDF](/cells/fr/python-net/draw-slicer-while-rendering-excel-to-pdf/)
- [Formatage d'un tronçonneur](/cells/fr/python-net/formatting-slicer/)
- [Suppression du tronçonneur](/cells/fr/python-net/removing-slicer/)
- [Rendu du tronçonneur](/cells/fr/python-net/rendering-slicer/)
- [Mise à jour du tronçonneur](/cells/fr/python-net/updating-slicer/)
{{< app/cells/assistant language="python-net" >}}
