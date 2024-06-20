---
title: Fusionner et séparer des cellules
type: docs
weight: 140
url: /fr/java/merging-and-unmerging-cells/
---

{{% alert color="primary" %}}

Vous ne voulez pas toujours le même nombre de cellules dans chaque rangée ou colonne. Par exemple, vous pourriez vouloir mettre un titre dans une cellule qui s'étend sur plusieurs colonnes. Ou, si vous créez une facture, vous pourriez vouloir moins de colonnes pour le total. Pour faire une cellule à partir de deux ou plusieurs cellules, fusionnez-les. Microsoft Excel permet aux utilisateurs de sélectionner des cellules et de les fusionner pour structurer la feuille de calcul comme ils le souhaitent.

**Le résultat de la fusion et du découpage d'une plage de cellules formatées comme les cellules à gauche dans Microsoft Excel** 

![todo:image_alt_text](merging-and-unmerging-cells_1.png)

Aspose.Cells prend en charge cette fonctionnalité et peut également fusionner des cellules dans une feuille de calcul. Vous pouvez également scinder les cellules fusionnées. La référence de cellule d'une cellule fusionnée est la référence de la cellule en haut à gauche de la plage sélectionnée à l'origine.

Notez que lorsque les cellules sont fusionnées, seules les données de la cellule en haut à gauche sont conservées. Si des données se trouvent dans les autres cellules de la plage, ces données sont supprimées.

De même, la mise en forme est basée sur la cellule de référence de telle sorte que lorsque vous fusionnez des cellules, les paramètres de mise en forme de la cellule en haut à gauche de la plage sont appliqués sur la cellule fusionnée. Lorsque la cellule est scindée, les nouvelles cellules conservent leurs paramètres de format d'origine.

{{% /alert %}}

## **Fusionner les cellules dans une feuille de calcul.**

### **Utilisation de Microsoft Excel**

Les étapes suivantes décrivent comment fusionner des cellules dans la feuille de calcul en utilisant Microsoft Excel.

1. Copiez les données que vous souhaitez dans la cellule en haut à gauche dans la plage.
1. Sélectionnez les cellules que vous souhaitez fusionner.
1. Pour fusionner des cellules dans une ligne ou une colonne et centrer le contenu de la cellule, cliquez sur l'icône **Fusionner et centrer** dans la barre d'outils **Mise en forme**.

### **Utilisation d'Aspose.Cells**

La classe [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) possède quelques méthodes utiles pour la tâche. Par exemple, la méthode [**merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) fusionne les cellules en une seule cellule dans une plage spécifiée de cellules.

Le résultat suivant est généré après l'exécution du code ci-dessous.

**Les cellules (C6:E7) ont été fusionnées** 

![todo:image_alt_text](merging-and-unmerging-cells_2.png)

#### **Exemple de code**

L'exemple suivant montre comment fusionner des cellules (C6:E7) dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **Dissocier (diviser) les cellules fusionnées**

### **Utilisation de Microsoft Excel**

Les étapes suivantes décrivent comment diviser les cellules fusionnées à l'aide de Microsoft Excel.

1. Sélectionnez la cellule fusionnée. 
   Lorsque les cellules ont été combinées, **Fusionner et centrer** est sélectionné dans la barre d'outils **Mise en forme**.
1. Cliquez sur **Fusionner et centrer** dans la barre d'outils **Mise en forme**.

#### **Utilisation d'Aspose.Cells**

La classe [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) possède une méthode nommée [**unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)) qui divise les cellules dans leur état d'origine. La méthode défusionne les cellules en utilisant la référence de la cellule dans la plage de cellules fusionnées.

#### **Exemple de code**

L'exemple suivant montre comment diviser les cellules fusionnées (C6). L'exemple utilise le fichier créé dans l'exemple précédent et divise les cellules fusionnées.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **Articles connexes**

- [Trouver et scinder des cellules fusionnées](/cells/fr/java/detect-merged-cells-in-a-worksheet/).
- [Fusionner et scinder une plage de cellules en utilisant les méthodes Range.merge() et Range.unMerge()](/cells/fr/java/merge-or-unmerge-range-of-cells/).

