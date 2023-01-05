---
title: Fusionner et dissocier Cells
type: docs
weight: 60
url: /fr/net/merge-and-unmerge-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb a une fonction utilitaire pratique qui vous permet de fusionner des cellules en une seule grande cellule. Cette rubrique décrit comment fusionner des cellules par programmation.

{{% /alert %}} 
## **Fusion Cells**
Fusionnez plusieurs cellules d'une feuille de calcul en une seule cellule en appelant la méthode Merge de la collection Cells. Spécifiez la plage de cellules à fusionner lors de l'appel de la méthode Merge.

{{% alert color="primary" %}} 

Si vous fusionnez plusieurs cellules et que chaque cellule contient des données, seul le contenu de la cellule supérieure gauche de la plage est conservé après la fusion. Les données des autres cellules ne sont pas perdues. Si vous dissociez les cellules, chaque cellule récupère ses données.

{{% /alert %}} 

**Quatre cellules fusionnées en une seule** 

![tâche : image_autre_texte](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **Défusion Cells**
Pour dissocier des cellules, utilisez la méthode UnMerge de la collection Cells qui prend les mêmes paramètres que la méthode Merge et effectue la dissociation des cellules.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
