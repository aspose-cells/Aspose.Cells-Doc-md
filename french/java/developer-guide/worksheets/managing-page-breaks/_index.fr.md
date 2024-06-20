---
title: Gestion des sauts de page
type: docs
weight: 30
url: /fr/java/managing-page-breaks/
---

{{% alert color="primary" %}}

Un saut de page est un endroit dans le texte où une page se termine et où la suivante commence. Microsoft Excel peut ajouter des sauts de page à n'importe quelle cellule sélectionnée dans une feuille de calcul.
La page se termine à la cellule où le saut de page est ajouté et toutes les données après le saut de page sont imprimées sur la page suivante. En d'autres termes, les sauts de page divisent les feuilles de calcul en plusieurs pages. Il est également possible d'ajouter des sauts de page aux feuilles de calcul à l'exécution en utilisant Aspose.Cells. Aspose.Cells prend en charge deux types de sauts de page:

- horizontal
- vertical.

Cet article décrit comment ajouter des sauts de page horizontaux ou verticaux dans les feuilles de calcul en utilisant Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells & Sauts de page**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) qui fournit une large gamme de propriétés et de méthodes pour la gestion des feuilles de calcul. Pour ajouter les sauts de page, utilisez les propriétés [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) et [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Les propriétés [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) et [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) sont en fait des collections qui peuvent contenir plusieurs sauts de page. Chaque collection contient plusieurs méthodes pour gérer les sauts de page horizontaux et verticaux. La façon d'utiliser ces méthodes est décrite ci-dessous.

## **Ajout de sauts de page**

Pour ajouter un saut de page dans une feuille de calcul, insérez des sauts de page verticaux et horizontaux à la cellule spécifiée en appelant les méthodes **Ajouter** des collections [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) et [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection). Chaque méthode **Ajouter** prend le nom de la cellule où le saut de page doit être ajouté.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

En mode Aperçu des sauts de page ou Aperçu avant impression, vous pouvez voir comment fonctionnent ces sauts de page.

{{% /alert %}}

## **Effacement de tous les sauts de page**

Pour effacer tous les sauts de page dans une feuille de calcul, appelez les méthodes **Effacer** des collections [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) et [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Suppression d'un saut de page spécifique**

Pour supprimer un saut de page spécifique dans la feuille de calcul, appelez les méthodes **removeAt** des collections [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) et [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection). Chaque méthode **removeAt** prend l'index du saut de page à supprimer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Important à savoir**: Lorsque vous définissez les propriétés ajuster à la page (c'est-à-dire [**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) et [**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)) dans les paramètres de configuration de la mise en page, les paramètres des sauts de page sont affectés. Ainsi, si vous imprimez la feuille de calcul, les paramètres des sauts de page ne sont pas pris en compte bien qu'ils existent toujours dans le fichier.

{{% /alert %}}
