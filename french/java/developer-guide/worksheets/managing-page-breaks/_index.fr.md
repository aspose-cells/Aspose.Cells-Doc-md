---
title: Gestion des sauts de page
type: docs
weight: 30
url: /fr/java/managing-page-breaks/
---
{{% alert color="primary" %}}

Un saut de page est un endroit dans le texte où une page se termine et la suivante commence. Microsoft Excel peut ajouter des sauts de page à n'importe quelle cellule sélectionnée dans une feuille de calcul.
La page se termine à la cellule où le saut de page est ajouté et toutes les données après le saut de page sont imprimées sur la page suivante. En termes simples, les sauts de page divisent les feuilles de calcul en plusieurs pages. Il est également possible d'ajouter des sauts de page aux feuilles de calcul lors de l'exécution à l'aide de Aspose.Cells. Aspose.Cells prend en charge deux types de saut de page :

- horizontal
- vertical.

Cet article explique comment ajouter des sauts de page horizontaux ou verticaux dans des feuilles de calcul à l'aide de Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells et sauts de page**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel. La[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe qui fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour ajouter des sauts de page, utilisez le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[**Sauts de page horizontaux**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) et[**Sauts de page verticaux**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)Propriétés.

 La[**Sauts de page horizontaux**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) et[**Sauts de page verticaux**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)Les propriétés sont en fait des collections pouvant contenir plusieurs sauts de page. Chaque collection contient plusieurs méthodes de gestion des sauts de page horizontaux et verticaux. La façon dont ces méthodes sont utilisées est discutée ci-dessous.

## **Ajouter des sauts de page**

 Pour ajouter un saut de page dans une feuille de calcul, insérez des sauts de page verticaux et horizontaux dans la cellule spécifiée en appelant la commande[**Sauts de page horizontaux**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) et[**Sauts de page verticaux**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) collections'**Ajouter** méthodes. Chaque**Ajouter**prend le nom de la cellule où le saut de page doit être ajouté.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

Dans les modes d'aperçu des sauts de page ou d'aperçu avant impression, vous pouvez voir comment ces sauts de page fonctionnent.

{{% /alert %}}

## **Effacer tous les sauts de page**

 Pour effacer tous les sauts de page dans une feuille de calcul, appelez le[**HorizontalPageBreakCollectionHorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) et[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) collections'**Dégager**méthodes.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Suppression d'un saut de page spécifique**

 Pour supprimer un saut de page spécifique dans la feuille de calcul, appelez le[**HorizontalPageBreakCollectionHorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) et[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) collections'**removeAt** méthodes. Chaque**removeAt**prendra l'index du saut de page à supprimer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Important à savoir** : lorsque vous définissez les propriétés d'ajustement à la page (c'est-à-dire[**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) et[**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)) dans les paramètres de mise en page, les paramètres de saut de page sont affectés. Par conséquent, si vous imprimez la feuille de calcul, les paramètres de saut de page ne sont pas pris en compte bien qu'ils existent toujours dans le fichier.

{{% /alert %}}
