---
title: Copier des plages d Excel
linktitle: Copier des plages
type: docs
weight: 105
url: /fr/python-net/copy-ranges-of-excel/
description: Cet article décrit comment copier des plages d Excel avec la bibliothèque Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Comment copier des plages d Excel en Python, Comment copier uniquement les données de la plage avec la bibliothèque Python Excel, Comment coller une plage avec des options, Comment copier uniquement les données de la plage.
---

## **Introduction**

Dans Excel, vous pouvez sélectionner une plage, copier la plage, puis la coller avec des options spécifiques dans la même feuille de calcul, d'autres feuilles de calcul ou d'autres fichiers.

## **Copier des plages en utilisant la bibliothèque Aspose.Cells pour Python Excel**

Aspose.Cells pour Python via .NET fournit des surcharges de méthodes [**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range) pour copier la plage.
Et [**Range.copy_style**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_style/#aspose.cells.Range) seulement le style de copie de la plage; [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range) seulement la valeur de copie de la plage

## **Copier la plage**

Création de deux plages : la plage source, la plage cible, puis copie de la plage source vers la plage cible avec la méthode [**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range).

Voir le code suivant :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range.py" >}}

## **Coller la plage avec des options**

Aspose.Cells pour Python via .NET prend en charge le collage de la plage avec un type spécifique.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Paste-Range.py" >}}

## **Copier uniquement les données de la plage**
Vous pouvez également copier les données avec la méthode [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range) comme dans les codes suivants:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range-Data.py" >}}

## **Sujets avancés**
- [Copier les hauteurs de ligne de la plage source vers la plage de destination](/cells/fr/python-net/copy-row-heights-of-source-range-to-destination-range/)


