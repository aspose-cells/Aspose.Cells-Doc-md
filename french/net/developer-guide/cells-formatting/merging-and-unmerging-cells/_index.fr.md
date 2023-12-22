---
title: Fusion et dissociation Cells
description: Aspose.Cells est une bibliothèque .NET permettant de travailler avec des feuilles de calcul, qui prend en charge la fusion et la dissociation de cellules. Cet article explique comment fusionner et annuler la fusion de cellules à l'aide de la bibliothèque Aspose.Cells et comment personnaliser le style de cellule fusionnée.
keywords: Aspose.Cells, NET library, spreadsheet, merge cells, unmerge cells, style settings, custom styles
type: docs
weight: 190
url: /fr/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells prend en charge cette fonctionnalité et peut également fusionner des cellules dans une feuille de calcul. Vous pouvez également annuler la fusion ou diviser les cellules fusionnées. La référence de cellule d’une cellule fusionnée est la référence de la cellule supérieure gauche de la plage sélectionnée d’origine.

{{% /alert %}} 
##  **Introduction**
Vous ne voulez pas toujours le même nombre de cellules dans chaque ligne ou colonne. Par exemple, vous souhaiterez peut-être mettre un titre dans une cellule qui s'étend sur plusieurs colonnes. Ou, si vous créez une facture, vous souhaiterez peut-être moins de colonnes pour le total. Pour créer une cellule à partir de deux cellules ou plus, fusionnez-les. Microsoft Excel permet aux utilisateurs de sélectionner des fichiers et de les fusionner pour structurer la feuille de calcul comme ils le souhaitent.

{{% alert color="primary" %}} 

Notez que lorsque les cellules sont fusionnées, seules les données des cellules en haut à gauche sont conservées. S'il y a des données dans les autres cellules de la plage, ces données sont supprimées.
De même, le formatage est basé sur la cellule de référence, de sorte que lorsque vous fusionnez des cellules, les paramètres de formatage de la cellule supérieure gauche de la plage sont appliqués à la cellule fusionnée. Lorsque la cellule est divisée, les nouvelles cellules conservent leurs paramètres de format d'origine.

{{% /alert %}} 
##  **Fusionner Cells dans une feuille de calcul**
###  **Fusionner Cells dans Microsoft Excel**
Les étapes suivantes décrivent comment fusionner des cellules dans la feuille de calcul à l'aide de MS Excel.

1. Copiez les données souhaitées dans la cellule la plus à gauche de la plage.
1. Sélectionnez les cellules que vous souhaitez fusionner.
1.  Pour fusionner des cellules dans une ligne ou une colonne et centrer le contenu des cellules, cliquez sur**Fusionner et centrer** icône sur le**Mise en page** barre d'outils.
###  **Fusionner Cells avec Aspose.Cells**
La classe Aspose.Cells.Cells propose des méthodes utiles pour cette tâche. Par exemple, la méthode Merge() fusionne les cellules en une seule cellule dans une plage spécifiée.

L'exemple suivant montre comment fusionner des cellules (C6:E7) dans une feuille de calcul.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
##  **Dissociation (scission) Fusionné Cells**
###  **Utilisation d'Excel Microsoft**
Les étapes suivantes décrivent comment diviser les cellules fusionnées à l'aide d'Excel Microsoft.

1. Sélectionnez la cellule fusionnée.
 Lorsque les cellules ont été combinées,**Fusionner et centrer** est sélectionné sur le**Mise en page** barre d'outils.
1.  Cliquez sur**Fusionner et centrer** sur le**Mise en page** barre d'outils.
###  **En utilisant le Aspose.Cells**
La classe Aspose.Cells.Cells possède une méthode nommée UnMerge() qui divise les cellules dans leur état d'origine. La méthode annule la fusion des cellules en utilisant la référence de la cellule dans la plage de cellules fusionnées.

L'exemple suivant montre comment diviser les cellules fusionnées (C6). L'exemple utilise le fichier créé dans l'exemple précédent et divise les cellules fusionnées.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


##  **Sujets avancés**
- [Détecter le Cells fusionné dans une feuille de calcul](/cells/fr/net/detect-merged-cells-in-a-worksheet/)
