---
title: Copier des lignes et des colonnes
type: docs
weight: 40
url: /fr/python-net/copying-rows-and-columns/
description: Cet article montre comment copier des lignes et des colonnes à l aide de l API Aspose.Cells for Python via .NET.
keywords: Python Excel Library, Python Comment copier des lignes et des colonnes, Copier des lignes en Python, Copier des colonnes en utilisant Python, Comment coller des lignes et des colonnes en utilisant Aspose.Cells pour Python via .NET, Python Coller plusieurs lignes et colonnes, Comment Copier et coller une seule ligne ou colonne en Python.
---

## **Introduction**

Parfois, vous devez copier des lignes et des colonnes dans une feuille de calcul sans copier toute la feuille de calcul. Avec Aspose.Cells, il est possible de copier des lignes et des colonnes à l'intérieur ou entre les classeurs.
Lorsqu'une ligne (ou une colonne) est copiée, les données qu'elle contient, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, la mise en forme, les cellules masquées, les images et autres objets graphiques sont également copiés.

## **Comment copier des lignes et des colonnes avec Microsoft Excel**

1. Sélectionnez la ligne ou la colonne que vous souhaitez copier.
1. Pour copier des lignes ou des colonnes, cliquez sur **Copier** dans la barre d'outils **Standard**, ou appuyez sur **CTRL**+**C**.
1. Sélectionnez une ligne ou une colonne en dessous ou à droite de l'endroit où vous souhaitez copier votre sélection.
1. Lorsque vous copiez des lignes ou des colonnes, cliquez sur **Cellules copiées** dans le menu **Insérer**.

{{% alert color="primary" %}}

Si vous cliquez sur **Coller** dans la barre d'outils **Standard** ou appuyez sur **CTRL**+**V** au lieu de cliquer sur une commande dans le menu **Insérer**, tout contenu des cellules de destination est remplacé.

{{% /alert %}}

## **Comment coller des lignes et des colonnes en utilisant les options de collage avec Microsoft Excel**

1. Sélectionnez les cellules contenant les données ou autres attributs que vous souhaitez copier.
1. Sur l'onglet Accueil, cliquez sur **Copier**.
1. Cliquez sur la première cellule dans la zone où vous souhaitez **coller** ce que vous avez copié.
1. Sur l'onglet Accueil, cliquez sur la flèche à côté de **Coller**, puis sélectionnez **Collage** spécial.
1. Sélectionnez les **options** que vous souhaitez.

## **Comment copier des lignes et des colonnes en utilisant Aspose.Cells pour Python via .NET**

## **Comment copier des lignes uniques**

Aspose.Cells fournit la méthode [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) de la classe [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Cette méthode copie tous types de données y compris les formules, les valeurs, les commentaires, les formats de cellules, les cellules masquées, les images et autres objets graphiques de la ligne source à la ligne de destination.

La méthode [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) prend les paramètres suivants :

- l'objet de la source [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells),
- indice de la ligne source, et
- indice de la ligne de destination.

Utilisez cette méthode pour copier une ligne dans une feuille de calcul, ou vers une autre feuille. La méthode [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) fonctionne de manière similaire à Microsoft Excel. Par exemple, vous n'avez pas besoin de définir explicitement la hauteur de la ligne de destination, cette valeur est également copiée.

L'exemple suivant montre comment copier une ligne dans une feuille de calcul. Il utilise un fichier modèle Microsoft Excel et copie la deuxième ligne (complète avec des données, un formatage, des commentaires, des images, etc.) et la colle dans la 12e ligne de la même feuille de calcul.

Vous pouvez sauter l'étape qui obtient la hauteur de la ligne source en utilisant la méthode [**Cells.get_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/get_row_height/#int) et ensuite définir la hauteur de la ligne de destination en utilisant la méthode [**Cells.set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) car la méthode [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) prend automatiquement soin de la hauteur de la ligne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingRows-1.py" >}}

{{% alert color="primary" %}}

Lors de la copie de lignes, il est important de noter les images, les graphiques ou autres objets de dessin associés, car c'est la même chose avec Microsoft Excel :

1. Si l'indice de la ligne source est 5, l'image, le graphique, etc., est copié s'il est contenu dans les trois lignes (l'indice de début de la ligne est 4 et l'indice de fin de la ligne est 6).
1. Les images existantes, les graphiques, etc. dans la ligne de destination ne seront pas supprimés.

{{% /alert %}}

## **Comment copier plusieurs lignes**

Vous pouvez également copier plusieurs lignes sur une nouvelle destination tout en utilisant la méthode [**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int) qui prend un paramètre supplémentaire de type entier pour spécifier le nombre de lignes sources à copier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingMultipleRows-1.py" >}}


## **Comment copier des colonnes**

Aspose.Cells fournit la méthode [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) de la classe [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), cette méthode copie tous les types de données, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, les formats de cellules, les cellules masquées, les images et autres objets de dessin de la colonne source à la colonne de destination.

La méthode [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) prend les paramètres suivants :

- l'objet de la source [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells),
- indice de la colonne source, et
- indice de la colonne de destination.

Utilisez la méthode [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) pour copier une colonne dans une feuille de calcul ou vers une autre feuille.

Cet exemple copie une colonne d'une feuille de calcul et la colle dans une feuille de calcul d'un autre classeur.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingColumns-1.py" >}}

## **Comment copier plusieurs colonnes**

Similaire à la méthode [**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int), les API Aspose.Cells fournissent également la méthode [**Cells.copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/) pour copier plusieurs colonnes sources vers un nouvel emplacement.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingMultipleColumns-1.py" >}}


## **Comment coller des lignes et des colonnes avec des options de collage**

Aspose.Cells fournit maintenant [**PasteOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions) tout en utilisant les fonctions [**copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int-aspose.cells.CopyOptions-aspose.cells.PasteOptions) et [**copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/#aspose.cells.Cells-int-int-int-aspose.cells.PasteOptions). Il permet de définir une option de collage appropriée similaire à Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
