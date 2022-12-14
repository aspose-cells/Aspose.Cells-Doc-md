---
title: Fusion et défusion Cells
type: docs
weight: 190
url: /fr/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells prend en charge cette fonctionnalité et peut également fusionner des cellules dans une feuille de calcul. Vous pouvez également dissocier ou diviser les cellules fusionnées. La référence de cellule d'une cellule fusionnée est la référence de la cellule supérieure gauche dans la plage sélectionnée d'origine.

{{% /alert %}} 
## **Introduction**
Vous ne voulez pas toujours le même nombre de cellules dans chaque ligne ou colonne. Par exemple, vous voudrez peut-être mettre un titre dans une cellule qui s'étend sur plusieurs colonnes. Ou, si vous créez une facture, vous voudrez peut-être moins de colonnes pour le total. Pour créer une cellule à partir de deux cellules ou plus, fusionnez-les. Microsoft Excel permet aux utilisateurs de sélectionner des fichiers et de les fusionner pour structurer la feuille de calcul comme ils le souhaitent.

{{% alert color="primary" %}} 

Notez que lorsque les cellules sont fusionnées, seules les données des cellules en haut à gauche sont conservées. S'il existe des données dans les autres cellules de la plage, ces données sont supprimées.
De même, la mise en forme est basée sur la cellule de référence de sorte que lorsque vous fusionnez des cellules, les paramètres de mise en forme de la cellule supérieure gauche de la plage sont appliqués à la cellule fusionnée. Lorsque la cellule est fractionnée, les nouvelles cellules conservent leurs paramètres de format d'origine.

{{% /alert %}} 
## **Fusionner Cells dans une feuille de calcul**
### **Fusion de Cells dans Microsoft Excel**
Les étapes suivantes décrivent comment fusionner des cellules dans la feuille de calcul à l'aide de MS Excel.

1. Copiez les données souhaitées dans la cellule la plus à gauche de la plage.
1. Sélectionnez les cellules que vous souhaitez fusionner.
1.  Pour fusionner des cellules dans une ligne ou une colonne et centrer le contenu des cellules, cliquez sur**Fusionner et centrer** icône sur le**Mise en page** barre d'outils.
### **Fusion de Cells avec Aspose.Cells**
La classe Aspose.Cells.Cells a quelques méthodes utiles pour la tâche. Par exemple, la méthode Merge() fusionne les cellules en une seule cellule dans une plage spécifiée.

L'exemple suivant montre comment fusionner des cellules (C6:E7) dans une feuille de calcul.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **Défusion (Fractionnement) Fusionné Cells**
### **Utilisation d'Excel Microsoft**
Les étapes suivantes décrivent comment fractionner des cellules fusionnées à l'aide de Microsoft Excel.

1. Sélectionnez la cellule fusionnée.
 Lorsque les cellules ont été combinées,**Fusionner et centrer** est sélectionné sur le**Mise en page** barre d'outils.
1.  Cliquez sur**Fusionner et centrer** sur le**Mise en page** barre d'outils.
### **En utilisant Aspose.Cells**
La classe Aspose.Cells.Cells a une méthode nommée UnMerge() qui divise les cellules dans leur état d'origine. La méthode dissocie les cellules à l'aide de la référence de la cellule dans la plage de cellules fusionnées.

L'exemple suivant montre comment diviser les cellules fusionnées (C6). L'exemple utilise le fichier créé dans l'exemple précédent et divise les cellules fusionnées.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


## **Sujets avancés**
- [Détecter fusionné Cells dans une feuille de calcul](/cells/fr/net/detect-merged-cells-in-a-worksheet/)
