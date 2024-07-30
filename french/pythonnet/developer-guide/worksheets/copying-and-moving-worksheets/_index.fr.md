---
title: Copier et Déplacer des Feuilles de calcul
type: docs
weight: 10
url: /fr/python-net/copying-and-moving-worksheets/
description: Cet article inclut un code d exemple et décrit comment copier et déplacer des feuilles de calcul de manière programmatique à la fois dans un classeur Excel et entre des classeurs Excel en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Copier une feuille de calcul en Python, Déplacer une feuille de calcul en Python, Copier des feuilles de calcul entre des classeurs, Déplacer des feuilles de calcul à l intérieur d un classeur, Copier des feuilles de calcul entre des classeurs, Copier des feuilles de calcul à l intérieur d un classeur.
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec une mise en forme et des données communes. Par exemple, si vous travaillez avec des budgets trimestriels, vous voudrez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonne, en-têtes de ligne et formules. Il y a un moyen de le faire : en créant une feuille, puis en la copiant.

Aspose.Cells pour Python via .NET prend en charge la copie et le déplacement de feuilles de calcul à l'intérieur ou entre des classeurs. Les feuilles de calcul, avec les données, la mise en forme, les tableaux, les matrices, les graphiques, les images et d'autres objets, sont copiées avec le plus grand degré de précision.

{{% /alert %}}

## **Comment déplacer ou copier des feuilles à l'aide de Microsoft Excel**

Voici les étapes à suivre pour copier et déplacer des feuilles de calcul à l'intérieur ou entre des classeurs dans Microsoft Excel.

1. Pour déplacer ou copier des feuilles vers un autre classeur, ouvrez le classeur qui recevra les feuilles.
1. Basculez vers le classeur contenant les feuilles que vous souhaitez déplacer ou copier, puis sélectionnez les feuilles.
1. Dans le menu **Édition**, cliquez sur **Déplacer ou copier la feuille**.
1. Dans la boîte de dialogue **Vers le classeur**, cliquez sur le classeur qui recevra les feuilles.
1. Pour déplacer ou copier les feuilles sélectionnées vers un nouveau classeur, cliquez sur **Nouveau Classeur**.
1. Dans la zone **Avant la feuille**, cliquez sur la feuille avant laquelle vous souhaitez insérer les feuilles déplacées ou copiées.
1. Pour copier les feuilles au lieu de les déplacer, sélectionnez la case à cocher **Créer une copie**.

## **Comment copier des feuilles de calcul dans un classeur avec Aspose.Cells pour la bibliothèque Python Excel**

Aspose.Cells pour Python via .NET fournit une méthode surchargée, [**Aspose.Cells.WorksheetCollection.add_copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add_copy/#str), qui est utilisée pour ajouter une feuille de calcul à la collection et copier des données à partir d'une feuille de calcul existante. Une version de la méthode prend l'index de la feuille de calcul source en paramètre. L'autre version prend le nom de la feuille de calcul source.

L'exemple suivant montre comment copier une feuille existante dans un classeur.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWithinWorkbook-1.py" >}}

## **Comment copier des feuilles entre les classeurs**

Aspose.Cells pour Python via .NET fournit une méthode, [**Aspose.Cells.Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy/#aspose.cells.Worksheet) utilisée pour copier des données et mise en forme d'une feuille de calcul source à une autre feuille de calcul à l'intérieur ou entre des classeurs. La méthode prend l'objet de la feuille de calcul source en paramètre.

L'exemple suivant montre comment copier une feuille de calcul d'un classeur à un autre.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.py" >}}

L'exemple suivant montre comment copier une feuille de calcul d'un classeur vers un autre.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.py" >}}

## **Comment déplacer des feuilles de calcul à l'intérieur du classeur**

Aspose.Cells pour Python via .NET fournit une méthode [**Aspose.Cells.Worksheet.move_to()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/move_to/#int) qui est utilisée pour déplacer une feuille de calcul vers un autre emplacement dans la même feuille de calcul. La méthode prend l'index de la feuille de calcul cible en paramètre.

L'exemple suivant montre comment déplacer une feuille de calcul vers un autre emplacement dans le classeur.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-MoveWorksheet-1.py" >}}
