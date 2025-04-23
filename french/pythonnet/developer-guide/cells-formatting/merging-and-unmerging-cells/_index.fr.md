---
title: Fusionner et séparer des cellules
description: Aspose.Cells est une bibliothèque Python pour travailler avec des fichiers de feuilles de calcul, prenant en charge la fusion et la séparation des cellules. Cet article présente comment fusionner et dé fusionner les cellules en utilisant Aspose.Cells pour Python via .NET, et comment personnaliser le style de la cellule fusionnée.
keywords: Aspose.Cells pour Python via .NET, bibliothèque .NET, feuille de calcul, fusionner des cellules, dé fusionner des cellules, paramètres de style, styles personnalisés
type: docs
weight: 190
url: /fr/python-net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells pour Python via .NET supporte cette fonctionnalité et peut également fusionner des cellules dans une feuille. Vous pouvez dé-fusionner ou diviser les cellules fusionnées aussi. La référence d'une cellule fusionnée est la référence de la cellule en haut à gauche de la plage sélectionnée d'origine.

{{% /alert %}} 
## **Introduction**
Vous ne souhaitez pas toujours le même nombre de cellules dans chaque ligne ou colonne. Par exemple, vous pouvez vouloir mettre un titre dans une cellule qui s'étend sur plusieurs colonnes. Ou, si vous créez une facture, vous souhaitez peut-être moins de colonnes pour le total. Pour fusionner deux cellules ou plus en une seule cellule, utilisez la fusion. Microsoft Excel permet aux utilisateurs de sélectionner des fichiers et de les fusionner pour structurer le tableur à leur convenance.

{{% alert color="primary" %}} 

Remarquez que lorsque des cellules sont fusionnées, seules les données de la cellule en haut à gauche sont conservées. Si des données se trouvent dans les autres cellules de la plage, ces données sont supprimées.
De même, la mise en forme repose sur la cellule de référence de sorte que lorsque vous fusionnez des cellules, les paramètres de mise en forme de la cellule en haut à gauche de la plage sont appliqués sur la cellule fusionnée. Lorsque la cellule est scindée, les nouvelles cellules conservent leurs paramètres de mise en forme d'origine.

{{% /alert %}} 
## **Fusion de cellules dans une feuille de calcul**
### **Fusionner des cellules dans Microsoft Excel**
Les étapes suivantes décrivent comment fusionner des cellules dans la feuille de calcul à l'aide de MS Excel.

1. Copiez les données que vous souhaitez dans la cellule en haut à gauche dans la plage.
1. Sélectionnez les cellules que vous souhaitez fusionner.
1. Pour fusionner des cellules dans une ligne ou une colonne et centrer le contenu de la cellule, cliquez sur l'icône **Fusionner et centrer** dans la barre d'outils **Mise en forme**.

### **Fusionner des cellules avec Aspose.Cells pour Python via .NET**
La classe Aspose.Cells.Cells dispose de certaines méthodes utiles pour la tâche. Par exemple, la méthode Merge() fusionne les cellules en une seule cellule dans une plage spécifiée.

L'exemple suivant montre comment fusionner des cellules (C6:E7) dans une feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-MergingCellsInWorksheet.-1.py" >}}

## **Dissocier (diviser) les cellules fusionnées**
### **Utilisation de Microsoft Excel**
Les étapes suivantes décrivent comment diviser les cellules fusionnées à l'aide de Microsoft Excel.

1. Sélectionnez la cellule fusionnée. Lorsque les cellules ont été combinées, **Fusionner et Centrer** est sélectionné dans la barre d'outils **Mise en forme**.
1. Cliquez sur **Fusionner et centrer** dans la barre d'outils **Mise en forme**.

### **Utiliser Aspose.Cells pour Python via .NET**
La classe Aspose.Cells.Cells dispose d'une méthode nommée UnMerge() qui divise les cellules dans leur état d'origine. La méthode dissocie les cellules en utilisant la référence de la cellule dans la plage de cellules fusionnées.

L'exemple suivant montre comment diviser les cellules fusionnées (C6). L'exemple utilise le fichier créé dans l'exemple précédent et divise les cellules fusionnées.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UnMergingtheMergedCells-1.py" >}}


## **Sujets avancés**
- [Détecter les cellules fusionnées dans une feuille de calcul](/cells/fr/python-net/detect-merged-cells-in-a-worksheet/)

