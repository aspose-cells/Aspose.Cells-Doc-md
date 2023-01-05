---
title: Fusion et défusion Cells
type: docs
weight: 140
url: /fr/java/merging-and-unmerging-cells/
---
{{% alert color="primary" %}}

Vous ne voulez pas toujours le même nombre de cellules dans chaque ligne ou colonne. Par exemple, vous voudrez peut-être mettre un titre dans une cellule qui s'étend sur plusieurs colonnes. Ou, si vous créez une facture, vous voudrez peut-être moins de colonnes pour le total. Pour créer une cellule à partir de deux cellules ou plus, fusionnez-les. Microsoft Excel permet aux utilisateurs de sélectionner des cellules et de les fusionner pour structurer la feuille de calcul comme ils le souhaitent.

**Le résultat de la fusion puis de la division d'une plage de cellules formatées comme les cellules à gauche dans Microsoft Excel** 

![tâche : image_autre_texte](merging-and-unmerging-cells_1.png)

Aspose.Cells prend en charge cette fonctionnalité et peut également fusionner des cellules dans une feuille de calcul. Vous pouvez également dissocier ou diviser les cellules fusionnées. La référence de cellule d'une cellule fusionnée est la référence de la cellule en haut à gauche dans la plage sélectionnée à l'origine.

Notez que lorsque les cellules sont fusionnées, seules les données de la cellule en haut à gauche sont conservées. S'il existe des données dans les autres cellules de la plage, ces données sont supprimées.

De même, la mise en forme est basée sur la cellule de référence de sorte que lorsque vous fusionnez des cellules, les paramètres de mise en forme de la cellule en haut à gauche de la plage sont appliqués à la cellule fusionnée. Lorsque la cellule est fractionnée, les nouvelles cellules conservent leurs paramètres de format d'origine.

{{% /alert %}}

## **Fusion de Cells dans une feuille de travail.**

### **Utilisation d'Excel Microsoft**

Les étapes suivantes décrivent comment fusionner des cellules dans la feuille de calcul à l'aide de Microsoft Excel.

1. Copiez les données souhaitées dans la cellule la plus à gauche de la plage.
1. Sélectionnez les cellules que vous souhaitez fusionner.
1.  Pour fusionner des cellules dans une ligne ou une colonne et centrer le contenu des cellules, cliquez sur**Fusionner et centrer** icône sur le**Mise en page** barre d'outils.

### **En utilisant Aspose.Cells**

 Le[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) classe a quelques méthodes utiles pour la tâche. Par exemple, la méthode[**fusionner()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) fusionne les cellules en une seule cellule dans une plage spécifiée de cellules.

La sortie suivante est générée après l'exécution du code ci-dessous.

**Les cellules (C6:E7) ont été fusionnées** 

![tâche : image_autre_texte](merging-and-unmerging-cells_2.png)

#### **Exemple de code**

L'exemple suivant montre comment fusionner des cellules (C6:E7) dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **Défusion (Fractionnement) Fusionné Cells**

### **Utilisation d'Excel Microsoft**

Les étapes suivantes décrivent comment fractionner des cellules fusionnées à l'aide de Microsoft Excel.

1.  Sélectionnez la cellule fusionnée.
 Lorsque les cellules ont été combinées,**Fusionner et centrer** est sélectionné sur le**Mise en page** barre d'outils.
1.  Cliquez sur**Fusionner et centrer** sur le**Mise en page** barre d'outils.

#### **En utilisant Aspose.Cells**

 Le[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) classe a une méthode nommée[**défusionner()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)) qui divise les cellules dans leur état d'origine. La méthode dissocie les cellules à l'aide de la référence de la cellule dans la plage de cellules fusionnées.

#### **Exemple de code**

L'exemple suivant montre comment diviser les cellules fusionnées (C6). L'exemple utilise le fichier créé dans l'exemple précédent et divise les cellules fusionnées.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **Articles Liés**

- [Recherche et division de cellules fusionnées](/cells/fr/java/detect-merged-cells-in-a-worksheet/).
- [Fusionner et fractionner une plage de cellules à l'aide des méthodes Range.merge() et Range.unMerge()](/cells/fr/java/merge-or-unmerge-range-of-cells/).

