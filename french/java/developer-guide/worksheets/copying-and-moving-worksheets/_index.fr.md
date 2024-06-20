---
title: Copier et Déplacer des Feuilles de calcul
type: docs
weight: 20
url: /fr/java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec une mise en forme et des données communes. Par exemple, si vous travaillez avec des budgets trimestriels, vous voudrez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonne, en-têtes de ligne et formules. Il y a un moyen de le faire : en créant une feuille, puis en la copiant.

Aspose.Cells prend en charge la copie et le déplacement des feuilles de calcul à l'intérieur ou entre des classeurs. Les feuilles de calcul, complètes avec les données, la mise en forme, les tableaux, les matrices, les graphiques, les images et les autres objets, sont copiées avec le plus haut degré de précision.

{{% /alert %}}

## **Déplacement ou Copie de feuilles à l'aide de Microsoft Excel**

Voici les étapes à suivre pour copier et déplacer des feuilles de calcul au sein d'un classeur ou entre des classeurs.

1. Pour déplacer ou copier des feuilles vers un autre classeur, ouvrez le classeur qui recevra les feuilles.
1. Basculez vers le classeur contenant les feuilles que vous souhaitez déplacer ou copier, puis sélectionnez les feuilles.
1. Dans le menu **Édition**, cliquez sur **Déplacer ou copier la feuille**.
1. Dans la zone Vers le classeur, cliquez sur le classeur pour recevoir les feuilles.
1. Pour déplacer ou copier les feuilles sélectionnées dans un nouveau classeur, cliquez sur **nouveau classeur**.
1. Dans la zone **Avant la feuille**, cliquez sur la feuille avant laquelle vous souhaitez insérer les feuilles déplacées ou copiées.
1. Pour copier les feuilles au lieu de les déplacer, sélectionnez la case à cocher **Créer une copie**.

## **Copier des feuilles de calcul dans un classeur**

Aspose.Cells fournit une méthode surchargée, [**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int)), qui est utilisée pour ajouter une feuille de calcul à la collection et copier les données à partir d'une feuille de calcul existante. Une version de la méthode prend l'index de la feuille source comme paramètre. L'autre version prend le nom de la feuille de calcul source.

L'exemple suivant montre comment copier une feuille existante dans un classeur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **Copier des feuilles de calcul entre des classeurs**

Aspose.Cells fournit une méthode, [**Worksheet.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)), utilisée pour copier des données et la mise en forme d'une feuille source vers une autre feuille, dans ou entre des classeurs. La méthode prend l'objet de la feuille source comme paramètre.

L'exemple suivant montre comment copier une feuille de calcul d'un classeur à un autre.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

L'exemple suivant montre comment copier une feuille de calcul d'un classeur vers un autre.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **Déplacer des feuilles de calcul dans un classeur**

Aspose.Cells fournit une méthode, [**Worksheet.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int)), utilisée pour déplacer une feuille vers un autre emplacement dans la même feuille de calcul.

L'exemple suivant montre comment déplacer une feuille de calcul vers un autre emplacement dans le classeur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
