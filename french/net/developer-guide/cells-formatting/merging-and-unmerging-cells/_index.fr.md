---
title: Fusionner et séparer des cellules
description: Aspose.Cells est une bibliothèque .NET pour travailler avec des fichiers de tableurs, qui prend en charge la fusion et la séparation de cellules. Cet article présentera comment fusionner et séparer des cellules en utilisant la bibliothèque Aspose.Cells, et comment personnaliser le style des cellules fusionnées.
keywords: Aspose.Cells, bibliothèque .NET, tableur, fusion de cellules, séparation de cellules, paramètres de style, styles personnalisés
type: docs
weight: 190
url: /fr/net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells prend en charge cette fonctionnalité et peut également fusionner des cellules dans une feuille de calcul. Vous pouvez également séparer, ou diviser, les cellules fusionnées. La référence de cellule d'une cellule fusionnée est la référence de la cellule en haut à gauche de la plage sélectionnée d'origine.

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
### **Fusion de cellules avec Aspose.Cells**
La classe Aspose.Cells.Cells dispose de certaines méthodes utiles pour la tâche. Par exemple, la méthode Merge() fusionne les cellules en une seule cellule dans une plage spécifiée.

L'exemple suivant montre comment fusionner des cellules (C6:E7) dans une feuille de calcul.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **Dissocier (diviser) les cellules fusionnées**
### **Utilisation de Microsoft Excel**
Les étapes suivantes décrivent comment diviser les cellules fusionnées à l'aide de Microsoft Excel.

1. Sélectionnez la cellule fusionnée.
   Lorsque les cellules ont été combinées, **Fusionner et centrer** est sélectionné dans la barre d'outils **Mise en forme**.
1. Cliquez sur **Fusionner et centrer** dans la barre d'outils **Mise en forme**.
### **Utilisation d'Aspose.Cells**
La classe Aspose.Cells.Cells dispose d'une méthode nommée UnMerge() qui divise les cellules dans leur état d'origine. La méthode dissocie les cellules en utilisant la référence de la cellule dans la plage de cellules fusionnées.

L'exemple suivant montre comment diviser les cellules fusionnées (C6). L'exemple utilise le fichier créé dans l'exemple précédent et divise les cellules fusionnées.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


## **Sujets avancés**
- [Détecter les cellules fusionnées dans une feuille de calcul](/cells/fr/net/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="csharp" >}}
