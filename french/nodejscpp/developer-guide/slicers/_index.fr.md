---
title: Insérer un segmentateur
linktitle: Segmentateurs
type: docs
weight: 170
url: /fr/nodejs-cpp/create-slicer/
description: Gérer les trancheurs des fichiers Excel avec Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Un trancheur est utilisé pour filtrer rapidement des données. Il peut être utilisé pour filtrer des données dans un tableau ou un tableau croisé dynamique. Microsoft Excel permet de créer un trancheur en sélectionnant un tableau ou un tableau croisé dynamique, puis en cliquant sur *Insérer > Trancheur*. Aspose.Cells for Node.js via C++ permet également de créer un trancheur en utilisant la méthode [**Worksheet.getSlicers().add()**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#add-pivottable-string-string-).

## **Créer un segmentateur pour un tableau croisé dynamique**

Veuillez consulter le code d'exemple ci-dessous. Il charge le [fichier Excel d'exemple](67338470.xlsx) contenant le tableau croisé dynamique. Il crée ensuite le trancheur basé sur le premier champ de pivot de base. Enfin, il sauvegarde le classeur au format [XLSX de sortie](67338471.xlsx) et [XLSB de sortie](67338472.xlsb). La capture d'écran suivante montre le trancheur créé par Aspose.Cells for Node.js via C++ dans le fichier Excel de sortie.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Code d'exemple**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToPivotTable.js" >}}

## **Créer un segmentateur pour un tableau Excel**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel exemple](sampleCreateSlicerToExcelTable.xlsx) qui contient un tableau. Il crée ensuite le segmentateur en fonction de la première colonne. Enfin, il enregistre le classeur au format [XLSX de sortie](outputCreateSlicerToExcelTable.xlsx).

### **Code d'exemple**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToExcelTable-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
