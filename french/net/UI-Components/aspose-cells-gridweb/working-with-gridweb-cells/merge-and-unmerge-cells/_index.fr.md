---
title: Fusionner et séparer des cellules
type: docs
weight: 60
url: /fr/net/aspose-cells-gridweb/merge-and-unmerge-cells/
keywords: GridWeb, fusion, séparation
description: Cet article présente comment fusionner/séparer des cellules dans GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb dispose d'une fonctionnalité utilitaire pratique qui vous permet de fusionner des cellules en une seule grande cellule. Ce sujet décrit comment fusionner des cellules de manière programmée.

{{% /alert %}} 
## **Fusion de cellules**
Fusionnez plusieurs cellules dans une feuille de calcul en une seule cellule en appelant la méthode Merge de la collection Cells. Spécifiez la plage de cellules à fusionner lors de l'appel de la méthode Merge.

{{% alert color="primary" %}} 

Si vous fusionnez plusieurs cellules et que chaque cellule contient des données, seul le contenu de la cellule en haut à gauche de la plage est conservé après la fusion. Les données des autres cellules ne sont pas perdues. Si vous divisez les cellules, chaque cellule récupère ses données.

{{% /alert %}} 

**Quatre cellules fusionnées en une seule** 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Désélectionner les cellules**
Pour désélectionner les cellules, utilisez la méthode UnMerge de la collection Cells qui prend les mêmes paramètres que la méthode Merge et effectue la désélection des cellules.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
